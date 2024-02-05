# set_path_plan_area_handler.py

import os
from shapely.geometry import box
from utilities.shapefile_handler import ShapefileHandler

class SetPathPlanningAreaHandler:
    def __init__(self, shapefile_handler, ax, on_set_path_area):
        self.shapefile_handler = shapefile_handler
        self.ax = ax
        self.bounding_box = None
        self.on_set_path_area = on_set_path_area # Called when the area is set

        # Connect the update_bounding_box method to the 'button_press_event' event
        self.ax.figure.canvas.mpl_connect('button_press_event', self.update_bounding_box)

    def update_bounding_box(self, event):
        if event.inaxes == self.ax:
            x, y = event.xdata, event.ydata
            self.bounding_box = self.get_current_bounding_box(start=(x, y))
            self.on_set_path_area(self.bounding_box)
            self.ax.figure.canvas.draw()

    def get_current_bounding_box(self, start=None):
        if start is None:
            return None
        end = (self.ax.get_xlim()[1], self.ax.get_ylim()[1])
        return box(start[0], start[1], end[0], end[1])

    def get_bounding_box(self):
        return self.bounding_box

    def process_bounding_box(self, bounding_box):
        if bounding_box is not None:
            path_area = self.shapefile_handler.get_land_coordinates_in_bounding_box(bounding_box)
            # Save the DataFrame to a CSV file
            project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
            csv_folder = os.path.join(project_root, 'data', 'path_planning_area')
            path_area.to_csv(os.path.join(csv_folder, 'path_area_data.csv'), index=False)

            print("Path Planning Area Selected")
            return path_area
        else:
            print("No Path Planning Bounding Box Area Selected")
