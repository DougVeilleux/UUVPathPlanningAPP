# quad_tree_geodata.py
import geopandas as gpd
import pandas as pd
from shapely.geometry import Polygon, MultiPolygon, Point, LineString, MultiLineString, box
from shapely.ops import unary_union
from matplotlib.patches import Polygon as MatplotlibPolygon
from utilities.shapefile_handler import *





class QuadTreeNode:
    """
    Class to define a QuadTree node which contains 4 children.  NW, NE, SE, & SW
        sub-region
    Parameter: domain_data, shapely geometry data for the quadtree to structure
               landOrWater, int - land / water classifier.  If =0-> water, if =1->land
    Attributes:
        northWest...southWest: represent children of the node in the four quadrants
        is_leaf: indicates whether the node is a leaf node (i.e. no children)
        is_boundary: indicates whether the node lies on the boundary of the data region
         (e.g. a water / land boundary)
    """
    def __init__(self, domain_data, landOrWater=None):
        self.domain_data = domain_data
        self.min_x, self.min_y, self.max_x, self.max_y = self.calculate_bounds()
        self.landOrWater = landOrWater
        self.northWest = None
        self.northEast = None
        self.southEast = None
        self.southWest = None
        self.is_leaf = True
        self.is_boundary = False

    def calculate_bounds(self):
        """
        Calculate the bounds of the domain_polygon.  Thru the recursive subdivide
            call this will be run at each new QuadTreeNode instantiation.
            Looking for a GeoDataFrame Type
        """
        if isinstance(self.domain_data, gpd.GeoDataFrame):
            # Extract geometries from the 'geometry' column
            geometries = self.domain_data['geometry']
            # Merge all geometries into a single MultiPolygon or MultiLineString
            merged_geometry = unary_union(geometries)
            bounds = merged_geometry.bounds
            # print("Calculated Bounds:", bounds)
            # Check for boundary intersection
            node_boundary = Polygon([(bounds[0], bounds[1]), (bounds[2], bounds[1]),
                                     (bounds[2], bounds[3]), (bounds[0], bounds[3])])
            self.is_boundary = node_boundary.intersects(merged_geometry)
            # print("is boundary:", self.is_boundary)
            return bounds
        else:
            print("Unknown geometry type:", type(self.domain_data))
            return 0, 0, 0, 0

    def subdivide(self):
        """
        Subdivide the node into four quadrants.  Called recursively thru the
        QuadTree class build_quadtree method.  The new polygon must be a type
        GeoDataFrame for the new QuadTreeNode instantiation to work properly
        """
        mid_x = (self.min_x + self.max_x) / 2
        mid_y = (self.min_y + self.max_y) / 2
        # Define vertices for each quadrant
        nw_vertices = [(self.min_x, mid_y), (mid_x, mid_y), (mid_x, self.max_y), (self.min_x, self.max_y)]
        ne_vertices = [(mid_x, mid_y), (self.max_x, mid_y), (self.max_x, self.max_y), (mid_x, self.max_y)]
        se_vertices = [(self.min_x, self.min_y), (mid_x, self.min_y), (mid_x, mid_y), (self.min_x, mid_y)]
        sw_vertices = [(mid_x, self.min_y), (self.max_x, self.min_y), (self.max_x, mid_y), (mid_x, mid_y)]
        # Create GeoDataFrame with Polygon for each quadrant
        # Just a data type conversion to keep
        nw_polygon = gpd.GeoDataFrame(geometry=[Polygon(nw_vertices)])
        ne_polygon = gpd.GeoDataFrame(geometry=[Polygon(ne_vertices)])
        se_polygon = gpd.GeoDataFrame(geometry=[Polygon(se_vertices)])
        sw_polygon = gpd.GeoDataFrame(geometry=[Polygon(sw_vertices)])

        # Create four child nodes
        self.northWest = QuadTreeNode(nw_polygon)
        self.northEast = QuadTreeNode(ne_polygon)
        self.southWest = QuadTreeNode(se_polygon)
        self.southEast = QuadTreeNode(sw_polygon)

        # Update leaf status
        self.is_leaf = False



class QuadTree:
    """
    Class to form QuadTree data structure of the land / water boundary
    Parameters:
        domain polygon: polygon data for the quadtree to structure
        node_length: float, represents the min length to recursively divide nodes
            down to at the land / water boundary
            @ lat of 0 deg
            note - 100m resolution ~= 0.001
                 - 500m resolution ~= 0.005
                 - 1000m resolution ~= 0.0001
            @ lat of 41 deg about 15-20% less than above

    """
    def __init__(self, domain_data, node_length=0.001):
        self.root = QuadTreeNode(domain_data)
        self.node_length = node_length

    def build_quadtree(self):
        """
        Build the quadtree structure recursively via the
        _build_quadtree_recursive helper method
        """
        print("Building quadtree...")
        self._build_quadtree_recursive(self.root)

    def _build_quadtree_recursive(self, node):
        """
        Recursively build the quadtree structure.
        """
        # print("Checking node:", node)
        if node.is_leaf:
            # print("Node is a leaf.")
            if self._node_needs_subdivision(node):
                # print("Node needs subdivision. Subdividing...")
                node.subdivide()
                for child in [node.northWest, node.northEast, node.southWest, node.southEast]:
                    self._build_quadtree_recursive(child)

    def _node_needs_subdivision(self, node):
        """
        Check if the node's boundary intersects with the domain_data.
        Returns: bools, both must be true
            boundary_intersects: determines boundary intersection, True -> needs subdividing
            large_enough: checks node length vs. node_length argument value True -> needs subdividing
        """
        node_boundary = Polygon([(node.min_x, node.min_y), (node.max_x, node.min_y),
                                 (node.max_x, node.max_y), (node.min_x, node.max_y)])
        line_strings = self.root.domain_data['geometry'].tolist()
        boundary_intersects = node_boundary.intersects(line_strings)

        # Check if the node is large enough to subdivide based on node_length
        width = node.max_x - node.min_x
        height = node.max_y - node.min_y
        large_enough = width > self.node_length or height > self.node_length

        # print("Boundary intersects:", boundary_intersects)
        # print("Large enough:", large_enough)

        # Subdivide if both conditions are met
        return boundary_intersects and large_enough

    def classify_nodes(self):
        """
        Classify nodes in the quadtree as land (1) or water (0) based on their length.
        """
        print("Classifying quadtree nodes...")
        # Get the land polygon from the domain data
        geo_data = self.root.domain_data['geometry'].tolist()
        land_polygon = unary_union(geo_data)

        # Start recursive classification
        self._classify_nodes_recursive(self.root, land_polygon)

    def _classify_nodes_recursive(self, node, land_polygon):
        """
        Recursively classify nodes as land or water based on contained geometries.
        """
        if node is not None:
            # Check if the node's boundary intersects with the land polygon
            node_boundary = Polygon([(node.min_x, node.min_y), (node.max_x, node.min_y),
                                     (node.max_x, node.max_y), (node.min_x, node.max_y)])
            node_intersects_land = node_boundary.intersects(land_polygon)
            # Set landOrWater value accordingly
            node.landOrWater = 1 if node_intersects_land else 0

            # Recursively classify child nodes
            self._classify_nodes_recursive(node.northWest, land_polygon)
            self._classify_nodes_recursive(node.northEast, land_polygon)
            self._classify_nodes_recursive(node.southWest, land_polygon)
            self._classify_nodes_recursive(node.southEast, land_polygon)

    def collect_node_data(self):
        """
        Collect node coordinates and landOrWater classification values.
        """
        node_data = []
        self._collect_node_data_recursive(self.root, node_data)
        return pd.DataFrame(node_data, columns=['min_x', 'min_y', 'max_x', 'max_y', 'landOrWater'])

    def _collect_node_data_recursive(self, node, node_data):
        """
        Recursively collect node coordinates and landOrWater classification values.
        """
        # Check if the node is a leaf node
        if node.is_leaf:
            # Append node coordinates and landOrWater value to node_data list
            node_data.append([node.min_x, node.min_y, node.max_x, node.max_y, node.landOrWater])
        else:
            # If the node is not a leaf node, collect data for its children recursively
            for child in [node.northWest, node.northEast, node.southWest, node.southEast]:
                self._collect_node_data_recursive(child, node_data)

    def delete_unnecessary_land_nodes(self):
        """
        Delete the land nodes that are not directly adjacent to a water node in the
        north, south, east, west directions
        """
        self._delete_inland_nodes_recursive(self.root)
        return

    def _delete_inland_nodes_recursive(self, node):
        """
        Recursively delete unnecessary land nodes.
        """
        if node is not None:
            if not node.is_leaf:
                # Recursively call the method for child nodes
                self._delete_inland_nodes_recursive(node.northWest)
                self._delete_inland_nodes_recursive(node.northEast)
                self._delete_inland_nodes_recursive(node.southEast)
                self._delete_inland_nodes_recursive(node.southWest)
                # If all children are leaf nodes and have the same landOrWater value, merge them
                if (node.northWest.is_leaf and node.northEast.is_leaf and
                        node.southEast.is_leaf and node.southWest.is_leaf and
                        node.northWest.landOrWater == node.northEast.landOrWater ==
                        node.southEast.landOrWater == node.southWest.landOrWater):
                    node.landOrWater = node.northWest.landOrWater
                    node.is_leaf = True
                    node.is_boundary = False
                    node.northWest = node.northEast = node.southEast = node.southWest = None
            else:
                # Check if node is a land node and if it is adjacent to water nodes
                # in the north, south, east, west directions
                if node.landOrWater == 1 and self._is_adjacent_to_water(node):
                    # Keep the land node
                    node.is_boundary = False
                else:
                    # Set node as boundary if it's not adjacent to water
                    node.is_boundary = True

    def _is_adjacent_to_water(self, node):
        """
        Check if the land node is adjacent to a water node in the north, south,
        east, west direction.
        """
        # Check if there is a water node in the north, south, east, or west direction
        return (self._has_water_in_direction(node, 'north') or
                self._has_water_in_direction(node, 'south') or
                self._has_water_in_direction(node, 'east') or
                self._has_water_in_direction(node, 'west'))

    def _has_water_in_direction(self, node, direction):
        """
        Check if there is a water node in the specified direction
        """
        # Determine the neighboring node based on the specified direction
        if direction == 'north':
            neighboring_node = node.northWest or node.northEast
        elif direction == 'south':
            neighboring_node = node.southWest or node.southEast
        elif direction == 'east':
            neighboring_node = node.northEast or node.southEast
        elif direction == 'west':
            neighboring_node = node.northWest or node.southWest

        # Check if the neighboring node is water
        return neighboring_node is not None and neighboring_node.landOrWater == 0




    #### vvvv PLOTTING vvvv ####
    def visualize_quadtree(self):
        # Create a new figure and axis
        fig, ax = plt.subplots(figsize=(14, 9))

        # Plot the initial bounding box representing water
        water_bounds = self.root.domain_data.unary_union.bounds
        water_polygon = Polygon([(water_bounds[0], water_bounds[1]), (water_bounds[2], water_bounds[1]),
                                 (water_bounds[2], water_bounds[3]), (water_bounds[0], water_bounds[3])])
        gpd.GeoSeries([water_polygon]).plot(ax=ax, color='lightblue')

        # Plot the linestring domain
        geo_data = self.root.domain_data['geometry'].tolist()
        gdf = gpd.GeoDataFrame(geometry=geo_data)
        gdf.plot(ax=ax, color='tan', linewidth=1, edgecolor='blue')

        # Plot the quadtree divisions
        self.plot_quadtree_partitions(self.root, ax)

        # FORMATING
        # Set plot title and labels
        ax.set_title('Data Domain with Quadtree Overlay')
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        # Add grid
        # ax.grid(True, which='both', linestyle='--', linewidth=0.5)

        # Show the plot
        plt.show()

    def plot_quadtree_partitions(self, node, ax):
        # Recursively plot the quadtree divisions
        # print("Plotting node...")
        if node is not None:
            if not node.is_leaf:
                # Plot the boundaries of the current node
                x = [node.min_x, node.max_x, node.max_x, node.min_x, node.min_x]
                y = [node.min_y, node.min_y, node.max_y, node.max_y, node.min_y]
                ax.plot(x, y, color='red', lw=0.5)

                # Plot the divisions of the child nodes
                # print("Plotting child nodes...")
                self.plot_quadtree_partitions(node.northWest, ax)
                self.plot_quadtree_partitions(node.northEast, ax)
                self.plot_quadtree_partitions(node.southWest, ax)
                self.plot_quadtree_partitions(node.southEast, ax)

    def plot_node_data(self, node_dataframe):
        """
        Plot node coordinates with landOrWater classification values.
        """
        fig, ax = plt.subplots(figsize=(14, 9))

        # Plot nodes
        for index, row in node_dataframe.iterrows():
            # Extract node coordinates
            min_x, min_y, max_x, max_y = row['min_x'], row['min_y'], row['max_x'], row['max_y']
            mid_x = (min_x + max_x) / 2
            mid_y = (min_y + max_y) / 2
            # Extract landOrWater value
            land_or_water = row['landOrWater']

            # Plot center point of the node
            ax.scatter(mid_x, mid_y, c='tan' if land_or_water == 1 else 'blue', marker='o', s=10)

        ax.set_aspect('equal', 'box')
        ax.set_xlabel('Longitude')  # Set the x-axis label to 'Longitude'
        ax.set_ylabel('Latitude')  # Set the y-axis label to 'Latitude'
        ax.set_title('Node Coordinates with Land or Water Classification')
        plt.show()

    def plot_node_data_after_deletion(self):
        """
        Plot node coordinates with landOrWater classification values after deletion of unnecessary land nodes.
        """
        # Collect node data after deletion (assuming you have a method for this)
        final_node_dataframe = self.collect_node_data()

        # Check if final_node_dataframe is not None (ensure deletion step was successful)
        if final_node_dataframe is not None:
            # Plot nodes
            fig, ax = plt.subplots(figsize=(14, 9))
            for index, row in final_node_dataframe.iterrows():
                # Extract node coordinates
                min_x, min_y, max_x, max_y = row['min_x'], row['min_y'], row['max_x'], row['max_y']
                mid_x = (min_x + max_x) / 2
                mid_y = (min_y + max_y) / 2
                # Extract landOrWater value
                land_or_water = row['landOrWater']
                # Plot center point of the node
                ax.scatter(mid_x, mid_y, c='tan' if land_or_water == 1 else 'blue', marker='o', s=10)
            ax.set_aspect('equal', 'box')
            ax.set_xlabel('Longitude')  # Set the x-axis label to 'Longitude'
            ax.set_ylabel('Latitude')  # Set the y-axis label to 'Latitude'
            ax.set_title('Node Coordinates with Land or Water Classification After Deletion')
            plt.show()
        else:
            print("Node data is not available after deletion.")



##=========================================================================================##
##=========================================================================================##
##=========================================================================================##
if __name__ == '__main__':
    shapefile_path = (
    '/Users/dougveilleux/Documents/GitHub/UUVPathPlanningApp/'
    'data/SHAPE_FILE/US4MA23M/US4MA23M_SHAPEFILE.shp'
    )

    chart_us4ma23m = ShapefileHandler(shapefile_path)
    # From shapefile object get the coords and linestring data
    coords = chart_us4ma23m.get_coordinate_data()
    domain_data = chart_us4ma23m.polygon_from_coords_data(coords, interpolate=False, showPlot=False)
    print(type(domain_data))
    print(domain_data)

    # Instantiate a QuadTree with the water domain polygon and the desired node length
    quad_tree = QuadTree(domain_data, node_length=0.0025)
    # Build the Quad Tree
    quad_tree.build_quadtree()
    # Visualize the Quad Tree
    quad_tree.visualize_quadtree()

    # Classify the nodes and Land or Water
    quad_tree.classify_nodes()
    # Collect the nodes and plot to confirm classification worked
    node_dataframe = quad_tree.collect_node_data()
    # plot node data
    quad_tree.plot_node_data(node_dataframe)
    # Delete unnecessary land nodes to reduce data set
    quad_tree.delete_unnecessary_land_nodes()
    # plot node to confirm deletion
    quad_tree.plot_node_data_after_deletion()
    # Visualize the Quad Tree
    quad_tree.visualize_quadtree()
