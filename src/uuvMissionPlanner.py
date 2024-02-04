
"""

Simple GUI app to interface with Chart for planning a mission.
Additionaly, it feeds input data to path planning and survey
planning alogrithms.  Finally, displaying and animating the
UUV motions.

"""
import tkinter as tk
import sys
# Use TkAgg backend for macOS
if sys.platform == "darwin":
    import matplotlib
    matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import matplotlib.figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from utilities.shapefile_handler import ShapefileHandler
from button_handler import ButtonHandler
# from set_path_plan_area_handler import SetPathPlanningAreaHandler

import numpy as np


class UUVMissionPlannerApp:
    def __init__(self, shapefile_path):
        self.shapefile_path = shapefile_path
        self.shapefile_handler = ShapefileHandler(self.shapefile_path)

        # Instantiate the Tkinter Window Object
        self.root = tk.Tk()
        self.root.title("UUV Mission Planner")
        self.root.geometry("900x900")
        # Setup the figure size within the Tk Window
        self.fig, self.ax = plt.subplots(figsize=(7.0, 5.5))
        self.fig.subplots_adjust(left=0.08, right=0.92, top=0.92, bottom=0.08)

        self.frame = tk.Frame(self.root)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        # Add Matplotlib Nav/Zoom Toolbar to Tk Window
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.frame)
        self.toolbar.update()
        self.toolbar.pack(side="top", fill=tk.X)
        # Pad the Top Margin again
        self.frame.pack(pady=40)

        # Setup / Display Interactive Buttons
        # Create an instance of ButtonHandler
        self.button_handler = ButtonHandler(self.root, self.plot_shapefile_data,
                                            self.plot_random_data)
        # Call create_buttons method to create buttons
        self.button_handler.create_buttons()

        # Call the plot shapefile to load and plot during instantiation
        self.plot_shapefile_data()


    def plot_shapefile_data(self):
        # print("Set Path Planning Area button pressed")
        # Use the ShapefileHandler to plot shapefile data
        self.shapefile_handler.plot_land_coordinates(self.ax)
        self.canvas.draw()
        # If reset from Toolbar navigation is casuing problems this can fix it.
        # self.ax.cla()
        # self.ax.plot(data['x'], data['y'])
        # self.ax.grid(True)
        # self.canvas.draw()

    def plot_random_data(self):
        print("Generate Paths / Set Survey Area / Generate Survey Paths button pressed")
        self.ax.cla()
        x = np.random.randint(0, 10, 10)
        y = [val**2 for val in x]
        self.ax.plot(x, y)
        self.ax.grid(True)
        self.canvas.draw()

    def set_path_planning_area(self):
        """
        Description:
            When method is run it shall take the lat, lon and land data within the full area shown
            on the figure.

        Return:
            path_area : dataframe
        """
        pass

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







