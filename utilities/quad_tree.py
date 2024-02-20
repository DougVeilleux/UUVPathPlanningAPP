# quad_tree.py

"""
Using https://en.wikipedia.org/wiki/Quadtree
as the reference

"""

import matplotlib.pyplot as plt

class Point:
    """
    A point with (x,y) coordinates in a 2D plane / space.
    """
    def __init__(self, x, y):
        self.x = x  # x, coord.
        self.y = y  # y, coord.

class Rectangle:
    """
    A rectangle with a center Point location and width and height definition
    """
    def __init__(self, center, width, height):
        self.center = center
        self.width = width
        self.height = height


    def contains_point(self, point):
        """
        Is a point (Point object) contained within the Rectangle
        """
        half_width = self.width/2
        half_height = self.height/2
        return (self.center.x - half_width <= point.x <= self.center.x + half_width) and \
                (self.center.y - half_height <= point.y <= self.center.y + half_height)

    def intersects_rectangle(self, other):
        half_width1 = self.width/2
        half_height1 = self.height/2
        half_width2 = other.width/2
        half_height2 = other.height/2

        return (abs(self.center.x - other.center.x) < (half_width1 + half_width2)) and \
            (abs(self.center.y - other.center.y) < (half_height1 + half_height2))

    def draw(self, ax, c='k', lw=1, **kwargs):
        half_width = self.width / 2
        half_height = self.height / 2
        x1, y1 = self.center.x - half_width, self.center.y - half_height
        x2, y2 = self.center.x + half_width, self.center.y + half_height
        ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], c=c, lw=lw, **kwargs)


class QuadTree:
    """
    Boundary is a Rectangle Object defining the region for which points are
    placed into this node.
    MAX_POINTS_PER_NODE: the max number of points a node can hold before
        it must be divided (branch into more nodes)
    depth: keeps track of how deep into the quadtree this node lies.
    """
    MAX_POINTS_PER_NODE = 1

    def __init__(self, boundary, depth=0):
        self.boundary = boundary
        self.depth = depth
        self.points = []
        self.northWest = None
        self.northEast = None
        self.southWest = None
        self.southEast = None

    def insert(self, point):
        """
        Point insertion method
        """
        # check if point lies within the boundary
        if not self.boundary.contains_point(point):
            return False

        # check if there is room for point without dividing the QuadTree
        if len(self.points) < self.MAX_POINTS_PER_NODE:
            self.points.append(point)
            return True
        else: #Subdivide the node if it hasn't been subdivided yet
            if self.northWest is None:
                self.subdivide()

            # Attempt to insert the point into one of the child nodes
            if self.northWest.insert(point):
                return True
            elif self.northEast.insert(point):
                return True
            elif self.southWest.insert(point):
                return True
            elif self.southEast.insert(point):
                return True

            # Point cannot be inserted (should never happen)
            return False

    def subdivide(self):
        """
        Method subdivides the current quadtree node into four child nodes.  Each
            representing one quadrant of the parent node's boundary.  Continues
            recursively until each node contains the max number of points.
        """
        center = self.boundary.center
        half_width = self.boundary.width / 2.0
        half_height = self.boundary.height / 2.0

        nw_boundary = Rectangle(Point(center.x - half_width, center.y + half_height),
                                half_width, half_height)
        self.northWest = QuadTree(nw_boundary, self.depth + 1)

        ne_boundary = Rectangle(Point(center.x + half_width, center.y + half_height),
                                half_width, half_height)
        self.northEast = QuadTree(ne_boundary, self.depth + 1)

        sw_boundary = Rectangle(Point(center.x - half_width, center.y - half_height),
                                half_width, half_height)
        self.southWest = QuadTree(sw_boundary, self.depth + 1)

        se_boundary = Rectangle(Point(center.x + half_width, center.y - half_height),
                                half_width, half_height)
        self.southEast = QuadTree(se_boundary, self.depth + 1)

    # def query_range(self, range):

    def draw(self, ax):
        """
        Method to recursively draw the quadtree and its points
        """
        self.boundary.draw(ax, c='black', lw=1)

        for point in self.points:
            ax.plot(point.x, point.y, 'ro', markersize=2)

        if self.northWest:
            self.northWest.draw(ax)
        if self.northEast:
            self.northEast.draw(ax)
        if self.southWest:
            self.southWest.draw(ax)
        if self.southEast:
            self.southEast.draw(ax)




import random
import numpy as np
DPI = 72
np.random.seed(60)

width, height = 600, 400
N =500

coords = np.random.randn(N, 2) * height/3 + (width/2, height/2)
points = [Point(*coord) for coord in coords]

boundary = Rectangle(Point(width/2, height/2), width, height)
qtree = QuadTree(boundary)
for point in points:
    qtree.insert(point)


fig = plt.figure(figsize=(700/DPI, 500/DPI), dpi=DPI)
ax = plt.subplot()
ax.set_xlim(0, width)
ax.set_ylim(0, height)
qtree.draw(ax)




plt.show()





