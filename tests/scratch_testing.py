
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.patches import Rectangle

from utilities.simple_polygon_builder import *
from shapely.geometry import box  # Import the box function

# Assuming you have a GeoDataFrame for the blue polygon
# blue_polygon = gpd.read_file('blue_polygon.shp')
blue_polygon = generate_sample_domain()

# Define the bounds of the space
minx, miny, maxx, maxy = blue_polygon.total_bounds


class QuadTreeNode:
    def __init__(self, bounds):
        self.bounds = bounds
        self.children = [None, None, None, None]  # NW, NE, SW, SE
        self.cost = None  # Cost associated with this node


def build_quadtree(bounds, depth):
    if depth == 0:
        return None

    node = QuadTreeNode(bounds)

    # Check if bounds intersect with the blue polygon
    intersect = blue_polygon.intersects(gpd.GeoSeries([box(*bounds)]))

    if intersect.any():
        # If intersection exists, assign lower cost
        node.cost = 0
    else:
        # If no intersection, assign higher cost
        node.cost = 1

    # Divide bounds into quadrants
    midx = (bounds[0] + bounds[2]) / 2
    midy = (bounds[1] + bounds[3]) / 2

    node.children[0] = build_quadtree((bounds[0], midy, midx, bounds[3]), depth - 1)  # NW
    node.children[1] = build_quadtree((midx, midy, bounds[2], bounds[3]), depth - 1)  # NE
    node.children[2] = build_quadtree((bounds[0], bounds[1], midx, midy), depth - 1)  # SW
    node.children[3] = build_quadtree((midx, bounds[1], bounds[2], midy), depth - 1)  # SE

    return node


# Function to visualize quadtree with different colors for different costs
def visualize_quadtree_cost(node, ax):
    if node:
        minx, miny, maxx, maxy = node.bounds
        cost = node.cost

        # Define color based on cost
        if cost == 0:
            color = 'lightblue'  # Lower cost
        else:
            color = 'lightgray'  # Higher cost

        ax.add_patch(Rectangle((minx, miny), maxx - minx, maxy - miny, fill=True, color=color))

        for child in node.children:
            visualize_quadtree_cost(child, ax)


def print_quadtree(node):
    if node:
        minx, miny, maxx, maxy = node.bounds
        center_x = (minx + maxx) / 2
        center_y = (miny + maxy) / 2
        cost = node.cost
        print(f"Bounds: ({minx}, {miny}), ({maxx}, {maxy}) | Center: ({center_x}, {center_y}) | Cost: {cost}")

        for child in node.children:
            print_quadtree(child)
# Example usage
depth = 4  # Adjust this according to desired level of detail
root = build_quadtree((minx, miny, maxx, maxy), depth)

fig, ax = plt.subplots()
visualize_quadtree_cost(root, ax)
blue_polygon.plot(ax=ax, color='blue', alpha=0.5)  # Overlay blue polygon for reference
plt.show()
print_quadtree(root)
