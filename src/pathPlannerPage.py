# pathPlannerPage.py
import tkinter as tk
import matplotlib
import sys

matplotlib.use('TkAgg')
from utilities.AstarPathPlanner import *
from utilities.QuadTreeGeodata import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import messagebox

class PathPlannerPage(tk.Frame):
    """
    Class to handle the Path Planner Page of the App:
        - For this stage of the development the operational area will be predefined
            (though many miles width and height) to simplify the GUI and keep the
            focus to the Astar Planning
        - The QuadTree Data will be loaded during class instantiation.
        - The user will be able to interact with page by selecting the start and goal
            points and then select "Plan Path"
        - The app wil then display an animation of the Astar solution computing and then
            displaying the final Astar computed path.
    """
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="UUV Path Planner").pack(side="top", fill="x", pady=10)

        # Initialize connection IDs for event handlers
        self.cid_start = None
        self.cid_goal = None
        # Variables to store selected coordinates
        self.start_point = (-70.80, 41.28)
        self.goal_point = (-70.87, 41.28)
        self.start_point = None
        self.goal_point = None


        # Instantiate the QuadTree Data for Main Frame Figure Interaction
        # AND for the AStar Algorithm to work with
        quadtree_data_path = (
            '/Users/dougveilleux/Documents/GitHub/UUVPathPlanningApp/'
            'data/quad_tree/vineyardsound_coarse.qtdata'
        )
        self.quadtree = deserialize_quad_tree(quadtree_data_path)

        back_color = "#AEBFCF"
        # Main figure and buttons
        main_frame = tk.Frame(self, bg=back_color)
        main_frame.pack(side="left", fill="both", expand=True)

        self.fig1 = Figure(figsize=(7, 7), dpi=100)
        self.ax1 = self.fig1.add_subplot(111)
        self.ax1.set_title('SELECTED UUV OP AREA', fontdict={'family': 'Helvetica', 'size': 24})
        self.fig1.set_facecolor(back_color)
        self.quadtree.visualize_chart_data(ax=self.ax1)

        self.canvas1 = FigureCanvasTkAgg(self.fig1, main_frame)
        self.canvas1.draw()
        self.canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # Add navigation toolbar
        self.toolbar1 = NavigationToolbar2Tk(self.canvas1, main_frame)
        self.toolbar1.update()
        self.canvas1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Add buttons to select start and goal points
        button_frame = tk.Frame(main_frame)
        button_frame.config(bg=back_color)
        button_frame.pack(side="bottom", pady=50)

        self.select_start_point_button = tk.Button(button_frame, text="Select Start Point",
                                                   command=lambda: self.select_point("start"),
                                                   height=2)
        self.select_start_point_button.pack(side=tk.LEFT, padx=10)
        self.select_goal_point_button = tk.Button(button_frame, text="Select Goal Point",
                                                  command=lambda: self.select_point("goal"),
                                                  height=2)
        self.select_goal_point_button.pack(side=tk.LEFT, padx=10)
        self.reset_points_button = tk.Button(button_frame, text="Reset Points",
                                             command=self.reset_points,
                                             height=2)
        self.reset_points_button.pack(side=tk.LEFT, padx=10)
        self.path_plan_button = tk.Button(button_frame, text="Plan Path",
                                          command=self.plan_path,
                                          height=2)
        self.path_plan_button.pack(side=tk.LEFT, padx=10)

        # Right side frames
        right_frame = tk.Frame(self, bg=back_color)
        right_frame.pack(side="right", fill="both", expand=True)
        right_top_frame = tk.Frame(right_frame)
        right_top_frame.pack(side="top", fill="both", expand=True)
        right_bottom_frame = tk.Frame(right_frame)
        right_bottom_frame.pack(side="bottom", fill="both", expand=True)

        # Second figure Top Right Frame
        self.fig2 = Figure(figsize=(3, 3), dpi=100)
        self.ax2 = self.fig2.add_subplot(111)
        self.ax2.set_title("AStar Algorithm Visualization")
        self.fig2.set_facecolor(back_color)
        self.quadtree.visualize_chart_data(ax=self.ax2)

        self.canvas2 = FigureCanvasTkAgg(self.fig2, right_bottom_frame)
        self.canvas2.draw()
        self.canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # Add navigation toolbar
        self.toolbar2 = NavigationToolbar2Tk(self.canvas2, right_bottom_frame)
        self.toolbar2.update()
        self.canvas2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.toolbar2.config(background=back_color)

        # Terminal title
        terminal_title = tk.Label(right_top_frame, text="Terminal Window", font=("Helvetica", 14))
        terminal_title.pack(side="top", pady=10)
        # Terminal
        self.terminal = tk.Text(right_top_frame, wrap="word", height=30, width=50)
        self.terminal.pack(side="top", fill="both", expand=True)
        self.terminal.config(bg="#262660")
        # Clear Terminal Button
        clear_button = tk.Button(right_top_frame, text="Clear Terminal", command=self.clear_terminal)
        clear_button.pack(side="bottom", pady=10)

        # Instantiate the AStarPathPlanner object
        self.astar_planner = AStarPathPlanner(self.quadtree)


    ### vvv Helper Methods vvv###
    def clear_terminal(self):
        self.terminal.delete(1.0, tk.END)

    def select_point(self, point_type):
        # Disconnect previous event handlers
        self.canvas1.mpl_disconnect(self.cid_start)
        self.canvas1.mpl_disconnect(self.cid_goal)

        # Bind the click event to get coordinates
        if point_type == "start":
            self.cid_start = self.canvas1.mpl_connect('button_press_event',
                                                      lambda event: self.get_coordinates(event, point_type))
        elif point_type == "goal":
            self.cid_goal = self.canvas1.mpl_connect('button_press_event',
                                                     lambda event: self.get_coordinates(event, point_type))


    def get_coordinates(self, event, point_type):
        # Get coordinates of the cursor location
        x = event.xdata
        y = event.ydata
        if x is not None and y is not None:
            # Round coordinates to three decimal places
            x_rounded = round(x, 3)
            y_rounded = round(y, 3)
            # Save rounded coordinates as a tuple based on point type
            if point_type == "start":
                self.start_point = (x_rounded, y_rounded)
                self.plot_star(x_rounded, y_rounded, 'g')  # Plot green star for start point
                print("Start Point coordinates:", self.start_point)
                self.terminal.insert(tk.END, "Start Point coordinates: {}\n".format(self.start_point))
            elif point_type == "goal":
                self.goal_point = (x_rounded, y_rounded)
                self.plot_star(x_rounded, y_rounded, 'r')  # Plot red star for goal point
                print("Goal Point coordinates:", self.goal_point)
                self.terminal.insert(tk.END, "Goal Point coordinates: {}\n".format(self.goal_point))

    def plot_star(self, x, y, color):
        self.ax1.plot(x, y, marker='*', markersize=10, markerfacecolor=color)
        self.canvas1.draw()

    def reset_points(self):
        # Clear stored points
        self.start_point = None
        self.goal_point = None
        # Clear plot
        self.ax1.clear()
        self.quadtree.visualize_chart_data(ax=self.ax1)
        self.ax1.set_title("SELECTED UUV OP AREA")
        self.terminal.insert(tk.END, "Reset both start and goal points. Select again.")
        # Update plot with cleared points
        self.canvas1.draw()

    def plan_path(self):
        """
        Run the AStar Path Planner
        """
        print("Starting plan_path method...")
        self.terminal.insert(tk.END, "Starting plan_path method...")
        # Check if start and goal points are selected
        if self.start_point is None or self.goal_point is None:
            messagebox.showwarning("Warning", "Please select start and goal points.")
            return

        # print("Start point:", self.start_point)  # Debug Statement
        # print("Goal point:", self.goal_point)  # Debug Statement
        # Call astar_path method to calculate the optimal path
        PATH = self.astar_planner.astar_path(self.start_point, self.goal_point, distance=1000)

        # Visualize the optimal path
        if PATH:
            print("Path found:", PATH)  # Debug Statement
            self.terminal.insert(tk.END, "Path found: {}", PATH)
            self.astar_planner.visualize_astar_path(self.start_point, self.goal_point, PATH,
                                                    ax=self.ax1, appDisplay=True)
            self.canvas1.draw()  # Update the canvas

            # # Update the AStar algorithm visualization in self.fig2
            # past_points_for_display = []  # Assuming you have past points to display
            # self.astar_planner.visualize_astar_algorithm(self.start_point, self.goal_point, path[-1],
            #                                              past_points_for_display,
            #                                              ax=self.ax2, appDisplay=False)
            # self.canvas2.draw()  # Update the canvas for self.fig2
        else:
            print("Failed to find a path.")  # Debug Statement
            messagebox.showinfo("Information", "Failed to find a path.")

        print("Exiting plan_path method.")  # Debug Statement
        self.terminal.insert(tk.END, "Exiting plan_path method.")
