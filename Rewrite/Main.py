import CoverScreen
import logging
from tkinter import *


class WindowBase(Tk):
    def __init__(self):
        super().__init__()
        logging.debug("WindowBase is initalising!")
        self.update_window_title("Loading...")
        #self.attributes("-fullscreen", True)
        self.toggle_fullscreen()
        self.open_cover_screen()

    def update_window_title(self, status):
        if status == "":
            self.title("Fate Game")
        else:
            self.title(str("Fate Game - " + status))

    def toggle_fullscreen(self):
        if self.attributes("-fullscreen"):
            self.attributes("-fullscreen", False)
        else:
            self.attributes("-fullscreen", True)

    def open_cover_screen(self):
        self.CoverScreen = CoverScreen.CoverScreen(WindowBase)


WindowBase = WindowBase()
WindowBase.mainloop()