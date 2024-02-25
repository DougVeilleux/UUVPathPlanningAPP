# test_quad_tree.py
"""
Testing script which creates sample testing polygon geometry to develop
the QuadTree Class
"""

from utilities.shapefile_handler import *
from utilities.quad_tree_geodata import *


if __name__ == '__main__':
    shapefile_path = (
    '/Users/dougveilleux/Documents/GitHub/UUVPathPlanningApp/'
    'data/SHAPE_FILE/US4MA23M/US4MA23M_SHAPEFILE.shp'
    )

    chart_us4ma23m = ShapefileHandler(shapefile_path)
    # From shapefile object get the coords and linestring data
    coords = chart_us4ma23m.get_coordinate_data()
    domain_data = chart_us4ma23m.polygon_from_coords_data(coords, interpolate=False, showPlot=False)


    # Instantiate a QuadTree with the water domain polygon and the desired node length
    quad_tree = QuadTree(domain_data, node_length=0.00005)

    quad_tree.build_quadtree()
    quad_tree.visualize_quadtree()