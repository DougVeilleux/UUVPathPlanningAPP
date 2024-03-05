# astar_path_planner.py

import math
import heapq
import pickle

from utilities.quad_tree_geodata_multipolygon import *


class AStarPathPlanner:
    def __init__(self, quadtree):
        self.quadtree = quadtree

    def heuristic(self, node, goal_node):
        """
        Calculate the Euclidean distance
        """
        return math.sqrt((node.latitude - goal_node.latitude)**2 + (node.longitude - goal_node.longitude)**2)



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
    quadtree_data.visualize_quadtree()


    def count_nodes(node):
        if node is None:
            return 0
        # Count the current node and recursively count the nodes in its children
        return 1 + count_nodes(node.northWest) + count_nodes(node.northEast) + count_nodes(
            node.southEast) + count_nodes(node.southWest)
    # Example usage:
    total_nodes = count_nodes(quadtree_data.root)
    print("Total number of nodes:", total_nodes, "\n")


    # Accessing node data
    def print_node(node):
        # Check if the node is not None before accessing its attributes
        if node is not None:
            print(f"Latitude: {node.latitude}, Longitude: {node.longitude}, Is Land: {node.landOrWater}")

    def traverse_quadtree(node):
        # Base case: If the node is None, return
        if node is None:
            return
        # Print attributes of the current node
        print_node(node)
        # Recursively traverse the children of the current node
        traverse_quadtree(node.northWest)
        traverse_quadtree(node.northEast)
        traverse_quadtree(node.southEast)
        traverse_quadtree(node.southWest)


    # Example usage:
    NODES = traverse_quadtree(quadtree_data.root)


    def plot_node(node, ax):
        # Plot the node point
        ax.plot(node.longitude, node.latitude, c='tan' if node.landOrWater == 1 else 'blue', marker='o', markersize=1)

    def plot_quadtree(node, ax):
        # Base case: If the node is None, return
        if node is None:
            return
        # Plot the node point
        plot_node(node, ax)
        # Recursively plot the children of the current node
        plot_quadtree(node.northWest, ax)
        plot_quadtree(node.northEast, ax)
        plot_quadtree(node.southEast, ax)
        plot_quadtree(node.southWest, ax)

    # Create a new figure and axis for plotting
    fig, ax = plt.subplots(figsize=(14,9))
    # Plot the quadtree nodes
    plot_quadtree(quadtree_data.root, ax)
    # Set labels and title
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title('Quadtree Node Points')
    # Show the plot
    plt.show()