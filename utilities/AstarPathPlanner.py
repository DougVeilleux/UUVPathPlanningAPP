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

    def heuristic(self, node, goal_node):
        """
        Calculate the Euclidean distance
        """
        return math.sqrt((node.latitude - goal_node.latitude)**2 + (node.longitude - goal_node.longitude)**2)

    def astar_plan_path(self, start_point, goal_point):
        """
        This method contains the Astar method
        Parameter: start: (Longitude, Latitude) Point
                 : goal: (Longitude, Latitude) Point
        Returns: Path
        """
        start_node = self.find_node(start_point)
        goal_node = self.find_node(goal_point)

        if start_node is None or goal_node is None:
            return None

        open_set = []
        heapq.heappush(open_set, (0, start_node))
        came_from = {}
        g_score = {start_node: 0}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal_node:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start_node)
                path.reverse()
                return path

        for neighbor in self.get_neighbors(current):
            tentative_g_score = g_score[current] + 1

            if tentative_g_score < g_score.get(neighbor, math.inf):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + self.heuristic(neighbor, goal_node)
                heapq.heappush(open_set, (f_score, neighbor))

        return None



    def get_neighbors(self, node):
        """
        Get neighboring nodes of the given node from the quadtree and use the
        landOrWater value determine if this neighbor is a viable option to move.
        """
        neighbors = []
        # Check neighboring quadrants
        if node.northWest and node.northWest.landOrWater == 0:
            neighbors.append(node.northWest)
        if node.northEast and node.northEast.landOrWater == 0:
            neighbors.append(node.northEast)
        if node.southWest and node.southWest.landOrWater == 0:
            neighbors.append(node.southWest)
        if node.southEast and node.southEast.landOrWater == 0:
            neighbors.append(node.southEast)

        return neighbors

    def find_node(self, point):
        """
        Traverse the quadtree to find the node containing the given point
        """
        return self._find_node_recursive(self.quadtree.root, point)

    def _find_node_recursive(self, node, point):
        """
        Recursively find the node containing the given point
        """
        # Check if the node is a leaf
        if node.is_leaf:
            return node if node.contains_point(point) else None
        # traverse in if not a leaf
        for child in [node.northWest, node.northEast, node.southWest, node.southEast]:
            if child.contains_point(point):
                return self._find_node_recursive(child, point)

        return None






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
    'data/quad_tree/west_island_fine.qtdata'
    )
    quadtree_data = deserialize_quad_tree(quadtree_data_path)
    print(type(quadtree_data))
    print(quadtree_data)
    # Visualize Quad Tree Data
    # quadtree_data.visualize_quadtree()

    # node_data = quadtree_data.collect_node_data()
    # print(node_data)

    # Define Start and Goal Points
    """
    Define these initially as hard code start and goal points.  Once working
        clicks from the GUI Map will set the points from event handlers.
    """
    startPoint = (-70.84094, 41.58692)
    goalPoint = (-70.81589, 41.62664)
    print(startPoint)

    # Load Quad Data into AStarPathPlanner Class
    uuvIngressPath = AStarPathPlanner(quadtree_data)

    # Plan the Path
    path = uuvIngressPath.astar_plan_path(startPoint, goalPoint)
    print(path)







