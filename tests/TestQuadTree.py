# TestQuadTree.py
"""
Testing script which reads a shapefile .shp data file and transforms that
    data into a QuadTree data structure
"""

from utilities.ShapefileHandler import *
from utilities.QuadTreeGeodata import *




##=========================================================================================##
if __name__ == '__main__':
    # Load the data
    shapefile_path = (
    '/Users/dougveilleux/Documents/GitHub/UUVPathPlanningApp/'
    'data/SHAPE_FILE/US4MA23M/US4MA23M_SHAPEFILE.shp'
    )
    # Instantiate the data object
    chart_us4ma23m = ShapefileHandler(shapefile_path)

    # Create a Selection box Manually for now.  Eventually this will come from mouse interaction
    x1, y1, x2, y2 = -70.8714, 41.573, -70.7866, 41.6372
    bounding_box = box(x1, y1, x2, y2)
    domain_data = chart_us4ma23m.make_land_polygon(showPlot=True, bounding_box=bounding_box)
    print(type(domain_data))
    print(domain_data)
    print("Bounding dimensions of domain_data before quadtree:", domain_data.total_bounds)

    # Instantiate a QuadTree with the domain data polygon and the desired node lengths
    quad_tree = QuadTree(domain_data, node_length_near_boundary=0.0001, node_length_far_from_boundary=0.01)

    # Build the Quad Tree
    # Start time
    start_time = time.time()
    quad_tree.build_quadtree()
    # End time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("\nQuad Tree Built in:", elapsed_time, "seconds\n")

    # Visualize the Quad Tree
    quad_tree.visualize_quadtree()

    # Classify the nodes and Land or Water
    # Start time
    start_time = time.time()
    quad_tree.classify_nodes()
    # End time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Nodes Classified in:", elapsed_time, "seconds\n")

    # Collect the nodes and plot to confirm classification worked
    # Start time
    start_time = time.time()
    node_dataframe = quad_tree.collect_node_data()
    # End time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Collected Node Data in:", elapsed_time, "seconds\n")
    # plot node data
    # quad_tree.plot_node_data(node_dataframe)

    # Delete unnecessary land nodes to reduce data set
    # Start time
    start_time = time.time()
    quad_tree.delete_unnecessary_land_nodes()
    # End time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Land Nodes Deleted in:", elapsed_time, "seconds\n")
    # plot node to confirm deletion
    quad_tree.plot_node_data_after_deletion()
    quad_tree.write_serialize_quad_tree('presentation.qtdata')

    # Visualize the Quad Tree (after node deletion)
    quad_tree.visualize_quadtree()