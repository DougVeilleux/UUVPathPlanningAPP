# AstarPathPlanner.py

import math
import heapq
import time

from utilities.QuadTreeGeodata import *


class AStarPathPlanner:
    """
    This class contains the methods needed to generate a path plan from a start point
        and end up at a goal point.  These points given as a GPS coordinate.
    """

    def __init__(self, quadtree):
        """ Initialize the path planning object. """
        self.quadtree = quadtree


    def h_euclidean(self, current_node, goal_node):
        """
        Calculate the Euclidean distance from current node to the goal_node
        Parameters:
            current_node: current_node that heuristic is being calculated for
            goal_node:  the end position
        """
        # Check if node is a QuadTreeNode and goal_node is a tuple
        if not isinstance(current_node, QuadTreeNode):
            raise TypeError("The 'current_node' parameter must be a QuadTreeNode instance.")
        if not isinstance(goal_node, QuadTreeNode):
            raise TypeError("The 'goal_node' parameter must be a QuadTreeNode instance.")

        # Calculate the Euclidean distance
        return math.sqrt(
            (current_node.latitude - goal_node.latitude) ** 2
            + (current_node.longitude - goal_node.longitude) ** 2)


    def get_neighbors(self, node, search_radius=0.015):
        """
        Find the closest node in the quadtree to the given point within a search radius.
        :param node: the coordinate (longitude, latitude)
        :param search_radius: the radius within which to search for the closest node
        :return: closest node within the search radius
        """
        search_region = (
            node.longitude - search_radius,  # left
            node.latitude - search_radius,  # bottom
            node.longitude + search_radius,  # right
            node.latitude + search_radius  # top
        )
        search_region_nodes = self._get_neighbors_recursive(self.quadtree.root, search_region)

        # Calculate the Euclidean distance between each node and the given point
        distances = []
        for neighbor_node in search_region_nodes:
            distance = math.sqrt((node.longitude - neighbor_node.longitude) ** 2 +
                                 (node.latitude - neighbor_node.latitude) ** 2)
            # Skip the current node (distance = 0.0)
            if distance == 0.0:
                continue
            distances.append((distance, neighbor_node))
            # Print the longitude, latitude, and distance for debugging
            # print("Target Node: (Longitude: {}, Latitude: {})".format(node.longitude, node.latitude))
            # print("Neighbor Node: (Longitude: {}, Latitude: {})".format(neighbor_node.longitude, neighbor_node.latitude))
            # print("Distance: {}".format(distance))

        # Sort distances based on the distance value in each tuple
        distances.sort(key=lambda x: x[0])
        # Debug print statement
        # print("Sorted distances:", distances)

        # Get the four closest nodes and return them directly
        closest_neighbor_nodes = [neighbor_node for distance, neighbor_node in distances[:8]]

        return closest_neighbor_nodes #, search_region_nodes, search_region


    def _get_neighbors_recursive(self, node, search_region, nodes=None):
        """
        Recursively find the closest node in the quadtree to the given point within the search region.
        :param node: the current node being considered
        :param search_region: the region within which to search for the closest node
        :return: nodes within the search region
        """

        # Check if the bounding box of the node intersects with the search region
        if nodes is None:
            nodes = []

        if self._intersects_search_region(node, search_region):
            nodes.append(node)

            # Check if the node is a leaf node
            if node.northWest is None:
                return nodes

        # Recursively search in the child nodes
        for child in [node.northWest, node.northEast, node.southWest, node.southEast]:
            if child:
                self._get_neighbors_recursive(child, search_region, nodes)

        return nodes

    def _intersects_search_region(self, node, search_region):
        """
        Check if the node intersects with the given search region.
        :param node: the node to check for intersection
        :param search_region: the search region defined by (left, bottom, right, top)
        :return: True if the node intersects the search region, False otherwise
        """

        # Check if the bounding box of the node intersects with the search region
        intersects = (node.longitude >= search_region[0] and node.longitude <= search_region[2] and
                      node.latitude >= search_region[1] and node.latitude <= search_region[3])
        return intersects



    def plot_neighbors(self, neighbors, start_point, goal_point, start_closest_node, goal_closest_node,
                          start_collected_nodes, goal_collected_nodes,
                          start_search_region, goal_search_region):
        """
        Plot the nearest node along with the start and goal points.
        :param point: Coordinates of the point (longitude, latitude)
        :param collected_nodes: List collected nodes within the search region
        :param closest_node: the closest node to the start point
        """

        # Collect node data after deletion (assuming you have a method for this)
        final_node_dataframe = self.quadtree.collect_node_data()

        # Check if final_node_dataframe is not None (ensure deletion step was successful)
        if final_node_dataframe is not None:
            # Plot nodes
            fig, ax = plt.subplots(figsize=(14, 9))
            for index, row in final_node_dataframe.iterrows():
                # Extract node coordinates
                min_x, min_y, max_x, max_y = row['min_x'], row['min_y'], row['max_x'], row['max_y']
                mid_x = (min_x + max_x) / 2
                mid_y = (min_y + max_y) / 2
                # Extract landOrWater value
                land_or_water = row['landOrWater']
                # Plot center point of the node
                ax.scatter(mid_x, mid_y, c='tan' if land_or_water == 1 else 'blue', marker='o', s=10)

            # Plot points (green / red)
            ax.scatter(start_point[0], start_point[1], c='green', marker='*', s=150, label='Start Point')
            ax.scatter(goal_point[0], goal_point[1], c='red', marker='*', s=150, label='Goal Point')

            # Plot collected nodes
            for node in start_collected_nodes:
                ax.scatter(node.longitude, node.latitude, facecolor='none', edgecolor='gray',
                           linestyle='--', marker='o', s=150)
            for node in goal_collected_nodes:
                ax.scatter(node.longitude, node.latitude, facecolor='none', edgecolor='gray',
                           linestyle='--', marker='o', s=150)

            # Plot search region
            left, bottom, right, top = start_search_region
            plt.plot([left, left, right, right, left], [bottom, top, top, bottom, bottom], linestyle='--',
                     color='green', label='Start Search Region')
            left, bottom, right, top = goal_search_region
            plt.plot([left, left, right, right, left], [bottom, top, top, bottom, bottom], linestyle='--',
                     color='red', label='Goal Search Region')

            # Plot closest node (green / red)
            ax.scatter(start_closest_node.longitude, start_closest_node.latitude, facecolor='none', edgecolor='green',
                       marker='o', linewidth=3.0, s=150, label='Start Closest Node')
            ax.scatter(goal_closest_node.longitude, goal_closest_node.latitude, facecolor='none', edgecolor='red',
                       marker='o', linewidth=3.0, s=150, label='Goal Closest Node')

            # Plot the neighbors
            for neighbor in neighbors:
                ax.scatter(neighbor.longitude, neighbor.latitude, c='orange', marker='o', s=50,
                           label='Neighbors')


            ax.set_aspect('equal', 'box')
            ax.set_xlabel('Longitude')  # Set the x-axis label to 'Longitude'
            ax.set_ylabel('Latitude')  # Set the y-axis label to 'Latitude'
            ax.set_title('Node Data with Start & Goal Points and Closest Calculated Start & Goal Nodes')
            ax.legend(loc='upper center')
            plt.show()

        else:
            print("Node data is not available after deletion.")




#### vvvv FUNCTIONS vvvv ####
def deserialize_quad_tree(file_path):
    """
    Method to load a .qtdata file containing Chart Data in a quad tree data structure format
    Parameter: file_path: including data file
    Return: quadtree
    """
    with open(file_path, 'rb') as f:
        quadtree = pickle.load(f)
    return quadtree


if __name__ == '__main__':
    # Load QuadTree Data
    quadtree_data_path = (
        '/Users/dougveilleux/Documents/GitHub/UUVPathPlanningApp/'
        'data/quad_tree/west_island_medium.qtdata'
    )
    quadtree_data = deserialize_quad_tree(quadtree_data_path)
    # Visualize Quad Tree Data
    # quadtree_data.visualize_quadtree()

    # node_data = quadtree_data.collect_node_data()
    # print(node_data)

    # Define Start and Goal Points
    """
    Define these initially as hard code start and goal points.  Once working
        clicks from the GUI Map will set the points from event handlers.
    """
    # Start time
    start_time = time.time()
    startPoint = (-70.9035, 41.6278)
    goalPoint = (-70.8240, 41.6095)
    # print("Start Point:", startPoint)
    # print("Goal Point:", goalPoint)
    # Find closest nodes in the quad tree to Start and Goal points
    closest_start_node, closest_start_nodes, start_search_region = quadtree_data.find_closest_node(startPoint)
    closest_goal_node, closest_goal_nodes, goal_search_region = quadtree_data.find_closest_node(goalPoint)
    print(type(closest_start_node))
    # quadtree_data.plot_nearest_node(startPoint, goalPoint,
    #                             closest_start_node, closest_goal_node,
    #                             closest_start_nodes, closest_goal_nodes,
    #                             start_search_region, goal_search_region)
    # Plot takes 40 seconds with medium
    # End time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Start and Goal Nodes found in:", elapsed_time, "seconds\n")


    # Start time
    start_time = time.time()
    # Load Quad Data into AStarPathPlanner Class
    uuvIngressPath = AStarPathPlanner(quadtree_data)
    # End time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("AStar Class Instantiated in:", elapsed_time, "seconds\n")


    # Test the heuristic method
    # Start time
    start_time = time.time()
    print("Heuristic Distance Start to Goal:", uuvIngressPath.h_euclidean(closest_start_node, closest_goal_node))
    # End time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Start and Goal Heuristic Calculated in:", elapsed_time, "seconds\n")


    # Test the get_neighbors method
    # Start time
    start_time = time.time()

    start_neighbors = uuvIngressPath.get_neighbors(closest_start_node)
    goal_neighbors = uuvIngressPath.get_neighbors(closest_goal_node)
    # print(type(start_neighbors))
    for neighbor_node in goal_neighbors:
        print("Closest Neighbor Node: (Longitude: {}, Latitude: {}), LandOrWater: {}".format(neighbor_node.longitude,
                                                                                             neighbor_node.latitude,
                                                                                             neighbor_node.landOrWater))
    # End time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Get Neighbor Calculated in:", elapsed_time, "seconds\n")

    # Add more attributes as needed
    print()  # Print an empty line for better readability


    uuvIngressPath.plot_neighbors(start_neighbors, startPoint, goalPoint,
                                closest_start_node, closest_goal_node,
                                closest_start_nodes, closest_goal_nodes,
                                start_search_region, goal_search_region)

    uuvIngressPath.plot_neighbors(goal_neighbors, startPoint, goalPoint,
                                closest_start_node, closest_goal_node,
                                closest_start_nodes, closest_goal_nodes,
                                start_search_region, goal_search_region)





    # Plan the Path
    # path = uuvIngressPath.astar_plan_path(startPoint, goalPoint)
    # print(path)
