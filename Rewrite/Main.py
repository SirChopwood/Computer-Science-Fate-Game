import CoverScreen, CharacterMenu
from tkinter import *


class WindowBase(Tk):
    def __init__(self):
        super().__init__()
        print("WindowBase is initalising!")
        self.current_screen = 0
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
        self.active_screen = CoverScreen.CoverScreen(self)

    def open_character_menu(self):
        self.active_screen = CharacterMenu.CharacterMenu(self)


WindowBase = WindowBase()
WindowBase.mainloop()
