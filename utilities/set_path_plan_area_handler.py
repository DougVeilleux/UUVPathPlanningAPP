# set_path_plan_area_handler.py

from shapely.geometry import box

class SetPathPlanningAreaHandler:
    def __init__(self, shapefile_handler, ax):
        self.shapefile_handler = shapefile_handler
        self.ax = ax
        self.bounding_box = None

        # Connect the update_bounding_box method to the 'button_press_event' event
        self.ax.figure.canvas.mpl_connect('button_press_event', self.update_bounding_box)

    def update_bounding_box(self, event):
        if event.inaxes == self.ax:
            x, y = event.xdata, event.ydata
            self.bounding_box = self.get_current_bounding_box(start=(x, y))
            self.ax.figure.canvas.draw()

    def get_current_bounding_box(self, start=None):
        if start is None:
            return None
        end = (self.ax.get_xlim()[1], self.ax.get_ylim()[1])
        return box(start[0], start[1], end[0], end[1])

    def get_bounding_box(self):
        return self.bounding_box
