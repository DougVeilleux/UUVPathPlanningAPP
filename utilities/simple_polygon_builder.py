# simple_polygon_builder.py

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import Polygon, Point, MultiPolygon

class PolygonShapeBuilder:
    @staticmethod
    def rectangle(nw_point, ne_point, se_point, sw_point):
        """
        Take in 4 Points (Shapely type)
        Parameters:
        - nw_point: Point
        - ne_point: Point
        - se_point: Point
        - sw_pont: Point
        Returns:
        - GeoDataFrame: GeoDataFrame containing the rectangular polygon
        """
        polygon = Polygon([nw_point, ne_point, se_point, sw_point])
        return gpd.GeoDataFrame(geometry=[polygon])
    @staticmethod
    def circle(x_pos, y_pos, radius, num_segments=50):
        """
        Create a circular polygon with a given center point and radius.
        Parameters:
        - x_pos: float, x-coordinate of the center point
        - y_pos: float, y-coordinate of the center point
        - radius: float, radius of the circle
        - num_segments: int, number of line segments to approximate the circle
        Returns:
        - GeoDataFrame: GeoDataFrame containing the circular polygon
        """
        angles = np.linspace(0, 2*np.pi, num_segments)
        x = x_pos + radius*np.cos(angles)
        y = y_pos + radius*np.sin(angles)
        circle_points = [Point(x_i, y_i) for x_i, y_i in zip(x,y)]
        circle = Polygon(circle_points)
        return gpd.GeoDataFrame(geometry=[circle])
    @staticmethod
    def triangle(point1, point2, point3):
        """
        Create a triangle polygon from three points.
        Parameters:
        - point1: shapely.geometry.Point, first vertex of the triangle
        - point2: shapely.geometry.Point, second vertex of the triangle
        - point3: shapely.geometry.Point, third vertex of the triangle
        Returns:
        - GeoDataFrame: GeoDataFrame containing the triangle polygon
        """
        triangle = Polygon([point1, point2, point3, point1])
        return gpd.GeoDataFrame(geometry=[triangle])

    @staticmethod
    def extract_polygon_points(polygon):
        """
        Extracts exterior and interior points of a polygon.
        Parameters:
        - polygon: shapely.geometry.Polygon, input polygon

        Returns:
        - exterior_points: list of tuples, exterior points of the polygon
        - interior_points: list of tuples, interior points of the polygon
        """
        exterior_points = list(polygon.exterior.coords)
        interior_points = []
        for interior in polygon.interiors:
            interior_points.extend(list(interior.coords))
        return exterior_points, interior_points

def generate_sample_domain():
    # Define coordinates for the corners of the rectangle
    nw = Point(0, 10)  # Northwest corner
    ne = Point(20, 10)  # Northeast corner
    se = Point(20, 0)  # Southeast corner
    sw = Point(0, 0)  # Southwest corner

    rectangle_gdf = PolygonShapeBuilder.rectangle(nw, ne, se, sw)
    circle_gdf1 = PolygonShapeBuilder.circle(x_pos=6, y_pos=2, radius=0.5, num_segments=10)
    circle_gdf2 = PolygonShapeBuilder.circle(x_pos=3, y_pos=5, radius=1, num_segments=15)
    circle_gdf3 = PolygonShapeBuilder.circle(x_pos=12, y_pos=6, radius=1.5, num_segments=20)
    tp1 = Point(15, 0)
    tp2 = se
    tp3 = Point(20, 3)
    triangle_gdf1 = PolygonShapeBuilder.triangle(tp1, tp2, tp3)
    tp1 = Point(7.5, 6)
    tp2 = Point(8.0, 9.5)
    tp3 = Point(5, 8)
    triangle_gdf2 = PolygonShapeBuilder.triangle(tp1, tp2, tp3)

    sample_domain_gdf = rectangle_gdf.difference(circle_gdf1)
    sample_domain_gdf = sample_domain_gdf.difference(circle_gdf2)
    sample_domain_gdf = sample_domain_gdf.difference(circle_gdf3)
    sample_domain_gdf = sample_domain_gdf.difference(triangle_gdf1)
    sample_domain_gdf = sample_domain_gdf.difference(triangle_gdf2)

    return sample_domain_gdf

def plot_domain(quad_domain_gdf):
    # Plot Polygons
    fig, ax = plt.subplots(figsize=(14, 9))
    quad_domain_gdf.plot(ax=ax, color='lightblue', edgecolor='black')

    # Extract exterior and interior points of the polygon
    polygon = quad_domain_gdf.geometry.iloc[0]
    exterior_points, interior_points = PolygonShapeBuilder.extract_polygon_points(polygon)

    # Plot exterior and interior points
    exterior_x, exterior_y = zip(*exterior_points)
    interior_x, interior_y = zip(*interior_points)
    ax.scatter(exterior_x, exterior_y, color='red', s=12, label='Exterior Points')
    ax.scatter(interior_x, interior_y, color='blue', s=12, label='Interior Points')

    # vvv FORMATTING vvv
    # Set axis labels
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    # Add grid
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    # Setting Title
    ax.set_title('Quad Tester Domain', fontsize=20)
    # Show plot
    plt.show()









if __name__ == '__main__':
    quad_domain_gdf = generate_sample_domain()
    plot_domain(quad_domain_gdf)