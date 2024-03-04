# astar_path_planner.py

import math
import heapq
import pickle

from utilities.quad_tree_geodata_multipolygon import *


class AStar:
    def __init__(self, quadtree_data):
        self.quadtree_data = quadtree_data

    # Deserialize quad tree data structure from a file with specified file path





    def heuristic(self, node, goal):
        return math.sqrt((node.lat - goal.lat) ** 2 + (node.long - goal.long) ** 2)

    def astar(self, start, goal):
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {start: 0}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == goal:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path

            for neighbor in self.get_neighbors(current):
                tentative_g_score = g_score[current] + 1

                if tentative_g_score < g_score.get(neighbor, math.inf):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score = tentative_g_score + self.heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))

        return None

    def get_neighbors(self, node):
        # Get neighboring nodes of the given node from the quadtree
        # You can implement logic to traverse the quadtree efficiently here

        return []


def deserialize_quad_tree(file_path):
    with open(file_path, 'rb') as f:
        quad_tree = pickle.load(f)
    return quad_tree

if __name__ == '__main__':
    # Load QuadTree Data
    quadtree_data_path = (
    '/Users/dougveilleux/Documents/GitHub/UUVPathPlanningApp/'
    'data/quad_tree/west_island_fine.qtdata'
    )
    quad_tree_data = deserialize_quad_tree(quadtree_data_path)
    print(type(quad_tree_data))
    print(quad_tree_data)
    quad_tree_data.visualize_quadtree()




    # root = QuadTreeNode(0, 0, 1)  # Assuming initial root node is land
    # quadtree = QuadTree(root)
    # start = QuadTreeNode(start_lat, start_long, 1)  # Assuming start point is on land
    # end = QuadTreeNode(end_lat, end_long, 1)  # Assuming end point is on land
    #
    # astar = AStar(quadtree)
    # path = astar.astar(start, end)
    #
    # if path:
    #     print("Path found:", path)
    # else:
    #     print("No path found.")
