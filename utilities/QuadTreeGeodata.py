# QuadTreeGeodata.py
"""
D. Veilleux, Feb. 2024

Contained within are classes to create a quad tree data structure to
    represent land / water boundary information when a GeoSeries
    Multipolygon is provided.
Methods to process, display and write quad tree to a file are included.

"""

import time
import pickle
import math

import matplotlib.pyplot as plt
from geopy.distance import geodesic
from shapely.ops import nearest_points
from utilities.ShapefileHandler import *


class QuadTreeNode:
    """
    Class to define a QuadTree node which contains 4 children.  NW, NE, SE, & SW
        sub-region
    Parameter: domain_data, shapely geometry data for the quadtree to structure
               landOrWater, int - land / water classifier.  If =0-> water, if =1->land
    Attributes:
        northWest...southWest: represent children of the node in the four quadrants
        min_x, max_x, min_y, max_y are the bounds of the node
        latitude and longitude are the center of the node
        point: (longitude, latitude) tuple representing the center of the node
        is_leaf: indicates whether the node is a leaf node (i.e. no children)
        is_boundary: indicates whether the node lies on the boundary of the data region
         (e.g. a water / land boundary)
    """
    def __init__(self, domain_data, landOrWater=None):
        self.domain_data = domain_data
        self.landOrWater = landOrWater
        self.min_x, self.min_y, self.max_x, self.max_y = self.calculate_bounds()
        self.longitude = (self.min_x + self.max_x) / 2
        self.latitude = (self.min_y + self.max_y) / 2
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
            bounds = self.domain_data.bounds
            min_x = bounds['minx'].min()
            min_y = bounds['miny'].min()
            max_x = bounds['maxx'].max()
            max_y = bounds['maxy'].max()
            # Check for boundary intersection
            node_boundary = Polygon([(min_x, min_y), (max_x, min_y),
                                     (max_x, max_y), (min_x, max_y)])
            self.is_boundary = node_boundary.intersects(self.domain_data.unary_union)
            return min_x, min_y, max_x, max_y
        elif isinstance(self.domain_data, gpd.GeoSeries):
            bounds = self.domain_data.bounds
            min_x = bounds['minx'].min()
            min_y = bounds['miny'].min()
            max_x = bounds['maxx'].max()
            max_y = bounds['maxy'].max()
            return min_x, min_y, max_x, max_y
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

    def contains_point(self, point):
        """
        Check if the given point lies within the bounds of this node.
        """
        x, y = point
        return self.min_x <= x <= self.max_x and self.min_y <= y <= self.max_y




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
                 - ~10m resolution ~= 0.0001
                 - ~42m resolution ~= 0.0005
            @ lat of 41 deg about 15-20% less than above
    """
    def __init__(self, domain_data, node_length_near_boundary=0.001, node_length_far_from_boundary=0.1):
        # Initialize the root node
        self.root = QuadTreeNode(domain_data)
        self.node_length_near_boundary = node_length_near_boundary
        self.node_length_far_from_boundary = node_length_far_from_boundary
        self.recursion_counter = 0
        self.original_bounds = self.calculate_original_bounds()

    def calculate_original_bounds(self):
        if isinstance(self.root.domain_data, gpd.GeoDataFrame):
            geometries = self.root.domain_data['geometry']
            merged_geometry = unary_union(geometries)
            bounds = merged_geometry.bounds
            return bounds
        elif isinstance(self.root.domain_data, gpd.GeoSeries):
            min_x = min_y = float('inf')
            max_x = max_y = float('-inf')
            for polygon in self.root.domain_data:
                poly_bounds = polygon.bounds
                min_x = min(min_x, poly_bounds[0])
                min_y = min(min_y, poly_bounds[1])
                max_x = max(max_x, poly_bounds[2])
                max_y = max(max_y, poly_bounds[3])
            return min_x, min_y, max_x, max_y
        else:
            print("Unknown geometry type:", type(self.root.domain_data))
            return 0, 0, 0, 0

    def build_quadtree(self):
        """
        Build the quadtree structure recursively via the
        _build_quadtree_recursive helper method
        """
        print("Building quadtree...")
        # Recursively build the quadtree
        self._build_quadtree_recursive(self.root)

    def _build_quadtree_recursive(self, node, recursion_count=0):
        """
        Recursively build the quadtree structure.
        """
        # Increment the recursion count
        recursion_count += 1
        # Print status message every 100 recursions
        if recursion_count % 100 == 0:
            print("Recursively dividing...")

        # print("Checking node:", node)
        if node.is_leaf:
            # print("Node is a leaf.")
            if self._node_needs_subdivision(node):
                # print("Node needs subdivision. Subdividing...")
                node.subdivide()
                for child in [node.northWest, node.northEast, node.southWest, node.southEast]:
                    self._build_quadtree_recursive(child, recursion_count)

    def _node_needs_subdivision(self, node):
        """
        Check if the node's boundary intersects with the domain_data.
        Returns: bools, both must be true
            boundary_intersects: determines boundary intersection, True -> needs subdividing
            large_enough: checks node length vs. node_length argument value True -> needs subdividing
        """
        node_boundary = Polygon([(node.min_x, node.min_y), (node.max_x, node.min_y),
                                 (node.max_x, node.max_y), (node.min_x, node.max_y)])
        # Print the node_boundary for debugging
        # print("Node Boundary:", node_boundary)

        multi_polygon = self.root.domain_data.unary_union
        # Print the node_boundary for debugging
        # print("MultiPolygon Boundary:", node_boundary.boundary)

        boundary_intersects = node_boundary.intersects(multi_polygon.boundary)

        # Calculate the nearest points from the node center to the multi_polygon boundary (land)
        nearest_point_node, nearest_point_boundary = nearest_points(node_boundary.centroid, multi_polygon.boundary)
        # Calculate the distance from the node to the nearest boundary
        distance_to_boundary_meters = geodesic((nearest_point_node.y, nearest_point_node.x),
                                               (nearest_point_boundary.y, nearest_point_boundary.x)).meters

        # Set node_length based of the distance from the boundary
        threshold_distance = 1000  # meters
        if distance_to_boundary_meters < threshold_distance:
            node_length = self.node_length_near_boundary
        else:
            node_length = self.node_length_far_from_boundary

        # Check if the node is large enough to subdivide based on node_length
        width = node.max_x - node.min_x
        height = node.max_y - node.min_y
        large_enough = width > node_length or height > node_length

        # Increment the subdivision counter
        self.recursion_counter += 1

        if self.recursion_counter % 100 == 0:
            print("")
            print("Recursion Counter:", self.recursion_counter)
            print("Node distance to the nearest boundary:", distance_to_boundary_meters)
            print("Node Length:", node_length)
            print("Boundary intersects:", boundary_intersects)
            print("Large enough:", large_enough)
            if boundary_intersects and large_enough:
                print("Dividing Node...")

        # Subdivide if both conditions are met
        return boundary_intersects and large_enough




    #### vvvv HELPERS vvvv####
    def classify_nodes(self):
        """
        Classify nodes in the quadtree as land (1) or water (0) based on their length.
        """
        print("Classifying quadtree nodes...")
        # Get the land polygon from the domain data
        # geo_data = self.root.domain_data['geometry'].tolist()
        land_polygon = self.root.domain_data.unary_union

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
        return pd.DataFrame(node_data,
                            columns=['longitude', 'latitude', 'min_x', 'min_y', 'max_x', 'max_y', 'landOrWater'])

    def _collect_node_data_recursive(self, node, node_data):
        """
        Recursively collect node coordinates and landOrWater classification values.
        """
        # Calculate longitude and latitude
        longitude = (node.min_x + node.max_x) / 2
        latitude = (node.min_y + node.max_y) / 2

        # Check if the node is a leaf node
        if node.is_leaf:
            # Append node coordinates and landOrWater value to node_data list
            node_data.append([longitude, latitude, node.min_x, node.min_y, node.max_x, node.max_y, node.landOrWater])
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

    def find_closest_node(self, point, search_radius=0.015):
        """
        Find the closest node in the quadtree to the given point within a search radius.
        :param point: the coordinate (longitude, latitude)
        :param search_radius: the radius within which to search for the closest node
        :return: closest node within the search radius
        """
        search_region = (
            point[0] - search_radius,  # left
            point[1] - search_radius,  # bottom
            point[0] + search_radius,  # right
            point[1] + search_radius  # top
        )
        search_region_nodes = self._find_closest_node_recursive(self.root, point, search_region)

        # Calculate the Euclidean distance between each node and the given point
        min_distance = float('inf')
        closest_node = None
        for node in search_region_nodes:
            distance = math.sqrt((node.longitude - point[0]) ** 2 + (node.latitude - point[1]) ** 2)
            if distance < min_distance:
                min_distance = distance
                closest_node = node

        return closest_node, search_region_nodes, search_region

    def _find_closest_node_recursive(self, node, point, search_region, nodes=None):
        """
        Recursively find the closest node in the quadtree to the given point within the search region.
        :param node: the current node being considered
        :param point: the coordinate (longitude, latitude)
        :param search_region: the region within which to search for the closest node
        :return: nodes within the search region
        """

        # Check if the bounding box of the node intersects with the search region
        if nodes is None:
            nodes = []

        if self._intersects_search_region(node, search_region):
            nodes.append(node)

            # Check if the node is a leaf node
            if node.northWest is None:
                return nodes

        # Recursively search in the child nodes
        for child in [node.northWest, node.northEast, node.southWest, node.southEast]:
            if child:
                self._find_closest_node_recursive(child, point, search_region, nodes)

        return nodes

    def _intersects_search_region(self, node, search_region):
        """
        Check if the node intersects with the given search region.
        :param node: the node to check for intersection
        :param search_region: the search region defined by (left, bottom, right, top)
        :return: True if the node intersects the search region, False otherwise
        """

        # Check if the bounding box of the node intersects with the search region
        intersects = (node.longitude >= search_region[0] and node.longitude <= search_region[2] and
                      node.latitude >= search_region[1] and node.latitude <= search_region[3])
        return intersects

    def get_neighbors(self, target_node, search_radius=0.015):
        """
        Get the neighbors of a given node in the quadtree
        :param target_node: the target _node is the node for which neighbors are being sought
        :return: neighbors: list neighbor nodes
        """
        # Define empty neighbors list
        neighbors = []

        # assembly "point" to match required type for .find_closest_node
        point = (target_node.longitude, target_node.latitude)
        # Find target_node in the tree with find.closest_node method.  Reuse of method to find
        # closest node for start and goal points.  Still works and traverses the tree
        current_node, nodes_near_target, initial_search_region = self.find_closest_node(point, search_radius)
        # print("Found Target node: ", current_node.longitude, current_node.latitude)

        # Define empty lists for neighbors in each half / quadrant
        n_neighbors = []
        s_neighbors = []
        e_neighbors = []
        w_neighbors = []
        ne_neighbors = []
        se_neighbors = []
        sw_neighbors = []
        nw_neighbors = []

        n_distance = float('inf')
        s_distance = float('inf')
        e_distance = float('inf')
        w_distance = float('inf')
        ne_distance = float('inf')
        se_distance = float('inf')
        sw_distance = float('inf')
        nw_distance = float('inf')
        # Iterate through nodes near the target to find neighbors in each quadrant
        for node in nodes_near_target:
            # Calculate Euclidean distance between nod and current_node
            distance = math.sqrt(
                (current_node.latitude - node.latitude) ** 2
                + (current_node.longitude - node.longitude) ** 2)

            # N Half
            if node.latitude > current_node.latitude:
                if distance < n_distance:
                    n_neighbors = [node]
                # n_neighbors.append(node)
                    n_distance = distance

            # S Half
            if node.latitude < current_node.latitude:
                if distance < s_distance:
                    s_neighbors = [node]
                # s_neighbors.append(node)
                    s_distance = distance

            # E Half
            if node.longitude > current_node.longitude:
                if distance < e_distance:
                    e_neighbors = [node]
                # e_neighbors.append(node)
                    e_distance = distance

            # W Half
            if node.longitude < current_node.longitude:
                if distance < w_distance:
                    w_neighbors = [node]
                # w_neighbors.append(node)
                    w_distance = distance

            # NE Quadrant
            if node.longitude > current_node.longitude and node.latitude > current_node.latitude:
                if distance < ne_distance:
                    ne_neighbors = [node]
                # ne_neighbors.append(node)
                    ne_distance = distance
            # SE Quadrant
            elif node.longitude > current_node.longitude and node.latitude < current_node.latitude:
                if distance < se_distance:
                    se_neighbors = [node]
                # se_neighbors.append(node)
                    se_distance = distance
            # SW Quadrant
            elif node.longitude < current_node.longitude and node.latitude < current_node.latitude:
                if distance < sw_distance:
                    sw_neighbors = [node]
                # sw_neighbors.append(node)
                    sw_distance = distance
            # NW Quadrant
            elif node.longitude < current_node.longitude and node.latitude > current_node.latitude:
                if distance < nw_distance:
                    nw_neighbors = [node]
                # nw_neighbors.append(node)
                    nw_distance = distance

        # Append neighbors from all quadrants to the neighbors list
        neighbors.extend(n_neighbors)
        neighbors.extend(s_neighbors)
        neighbors.extend(e_neighbors)
        neighbors.extend(w_neighbors)
        neighbors.extend(ne_neighbors)
        neighbors.extend(se_neighbors)
        neighbors.extend(sw_neighbors)
        neighbors.extend(nw_neighbors)

        return neighbors

    def __str__(self):
        return f"Node: ({self.longitude}, {self.latitude}), Leaf: {self.is_leaf}"
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

    def write_serialize_quad_tree(self, filename):
        filepath = '/Users/dougveilleux/Documents/GitHub/UUVPathPlanningAPP/data/quad_tree/'
        with open(filepath + filename, 'wb') as f:
            pickle.dump(quad_tree, f)

    def count_nodes(self, node):
        """
        Count the total number of nodes in the QuadTree recursively.
        """
        if node is None:
            return 0
        # Count the current node and recursively count the nodes in its children
        return 1 + self.count_nodes(node.northWest) + self.count_nodes(node.northEast) + self.count_nodes(
            node.southEast) + self.count_nodes(node.southWest)


    #### vvvv PLOTTING vvvv ####
    def visualize_chart_data(self, ax):
        # Create a new figure and axis
        # fig, ax = plt.subplots(figsize=(14, 9))

        # Plot the initial bounding box representing water
        water_bounds = self.root.domain_data.unary_union.bounds
        water_polygon = Polygon([(water_bounds[0], water_bounds[1]), (water_bounds[2], water_bounds[1]),
                                 (water_bounds[2], water_bounds[3]), (water_bounds[0], water_bounds[3])])
        gpd.GeoSeries([water_polygon]).plot(ax=ax, color='lightblue')

        # Plot the MultiPolygon domain
        multi_polygon = self.root.domain_data.iloc[0]
        gpd.GeoSeries([multi_polygon]).plot(ax=ax, color='tan', linewidth=1, edgecolor='blue')

        # Formatting
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        # Add grid
        ax.grid(True, which='both', color='darkgrey', linestyle='--', linewidth=0.5)
        # Setting Title
        ax.set_title('', fontsize=20)

        # Show the plot
        # plt.show()

    def visualize_quadtree(self):
        # Create a new figure and axis
        fig, ax = plt.subplots(figsize=(14, 9))

        # Plot the initial bounding box representing water
        water_bounds = self.root.domain_data.unary_union.bounds
        water_polygon = Polygon([(water_bounds[0], water_bounds[1]), (water_bounds[2], water_bounds[1]),
                                 (water_bounds[2], water_bounds[3]), (water_bounds[0], water_bounds[3])])
        gpd.GeoSeries([water_polygon]).plot(ax=ax, color='lightblue')

        # Plot the MultiPolygon domain
        multi_polygon = self.root.domain_data.iloc[0]
        gpd.GeoSeries([multi_polygon]).plot(ax=ax, color='tan', linewidth=1, edgecolor='blue')

        # Plot the quadtree partitions
        self.plot_quadtree_partitions(self.root, ax)

        # Formatting
        ax.set_title('Data Domain with Quadtree Overlay')
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')

        # Show the plot
        plt.show()

    def plot_quadtree_partitions(self, node, ax):
        """
        Recursively collect quadtree partitions based on the MultiPolygon.
        """
        if node is not None:
            if not node.is_leaf:
                # Plot the boundaries of the current node
                x = [node.min_x, node.max_x, node.max_x, node.min_x, node.min_x]
                y = [node.min_y, node.min_y, node.max_y, node.max_y, node.min_y]
                ax.plot(x, y, color='red', lw=0.5)

                # Plot the divisions of the child nodes
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

    def plot_nearest_node(self, start_point, goal_point, start_closest_node, goal_closest_node,
                          start_collected_nodes, goal_collected_nodes,
                          start_search_region, goal_search_region):
        """
        Plot the nearest node along with the start and goal points.
        :param point: Coordinates of the point (longitude, latitude)
        :param collected_nodes: List collected nodes within the search region
        :param closest_node: the closest node to the start point
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

            # Plot points (green / red)
            ax.scatter(start_point[0], start_point[1], c='green', marker='*', s=150, label='Start Point')
            ax.scatter(goal_point[0], goal_point[1], c='red', marker='*', s=150, label='Goal Point')

            # Plot collected nodes
            for node in start_collected_nodes:
                ax.scatter(node.longitude, node.latitude, facecolor='none', edgecolor='gray',
                           linestyle='--', marker='o', s=150)
            for node in goal_collected_nodes:
                ax.scatter(node.longitude, node.latitude, facecolor='none', edgecolor='gray',
                           linestyle='--', marker='o', s=150)

            # Plot search region
            left, bottom, right, top = start_search_region
            plt.plot([left, left, right, right, left], [bottom, top, top, bottom, bottom], linestyle='--',
                     color='green', label='Start Search Region')
            left, bottom, right, top = goal_search_region
            plt.plot([left, left, right, right, left], [bottom, top, top, bottom, bottom], linestyle='--',
                     color='red', label='Goal Search Region')

            # Plot closest node (green / red)
            ax.scatter(start_closest_node.longitude, start_closest_node.latitude, facecolor='none', edgecolor='green',
                       marker='o', linewidth=3.0, s=150, label='Start Closest Node')
            ax.scatter(goal_closest_node.longitude, goal_closest_node.latitude, facecolor='none', edgecolor='red',
                       marker='o', linewidth=3.0, s=150, label='Goal Closest Node')

            ax.set_aspect('equal', 'box')
            ax.set_xlabel('Longitude')  # Set the x-axis label to 'Longitude'
            ax.set_ylabel('Latitude')  # Set the y-axis label to 'Latitude'
            ax.set_title('Node Data with Start & Goal Points and Closest Calculated Start & Goal Nodes')
            ax.legend(loc='upper center')
            plt.show()

        else:
            print("Node data is not available after deletion.")

    def plot_neighbors(self, neighbors, start_point, goal_point, start_closest_node, goal_closest_node,
                          start_collected_nodes, goal_collected_nodes,
                          start_search_region, goal_search_region):
        """
        Plot the nearest node along with the start and goal points.
        :param point: Coordinates of the point (longitude, latitude)
        :param collected_nodes: List collected nodes within the search region
        :param closest_node: the closest node to the start point
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

            # Plot points (green / red)
            ax.scatter(start_point[0], start_point[1], c='green', marker='*', s=150, label='Start Point')
            ax.scatter(goal_point[0], goal_point[1], c='red', marker='*', s=150, label='Goal Point')

            # Plot collected nodes
            for node in start_collected_nodes:
                ax.scatter(node.longitude, node.latitude, facecolor='none', edgecolor='gray',
                           linestyle='--', marker='o', s=10)
            for node in goal_collected_nodes:
                ax.scatter(node.longitude, node.latitude, facecolor='none', edgecolor='gray',
                           linestyle='--', marker='o', s=10)

            # Plot search region
            left, bottom, right, top = start_search_region
            plt.plot([left, left, right, right, left], [bottom, top, top, bottom, bottom], linestyle='--',
                     color='green', label='Start Search Region')
            left, bottom, right, top = goal_search_region
            plt.plot([left, left, right, right, left], [bottom, top, top, bottom, bottom], linestyle='--',
                     color='red', label='Goal Search Region')

            # Plot closest node (green / red)
            ax.scatter(start_closest_node.longitude, start_closest_node.latitude, facecolor='none', edgecolor='green',
                       marker='o', linewidth=3.0, s=150, label='Closest Start Node')
            ax.scatter(goal_closest_node.longitude, goal_closest_node.latitude, facecolor='none', edgecolor='red',
                       marker='o', linewidth=3.0, s=150, label='Closest Goal Node')

            # Plot the neighbors
            for neighbor in neighbors:
                ax.scatter(neighbor.longitude, neighbor.latitude, c='orange', marker='o', s=50,
                           label='Neighbors')


            ax.set_aspect('equal', 'box')
            ax.set_xlabel('Longitude')  # Set the x-axis label to 'Longitude'
            ax.set_ylabel('Latitude')  # Set the y-axis label to 'Latitude'
            ax.set_title('Node Data with Start & Goal Points and Closest Calculated Start & Goal Nodes')
            ax.legend(loc='upper center')
            plt.show()

        else:
            print("Node data is not available after deletion.")






def deserialize_quad_tree(file_path):
    """
    Method to load a .qtdata file containing Chart Data in a quad tree data structure format
    Parameter: file_path: including data file
    Return: quadtree
    """
    with open(file_path, 'rb') as f:
        quadtree = pickle.load(f)
    return quadtree




##=========================================================================================##
if __name__ == '__main__':
    # # Load the data
    # shapefile_path = (
    #     '/Users/dougveilleux/Documents/GitHub/UUVPathPlanningApp/'
    #     'data/SHAPE_FILE/US4MA23M/US4MA23M_SHAPEFILE.shp'
    # )
    # # Instantiate the data object
    # chart_us4ma23m = ShapefileHandler(shapefile_path)
    #
    # # Create a Selection box Manually for now.  Eventually this will come from mouse interaction
    # x1, y1, x2, y2 = -70.8714, 41.573, -70.7866, 41.6372
    # bounding_box = box(x1, y1, x2, y2)
    # domain_data = chart_us4ma23m.make_land_polygon(showPlot=False, bounding_box=bounding_box)
    # print(type(domain_data))
    # print(domain_data)
    # print("Bounding dimensions of domain_data before quadtree:", domain_data.total_bounds)
    #
    # # Instantiate a QuadTree with the domain data polygon and the desired node lengths
    # quad_tree = QuadTree(domain_data, node_length_near_boundary=0.0005, node_length_far_from_boundary=0.005)
    #
    # # Build the Quad Tree
    # # Start time
    # start_time = time.time()
    # quad_tree.build_quadtree()
    # # End time
    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # print("\nQuad Tree Built in:", elapsed_time, "seconds\n")
    #
    # # Visualize the Quad Tree
    # quad_tree.visualize_quadtree()
    #
    # # Classify the nodes and Land or Water
    # # Start time
    # start_time = time.time()
    # quad_tree.classify_nodes()
    # # End time
    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # print("Nodes Classified in:", elapsed_time, "seconds\n")
    #
    # # Collect the nodes and plot to confirm classification worked
    # # Start time
    # start_time = time.time()
    # node_dataframe = quad_tree.collect_node_data()
    # # End time
    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # print("Collected Node Data in:", elapsed_time, "seconds\n")
    # # plot node data
    # # quad_tree.plot_node_data(node_dataframe)
    #
    # # Delete unnecessary land nodes to reduce data set
    # # Start time
    # start_time = time.time()
    # quad_tree.delete_unnecessary_land_nodes()
    # # End time
    # end_time = time.time()
    # elapsed_time = end_time - start_time
    # print("Land Nodes Deleted in:", elapsed_time, "seconds\n")
    # # plot node to confirm deletion
    # # quad_tree.plot_node_data_after_deletion()
    # quad_tree.write_serialize_quad_tree('west_island_medium.qtdata')
    #
    # # Visualize the Quad Tree (after node deletion)
    # # quad_tree.visualize_quadtree()

    # Load QuadTree Data
    quadtree_data_path = (
        '/Users/dougveilleux/Documents/GitHub/UUVPathPlanningApp/'
        'data/quad_tree/west_island_medium.qtdata'
    )
    quad_tree = deserialize_quad_tree(quadtree_data_path)



    # Test Start Point & Goal Point Methods
    startPoint = (-70.840, 41.592)
    goalPoint = (-70.907, 41.6284)
    print("Start Point:", startPoint)
    print("Goal Point:", goalPoint)

    # Find closest nodes in the quad tree to Start and Goal points
    closest_start_node, closest_start_nodes, start_search_region = quad_tree.find_closest_node(startPoint)
    closest_goal_node, closest_goal_nodes, goal_search_region = quad_tree.find_closest_node(goalPoint)

    # quad_tree.plot_nearest_node(startPoint, goalPoint,
    #                             closest_start_node, closest_goal_node,
    #                             closest_start_nodes, closest_goal_nodes,
    #                             start_search_region, goal_search_region)
    # print(closest_start_node.longitude, closest_start_node.latitude)

    start_neighbors = quad_tree.get_neighbors(closest_start_node)
    for node in start_neighbors:
        print("Node Details:")
        print("Longitude:", node.longitude)
        print("Latitude:", node.latitude)
        print("landOrWater:", node.landOrWater)
        print()  # Add an empty line for better readability between nodes

    quad_tree.plot_neighbors(start_neighbors, startPoint, goalPoint,
                                closest_start_node, closest_goal_node,
                                closest_start_nodes, closest_goal_nodes,
                                start_search_region, goal_search_region)


    goal_neighbors = quad_tree.get_neighbors(closest_goal_node)
    for node in goal_neighbors:
        print("Node Details:")
        print("Longitude:", node.longitude)
        print("Latitude:", node.latitude)
        print("landOrWater:", node.landOrWater)
        print()  # Add an empty line for better readability between nodes

    # quad_tree.plot_neighbors(goal_neighbors, startPoint, goalPoint,
    #                             closest_start_node, closest_goal_node,
    #                             closest_start_nodes, closest_goal_nodes,
    #                             start_search_region, goal_search_region)




