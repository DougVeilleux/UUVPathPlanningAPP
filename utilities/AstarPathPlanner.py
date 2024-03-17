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
    startPoint = (-70.9065, 41.6278)
    goalPoint = (-70.8240, 41.6095)
    # print("Start Point:", startPoint)
    # print("Goal Point:", goalPoint)
    # Find closest nodes in the quad tree to Start and Goal points
    closest_start_node, closest_start_nodes, start_search_region = quadtree_data.find_closest_node(startPoint)
    closest_goal_node, closest_goal_nodes, goal_search_region = quadtree_data.find_closest_node(goalPoint)
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
    print("Heuristic Distance Start to Goal:", uuvIngressPath.heuristic(closest_start_node, closest_goal_node))
    # End time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Start and Goal Heuristic Calculated in:", elapsed_time, "seconds\n")




    # Plan the Path
    # path = uuvIngressPath.astar_plan_path(startPoint, goalPoint)
    # print(path)
