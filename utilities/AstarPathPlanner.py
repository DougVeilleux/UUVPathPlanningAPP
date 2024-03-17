# AstarPathPlanner.py

import math
import heapq

from utilities.QuadTreeGeodata import *


class AStarPathPlanner:
    """
    This class contains the methods needed to generate a path plan from a start point
        and end up at a goal point.  These points given as a GPS coordinate.
    """

    def __init__(self, quadtree):
        """ Initialize the path planning object. """
        self.quadtree = quadtree

    def find_closest_node(self, point):
        """
        Find the closest node in the quadtree to the given point.
        :param point: the coordinate (longitude, latitude)
        :return: closest node the point
        """
        return self._find_closest_node_recursive(self.quadtree.root, point, float('inf'))

    def _find_closest_node_recursive(self, node, point, min_distance, closest_node=None):
        """
        Recursively find the closest node in the quad tree to the given point.
        :param node:
        :param point: the coordinate (longitude, latitude)
        :param min_distance: min distance to the node in decimal degrees
        :return: closest node
        """
        # Initialize closest_node variable if not provided
        if closest_node is None:
            closest_node = node

        # Calculate the distance between the point and the centroid of the current node
        distance = math.sqrt((node.latitude - point[1]) ** 2 + (node.longitude - point[0]) ** 2)

        # print("Node:", node.longitude, node.latitude)
        # print("Distance:", distance)

        # Update the closest node if the current node is closer
        if distance < min_distance:
            min_distance = distance
            closest_node = node

        # Otherwise, recursively search in the child nodes
        for child in [node.northWest, node.northEast, node.southWest, node.southEast]:
            if child:
                closest_node = self._find_closest_node_recursive(child, point, min_distance, closest_node)

        return closest_node




    def heuristic(self, current_node, goal_node):
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


    def get_neighbor(self, node):
        """
        Get the neighboring leaf nodes of the given node in the quad tree.
        :param node: the node whose leaf neighbors are to be retrieved
        :return: list of neighboring leaf nodes
        """
        neighbors = []
        print("Getting neighbors for node:", node)
        # Find the parent node of the given node
        parent = self.find_parent(node)
        # Add the parent node if it exists and is not the same as the leaf node
        if parent and parent != node:
            neighbors.append(parent)
        # Add leaf nodes at the same level as the given node (excluding the given node itself)
        self._get_leaf_neighbors(node, neighbors)
        print("Neighbors found:", [str(neighbor) for neighbor in neighbors])
        return neighbors

    def _get_neighbor_recursive(self, node, neighbors):
        """
        Recursively find neighboring nodes of the current node.
        :param node: The current node for which neighbors are being found.
        :return: A list of neighboring nodes
        """
        # Base case: If the current node is a leaf node, add it to neighbors
        if node.is_leaf:
            # Add the current leaf node to the neighbors list
            neighbors.append(node)
        else:
            # Explore the four child nodes of the current node
            for child in [node.northWest, node.northEast, node.southWest, node.southEast]:
                if child:
                    self._get_neighbor_recursive(child, neighbors)  # Pass neighbors to child nodes

    def _get_leaf_neighbors(self, node, neighbors):
        """
        Recursively collect neighboring leaf nodes at the same level as the given node.
        :param node: the node to start collecting neighbors from
        :param neighbors: list to collect leaf neighbors
        """
        # Find the parent node of the given node
        parent = self.find_parent(node)
        if parent is None:
            return

        # Traverse the quadtree at the same level as the given node's parent
        for child in [parent.northWest, parent.northEast, parent.southWest, parent.southEast]:
            if child and child != node:
                # Add leaf neighbors at the same level as the given node's parent
                self._get_leaf_neighbors_recursive(child, neighbors)

    def _get_leaf_neighbors_recursive(self, node, neighbors):
        """
        Recursively collect leaf neighbors starting from the given node.
        :param node: the node to start collecting neighbors from
        :param neighbors: list to collect leaf neighbors
        """
        if node.is_leaf:
            neighbors.append(node)
            return
        # Traverse the quadtree at the same level as the given node
        for child in [node.northWest, node.northEast, node.southWest, node.southEast]:
            if child:
                self._get_leaf_neighbors_recursive(child, neighbors)

    def find_parent(self, node, current_node=None):
        """
        Find the parent node of the given node in the quadtree.
        :param node: the node whose parent is to be found
        :param current_node: the current node being traversed (used in recursive calls)
        :return: the parent node of the given node
        """
        return self._find_parent_recursive(self.quadtree.root, node)

    def _find_parent_recursive(self, current_node, node):
        """
        Recursively find the parent node in the quadtree that contains the given node.
        :param current_node: the current node being checked
        :param node: the node to find the parent for
        :return: the parent node
        """
        if current_node.is_leaf or self.node_is_contained(node, current_node):
            return current_node
        else:
            for child in [current_node.northWest, current_node.northEast, current_node.southWest,
                          current_node.southEast]:
                if child and self.node_is_contained(node, child):
                    return self._find_parent_recursive(child, node)
        return None  # Node not found in the tree

    def node_is_contained(self, node, current_node):
        """
        Check if the given node is contained within the boundaries of the current node.
        :param node: the node to check containment for
        :param current_node: the current node whose boundaries are checked
        :return: True if the node is contained, False otherwise
        """
        return (current_node.min_x <= node.longitude <= current_node.max_x and
                current_node.min_y <= node.latitude <= current_node.max_y)




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
        'data/quad_tree/west_island_coarse.qtdata'
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
    startPoint = (-70.907744, 41.630625)
    goalPoint = (-70.816990, 41.581272)
    print("Start Point:", startPoint)
    print("Goal Point:", goalPoint)

    # Load Quad Data into AStarPathPlanner Class
    uuvIngressPath = AStarPathPlanner(quadtree_data)
    start_node = uuvIngressPath.find_closest_node(startPoint)
    goal_node = uuvIngressPath.find_closest_node(goalPoint)
    print("Start Node:", start_node.longitude, start_node.latitude)
    print("Goal Node:", goal_node.longitude, goal_node.latitude)

    # Test the heuristic method
    print("Heuristic Distance Start to Goal:", uuvIngressPath.heuristic(start_node, goal_node))

    # Test the get_neighbor method
    # print("Neighbors of the Start Node:", uuvIngressPath.get_neighbor(start_node))
    # print("Neighbors of the Goal Node:", uuvIngressPath.get_neighbor(goal_node))
    uuvIngressPath.get_neighbor(start_node)
    uuvIngressPath.get_neighbor(goal_node)



    # Plan the Path
    # path = uuvIngressPath.astar_plan_path(startPoint, goalPoint)
    # print(path)
