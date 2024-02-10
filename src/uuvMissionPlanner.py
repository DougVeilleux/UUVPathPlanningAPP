# uuvMissionPlanner.py
"""

Simple GUI app to interface with Chart for planning a mission.
Additionaly, it feeds input data to path planning and survey
planning alogrithms.  Finally, displaying and animating the
UUV motions.

"""
import tkinter as tk
import sys
import numpy as np
import pandas as pd

# Use TkAgg backend for macOS
if sys.platform == "darwin":
    import matplotlib
    matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from utilities.shapefile_handler import ShapefileHandler
from utilities.set_path_plan_area_handler import SetPathPlanningAreaHandler
from utilities.mission_points_handler import MissionPointsHandler


from button_handler import ButtonHandler

class UUVMissionPlannerApp:
    # Constructor vvv
    def __init__(self, shapefile_path):
        self.shapefile_path = shapefile_path
        self.shapefile_handler = ShapefileHandler(self.shapefile_path)
        self.path_area_set = False
        self.start_point = None
        self.park_point = None



        # Instantiate the Tkinter Window Object
        self.root = tk.Tk()
        self.root.title("UUV Mission Planner")
        self.root.geometry("1050x1050")
        # Setup the figure size within the Tk Window
        self.fig, self.ax = plt.subplots(figsize=(7.0, 7.0))
        self.fig.subplots_adjust(left=0.08, right=0.92, top=0.92, bottom=0.08)
        # Setup Frame for Widgets (buttons, etc)
        self.frame = tk.Frame(self.root)
        # Create the canvas to embed Matplot figure in the Tkinter window.
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        # Add Matplotlib Nav/Zoom Toolbar to Tk Window
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.frame)
        self.toolbar.update()
        self.toolbar.pack(side="top", fill=tk.X)
        # Pad the Top Margin again and pack the frame into the Tk Window
        self.frame.pack(pady=40)

        # Callback the plot shapefile during instantiation
        self.plot_shapefile_data()

        # Instantiate Interactive Boxes and Buttons via ButtonHandler
        self.button_handler = ButtonHandler(self.root, self.plot_shapefile_data,
                                            self.set_path_planning_area_action,
                                            self.set_start_point, self.reset_start_point,
                                            self.set_park_point, self.reset_park_point).create_buttons()

        # Create an instance of SetPathPlanningAreaHandler
        self.set_path_plan_area_handler = SetPathPlanningAreaHandler(self.shapefile_handler, self.ax,

                                                                     self.on_set_path_area)
        # Create an instance of MissionPointsHandler
        self.mission_points_handler = MissionPointsHandler(self.ax, self.shapefile_handler)

    # METHODS vvv
    # Chart Area display
    def plot_shapefile_data(self):
        """
        Callback - using the Shapefile Handler method plot_land_coordinates
        to the Tk window. Then the constructor displays the plot upon instantiation.
        """
        self.shapefile_handler.plot_land_coordinates(self.ax)
        self.canvas.draw()

    # Path Planning Methods
    def on_set_path_area(self, bounding_box):
        if self.path_area_set:
            self.set_path_plan_area_handler.process_bounding_box(bounding_box)

    def set_path_planning_area_action(self):
        print(f"Path Planning Area Coordinates Stored.")
        bounding_box = self.set_path_plan_area_handler.get_bounding_box()
        self.on_set_path_area(bounding_box)
        self.path_area_set = True #Set flag

    def set_start_point(self, event):
        print("Select Start Point Location.")
        # Pass the event information when calling set_start_point
        # event = self.root.focus_get()  # Get the current event
        self.mission_points_handler.set_start_point(event)

    def reset_start_point(self):
        print("Start Point Reset.")
        self.mission_points_handler.reset_start_point()

    def set_park_point(self, event):
        print("Select Park Point Location.")
        self.mission_points_handler.set_park_point(event)

    def reset_park_point(self):
        print("Park Point Reset.")
        self.mission_points_handler.reset_park_point()










    def set_survey_planning_area(self):
        """
        Description:
            When method is run it shall take the lat, lon and land data within the full area selected
            on the figure.

        Return:
            survey_area : dataframe
        """
        pass

    def generate_paths(self):
        """
        Description:
            When method is run it reads in data frame from "set_path_planning_area".
        Args:
            path_area : dataframe
        Return:
            ingress_path : dataframe
        """
        pass

    def generate_survey_paths(self):
        """
        Description:
            When method is run it reads in dataframe from "set_survey_planning_area".
        Args:
            survey_area : dataframe
        Return:
            survey_path : dataframe
        """
        pass


    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    shapefile_path = ('/Users/dougveilleux/Documents/GitHub/UUVPathPlanningApp/data/'
                      'SHAPE_FILE/US4MA23M/US4MA23M_SHAPEFILE.shp')
    app = UUVMissionPlannerApp(shapefile_path)
    app.run()







