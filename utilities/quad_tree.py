# quad_tree.py

"""
Using https://en.wikipedia.org/wiki/Quadtree
as the reference

"""

import matplotlib.pyplot as plt
import numpy as np


class Point:
    """
    A point with (x,y) coordinates in a 2D plane / space.
    """
    def __init__(self, x, y):
        self.x = x  # x, coord.
        self.y = y  # y, coord.

    def distanceFrom(self, other):
        """
        Returns the distance between this point and another point.
        """
        dx = other.x - self.x
        dy = other.y - self.y
        return (dx ** 2 + dy ** 2) ** 0.5


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
    Boundary: is a Rectangle Object defining the region for which points are
    placed into this node.
    max_points_per_node: the max number of points a node can hold before
        it must be divided (branch into more nodes)
    depth: keeps track of how deep into the quadtree this node lies.
    """

    def __init__(self, boundary, depth=0, max_points_per_node=1):
        self.boundary = boundary
        self.depth = depth
        self.max_points_per_node = max_points_per_node
        self.points = []
        self.northWest = None
        self.northEast = None
        self.southWest = None
        self.southEast = None
        self.divided = False

    def insert(self, point):
        """
        Point insertion method
        """
        # check if point lies within the boundary
        if not self.boundary.contains_point(point):
            return False

        # check if there is room for point without dividing the QuadTree
        if len(self.points) < self.max_points_per_node:
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
        # Debug Code
        # print("Subdividing node at depth", self.depth)
        # print("Before subdivision - Boundary:", self.boundary.center.x, self.boundary.center.y, self.boundary.width,
        #       self.boundary.height)

        center = self.boundary.center
        half_width = self.boundary.width / 2.0
        half_height = self.boundary.height / 2.0

        nw_center = Point(center.x - half_width / 2, center.y + half_height / 2)
        ne_center = Point(center.x + half_width / 2, center.y + half_height / 2)
        sw_center = Point(center.x - half_width / 2, center.y - half_height / 2)
        se_center = Point(center.x + half_width / 2, center.y - half_height / 2)

        nw_boundary = Rectangle(nw_center, half_width, half_height)
        self.northWest = QuadTree(nw_boundary, self.depth + 1)
        ne_boundary = Rectangle(ne_center, half_width, half_height)
        self.northEast = QuadTree(ne_boundary, self.depth + 1)
        sw_boundary = Rectangle(sw_center, half_width, half_height)
        self.southWest = QuadTree(sw_boundary, self.depth + 1)
        se_boundary = Rectangle(se_center, half_width, half_height)
        self.southEast = QuadTree(se_boundary, self.depth + 1)

        self.divided = True
        # Debug Code
        # print("After subdivision - NW Boundary:", nw_boundary.center.x, nw_boundary.center.y, nw_boundary.width,
        #       nw_boundary.height)
        # print("After subdivision - NE Boundary:", ne_boundary.center.x, ne_boundary.center.y, ne_boundary.width,
        #       ne_boundary.height)
        # print("After subdivision - SW Boundary:", sw_boundary.center.x, sw_boundary.center.y, sw_boundary.width,
        #       sw_boundary.height)
        # print("After subdivision - SE Boundary:", se_boundary.center.x, se_boundary.center.y, se_boundary.width,
        #       se_boundary.height)


    # def query_range(self, range):

    def draw(self, ax):
        """
        Method to recursively draw the quadtree rectangles
        """
        self.draw_tree(ax, self)
    def draw_tree(self, ax, node, depth=0):
        """
        Method: Helper to draw
        """
        if node:
            node.boundary.draw(ax)
            self.draw_tree(ax, node.northWest, depth + 1)
            self.draw_tree(ax, node.northEast, depth + 1)
            self.draw_tree(ax, node.southWest, depth + 1)
            self.draw_tree(ax, node.southEast, depth + 1)
    def __str__(self):
        """Return a string representation of this node, suitably formatted."""
        sp = ' ' * self.depth * 2
        s = f"Depth {self.depth}: Boundary: {self.boundary.center.x}, {self.boundary.center.y}, {self.boundary.width}, {self.boundary.height}\n"
        if self.points:
            s += sp + "Points:\n"
            for point in self.points:
                s += sp + f"- {point.x}, {point.y}\n"
        if not self.divided:
            return s
        return s + '\n' + '\n'.join([
            sp + 'NW: \n' + str(self.northWest),
            sp + 'NE: \n' + str(self.northEast),
            sp + 'SE: \n' + str(self.southEast),
            sp + 'SW: \n' + str(self.southWest)])


if __name__ == '__main__':
    DPI = 72
    np.random.seed(60)

    N = 20
    x = np.random.rand(N)
    y = np.random.rand(N)
    # Calculate the width and height based on the range of x and y
    width = np.max(x) - np.min(x)
    height = np.max(y) - np.min(y)
    # Create a list of Point objects
    points = [Point(x[i], y[i]) for i in range(N)]
    for point in points:
        print(f"Point: ({point.x}, {point.y})")
    # Print width and height
    print("Width:", width)
    print("Height:", height)

    # Print all the points
    # for point in points:
    #     print("Point({}, {})".format(point.x, point.y))

    boundary = Rectangle(Point(width/2, height/2), width, height)
    qtree = QuadTree(boundary, max_points_per_node=2)
    for point in points:
        qtree.insert(point)

    # print(qtree)

    # Plot all the points
    fig = plt.figure(figsize=(8, 6))
    ax = plt.subplot()
    ax.scatter(x, y, color='blue', s=10)

    # Plot the quadtree boundaries
    qtree.draw(ax)

    # Set the limits for the plot
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)

    # Show the plot
    plt.show()


