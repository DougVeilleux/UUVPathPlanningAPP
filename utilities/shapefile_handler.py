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
        self.shapefile_path = shapefile_path
        self.data = None
        self.read_shapefile()

    def read_shapefile(self):
        """
        Reads Shapefile with gpd.read()
        """
        self.data = gpd.read_file(self.shapefile_path)

    def display_shapefile_data(self):
        """
        Display Shapefile contents as read in PandasGUI
        """
        show(self.data)

    def get_coordinate_data(self, displayPandasGUI=False):
        """
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
        ax.set_aspect('equal')
        # Setting Title
        ax.set_title('NOAA CHART DATA: US4MA23M', fontsize=20)
        # Comment out to work with Tkinter
        plt.show()

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

    def make_water_polygon(self, ax=None):
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

        bounding_polygon = Polygon([(min_lon, min_lat), (max_lon, min_lat),
                                    (max_lon, max_lat), (min_lon, max_lat)])
        # Set water polygon to chart data bounding box
        water_polygon = bounding_polygon
        # Take in the shapefile data geometry
        land_polygons = self.data['geometry']



        for i in range(len(land_polygons)):
            water_polygon = water_polygon.difference(land_polygons[i])
            # Debug Statements
            # if i % 30 == 0:
            #     print('Land Polygon: ', i + 1, "is being subtracted from the water domain.")
            #     print(f'Water Area Before Subtraction, {i+1}, {water_polygon.area}')
            #     # Subtract one land polygon from the water domain polygon
            #     print(f'Water Area AFTER Subtraction, {i+1}, {water_polygon.area}\n')

        if water_polygon.geom_type == 'MultiPolygon':
            print(f"Type Before Merge: {water_polygon.geom_type}")
            merged_water_polygon = unary_union(water_polygon)
            print(f"Type After Merge: {merged_water_polygon.geom_type}")



        # Plot the updated water polygon
        if ax is None:
            fig, ax = plt.subplots(figsize=(14, 9))
        else:
            fig = ax.figure
        if merged_water_polygon.geom_type == 'Polygon':
            ax.fill(*water_polygon.exterior.xy, color='cornflowerblue', edgecolor='lightgray')
        elif merged_water_polygon.geom_type == 'MultiPolygon':
            for polygon in water_polygon.geoms:
                ax.fill(*polygon.exterior.xy, color='cornflowerblue', edgecolor='lightgray')

        # vvv FORMATTING vvv
        # Set axis labels
        ax.set_xlabel('Longitude')
        ax.set_ylabel('Latitude')
        # Add grid
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        # Setting same scale for x and y axes
        ax.set_aspect('equal')
        # Setting Title
        ax.set_title('Water Domain Polygon', fontsize=20)
        # Show plot
        plt.show()




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

        # Create the bounding box polygon which establishes the starting water polygon
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
        # ax.set_aspect('equal')

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
    # chart_us4ma23m.display_shapefile_data()
    # Convert Shape Data to Dataframe
    df_coords = chart_us4ma23m.get_coordinate_data(displayPandasGUI=False)

    # chart_us4ma23m.plot_chart_data(plot_centroids=True)
    chart_us4ma23m.make_water_polygon()







"""
Reset this approach.
1) Let's get the shape file data into a GeoDataFrame.
2) Display and manipulate this dataframe into a form that can be plotted
3) I want the GeoDataframe to have each polygon in a row

"""