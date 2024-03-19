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


    def astar_path(self, start_node, goal_node):
        """
        A Star path planning algorithm
        :param start_node: the start node with coordinates longitude, latitude, and landOrWater value
        :param goal_node: the goal node with coordinates longitude, latitude, and landOrWater value
        :return: path: list of coordinates defining the optimal A star path.
        """
        # Initialize the open set to keep track of the nodes yet to be evaluated
        open_set = [(0, start_node)]
        # Initialize came from to store the parent node (in the path) of each node in the current
        # shortest path
        came_from = {}
        # Initialize g score to store the cost of the shortest path found so far from the start node
        # set to ZERO to start becasue the cost to reach start_node from start = ZERO
        g_score = {start_node: 0}

        while open_set:
            # Get node with the lowest f_score value from the open set and set to current node
            _, current = heapq.heappop(open_set)
            # Check if goal has been found and return the path
            if current == goal_node:
                return self.reconstruct_path(came_from, current)

            # Loop through neighbor nodes and evaluate
            for neighbor in self.get_neighbors(current):
                # Calculate the g score of the neighbor node and sum with the euclidean distance
                # (could use other distance method to experiment with, e.g. Manhattan)
                tentative_g_score = g_score.get(current, float('inf')) + self.h_euclidean(current, neighbor)
                # Check if g score is less than previous g score for neighbor node.
                # If true, update the scores for the better path
                if tentative_g_score < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.h_euclidean(neighbor, goal_node)
                    # Add the neighbor to the priority queue with its f_score
                    heapq.heappush(open_set, (f_score, neighbor))

        return None  # Failed to find a path

    def reconstruct_path(self, came_from, current):
        """
        Construct the a star optimized path
        :param came_from: store the parent nodes of the path
        :param current: current node
        :return: total_path: the path in the correct order from start node to goal node
        """
        total_path = [current]
        while current in came_from:
            current = came_from[current]
            total_path.append(current)
        # Extract longitude and latitude from each node in total_path
        path = [(node.longitude, node.latitude) for node in total_path]
        return path[::-1]




    #vvvvv HELPER METHODS vvvvv
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


    #vvvvv PLOTTING METHODS
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
                       marker='o', linewidth=3.0, s=150, label='Closest Start Node')
            ax.scatter(goal_closest_node.longitude, goal_closest_node.latitude, facecolor='none', edgecolor='red',
                       marker='o', linewidth=3.0, s=150, label='Closest Goal Node')

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

    def visualize_astar_path(self, start_point, goal_point, start_closest_node, goal_closest_node, path):
        """

        :param start_point:
        :param goal_point:
        :param start_closest_node:
        :param goal_closest_node:
        :return:
        """
        # Create a new figure and axis
        fig, ax = plt.subplots(figsize=(14, 9))

        self.quadtree.visualize_chart_data(ax)

        # Plot points (green / red)
        ax.scatter(start_point[0], start_point[1], c='green', marker='*', s=150, label='Start Point')
        ax.scatter(goal_point[0], goal_point[1], c='red', marker='*', s=150, label='Goal Point')
        # Plot closest node (green / red)
        ax.scatter(start_closest_node.longitude, start_closest_node.latitude, facecolor='none', edgecolor='green',
                   marker='o', linewidth=1.0, s=100, label='Closest Start Node')
        ax.scatter(goal_closest_node.longitude, goal_closest_node.latitude, facecolor='none', edgecolor='red',
                   marker='o', linewidth=1.0, s=100, label='Closest Goal Node')

        # Plot the path
        if path:
            path_lon, path_lat = zip(*path)  # Unzip path coordinates
            ax.plot(path_lon, path_lat, color='blue', marker='o', linewidth=1, label='A* Path')

        # Setting Title
        ax.set_title('AStar Optimized Path', fontsize=20)
        ax.legend(loc='upper center')

        plt.show()



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
    startPoint = (-70.90, 41.61)
    # goalPoint = (-70.8240, 41.6095)
    goalPoint = (-70.88, 41.62)

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
    for neighbor_node in start_neighbors:
        print("Closest Start Neighbor Node: (Longitude: {}, Latitude: {}), LandOrWater: {}".format(
            neighbor_node.longitude,
            neighbor_node.latitude,
            neighbor_node.landOrWater))
    print()
    for neighbor_node in goal_neighbors:
        print("Closest Goal Neighbor Node: (Longitude: {}, Latitude: {}), LandOrWater: {}".format(
            neighbor_node.longitude,
            neighbor_node.latitude,
            neighbor_node.landOrWater))
    # End time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("\nGet Neighbor Calculated in:", elapsed_time, "seconds\n")

    # Add more attributes as needed
    print()  # Print an empty line for better readability


    # uuvIngressPath.plot_neighbors(start_neighbors, startPoint, goalPoint,
    #                             closest_start_node, closest_goal_node,
    #                             closest_start_nodes, closest_goal_nodes,
    #                             start_search_region, goal_search_region)
    #
    # uuvIngressPath.plot_neighbors(goal_neighbors, startPoint, goalPoint,
    #                             closest_start_node, closest_goal_node,
    #                             closest_start_nodes, closest_goal_nodes,
    #                             start_search_region, goal_search_region)


    # Test the astar_path method
    # Start time
    start_time = time.time()
    path = uuvIngressPath.astar_path(closest_start_node, closest_start_node)
    print(type(path))
    if path:
        print("Optimal A* Path:")
        for lon, lat in path:
            print("Longitude:", lon, ", Latitude:", lat)
    else:
        print("Failed to find a path.")
    # End time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("\nAStar Path Calculated in:", elapsed_time, "seconds\n")

    uuvIngressPath.visualize_astar_path(startPoint, goalPoint,
                                closest_start_node, closest_goal_node, path)

