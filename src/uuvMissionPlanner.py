# uuvMissionPlanner.py

from startPage import *
from pathPlannerPage import *
from surveyPlannerPage import *


class UuvMissionPlanner(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("UUV Path Planner")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        self.start_page = StartPage(self.notebook)
        self.path_planner_page = PathPlannerPage(self.notebook)
        self.survey_page = SurveyPlannerPage(self.notebook)

        self.notebook.add(self.start_page, text="Start Page")
        self.notebook.add(self.path_planner_page, text="Path Planner")
        self.notebook.add(self.survey_page, text="Survey Planner")


if __name__ == "__main__":
    app = UuvMissionPlanner()
    app.geometry("1500x1000")

    # Start the main event loop
    app.mainloop()
