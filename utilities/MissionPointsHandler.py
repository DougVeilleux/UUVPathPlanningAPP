# MissionPointsHandler.py

from shapely.geometry import Point
import os

class MissionPointsHandler:
    def __init__(self, ax, shapefile_handler):
        self.ax = ax
        self.shapefile_handler = shapefile_handler
        self.start_point = None
        self.park_point = None
        self.start_point_set = False
        self.park_point_set = False

        # Connect the update_start_point method to the 'button_press_event' event
        self.start_click = self.ax.figure.canvas.mpl_connect('button_press_event', self.set_start_point)
        self.park_click = self.ax.figure.canvas.mpl_connect('button_press_event', self.set_park_point)

    def set_start_point(self, event):
        if event.inaxes == self.ax:
            # Get the click event coordinates
            x, y = event.xdata, event.ydata
            if x is not None and y is not None:
                # Convert the data coordinates to longitude and latitude
                lon, lat = x, y  # Assuming the data coordinates are already in lon-lat
                self.start_point = Point(lon, lat)
                self.add_point_to_figure(self.start_point, color='green')
                self.save_point_to_csv(self.start_point, 'start_point.csv')
                self.start_point_set = True

    def reset_start_point(self):
        self.start_point = None
        for collection in self.ax.collections:
            if collection.get_facecolor() == (0.0, 1.0, 0.0, 1.0):
                collection.remove()
        self.ax.figure.canvas.draw()


    def set_park_point(self, event):
        if event.inaxes == self.ax:
            # Get the click event coordinates
            x, y = event.xdata, event.ydata
            if x is not None and y is not None:
                # Convert the data coordinates to longitude and latitude
                lon, lat = x, y  # Assuming the data coordinates are already in lon-lat
                self.park_point = Point(lon, lat)
                self.add_point_to_figure(self.park_point, color='red')
                self.save_point_to_csv(self.park_point, 'manual_park_point.csv')
                self.park_point_set = True

    def reset_park_point(self):
        self.park_point = None
        for collection in self.ax.collections:
            if collection.get_facecolor() == (1.0, 0.0, 0.0, 1.0):
                collection.remove()
        self.ax.figure.canvas.draw()

    def add_point_to_figure(self, point, color='green'):
        if point is not None:
            self.ax.plot(point.x, point.y, marker='o', markersize=8,
                         markeredgecolor='black', markerfacecolor=color)
            self.ax.figure.canvas.draw()

    def save_point_to_csv(self, point, filename):
        if point is not None:
            project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
            csv_folder = os.path.join(project_root, 'data', 'mission_points')
            try:
                with open(os.path.join(csv_folder, filename), 'w') as file:
                    file.write('Longitude,Latitude\n')
                    file.write(f'{point.x},{point.y}\n')
            except Exception as e:
                print(f"Error writing to CSV file: {e}")



