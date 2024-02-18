# test_quad_grid.py
"""
Testing script which creates sample testing polygon geometry to develop
the QuadTree Class
"""
import geopandas as gpd
import matplotlib.pyplot as plt
import random
import numpy as np
from matplotlib import gridspec
from shapely.geometry import Point, Polygon, MultiPoint
from utilities.simple_polygon_builder import PolygonShapeBuilder, generate_sample_domain, plot_domain


class QTPoint:
    """
    Parameter: x: the x coordinate (longitude) of the point
    Parameter: y: the y coordinate (latitude) of the point
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


class QTRectangle:
    """
    Parameter: center: center of rectangle
    Parameter: width: 1/2 the full rectangle width because origin is center of rectangle
    Parameter: height: 1/2 the fill rectangle height because origin is center of rectangle

    Attribute: north: top edge of the rectangle
    Attribute: south: bottom edge of the rectangle
    Attribute: east: right edge of the rectangle
    Attribute: west: left edge of the rectangle

    """

    def __init__(self, center, width, height):
        self.center = center
        self.width = width
        self.height = height
        self.north = center.y + height
        self.south = center.y - height
        self.east = center.x + width
        self.west = center.x - width

    def containsPoint(self, point):
        return (self.west >= point.x < self.east
                and self.north >= point.y > self.south)

    def draw(self, ax, c='red', lw=1, **kwargs):
        x1, y1 = self.west, self.north
        x2, y2 = self.east, self.south
        ax.plot([x1, x2, x2, x1, x1], [y1, y1, y2, y2, y1], c=c, lw=lw, **kwargs)


class QuadTree:
    """

    Parameter: boundary, the boundary of the rectangle containing points
    Parameter: capacity, the number of points a rectangle can hold before
        having to subdivide
    """

    def __init__(self, boundary, capacity=2):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

    def insert(self, point):
        """

        Parameter: point to be inserted
        Return: bool
        """
        # if the point is in the range of the current quadtree
        if not self.boundary.containsPoint(point):
            return False

        # if has not reached capacity
        if len(self.points) < self.capacity:
            self.points.append(point)
            return True

        if not self.divided:
            self.divide()

        if self.nw.insert(point):
            return True
        elif self.ne.insert(point):
            return True
        elif self.sw.insert(point):
            return True
        elif self.se.insert(point):
            return True

        return False

    def divide(self):
        """
        Method: if divide conditions are met this will calculate the center point
            of the rectangle to divide, calculate the new width and height can
            create the new rectangles and recursively keep dividing by the QuadTree call
        """
        center_x = self.boundary.center.x
        center_y = self.boundary.center.y
        new_width = self.boundary.width / 2
        new_height = self.boundary.height / 2

        nw = QTRectangle(Point(center_x - new_width, center_y + new_height), new_width, new_height)
        self.nw = QuadTree(nw)
        ne = QTRectangle(Point(center_x + new_width, center_y + new_height), new_width, new_height)
        self.ne = QuadTree(ne)
        sw = QTRectangle(Point(center_x - new_width, center_y - new_height), new_width, new_height)
        self.sw = QuadTree(sw)
        se = QTRectangle(Point(center_x + new_width, center_y - new_height), new_width, new_height)
        self.se = QuadTree(se)

        self.divided = True

    def __len__(self):
        """
        Mehtod: override the length to recursively get the number of points in the tree
        Return: count, int, total number of points in the quad tree
        """
        count = len(self.points)
        if self.divided:
            count += len(self.nw) + len(self.ne) + len(self.se) + len(self.sw)
        return count

    def draw(self, ax):
        self.boundary.draw(ax)
        if self.divided:
            self.nw.draw(ax)
            self.ne.draw(ax)
            self.se.draw(ax)
            self.sw.draw(ax)


if __name__ == "__main__":

    # # Generate and Plot Simple Test Polygon
    # sample_domain_gdf = generate_sample_domain()
    # # plot_domain(sample_domain_gdf)
    #
    # water_domain = sample_domain_gdf.geometry.iloc[0]
    # exterior_points, interior_points = PolygonShapeBuilder.extract_polygon_points(water_domain)
    # all_points = exterior_points + interior_points
    # x_coords = [point[0] for point in all_points]
    # y_coords = [point[1] for point in all_points]

    # # Create scatter plot
    # plt.scatter(x_coords, y_coords, color='red', s=12)
    #
    # # Add labels and title
    # plt.xlabel('X')
    # plt.ylabel('Y')
    # plt.axis('equal')
    # plt.title('Scatter Plot of Points')
    #
    # # Show plot
    # plt.show()
    #
    # print(all_points)

    DPI = 72
    width, height = 600, 400
    N = 100
    xs = np.random.rand(N) * width
    ys = np.random.rand(N) * height
    points = [QTPoint(xs[i], ys[i]) for i in range(N)]

    domain = QTRectangle(QTPoint(width/2, height/2), width/2, height/2)
    quadtree = QuadTree(domain)

    for point in points:
        quadtree.insert(point)

    print('Total points: ', len(quadtree))

    # draw rectangles
    fig = plt.figure(figsize=(700 / DPI, 500 / DPI), dpi=DPI)
    ax = plt.subplot()
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    quadtree.draw(ax)

    # draw the points
    ax.scatter([p.x for p in points], [p.y for p in points], s=12)
    ax.set_xticks([])
    ax.set_yticks([])

    # format
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.axis('equal')
    plt.title('Quad Tree Rectangles and Points')
    plt.show()
    #
