import tkinter
from PIL import Image, ImageTk


class CoverScreen:
    def __init__(self, window_base):
        self.window_base = window_base
        self.window_x = self.window_base.winfo_screenwidth()
        self.window_y = self.window_base.winfo_screenheight()
        print(self.window_x,self.window_y)
        self.canvas = tkinter.Canvas(self.window_base, width=self.window_x, height=self.window_y, bd=0,
                                     highlightthickness=0, relief='ridge', bg="#999999")
        self.canvas.pack()
        self.canvas.create_text(0, 0, text=str(__name__), anchor="nw")
        self.cover_image = ImageTk.PhotoImage(file='Graphics\CoverImage.png')
        self.canvas.create_image(0, 0, image=self.cover_image, anchor="nw")
        custom_text(self.canvas, self.window_x*0.1, self.window_y*0.9, "Click to Start", "sw", "#000000", 40)
        custom_text(self.canvas, self.window_x*0.95, self.window_y*0.95, "by Louis Mayes", "se", "#000000", 15)
        self.canvas.bind("<Button-1>", self.click)

    def click(self, event):
        self.canvas.destroy()


def custom_text(canvas, x, y, text, anchor, colour, size):
    canvas.create_text(x, y, text=str(text), anchor=anchor, fill=colour, font=("Imperfecto Regular", size))

