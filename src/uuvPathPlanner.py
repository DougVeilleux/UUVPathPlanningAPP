# uuvPathPlanner.py

import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
from tkinter import ttk
from utilities.AstarPathPlanner import *
from utilities.QuadTreeGeodata import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from shapely.geometry import box
from utilities.QuadTreeGeodata import ShapefileHandler

class AStarGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("A* Path Planner")

        # Create Matplotlib figures and canvas with borders
        self.fig_upper = Figure(figsize=(14, 9), dpi=100)
        self.ax_upper = self.fig_upper.add_subplot(111)
        self.canvas_upper = FigureCanvasTkAgg(self.fig_upper, master=self.root)
        self.canvas_upper.get_tk_widget().grid(row=0, column=1, padx=10, pady=10, rowspan=2)
        self.canvas_upper.get_tk_widget().config(borderwidth=2, relief="solid")

        self.fig_lower = Figure(figsize=(7, 4.5), dpi=100)
        self.ax_lower = self.fig_lower.add_subplot(111)
        self.canvas_lower = FigureCanvasTkAgg(self.fig_lower, master=self.root)
        self.canvas_lower.get_tk_widget().grid(row=2, column=1, padx=10, pady=10)
        self.canvas_lower.get_tk_widget().config(borderwidth=2, relief="solid")

        # Create GUI elements
        self.create_buttons()
        self.create_terminal()

        # Load and plot shapefile data on the upper figure
        self.load_and_plot_shapefile()

    def create_buttons(self):
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.grid(row=0, column=0, rowspan=4, sticky="ns")

        self.set_start_button = tk.Button(self.buttons_frame, text="Set Start", command=self.set_start)
        self.set_start_button.grid(row=0, column=0, sticky="ew", padx=5, pady=(5,10))

        self.set_goal_button = tk.Button(self.buttons_frame, text="Set Goal", command=self.set_goal)
        self.set_goal_button.grid(row=1, column=0, sticky="ew", padx=5, pady=10)

        self.plan_path_button = tk.Button(self.buttons_frame, text="Plan Path", command=self.plan_path)
        self.plan_path_button.grid(row=2, column=0, sticky="ew", padx=5, pady=10)

        self.reset_button = tk.Button(self.buttons_frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=3, column=0, sticky="ew", padx=5, pady=10)

    def create_terminal(self):
        self.terminal = tk.Text(self.root, height=16, width=120, wrap="word")
        self.terminal.grid(row=4, column=0, columnspan=2, pady=10)



    self.quadtree.visualize_chart_data(ax)

    def set_start(self):
        # Implement logic to allow user to set the start point
        pass

    def set_goal(self):
        # Implement logic to allow user to set the goal point
        pass

    def plan_path(self):
        # Implement logic to trigger A* path planning
        pass

    def reset(self):
        # Implement logic to reset the map and clear paths
        pass

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = AStarGUI(root)
    app.run()