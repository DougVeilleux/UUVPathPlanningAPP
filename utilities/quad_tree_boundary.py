# quad_tree_boundary.py
import geopandas as gpd

from shapely.geometry import Polygon, MultiPolygon, Point, LineString, MultiLineString
from shapely.ops import unary_union
from utilities.shapefile_handler import *



class QuadTreeNode:
    """
    Class to define a QuadTree node which contains 4 children.  A NW, NE, SE, & SW
        sub-region
    Parameter: domain_polygon, polygon data for the quadtree to structure
    Attributes:
        northWest...southWest: represent children of the node in the four quadrants
        is_leaf: indicates whether the node is a leaf node (i.e. no children)
        is_boundary: indicates whether the node lies on the boundary of the data region
         (e.g. a water / land boundary)
    """
    def __init__(self, domain_polygon):
        self.domain_polygon = domain_polygon
        self.min_x, self.min_y, self.max_x, self.max_y = self.calculate_bounds()
        self.northWest = None
        self.northEast = None
        self.southEast = None
        self.southWest = None
        self.is_leaf = True
        self.is_boundary = False

    def calculate_bounds(self):
        """
        Extract the geometry from the GeoSeries if needed and get the bounding
        box of the polygon.
        """
        if isinstance(self.domain_polygon, gpd.GeoSeries):
            domain_polygons_geom = self.domain_polygon.geometry.iloc[0] \
                if len(self.domain_polygon) > 0 else None
        else:
            domain_polygons_geom = self.domain_polygon

        # Return the bounds of the domain polygon
        return domain_polygons_geom.bounds

    def insert(self):
        pass

    def subdivide(self):
        """
        Subdivide the node into four quadrants.
        """
        mid_x = (self.min_x + self.max_x) / 2
        mid_y = (self.min_y + self.max_y) / 2
        # Define vertices for each quadrant
        nw_vertices = [(self.min_x, mid_y), (mid_x, mid_y), (mid_x, self.max_y), (self.min_x, self.max_y)]
        ne_vertices = [(mid_x, mid_y), (self.max_x, mid_y), (self.max_x, self.max_y), (mid_x, self.max_y)]
        se_vertices = [(self.min_x, self.min_y), (mid_x, self.min_y), (mid_x, mid_y), (self.min_x, mid_y)]
        sw_vertices = [(mid_x, self.min_y), (self.max_x, self.min_y), (self.max_x, mid_y), (mid_x, mid_y)]
        # Create polygons for each quadrant
        nw_polygon = Polygon(nw_vertices)
        ne_polygon = Polygon(ne_vertices)
        se_polygon = Polygon(se_vertices)
        sw_polygon = Polygon(sw_vertices)
        # Create four child nodes
        self.northWest = QuadTreeNode(nw_polygon)
        self.northEast = QuadTreeNode(ne_polygon)
        self.southWest = QuadTreeNode(se_polygon)
        self.southEast = QuadTreeNode(sw_polygon)

        # Update leaf status
        self.is_leaf = False

        # Distribute domain polygon to children
        self.distribute_domain_polygon()

    def distribute_domain_polygon(self):
        """
        Distribute the domain polygon of the parent node to its children.
        """
        # print("Parent domain polygon type:", type(self.domain_polygon))
        parent_geom = self.domain_polygon.unary_union if isinstance(self.domain_polygon,
                                                                    gpd.GeoSeries) else self.domain_polygon
        for child in [self.northWest, self.northEast, self.southWest, self.southEast]:
            child_geom = child.domain_polygon.unary_union if isinstance(child.domain_polygon,
                                                                        gpd.GeoSeries) else child.domain_polygon
            if parent_geom.intersects(child_geom):
                if isinstance(child.domain_polygon, gpd.GeoSeries):
                    child.domain_polygon = child_geom.union(parent_geom)
                else:
                    child.domain_polygon = gpd.GeoSeries(child_geom.union(parent_geom))

        # print("Child domain polygon type:", type(child.domain_polygon))


    #### vvvvPLOTTINGvvvv ####
    def visualize(self, ax=None):
        """
        Visualize the domain polygon and the quadtree divisions recursively.
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(14, 9))

        # Plot domain polygon
        if isinstance(self.domain_polygon, gpd.GeoSeries):
            self.domain_polygon.plot(ax=ax, edgecolor='black')
        else:
            gpd.GeoSeries([self.domain_polygon]).plot(ax=ax, color='cornflowerblue', edgecolor='black')

        # Plot quadtree divisions
        if not self.is_leaf:
            for child in [self.northWest, self.northEast, self.southWest, self.southEast]:
                child.visualize(ax=ax)

        ax.set_title('Quadtree Division')
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        plt.show()





class QuadTree:
    """
    Class to form QuadTree data structure of the land / water boundary
    Parameters:
        domain polygon: polygon data for the quadtree to structure
        node_length: float, represents the min length to recursively divide nodes
            down to at the land / water boundary
    """
    def __init__(self, domain_polygon, node_length=0.01):
        self.root = QuadTreeNode(domain_polygon)
        self.node_length = node_length

    def build_quadtree(self):
        """
        Build the quadtree structure recursively.
        """
        self._build_quadtree_recursive(self.root)

    def _build_quadtree_recursive(self, node):
        """
        Recursively build the quadtree structure.
        """
        if node.is_leaf:
            if self._node_needs_subdivision(node):
                node.subdivide()
                for child in [node.northWest, node.northEast, node.southWest, node.southEast]:
                    self._build_quadtree_recursive(child)

    def _node_needs_subdivision(self, node):
        """
        Check if the node needs to be subdivided based on its size.
        """
        width = node.max_x - node.min_x
        height = node.max_y - node.min_y
        return width > self.node_length or height > self.node_length

    def refine_boundary(self, num_points=1000):
        # Access the boundary of the domain_polygon stored in the QuadTreeNode
        boundary_geoseries = self.root.domain_polygon.boundary

        # Initialize a list to store coordinates
        boundary_coords = []

        # Loop through each geometry in the GeoSeries
        for geom in boundary_geoseries:
            # Check if the geometry is a MultiLineString
            if isinstance(geom, MultiLineString):
                # Iterate over each LineString within the MultiLineString
                for line in geom:
                    # Extract coordinates as tuples for each LineString
                    boundary_coords.extend([(point.x, point.y) for point in line.coords])
            else:
                # Extract coordinates as tuples for the LineString
                boundary_coords.extend([(point.x, point.y) for point in geom.coords])

        # Interpolate additional points along the boundary
        refined_coords = [boundary_coords[0]]  # Start with the first point
        for i in range(1, len(boundary_coords)):
            # Interpolate points between successive boundary coordinates
            interpolated_points = LineString([boundary_coords[i - 1], boundary_coords[i]]).interpolate(
                distance=num_points, normalized=True
            )
            # Append the interpolated points to the refined coordinate list
            refined_coords.extend([(point.x, point.y) for point in interpolated_points])

        # Convert refined coordinates into a LineString object
        refined_boundary = LineString(refined_coords)
        return refined_boundary

    def generate_sparse_grid(self, resolution):
        # Generate a sparse grid based on the boundary cells and resolution
        # Skip cells that are entirely within water polygons
        pass

    def assign_cost_values(self, sparse_grid, water_polygons):
        # Assign cost values (0 for water, 1 for land) to grid cells
        # Use shapely's contains method to check if a point is within water polygons
        pass



    #### vvvv PLOTTING vvvv ####
    def visualize_quadtree(self):
        # Create a new figure and axis
        fig, ax = plt.subplots(figsize=(14,9))

        # Plot the water domain
        gpd.GeoSeries(self.root.domain_polygon).plot(ax=ax, color='cornflowerblue', edgecolor='black')

        # Plot the quadtree divisions
        self.plot_quadtree_partitions(self.root, ax)

        # Set plot title and labels
        ax.set_title('Water Domain with Quadtree Overlay')
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')

        # Show the plot
        plt.show()


    def plot_quadtree_partitions(self, node, ax):
        # Recursively plot the quadtree divisions
        if node is not None:
            if not node.is_leaf:
                # Plot the boundaries of the current node
                x = [node.min_x, node.max_x, node.max_x, node.min_x, node.min_x]
                y = [node.min_y, node.min_y, node.max_y, node.max_y, node.min_y]
                ax.plot(x, y, color='red', lw=1)

                # Plot the divisions of the child nodes
                self.plot_quadtree_partitions(node.northWest, ax)
                self.plot_quadtree_partitions(node.northEast, ax)
                self.plot_quadtree_partitions(node.southWest, ax)
                self.plot_quadtree_partitions(node.southEast, ax)











##=========================================================================================##
##=========================================================================================##
##=========================================================================================##
if __name__ == '__main__':
    shapefile_path = (
    '/Users/dougveilleux/Documents/GitHub/UUVPathPlanningApp/'
    'data/SHAPE_FILE/US4MA23M/US4MA23M_SHAPEFILE.shp'
    )

    chart_us4ma23m = ShapefileHandler(shapefile_path)
    # Form the Water Domain from the Shapefile Read in
    water_domain_polygon = chart_us4ma23m.make_water_polygon(showPlot=False)
    print(type(water_domain_polygon))
    print(water_domain_polygon)

    # Instantiate a QuadTree with the water domain polygon and the desired node length
    quad_tree = QuadTree(water_domain_polygon, node_length=0.08)
    # print(quad_tree.root.calculate_bounds())

    # Build the quadtree structure
    # quad_tree.build_quadtree()
    data = quad_tree.refine_boundary(num_points = 1000)
    print(data)
    # quad_tree.visualize_quadtree()
    plt.show()

    # import geopandas as gpd
    # import matplotlib.pyplot as plt
    # from shapely.geometry import Polygon
    #
    # # Create a rectangular polygon bounding box
    # rectangular_polygon = Polygon([(0, 0), (100, 0), (100, 50), (0, 50), (0, 0)])
    #
    # # Create a triangular polygon
    # triangular_polygon = Polygon([(0, 0), (60, 0), (60, 50), (0, 0)])
    #
    # # Subtract the triangular polygon from the rectangular polygon to create the water domain
    # water_domain_polygon = rectangular_polygon.difference(triangular_polygon)
    #
    # # Plotting the water domain
    # fig, ax = plt.subplots(figsize=(8, 6))
    # gpd.GeoSeries(water_domain_polygon).plot(ax=ax, edgecolor='blue', linewidth=2)
    # ax.set_title('Water Domain')
    # plt.xlabel('X')
    # plt.ylabel('Y')
    # plt.grid(True)
    # plt.show()
    #
    # # Instantiate a QuadTree with the water domain polygon and the desired max depth
    # max_depth = 5  # Adjust as needed
    # quad_tree = QuadTree(water_domain_polygon, max_depth)
    #
    # # Build the quadtree structure
    # quad_tree.build()
    #
    # # Plot the initial boundary
    # quad_tree.plot_quadtree_partitions_boundary()
