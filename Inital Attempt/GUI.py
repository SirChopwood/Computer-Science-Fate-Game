import tkinter
from PIL import Image, ImageTk
import GlobalLibrary

GlobalLibrary.initalise(__file__)


class Main:

    def __init__(self, grid_amount, grid_size):
        window = tkinter.Tk()
        self.window = window
        window.attributes("-fullscreen", True)
        # Set Window
        window.title("Fate Game")
        # Set ""Global"" Variables
        self.grid_amount = grid_amount  # Number of Boxes
        self.grid_size = grid_size  # Box Size
        self.image_array = []
        self.monitor_resolution_x = window.winfo_screenwidth()
        self.monitor_resolution_y = window.winfo_screenheight()
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

        #Set Mouse Binds
        self.canvas.bind("<Button-1>", self.click)

    def click(self, event):
        print(event.x,event.y)


    def start_mainloop(self):
        self.window.mainloop()

    def draw_grid(self):
        a1 = int(self.grid_amount / 2)
        a2 = -a1
        b2 = self.grid_size * a2
        for i in range(a2, a1):
            monitor_x = self.monitor_resolution_x / 2  # Get Center point of x
            monitor_y = self.monitor_resolution_y / 2  # Get Center point of y
            x1 = monitor_x + (i * self.grid_size)
            y1 = monitor_y + b2
            y2 = monitor_y - (b2 + self.grid_size)
            self.canvas.create_line(x1, y1, x1, y2, fill="#666666", width=2)  # Vertical Lines

            x1 = monitor_x + b2
            x2 = monitor_x - (b2 + self.grid_size)
            y1 = monitor_y + (i * self.grid_size)
            self.canvas.create_line(x1, y1, x2, y1, fill="#666666", width=2)  # Horizontal Lines

    def draw_image(self, image_path, pos_x, pos_y, grid_snap, scale):
        new_image = Image.open(image_path)  # Open Image
        if isinstance(scale, int):
            new_image = new_image.resize((scale, scale), Image.ANTIALIAS)  # Resize Image + AA
        else:
            new_image = new_image.resize((self.grid_size, self.grid_size), Image.ANTIALIAS)  # Resize Image + AA
        new_image = ImageTk.PhotoImage(new_image)  # Convert to Tk PhotoImage Object
        if grid_snap:
            new_pos_x = pos_x * self.grid_size + (self.monitor_resolution_x / 2)  # Convert x pos to Grid ref
            new_pos_y = pos_y * self.grid_size + (self.monitor_resolution_y / 2)  # Convert y pos to Grid ref

            self.canvas.create_image(new_pos_x, new_pos_y, image=new_image, anchor="nw")  # Place image at grid ref
        else:
            self.canvas.create_image(pos_x, pos_y, image=new_image, anchor="nw")  # Place image at absolute position
        self.image_array.append(new_image)  # Store Image file in array to preserve
        self.canvas.bind(new_image, )
