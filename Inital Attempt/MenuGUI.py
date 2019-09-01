import tkinter

import UIAssetImport
import GlobalLibrary
from PIL import Image, ImageTk

GlobalLibrary.initalise(__file__)


class Main:

    def __init__(self, player_stats):
        window = tkinter.Tk()

        self.window = window
        window.attributes("-fullscreen", True)
        # Set Window
        window.title("Fate Game")
        # Set ""Global"" Variables
        self.player_stats = player_stats
        self.image_array = []
        self.image_ref_array = []
        self.monitor_resolution_x = window.winfo_screenwidth()
        self.monitor_resolution_y = window.winfo_screenheight()
        if not hasattr(self, 'canvas'):
            UIAssetImport.Menu(self)
        # Create main Canvas
        self.canvas = tkinter.Canvas(window, width=self.monitor_resolution_x, height=self.monitor_resolution_y,
                                     bg="#333337")
        self.canvas.pack()
        # Create File Menu Bar
        self.root_menu = tkinter.Menu(window)
        window.config(menu=self.root_menu)
        self.file_menu = tkinter.Menu(self.root_menu)
        self.root_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=window.quit)
        self.canvas.create_image(0, 0, image=self.wallpaper, anchor="nw")
        self.canvas.create_image(10, 0, image=self.logo_image, anchor="nw")



    def start_mainloop(self):
        self.window.mainloop()
