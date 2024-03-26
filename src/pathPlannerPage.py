# pathPlannerPage.py
import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')
from utilities.AstarPathPlanner import *
from utilities.QuadTreeGeodata import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


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
        # tk.Button(self, text="Return to start page",
        #           command=lambda: master.switch_frame(StartPage)).pack()

        # Terminal window to display selected coordinates
        self.terminal = tk.Text(self, wrap="word", height=10, width=50)
        self.terminal.pack(side="bottom", fill="both", expand=False)

        # Variables to store selected coordinates
        self.start_point = None
        self.goal_point = None

        # Load QuadTree Data
        quadtree_data_path = (
            '/Users/dougveilleux/Documents/GitHub/UUVPathPlanningApp/'
            'data/quad_tree/vineyardsound_coarse.qtdata'
        )
        self.quadtree = deserialize_quad_tree(quadtree_data_path)

        self.f = Figure(figsize=(7, 4.5), dpi=100)
        self.a = self.f.add_subplot(111)
        self.a.set_title("SELECTED UUV OP AREA")
        self.quadtree.visualize_chart_data(ax=self.a)

        self.canvas = FigureCanvasTkAgg(self.f, self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Add navigation toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas, self)
        self.toolbar.update()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Add buttons to select start and goal points
        self.select_start_point_button = tk.Button(self, text="Select Start Point",
                                                   command=lambda: self.select_point("start"),
                                                   height=2)
        self.select_start_point_button.pack(side=tk.LEFT, padx=10)
        self.select_goal_point_button = tk.Button(self, text="Select Goal Point",
                                                  command=lambda: self.select_point("goal"),
                                                  height=2)
        self.select_goal_point_button.pack(side=tk.LEFT, padx=10)
        # Add button to reset points
        self.reset_points_button = tk.Button(self, text="Reset Points", command=self.reset_points,
                                             height=2)
        self.reset_points_button.pack(side=tk.LEFT, padx=10)
        # Add button to reset points
        self.path_plan_button = tk.Button(self, text="Plan Path", command=self.plan_path,
                                          height=2)
        self.path_plan_button.pack(side=tk.LEFT, padx=10)


    ### METHODS ###
    def select_point(self, point_type):
        # Bind the click event to get coordinates
        self.canvas.mpl_connect('button_press_event', lambda event: self.get_coordinates(event, point_type))

    def get_coordinates(self, event, point_type):
        # Get coordinates of the cursor location
        x = event.xdata
        y = event.ydata
        if x is not None and y is not None:
            # Save coordinates as a tuple based on point type
            if point_type == "start":
                self.start_point = (x, y)
                self.plot_star(x, y, 'g')  # Plot green star for start point
                print("Start Point coordinates:", self.start_point)
                self.terminal.insert(tk.END, "Start Point coordinates: {}\n".format(self.start_point))
                # # Disable the select start point button
                # self.select_start_point_button.config(state=tk.DISABLED)
            elif point_type == "goal":
                self.goal_point = (x, y)
                self.plot_star(x, y, 'r')  # Plot red star for goal point
                print("Goal Point coordinates:", self.goal_point)
                self.terminal.insert(tk.END, "Goal Point coordinates: {}\n".format(self.goal_point))
                # # Disable the select goal point button
                # self.select_goal_point_button.config(state=tk.DISABLED)

    def plot_star(self, x, y, color):
        self.a.plot(x, y, marker='*', markersize=10, markerfacecolor=color)
        self.canvas.draw()

    def reset_points(self):
        # Clear stored points
        self.start_point = None
        self.goal_point = None
        # Clear plot
        self.a.clear()
        self.quadtree.visualize_chart_data(ax=self.a)
        self.a.set_title("SELECTED UUV OP AREA")
        self.terminal.insert(tk.END, "Reset both start and goal points. Select again.")
        # Update plot with cleared points
        self.canvas.draw()

    def plan_path(self):
        if self.start_point is None or self.goal_point is None:
            print("Please select both start and goal points.")
            self.terminal.insert(tk.END, "Please select both start and goal points.")

            return

        print("Planning the path from", self.start_point, "to", self.goal_point)
        self.terminal.insert(tk.END, f"Planning the path from {self.start_point} to {self.goal_point}\n")

        closest_start_node, closest_start_nodes, start_search_region = self.quadtree.find_closest_node(self.start_point)
        closest_goal_node, closest_goal_nodes, goal_search_region = self.quadtree.find_closest_node(self.goal_point)

        uuvIngressPath = AStarPathPlanner(self.quadtree)
        path = uuvIngressPath.astar_path(closest_start_node, closest_goal_node)

        # Clear existing plot
        self.a.clear()
        # self.quad_tree.visualize_chart_data(ax=self.a)
        uuvIngressPath.visualize_astar_path(self.start_point, self.goal_point,
                                            closest_start_node, closest_goal_node, path, ax=self.a)
        # Update plot with cleared points
        self.canvas.draw()