# shapefile_handler.py

import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from shapely.geometry import Polygon, Point, MultiPolygon
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
    def get_coordinate_data(self, displayPandasGUI=False):
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
    def make_water_polygon(self, showPlot=True):
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
            ax.grid(True, which='both', linestyle='--', linewidth=0.5)
            # Setting same scale for x and y axes
            # ax.set_aspect('equal')
            # Setting Title
            ax.set_title('Water Domain Polygon', fontsize=20)
            # Show plot
            plt.show()

        return land_polygons, water_domain

    # Helper Methods:
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



    # Button Click Methods
    def set_path_area(self, event, ax, plot_centroids=True):
        print('Path Planning Area Set')
        # Get current axis limits (bounding box)
        xmin, xmax = ax.get_xlim()
        ymin, ymax = ax.get_ylim()

        # Draw a box around the bounding box
        self.path_area_box = plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, fill=False, edgecolor='red')
        ax.add_patch(self.path_area_box)
        # Update the plot
        plt.draw()

        # Create the bounding box polygon
        bounding_box_polygon = Polygon([(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)])



        # Plot the resulting water polygon
        fig2, ax2 = plt.subplots(figsize=(14, 9))






        ax2.set_xlabel('Longitude')
        ax2.set_ylabel('Latitude')
        ax2.grid(True, which='both', linestyle='--', linewidth=0.5)
        ax2.set_aspect('equal')
        ax2.set_title('Path Planning Water Area ONLY')
        plt.show()

    def reset_path_area(self, event, ax):
        print('Path Planning Area Reset')
        # Check if the path area box exists
        if hasattr(self, 'path_area_box'):
            print('Path area box exists')
            # Remove the path area box
            self.path_area_box.remove()
            self.path_area_box = None  # Reset the attribute
            print('Path area box removed')
        else:
            print('No path area box to reset')
        # Update the plot
        plt.draw()




if __name__ == '__main__':

    shapefile_path = (
        '/Users/dougveilleux/Documents/GitHub/UUVPathPlanningApp/'
        'data/SHAPE_FILE/US4MA23M/US4MA23M_SHAPEFILE.shp'
    )

    chart_us4ma23m = ShapefileHandler(shapefile_path)
    # chart_us4ma23m.plot_shapefile_data()
    chart_us4ma23m.make_water_polygon()

