# quad_tree.py

"""
Using https://en.wikipedia.org/wiki/Quadtree
as the reference

"""

import matplotlib.pyplot as plt
import numpy as np
import random



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

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

class Rectangle:
    """
    A rectangle with a center Point location and width and height definition
    Note: width and height are entered as half the rectangle width and height
        values to construct the rectangle from the center point
    """
    def __init__(self, center, half_width, half_height):
        self.center = center
        self.half_width = half_width
        self.half_height = half_height

    def contains_point(self, point):
        """
        Is a point (Point object) contained within the Rectangle
        """
        return (point.x > self.center.x - self.half_width and
                point.x < self.center.x + self.half_width and
                point.y > self.center.y - self.half_height and
                point.y < self.center.y + self.half_height)

    def intersects_rectangle(self, other):
        return not (self.center.x + self.half_width < other.center.x - other.half_width or
                    self.center.x - self.half_width > other.center.x + other.half_width or
                    self.center.y + self.half_height < other.center.y - other.half_height or
                    self.center.y - self.half_height > other.center.y + other.half_height)


class QuadTree:
    """
    Boundary: is a Rectangle Object defining the region for which points are
    placed into this node.
    capacity: the max number of points a node can hold before
        it must be divided (branch into more nodes)
    depth: keeps track of how deep into the quadtree this node lies.
    """
    def __init__(self, boundary, capacity=2, depth=0):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.northWest = None
        self.northEast = None
        self.southWest = None
        self.southEast = None
        self.divide = False
        self.depth = depth

    def insert(self, point):
        """
        Point insertion method
        """
        # Check if point lies within the boundary
        if not self.boundary.contains_point(point):
            return False
        # Check if there is room for point without dividing the QuadTree
        if len(self.points) < self.capacity:
            self.points.append(point)
            return True
        # Subdivide the node if it hasn't been subdivided yet
        if not self.divide:
            self.subdivide()
        # Recursively Insert Points
        return (self.northWest.insert(point) or
                self.northEast.insert(point) or
                self.southWest.insert(point) or
                self.southEast.insert(point))

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

        # Temp vars to make code easier to read
        x = self.boundary.center.x
        y = self.boundary.center.y
        half_width = self.boundary.half_width / 2
        half_height = self.boundary.half_height / 2

        nw_boundary = Rectangle(Point(x - half_width, y + half_height), half_width, half_height)
        self.northWest = QuadTree(nw_boundary, self.capacity, self.depth + 1)
        ne_boundary = Rectangle(Point(x + half_width, y + half_height), half_width, half_height)
        self.northEast = QuadTree(ne_boundary, self.capacity, self.depth + 1)
        sw_boundary = Rectangle(Point(x - half_width, y - half_height), half_width, half_height)
        self.southWest = QuadTree(sw_boundary, self.capacity, self.depth + 1)
        se_boundary = Rectangle(Point(x + half_width, y - half_height), half_width, half_height)
        self.southEast = QuadTree(se_boundary, self.capacity, self.depth + 1)

        self.divide = True

    def query_range(self, range_rect, found):
        if not self.boundary.intersects_rectangle(range_rect):
            return

        for point in self.points:
            if range_rect.contains_point(point):
                found.append(point)

        if self.northWest is None:
            return

        self.northWest.query_range(range_rect, found)
        self.northEast.query_range(range_rect, found)
        self.southWest.query_range(range_rect, found)
        self.southEast.query_range(range_rect, found)

    def draw(self):
        """
        Method to recursively draw the quadtree rectangles
        """
        fig, ax = plt.subplots(figsize=(14, 9))
        def draw_tree(node):
            if node is not None:
                # Calculate coordinates for the rectangle
                x = node.boundary.center.x - node.boundary.half_width
                y = node.boundary.center.y - node.boundary.half_height
                width = 2 * node.boundary.half_width
                height = 2 * node.boundary.half_height

                # Draw rectangle outline
                rect = plt.Rectangle((x, y), width, height,
                                     linewidth=1, edgecolor='r', facecolor='none')
                ax.add_patch(rect)

                # Draw points
                for point in node.points:
                    ax.plot(point.x, point.y, 'bo', markersize=3)

                draw_tree(node.northWest)
                draw_tree(node.northEast)
                draw_tree(node.southWest)
                draw_tree(node.southEast)

        draw_tree(self)
        plt.xlim(self.boundary.center.x - self.boundary.half_width, self.boundary.center.x + self.boundary.half_width)
        plt.ylim(self.boundary.center.y - self.boundary.half_height, self.boundary.center.y + self.boundary.half_height)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

    def __str__(self):
        """Return a string representation of this node, suitably formatted."""
        sp = ' ' * self.depth * 2
        s = f"Depth {self.depth}: Boundary: ({self.boundary.center.x}, {self.boundary.center.y}), ({self.boundary.half_width}, {self.boundary.half_height})\n"
        if self.points:
            s += sp + "Points:\n"
            for point in self.points:
                s += sp + f"- ({point.x}, {point.y})\n"
        if not self.divide:
            return s
        return s + '\n' + '\n'.join([
            sp + 'NW: \n' + str(self.northWest),
            sp + 'NE: \n' + str(self.northEast),
            sp + 'SE: \n' + str(self.southEast),
            sp + 'SW: \n' + str(self.southWest)])










if __name__ == "__main__":

    def generate_random_points(N, min_x, max_x, min_y, max_y):
        """
        Generate N random points within the specified range.

        Args:
            N (int): Number of points to generate.
            min_x (float): Minimum x-coordinate.
            max_x (float): Maximum x-coordinate.
            min_y (float): Minimum y-coordinate.
            max_y (float): Maximum y-coordinate.

        Returns:
            list: List of generated points.
        """
        points = []
        for _ in range(N):
            x = np.random.uniform(min_x, max_x)
            y = np.random.uniform(min_y, max_y)
            points.append(Point(x, y))
        return points




    random.seed(42)  # You can use any integer value as the seed

    width = 140
    height = 90
    # Define the boundary of the quadtree
    boundary = Rectangle(Point(0, 0), width, height)

    # Create a QuadTree with the specified boundary and capacity
    quadtree = QuadTree(boundary, capacity=2)

    # Define some points to insert into the quadtree
    N = 500  # Number of points to generate
    min_x = -width  # Minimum x-coordinate
    max_x = width  # Maximum x-coordinate
    min_y = -height  # Minimum y-coordinate
    max_y = height  # Maximum y-coordinate

    points = generate_random_points(N, min_x, max_x, min_y, max_y)

    # Insert the points into the quadtree
    for point in points:
        quadtree.insert(point)

    # Draw the quadtree and points
    quadtree.draw()
    # print(quadtree)