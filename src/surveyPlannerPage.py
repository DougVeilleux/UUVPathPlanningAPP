# surveyPlannerPage.py
import tkinter as tk
import matplotlib
matplotlib.use('TkAgg')

from tkinter import ttk
class SurveyPlannerPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self).pack(side="top", fill="x", pady=10)
