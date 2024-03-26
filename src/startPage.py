# startPage.py
import tkinter as tk

from tkinter import ttk
from PIL import Image, ImageTk

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self).pack(side="top", fill="x", pady=10)

        image_path = (
            '/Users/dougveilleux/Documents/GitHub/UUVPathPlanningApp/'
            'data/images/iver4-900.jpg')
        img = Image.open(image_path)
        img = img.resize((800, 600))
        img = ImageTk.PhotoImage(img)
        label = tk.Label(self, image=img)
        label.image = img
        label.pack(side="top", fill="both", expand=True)  # Pack the label onto the StartPage
