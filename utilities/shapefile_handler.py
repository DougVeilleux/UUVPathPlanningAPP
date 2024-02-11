# shapefile_handler.py

import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from shapely.geometry import Polygon, Point, MultiPolygon
from shapely.ops import unary_union
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

    def plot_chart_data(self, plot_centroids=False, ax=None):
        """
        Plot shapefile data into a chart using DataFrame.
        """
        if self.data is None:
            print("Shapefile data not loaded. Call read_shapefile() first.")
            return

        if ax is None:
            fig, ax = plt.subplots(figsize=(14, 9))
        else:
            fig = ax.figure

        # Create Set Path Area Button
        btn_set_path_area = plt.axes([0.2, 0.02, 0.08, 0.04])  # [left, bottom, width, height]
        set_path_area = Button(btn_set_path_area, 'Set Path\nArea')
        set_path_area.on_clicked(lambda event: self.set_path_area(event, ax))

        # Create Reset Path Area Button
        btn_reset_path_area = plt.axes([0.3, 0.02, 0.08, 0.04])  # [left, bottom, width, height]
        reset_path_area = Button(btn_reset_path_area, 'Reset Path\nArea')
        reset_path_area.on_clicked(lambda event: self.reset_path_area(event, ax))



        # Create bounding polygon to fill the entire area with light blue
        min_lon, max_lon = self.data.bounds.minx.min(), self.data.bounds.maxx.max()
        min_lat, max_lat = self.data.bounds.miny.min(), self.data.bounds.maxy.max()
        initial_bounding_polygon = Polygon([(min_lon, min_lat), (max_lon, min_lat),
                                            (max_lon, max_lat), (min_lon, max_lat)])
        # Fill the entire area with light blue for water representation
        ax.fill(initial_bounding_polygon.exterior.xy[0], initial_bounding_polygon.exterior.xy[1],
                facecolor='lightblue', edgecolor='none')

        # Overlay land polygons with tan color
        for index, row in self.get_land_coordinates().iterrows():
            lon, lat = row['Longitude'], row['Latitude']
            ax.fill(lon, lat, facecolor=[0.824, 0.706, 0.549], edgecolor='black', linewidth=1)
        # Plot red Dot at centroid of each polygon if desired.
        if plot_centroids:
            centroids = self.calculate_polygon_centroids()
            for centroid in centroids:
                ax.plot(centroid.x, centroid.y, 'ro', markersize=2)

        # vvv FORMATING vvv
        # Set axis labels
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        # Add grid
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        # Setting same scale for x and y axes
        ax.set_aspect('equal')
        # Setting Title
        ax.set_title('NOAA CHART DATA: US4MA23M', fontsize=20)
        # Comment out to work with Tkinter
        plt.show()

    # Button Click Methods
    def set_path_area(self, event, ax):
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

        # Get all polygons within the bounding box
        polygons_within_box = []
        for polygon in self.data['geometry']:
            buffered_polygon = polygon.buffer(0.0001)
            if buffered_polygon.intersects(bounding_box_polygon) or polygon.within(bounding_box_polygon):
                polygons_within_box.append(buffered_polygon)
        print('in box')
        polygons_within_box = MultiPolygon(polygons_within_box)
        print(type(polygons_within_box))
        print(polygons_within_box)


        # Subtract each land polygon from the bounding box polygon
        water_polygon = bounding_box_polygon
        poly_count = 1
        # for i in range(len(polygons_within_box)):
        #     print('Land Polygon: ', poly_count)
        #     # print(polygons_within_box[i])
        #     print('Start Water Area: ', water_polygon.area)
        #     water_polygon = water_polygon.difference(polygons_within_box[i])
        #     print(10*'*')
        #     print("End water Ares: ", water_polygon.area)
        #     poly_count += 1
        # print('water')
        # print(type(water_polygon))
        # print(water_polygon)
        for i, polygon in enumerate(polygons_within_box.geoms):
            print('Land Polygon: ', i + 1)
            print('Start Water Area: ', water_polygon.area)
            water_polygon = water_polygon.difference(polygon)
            print(10 * '*')
            print("End water Area: ", water_polygon.area)
        print('water')
        print(type(water_polygon))
        print(water_polygon)

        # Plot the resulting water polygon
        fig2, ax2 = plt.subplots(figsize=(14, 9))
        if water_polygon.geom_type == 'MultiPolygon':
            for polygon in water_polygon:
                x, y = polygon.exterior.xy
                ax2.fill(x, y, color='lightblue')
            else:
                x, y = water_polygon.exterior.xy
                ax2.fill(x, y, color='lightblue')
        # x, y = water_polygon.exterior.xy
        # ax2.fill(x, y, color='lightblue')

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

    def calculate_polygon_centroids(self):
        """
        Calculate the centroids of each polygon in the shapefile and store those
        :param: geometry from shapefile
        :return: Point data (x, y)
        """
        centroids = []
        for geometry in self.data['geometry']:
            if geometry.geom_type == 'Polygon':
                centroid = geometry.centroid
                # Create a point object representing the centroid
                centroid_point = Point(centroid.x, centroid.y)
                centroids.append(centroid_point)
        return centroids

    def get_water_polygon(self):
        """
        This method performs a subtraction of the land polygons from the polygon
        formed from the bounding polygon (box) of the chart data set.
        It also checks for invalid geometries and handles MultiPolygon objects.

        :return: water polygon or list of polygons
        """
        if self.data is None:
            print("Shapefile data not loaded. Call read_shapefile() first.")
            return

            # Create the bounding box polygon
        min_lon, max_lon = self.data.bounds.minx.min(), self.data.bounds.maxx.max()
        min_lat, max_lat = self.data.bounds.miny.min(), self.data.bounds.maxy.max()
        bounding_polygon = Polygon([(min_lon, min_lat), (max_lon, min_lat),
                                    (max_lon, max_lat), (min_lon, max_lat)])


        # Plot the bounding box
        fig, ax = plt.subplots(figsize=(12, 10))
        ax.fill(*bounding_polygon.exterior.xy, color='lightblue', edgecolor='lightgray')

        # Plot the land polygons on top of the bounding box
        for geometry in self.data['geometry']:
            if geometry.geom_type == 'Polygon':
                x, y = geometry.exterior.xy
                ax.fill(x, y, color='tan')

        # Set axis labels
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')

        # Add grid
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        # Setting same scale for x and y axes
        ax.set_aspect('equal')

        ax.set_title('Bounding Box with Land Polygons')

        poly_count = 1
        water_polygon = bounding_polygon
        land_polygon = self.data['geometry'].buffer(0.0001)

        for i in range(len(land_polygon)):
            print('Land Polygon: ', poly_count)
            print(land_polygon[i])

            water_polygon = water_polygon.difference(land_polygon[i])

            print(10*'*')
            print(water_polygon.area)
            poly_count += 1

            # if i % 10 == 0:
        fig2, ax2 = plt.subplots(figsize=(12, 10))
        # Check if water_polygon is a MultiPolygon
        if water_polygon.geom_type == 'MultiPolygon':
            for polygon in water_polygon.geoms:
                x, y = polygon.exterior.xy
                ax2.fill(x, y, color='lightblue')
        else:
            x, y = water_polygon.exterior.xy
            ax2.fill(x, y, color='lightblue')

        ax2.set_xlabel('Longitude')
        ax2.set_ylabel('Latitude')

        # Add grid
        ax2.grid(True, which='both', linestyle='--', linewidth=0.5)
        # Setting same scale for x and y axes
        ax2.set_aspect('equal')

        ax2.set_title('Water ONLY')
        # Show plot
        plt.show()


    def plot_water_polygons(self, water_polygons, ax=None):
        """
        Plot the water polygons.
        :param water_polygons: List of water polygons to plot
        :param ax: Optional matplotlib axis to plot on
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(12, 10))
        else:
            fig = ax.figure

        for polygon in water_polygons:
            if polygon.geom_type == 'Polygon':
                # pass
                ax.fill(*polygon.exterior.xy, facecolor='red', edgecolor='black')
            elif polygon.geom_type == 'MultiPolygon':
                # pass
                for sub_polygon in polygon.geoms:
                    ax.fill(*sub_polygon.exterior.xy, facecolor='lightblue', edgecolor='none')

        # Set axis labels
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')

        # Add grid
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        # Setting same scale for x and y axes
        ax.set_aspect('equal')

        # Add title
        ax.set_title('Water Polygons', fontsize=20)

        # Show plot
        plt.show()







if __name__ == '__main__':

    shapefile_path = (
        '/Users/dougveilleux/Documents/GitHub/UUVPathPlanningApp/'
        'data/SHAPE_FILE/US4MA23M/US4MA23M_SHAPEFILE.shp'
    )

    chart_us4ma23m = ShapefileHandler(shapefile_path)

    centroids = chart_us4ma23m.calculate_polygon_centroids()
    chart_us4ma23m.plot_chart_data(plot_centroids=False)
