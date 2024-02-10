# mission_points_handler.py

from shapely.geometry import Point
import os

class MissionPointsHandler:
    def __init__(self, ax, shapefile_handler, start_point_set=False, park_point_set=False):
        self.ax = ax
        self.shapefile_handler = shapefile_handler
        self.start_point = None
        self.park_point = None
        self.start_point_set = start_point_set
        self.park_point_set = park_point_set

        # Connect the update_start_point and update_park_point methods to the 'button_press_event' event
        self.ax.figure.canvas.mpl_connect('button_press_event', self.update_start_point)
        self.ax.figure.canvas.mpl_connect('button_press_event', self.update_park_point)

    def update_start_point(self, event):
        print("Update start point method called")
        if event.inaxes == self.ax and not self.start_point_set:  # Check if start point button is clicked
            x, y = event.xdata, event.ydata
            lon, lat = self.ax.transData.inverted().transform((x, y))  # Convert display coordinates to lon-lat
            self.start_point = Point(lon, lat)
            self.add_point_to_figure(self.start_point, color='green')
            self.save_point_to_csv(self.start_point, 'start_point.csv')
            self.start_point_set = True  # Set the start point flag to True after setting the point

    def update_park_point(self, event):
        print("Update park point method called")
        if event.inaxes == self.ax and not self.park_point_set:  # Check if park point button is clicked
            x, y = event.xdata, event.ydata
            lon, lat = self.ax.transData.inverted().transform((x, y))  # Convert display coordinates to lon-lat
            self.park_point = Point(lon, lat)
            self.add_point_to_figure(self.park_point, color='red')
            self.save_point_to_csv(self.park_point, 'park_point.csv')
            self.park_point_set = True  # Set the park point flag to True after setting the point

    def add_point_to_figure(self, point, color='green'):
        if point is not None:
            self.ax.plot(point.x, point.y, marker='o', markersize=8,
                         markeredgecolor='black', markerfacecolor=color)
            self.ax.figure.canvas.draw()

    def save_point_to_csv(self, point, filename):
        if point is not None:
            project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
            csv_folder = os.path.join(project_root, 'data', 'mission_points')
            with open(os.path.join(csv_folder, filename), 'w') as file:
                file.write('Longitude,Latitude\n')
                file.write(f'{point.x},{point.y}\n')



