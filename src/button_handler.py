import tkinter as tk



class ButtonHandler:
    def __init__(self, root, plot_shapefile_data, plot_random_data):
        self.root = root
        self.plot_shapefile_data = plot_shapefile_data
        self.plot_random_data = plot_random_data
        self.custom_font = ("Arial", 10)
        self.num_uuv = tk.StringVar()  # Initialize num_uuv as an attribute
        self.num_areas = tk.StringVar()  # Initialize num_areas as an attribute

    def create_buttons(self):
        # Create a frame for the left margin
        left_margin_frame = tk.Frame(self.root)
        left_margin_frame.pack(side="left", fill="y", padx=10, pady=10)

        # Create a Label, Entry, and Button for entering the number of UUVs
        label = tk.Label(left_margin_frame, text="Enter the\nNumber of UUVs", font=self.custom_font)
        label.grid(row=0, column=0, padx=10, pady=5)

        # Set a default value of 1
        self.num_uuv.set("1")
        num_uuv = tk.Entry(left_margin_frame, textvariable=self.num_uuv, font=self.custom_font, justify="center")
        num_uuv.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        tk.Button(left_margin_frame, text="Set Number\nof Vehicles", command=self.set_number_of_vehicles,
                  width=14, height=2, font=self.custom_font).grid(row=2, column=0, padx=10, pady=5)

        # Create a Label, Entry, and Button for entering the number of Survey Areas
        label = tk.Label(left_margin_frame, text="Enter the Number\nof Survey Areas", font=self.custom_font)
        label.grid(row=3, column=0, padx=10, pady=5)

        # Set a default value of 1
        self.num_areas.set("1")
        num_areas = tk.Entry(left_margin_frame, textvariable=self.num_areas, font=self.custom_font, justify="center")
        num_areas.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

        tk.Button(left_margin_frame, text="Set Number of Areas", command=self.set_number_of_surveys,
                  width=14, height=2, font=self.custom_font).grid(row=5, column=0, padx=10, pady=5)


        # # Create PATH Planning buttons in the main content area:
        main_content_frame = tk.Frame(self.root)
        main_content_frame.pack(side="top", expand=True, fill=tk.BOTH)
        #
        tk.Button(main_content_frame, text="Set Path\nPlanning Area", command=self.plot_shapefile_data,
                  width=12, height=3, font=self.custom_font).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(main_content_frame, text="Set Start\nPoint", command=self.plot_shapefile_data,
                  width=12, height=3, font=self.custom_font).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(main_content_frame, text="Set Park\nPoint", command=self.plot_shapefile_data,
                  width=12, height=3, font=self.custom_font).grid(row=1, column=2, padx=10, pady=10)
        tk.Button(main_content_frame, text="Generate\nPath Plans", command=self.plot_shapefile_data,
                  width=12, height=3, font=self.custom_font).grid(row=1, column=3, padx=10, pady=10)
        tk.Button(main_content_frame, text="Reset\nPath Plan", command=self.plot_shapefile_data,
                  width=12, height=3, font=self.custom_font).grid(row=1, column=4, padx=10, pady=10)



    def set_number_of_vehicles(self):
        # Access the entered value and use it as needed
        num_uuv = self.num_uuv.get()
        print("Number of UUV(s):", num_uuv)
        # Add logic to use the entered value in your application

    def set_number_of_surveys(self):
        # Access the entered value and use it as needed
        num_areas = self.num_areas.get()
        print("Number of Survey Area(s):", num_areas)
        # Add logic to use the entered value in your application





