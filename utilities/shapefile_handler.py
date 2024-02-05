# shapefile_handler.py

import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, Point
import pandas as pd
import numpy as np

class ShapefileHandler:

    def __init__(self, shapefile_path):
        self.shapefile_path = shapefile_path
        self.data = None
        self.read_shapefile()

    def read_shapefile(self):
        """
        Reads Shapefile with gpd.read()
        """
        self.data = gpd.read_file(self.shapefile_path)

    def get_land_coordinates(self):
        """
        Get the latitude and longitude data from each polygon in the
        shapefile and return a DataFrame of coordinates for each Polygon
        """
        coordinates = []

        for geometry in self.data['geometry']:
            if geometry.geom_type == 'Polygon':
                lon, lat = geometry.exterior.xy
                coordinates.append((lon, lat))

        df = pd.DataFrame(coordinates, columns=['Longitude', 'Latitude'])
        return df

    def plot_land_coordinates(self, ax=None):
        """
        Plot shapefile data into a chart using DataFrame.
        """
        if self.data is None:
            print("Shapefile data not loaded. Call read_shapefile() first.")
            return

        if ax is None:
            fig, ax = plt.subplots(figsize=(12, 10))
        else:
            fig = ax.figure

        # Create bounding polygon to fill the entire area with light blue
        min_lon, max_lon = self.data.bounds.minx.min(), self.data.bounds.maxx.max()
        min_lat, max_lat = self.data.bounds.miny.min(), self.data.bounds.maxy.max()
        bounding_polygon = Polygon([(min_lon, min_lat), (max_lon, min_lat), (max_lon, max_lat), (min_lon, max_lat)])

        # Fill the entire area with light blue
        ax.fill(bounding_polygon.exterior.xy[0], bounding_polygon.exterior.xy[1], facecolor='lightblue',
                edgecolor='none')

        # Overlay land polygons with tan color
        for index, row in self.get_land_coordinates().iterrows():
            lon, lat = row['Longitude'], row['Latitude']
            ax.fill(lon, lat, facecolor=[0.824, 0.706, 0.549], edgecolor='black', linewidth=1)

        # Set axis labels
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')

        # Add grid
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)

        def update_grid(event):
            # Update grid based on current plot limits (zoom adjustment)
            ax.set_xticks(np.arange(round(ax.get_xlim()[0], 1), ax.get_xlim()[1], 0.1))
            ax.set_yticks(np.arange(round(ax.get_ylim()[0], 1), ax.get_ylim()[1], 0.1))
            ax.grid(True, which='both', linestyle='--', linewidth=0.5)
            plt.draw()

        # Connect the update_grid function to the 'motion_notify_event' event
        fig.canvas.mpl_connect('resize_event', update_grid)

        ax.set_title('NOAA CHART DATA: US4MA23M', fontsize=20)

        # Comment out to work with Tkinter
        # plt.show()

    def get_land_coordinates_in_bounding_box(self, bounding_box):
        """
        Get the latitude and longitude data from each polygon in the
        shapefile within the specified bounding box and return a DataFrame
        of coordinates for each Polygon.
        """
        # Extract bounding box coordinates
        min_x, min_y, max_x, max_y = bounding_box.bounds

        # Filter polygons within the bounding box
        filtered_data = self.data.cx[min_x:max_x, min_y:max_y]

        coordinates = []
        for geometry in filtered_data['geometry']:
            if geometry.geom_type == 'Polygon':
                lon, lat = geometry.exterior.xy
                coordinates.append((lon, lat))

        df = pd.DataFrame(coordinates, columns=['Longitude', 'Latitude'])
        return df
