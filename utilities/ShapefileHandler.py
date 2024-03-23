# ShapefileHandler.py

import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from shapely.geometry import Polygon, Point, MultiPolygon, LineString, box
from shapely.ops import cascaded_union
from shapely.ops import unary_union
import pandas as pd
from pandasgui import show
import numpy as np

class ShapefileHandler:

    def __init__(self, shapefile_path):
        """
        Constructor: Instantiate by reading shapefile and storing to
            data variable.
        :param shapefile_path: '\Full\file_path\to\data_folder
        """
        self.shapefile_path = shapefile_path
        self.data = None
        self.read_shapefile()

    # Data Handling & Display Methods:
    def read_shapefile(self):
        """
        Reads Shapefile with gpd.read()
        """
        self.data = gpd.read_file(self.shapefile_path)

    def plot_shapefile_data(self, plot_centroids=False, ax=None):
        """
        Plot Shapefile data to confirm data read in correctly
        """
        if self.data is None:
            print("Shapefile data not loaded. Call read_shapefile() first.")
            return

        if ax is None:
            fig, ax = plt.subplots(figsize=(14, 9))
        else:
            fig = ax.figure

        # Create bounding polygon to fill the entire area with light blue
        min_lon, max_lon = self.data.bounds.minx.min(), self.data.bounds.maxx.max()
        min_lat, max_lat = self.data.bounds.miny.min(), self.data.bounds.maxy.max()
        initial_bounding_polygon = Polygon([(min_lon, min_lat), (max_lon, min_lat),
                                            (max_lon, max_lat), (min_lon, max_lat)])
        # Fill the entire area with light blue for water representation
        ax.fill(initial_bounding_polygon.exterior.xy[0], initial_bounding_polygon.exterior.xy[1],
                facecolor='lightblue', edgecolor='none')

        # Overlay land polygons with tan color
        for index, row in self.get_coordinate_data().iterrows():
            lon, lat = row['Longitude'], row['Latitude']
            ax.fill(lon, lat, facecolor=[0.824, 0.706, 0.549], edgecolor='black', linewidth=1)

        # Plot red Dot at centroid of each polygon if desired.
        if plot_centroids:
            centroids = self.calculate_polygon_centroids()
            for centroid, index in centroids:
                ax.plot(centroid.x, centroid.y, 'ro', markersize=2)
                ax.text(centroid.x, centroid.y, str(index), fontsize=8, color='blue')  # Plot index next to centroid

        # vvv FORMATING vvv
        # Set axis labels
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        # Add grid
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        # Setting same scale for x and y axes
        # ax.set_aspect('equal')
        # Setting Title
        ax.set_title('NOAA CHART DATA: US4MA23M', fontsize=20)
        # Comment out to work with Tkinter
        plt.show()

    def get_coordinate_data(self, displayPandasGUI: object = False) -> object:
        """
        Debug Method to read geometry coordinates.
        Get the latitude and longitude data from each polygon in the
        shapefile and return a DataFrame of coordinates for each Polygon
        from the file 'geometry'

        Option: to display data in pandasGUI -> set to True
        """
        coordinates = []
        for geometry in self.data['geometry']:
            if geometry.geom_type == 'Polygon':
                lon, lat = geometry.exterior.xy
                coordinates.append((lon, lat))
        df = pd.DataFrame(coordinates, columns=['Longitude', 'Latitude'])
        # Option to use GUI data display
        if displayPandasGUI:
            show(df)
        # Return dataframe
        return df

    def linestring_from_coords_data(self, coordinate_data, interpolate=False, showPlot=False):
        """
        Method to take in lat / lon coordinats to return a Geodataframe of a LINESTRING
        :param coordinate_data: coordinate data from "get_coordinate_data" method
        :param interpolate: Flag to do interpolation
        :param showPlot: Flag to show plot
        :return: GeoDataframe of Linespace object(s)
        """
        lon_data = list(coordinate_data.loc[0, 'Longitude'])
        lat_data = list(coordinate_data.loc[0, 'Latitude'])

        if interpolate:
            # Interpolate between points
            interpolated_lon = []
            interpolated_lat = []

            for i in range(len(lon_data) - 1):
                lon_start, lon_end = lon_data[i], lon_data[i + 1]
                lat_start, lat_end = lat_data[i], lat_data[i + 1]

                # Linear interpolation
                lon_interp = [lon_start + (lon_end - lon_start) * t for t in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]]
                lat_interp = [lat_start + (lat_end - lat_start) * t for t in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]]

                interpolated_lon.extend(lon_interp)
                interpolated_lat.extend(lat_interp)

            # Combine original and interpolated points
            lon_data.extend(interpolated_lon)
            lat_data.extend(interpolated_lat)

        # Create LineString
        line = LineString(zip(lon_data, lat_data))
        # Create GeoDataFrame
        gdf = gpd.GeoDataFrame(geometry=[line])

        if showPlot: # if True display the plot
            # Plot the GeoDataFrame
            fig = plt.figure(figsize=(14, 9))  # Adjust the width and height as needed
            ax = fig.add_subplot(111)
            gdf.plot(ax=ax, color='black', linewidth=1)

            if interpolate: # if True overlay point
                # Plot initial points in red
                ax.scatter(lon_data[:len(lon_data) // 2], lat_data[:len(lat_data) // 2], color='red',
                           label='Initial Points')
                # Plot interpolated points in blue
                ax.scatter(lon_data[len(lon_data) // 2:], lat_data[len(lat_data) // 2:], color='blue', marker='o',
                           facecolor='none', label='Interpolated Points')

            # vvv FORMATTING vvv
            # Set axis labels
            ax.set_xlabel('Longitude')
            ax.set_ylabel('Latitude')
            # Add grid
            ax.grid(True, which='both', color='lightgray', linestyle='--', linewidth=0.5)
            # Setting same scale for x and y axes
            # ax.set_aspect('equal')
            # Legend
            ax.legend()
            # Setting Title
            ax.set_title('Coords as LineString', fontsize=20)
            # Show plot
            plt.show()

        return gdf

    def polygon_from_coords_data(self, coordinate_data, interpolate=False, showPlot=False):
        """
        Method to take in lat / lon coordinats to return a Geodataframe of a LINESTRING
        :param coordinate_data: coordinate data from "get_coordinate_data" method
        :param interpolate: Flag to do interpolation
        :param showPlot: Flag to show plot
        :return: GeoDataframe of Polygon object(s)
        """
        lon_data = list(coordinate_data.loc[18, 'Longitude'])
        lat_data = list(coordinate_data.loc[18, 'Latitude'])

        if interpolate:
            # Interpolate between points
            interpolated_lon = []
            interpolated_lat = []

            for i in range(len(lon_data) - 1):
                lon_start, lon_end = lon_data[i], lon_data[i + 1]
                lat_start, lat_end = lat_data[i], lat_data[i + 1]

                # Linear interpolation
                lon_interp = [lon_start + (lon_end - lon_start) * t for t in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]]
                lat_interp = [lat_start + (lat_end - lat_start) * t for t in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]]

                interpolated_lon.extend(lon_interp)
                interpolated_lat.extend(lat_interp)

            # Combine original and interpolated points
            lon_data.extend(interpolated_lon)
            lat_data.extend(interpolated_lat)

        # Create LineString
        polygon = Polygon(zip(lon_data, lat_data))
        # Create GeoDataFrame
        gdf = gpd.GeoDataFrame(geometry=[polygon])

        if showPlot: # if True display the plot
            # Plot the GeoDataFrame
            fig = plt.figure(figsize=(14, 9))  # Adjust the width and height as needed
            ax = fig.add_subplot(111)
            gdf.plot(ax=ax, color='tan', linewidth=1, edgecolor='black')

            if interpolate: # if True overlay point
                # Plot initial points in red
                ax.scatter(lon_data[:len(lon_data) // 2], lat_data[:len(lat_data) // 2], color='red',
                           label='Initial Points')
                # Plot interpolated points in blue
                ax.scatter(lon_data[len(lon_data) // 2:], lat_data[len(lat_data) // 2:], color='blue', marker='o',
                           facecolor='none', label='Interpolated Points')

            # vvv FORMATTING vvv
            # Set axis labels
            ax.set_xlabel('Longitude')
            ax.set_ylabel('Latitude')
            # Add grid
            ax.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)
            # Setting same scale for x and y axes
            # ax.set_aspect('equal')
            # Legend
            ax.legend()
            # Setting Title
            ax.set_title('Coords as LineString', fontsize=20)
            # Show plot
            plt.show()

        return gdf

    def make_water_polygon(self, showPlot=False):
        """
        Using the latitude and longitude coordinates of the data create a single
        Polygon (the water) by subtracting the Land Polygons from the starting
        water domain.
        :return: Polygon of only the water.
        """
        # Data check
        if self.data is None:
            print("Shapefile data not loaded. Call read_shapefile() first.")
            return

        offset = 0.005  # Define the offset value
        # Calculate the new coordinates for the bounding box with inward offset
        # This offset helps clean up small gaps causing difficulty in completing
        # the subtraction of all polygons.
        min_lon, max_lon = self.data.bounds.minx.min() + offset, self.data.bounds.maxx.max() - offset
        min_lat, max_lat = self.data.bounds.miny.min() + offset, self.data.bounds.maxy.max() - offset

        bounding_polygon = gpd.GeoDataFrame(geometry=[Polygon([(min_lon, min_lat), (max_lon, min_lat),
                                                                     (max_lon, max_lat), (min_lon, max_lat)])])

        # Take in the shapefile data geometry and set as the land
        land_polygons = gpd.GeoDataFrame(geometry=self.data['geometry'])
        # Calculate the water domain
        water_domain = bounding_polygon.difference(land_polygons.unary_union)

        # Plot the updated water polygon
        if showPlot:
            fig, ax = plt.subplots(figsize=(14, 9))
            bounding_polygon.plot(ax=ax, color='tan', edgecolor='black')
            water_domain.plot(ax=ax, color='cornflowerblue', edgecolor='black')


            # vvv FORMATTING vvv
            # Set axis labels
            ax.set_xlabel('Longitude')
            ax.set_ylabel('Latitude')
            # Add grid
            ax.grid(True, which='both', color='lightgray', linestyle='--', linewidth=0.5)
            # Setting same scale for x and y axes
            # ax.set_aspect('equal')
            # Setting Title
            ax.set_title('Water Domain Polygon', fontsize=20)
            # Show plot
            plt.show()

        return water_domain

    def make_land_polygon(self, showPlot=True, bounding_box=None):
        """
        Using the latitude and longitude coordinates of the data create a single
        Polygon (the land) by unifying the Land Polygons from to one Multipolygon
        :return: Polygon of only the land.
        """
        # Data check
        if self.data is None:
            print("Shapefile data not loaded. Call read_shapefile() first.")
            return

        offset = 0.000  # Define the offset value
        # Calculate the new coordinates for the bounding box with inward offset
        # This offset helps clean up small gaps causing difficulty in completing
        # the subtraction of all polygons.
        min_lon, max_lon = self.data.bounds.minx.min() + offset, self.data.bounds.maxx.max() - offset
        min_lat, max_lat = self.data.bounds.miny.min() + offset, self.data.bounds.maxy.max() - offset

        bounding_polygon = gpd.GeoDataFrame(geometry=[Polygon([(min_lon, min_lat), (max_lon, min_lat),
                                                               (max_lon, max_lat), (min_lon, max_lat)])])

        # Take in the shapefile data geometry and set as the land
        land_polygons = gpd.GeoDataFrame(geometry=self.data['geometry'])

        # Filter land polygons based on bounding box if provided
        if bounding_box:
            land_polygons = land_polygons[land_polygons.intersects(bounding_box)]
            # Recalculate the bounding_polygon based on the limits of filtered land_polygons
            filtered_min_lon, filtered_max_lon = land_polygons.total_bounds[0], land_polygons.total_bounds[2]
            filtered_min_lat, filtered_max_lat = land_polygons.total_bounds[1], land_polygons.total_bounds[3]

            # Adjust the bounding_polygon edges with an additional offset
            extra_offset = 0.008
            filtered_min_lon = min_lon if round(filtered_min_lon, 4) == round(min_lon,
                                                                              4) else filtered_min_lon - extra_offset
            filtered_min_lat = min_lat if round(filtered_min_lat, 4) == round(min_lat,
                                                                              4) else filtered_min_lat - extra_offset
            filtered_max_lon = max_lon if round(filtered_max_lon, 4) == round(max_lon,
                                                                              4) else filtered_max_lon + extra_offset
            filtered_max_lat = max_lat if round(filtered_max_lat, 4) == round(max_lat,
                                                                              4) else filtered_max_lat + extra_offset

            # Recreate bounding_polygon with the adjusted edges
            bounding_polygon = gpd.GeoDataFrame(geometry=[Polygon([(filtered_min_lon, filtered_min_lat), (filtered_max_lon, filtered_min_lat),
                                                                   (filtered_max_lon, filtered_max_lat), (filtered_min_lon, filtered_max_lat)])])

        # Calculate the water domain
        land_domain = land_polygons.unary_union
        # Convert into GeoSeires to stay consistent with other code use
        land_domain_series = gpd.GeoSeries([land_domain])

        # Plot the updated water polygon
        if showPlot:
            fig, ax = plt.subplots(figsize=(14, 9))
            bounding_polygon.plot(ax=ax, color='lightblue', edgecolor='black')
            land_domain_series.plot(ax=ax, color='tan', edgecolor='black')

            # vvv FORMATTING vvv
            # Set axis labels
            ax.set_xlabel('Longitude')
            ax.set_ylabel('Latitude')
            # Add grid
            ax.grid(True, which='both', color='darkgray', linestyle='--', linewidth=0.5)
            # Setting same scale for x and y axes
            # ax.set_aspect('equal')
            # Setting Title
            # ax.set_title('Land Polygons -> Single MultiPolygon', fontsize=20)
            # Show plot
            # plt.show()

        return land_domain_series


    def extract_polygon_points(self, polygon, showPlot=False):
        """
        Extracts boundary and island points of a polygon or MultiPolygon.
        Parameters:
        - polygon: shapely.geometry.Polygon or shapely.geometry.MultiPolygon, input polygon(s)
        Returns:
        - boundary_points: list of tuples, boundary points of the polygon(s)
        - island_points: list of tuples, island points of the polygon(s)
        """
        # Extract the MultiPolygon geometry from the GeoSeries if needed
        if isinstance(polygon, gpd.GeoSeries):
            polygon = polygon.geometry.iloc[0]

        boundary_points = []
        island_points = []

        # Check if it's a MultiPolygon
        if isinstance(polygon, MultiPolygon):
            for poly in polygon.geoms:  # Extract components of the MultiPolygon
                boundary, island = self._extract_polygon_points(poly)
                boundary_points.extend(boundary)
                island_points.extend(island)
        else:
            boundary_points, island_points = self._extract_polygon_points(polygon)

        # Plot the points if showPlot is True
        if showPlot:
            fig, ax = plt.subplots(figsize=(14, 9))

            # Plot boundary points
            x_boundary, y_boundary = zip(*boundary_points)
            ax.scatter(x_boundary, y_boundary, c='blue', s=4, label='Boundary Points')
            # ax.plot(x_boundary, y_boundary, '--', c='blue')

            # Plot island points
            x_island, y_island = zip(*island_points)
            ax.scatter(x_island, y_island, c='red', s=4, label='Island Points')
            # ax.plot(x_island, y_island, '--', c='red')

            ax.set_xlabel('Longitude')
            ax.set_ylabel('Latitude')
            ax.legend()
            ax.grid(True)
            plt.title('Boundary and Island Points')
            plt.show()

        return boundary_points, island_points

    def _extract_polygon_points(self, polygon):
        """
        Helper method to extract boundary and island points of a single polygon.
        """
        boundary_points = list(polygon.exterior.coords)
        island_points = []
        for interior in polygon.interiors:
            island_points.extend(list(interior.coords))
        return boundary_points, island_points

    def assign_costs(self, water_polygon, max_resolution=0.1, boundary_resolution=0.001):
        """
        Assigns a cost of ZERO to all the latitude / longitude coordinates within the
            water polygon.
        Parameters:
            water_polygon: shapely.geometry.Polygon
            max_resolution: float, max_resolution of the default grid (default: 0.1)
            boundary_resolution: float, fine resolution near land / water boundaries (default: 0.001)
        Return:
            cost_grid: GeoDataFrame, containing points with their respective costs
        """
        # Extract the geometry from the GeoSeries if needed
        if isinstance(water_polygon, gpd.GeoSeries):
            water_polygons_geom = water_polygon.geometry.iloc[0] if len(water_polygon) > 0 else None
        else:
            water_polygons_geom = water_polygon

        # Get the Bounds of the Polygon
        min_x, min_y, max_x, max_y = water_polygons_geom.bounds

        # Ensure the water polygons are valid
        if isinstance(water_polygons_geom, Polygon):
            water_polygons = [water_polygons_geom]
        elif isinstance(water_polygons_geom, MultiPolygon):
            water_polygons = water_polygons_geom.geoms
        else:
            raise ValueError("Invalid water_polygons type. Expected Polygon or MultiPolygon.")

        # Initialize DataFrame to store points with their costs
        data = {'geometry': [], 'cost': []}

        # Iterate over each point within the bounding box
        for x in np.arange(min_x, max_x, max_resolution):
            for y in np.arange(min_y, max_y, max_resolution):
                point = Point(x, y)
                # Compute the distance to the nearest boundary
                min_distance = min(polygon.boundary.distance(point) for polygon in water_polygons)
                # Determine the resolution based on the distance to the boundary
                resolution = max(boundary_resolution, min_distance/10)  #Adjust factor to best fit data
                # Refine the grid near the boundaries
                for xx in np.arange(x, x+resolution, resolution):
                    for yy in np.arange(y, y+resolution, resolution):
                        point = Point(xx, yy)
                        # Check if point is within the water polygon
                        if any(polygon.contains(point) for polygon in water_polygons):
                            # Assign cost of 0 for water
                            data['geometry'].append(point)
                            data['cost'].append(0)
                        else:
                            data['geometry'].append(point)
                            data['cost'].append(1)

        # Create GeoDataFrame from the data
        cost_data = gpd.GeoDataFrame(data)
        return cost_data

    def plot_costs_overlay(self, water_polygon, cost_data):
        """
        Mehtod to visualize the cost_data during code develoment
        Parameters:
            water_polygon: result from "make_water_polygon" method
            cost_data: result from "assign_costs" method
        :return:
        """

        fig, ax = plt.subplots(figsize=(14, 9))
        # Plot water polygon
        water_polygon.plot(ax=ax, color='cornflowerblue', edgecolor='black', label='Water')
        # Plot cost data
        ax.scatter(cost_data.geometry.x, cost_data.geometry.y, c=cost_data['cost'], cmap='coolwarm', s=5,
                   label='Cost Data')

        # vvv FORMATTING vvv
        # Set axis labels
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        # Add grid
        ax.grid(True, which='both', color='red', linestyle='--', linewidth=0.5)
        # Setting same scale for x and y axes
        # ax.set_aspect('equal')
        # Setting Title
        ax.set_title('Costing Data Overlay', fontsize=20)
        # Show plot
        plt.show()




    # vvvvvvv    Helper Methods:
    def calculate_polygon_centroids(self):
        """
        Calculate the centroids of each polygon in the shapefile and store those
        as a Point(x, y) geometry
        :param: geometry from shapefile
        :return: Point data (x, y)
        """
        centroids = []
        for i, geometry in enumerate(self.data['geometry']):
            if geometry.geom_type == 'Polygon':
                centroid = geometry.centroid
                # Create a point object representing the centroid
                centroid_point = Point(centroid.x, centroid.y)
                centroids.append((centroid_point, i))  # Append tuple with centroid and index
        return centroids


if __name__ == '__main__':

    shapefile_path = (
        '/Users/dougveilleux/Documents/GitHub/UUVPathPlanningApp/'
        'data/SHAPE_FILE/US4MA23M/US4MA23M_SHAPEFILE.shp'
    )

    chart_us4ma23m = ShapefileHandler(shapefile_path)
    # chart_us4ma23m.plot_shapefile_data()
    # Form the Water Domain from the Shapefile Read in
    # water_domain_polygon = chart_us4ma23m.make_water_polygon(showPlot=False)

    # Extract the boundary and island points from the "Water Domain"
    # boundary_points, island_points = chart_us4ma23m.extract_polygon_points(water_domain_polygon, showPlot=False)
    # Assign cost values to land and water
    # cost_data = chart_us4ma23m.assign_costs(water_domain_polygon, max_resolution=0.01, boundary_resolution=0.001)
    # print(cost_data)
    # chart_us4ma23m.plot_costs_overlay(water_domain_polygon, cost_data)

    coords = chart_us4ma23m.get_coordinate_data()
    # print(coords)
    # print(type(coords))

    # Create a Selection box Manually for not.  Eventually this will come from mouse interaction
    x1, y1, x2, y2 = -70.8714, 41.193, -70.7866, 41.55
    bounding_box = box(x1, y1, x2, y2)
    land_domain = chart_us4ma23m.make_land_polygon(showPlot=True, bounding_box=bounding_box)
    print(type(land_domain))
    print(land_domain)
