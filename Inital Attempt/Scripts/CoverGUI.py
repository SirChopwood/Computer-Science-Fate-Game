import tkinter

from Scripts import UIAssetImport, GlobalLibrary, MenuGUI

GlobalLibrary.initalise(__file__)


class Main:

    def __init__(self, user_IP):
        window = tkinter.Tk()

        self.window = window
        window.attributes("-fullscreen", True)
        # Set Window
        window.title("Fate Game")
        # Set ""Global"" Variables
        self.user_IP = user_IP
        self.image_array = []
        self.image_ref_array = []
        self.monitor_resolution_x = window.winfo_screenwidth()
        self.monitor_resolution_y = window.winfo_screenheight()
        if not hasattr(self, 'canvas'):
            UIAssetImport.Cover(self)
        # Create main Canvas
        self.canvas = tkinter.Canvas(window, width=self.monitor_resolution_x, height=self.monitor_resolution_y,
                                     bg="#333337", bd=0, highlightthickness=0, relief='ridge')
        self.canvas.pack()

        self.canvas.create_image(0, 0, image=self.wallpaper, anchor="nw")
        self.canvas.create_image(10, 0, image=self.logo_image, anchor="nw", tags="logo_image")
        self.canvas.tag_bind("logo_image", "<Button-1>", self.quit_program)
        self.canvas.create_image(self.monitor_resolution_x / 2, self.monitor_resolution_y - 250,
                                 image=self.ui_click_to_start, anchor="c", tags="click_to_start")

    def start_mainloop(self):
        self.canvas.bind("<Button-1>", self.open_main_menu)
        self.window.mainloop()

    def quit_program(self, event):
        self.window.destroy()

    def open_main_menu(self, event):
        self.window.destroy()
        menu_interface = MenuGUI.Main()
        menu_interface.start_mainloop()
