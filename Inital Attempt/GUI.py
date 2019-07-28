import tkinter

import GlobalLibrary
import Servants
from PIL import Image, ImageTk

GlobalLibrary.initalise(__file__)


class Main:

    def __init__(self, grid_amount, grid_size, turn_tracker, player_stats):
        window = tkinter.Tk()
        self.window = window
        window.attributes("-fullscreen", True)
        # Set Window
        window.title("Fate Game")
        # Set ""Global"" Variables
        self.grid_amount = grid_amount  # Number of Boxes
        self.grid_size = grid_size  # Box Size
        self.grid_manager = None
        self.turn_tracker = turn_tracker
        self.player_stats = player_stats
        self.image_array = []
        self.image_ref_array = []
        self.selection_array = []
        self.monitor_resolution_x = window.winfo_screenwidth()
        self.monitor_resolution_y = window.winfo_screenheight()
        self.grid_origin_x = self.monitor_resolution_x / 2 + (-int(self.grid_amount / 2) * self.grid_size)
        self.grid_origin_y = self.monitor_resolution_y / 2 + (-int(self.grid_amount / 2) * self.grid_size)
        self.selected_servant = object
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

        # Set Mouse Binds
        self.canvas.bind("<Button-1>", self.click)

        self.turn_counter_text = (
            self.canvas.create_text(self.monitor_resolution_x / 2, 50, text="DEBUG", fill="#ffffff",
                                    font=("Coolvetica Rg", 20)))

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

    def draw_servant(self, entity, pos_x, pos_y, grid_snap, scale):
        new_image = Image.open(entity['Icon'])  # Open Image
        if isinstance(scale, int):
            new_image = new_image.resize((scale, scale), Image.ANTIALIAS)  # Resize Image + AA
        else:
            new_image = new_image.resize((self.grid_size, self.grid_size), Image.ANTIALIAS)  # Resize Image + AA
        new_image = ImageTk.PhotoImage(new_image)  # Convert to Tk PhotoImage Object
        if grid_snap:
            new_pos_x = pos_x * self.grid_size + self.grid_origin_x  # Convert x pos to Grid ref
            new_pos_y = pos_y * self.grid_size + self.grid_origin_y  # Convert y pos to Grid ref

            self.image_ref_array.append({'Name': entity['Name'],
                                         'Image': self.canvas.create_image(new_pos_x, new_pos_y, image=new_image,
                                                                           anchor="nw"),
                                         'File': entity['Icon']})  # Place image at absolute position
        else:
            self.image_ref_array.append(
                {'Name': entity['Name'], 'Image': self.canvas.create_image(pos_x, pos_y, image=new_image, anchor="nw"),
                 'File': entity['Icon']})  # Place image at absolute position
        self.image_array.append(new_image)  # Store Image file in array to preserve

    def click(self, event):
        self.grid_clicked_x = int((event.x - self.grid_origin_x) / self.grid_size)
        self.grid_clicked_y = int((event.y - self.grid_origin_y) / self.grid_size)
        click_selection = self.grid_manager.get_grid_pos(self.grid_clicked_x, self.grid_clicked_y)

        for shape in self.selection_array:
            self.canvas.delete(shape)
        self.selection_array.clear()
        if click_selection != "#" and click_selection is not None:
            for image_ref in self.image_ref_array:
                if image_ref['Name'] == click_selection['Name'] == self.turn_tracker.TurnCounterDict[
                    self.turn_tracker.CurrentTurnCounter]:
                    self.servant_selected_move(click_selection)

    def servant_selected_move(self, click_selection):
        GlobalLibrary.debug(click_selection['Name'] + " selected.")
        selected_servant = Servants.get_servant(click_selection['Name'])
        selected_servant_move = (selected_servant['Move'] * 2) + 1
        selected_servant_move_start_x = (
                (self.grid_clicked_x * self.grid_size) - (selected_servant['Move'] * self.grid_size))
        selected_servant_move_start_y = (
                (self.grid_clicked_y * self.grid_size) - (selected_servant['Move'] * self.grid_size))
        for row in range(selected_servant_move):
            for column in range(selected_servant_move):
                x = int(column + (selected_servant_move_start_x / self.grid_size))
                y = int(row + (selected_servant_move_start_y / self.grid_size))
                if 0 <= x < (self.grid_amount - 2) and 0 <= y < (self.grid_amount - 2):
                    if self.grid_manager.get_grid_pos(x, y) == "#":
                        x_start = selected_servant_move_start_x + (column * self.grid_size) + self.grid_origin_x
                        y_start = selected_servant_move_start_y + (row * self.grid_size) + self.grid_origin_y
                        x_end = selected_servant_move_start_x + ((column + 1) * self.grid_size) + self.grid_origin_x
                        y_end = selected_servant_move_start_y + ((row + 1) * self.grid_size) + self.grid_origin_y
                        selection_box = self.canvas.create_rectangle(x_start, y_start, x_end, y_end, fill="#88ff88",
                                                                     tags="selection_box")
                        self.selection_array.append(selection_box)
        self.selected_servant = selected_servant
        self.canvas.tag_bind("selection_box", "<Button-1>", self.servant_selected_move_click)
        self.selection_array.append(
            self.canvas.create_text(self.monitor_resolution_x / 2, self.monitor_resolution_y - 50,
                                    text=selected_servant['Name'], fill="#ffffff",
                                    font=("Coolvetica Rg", 20)))

    def servant_selected_move_click(self, event):
        self.selected_servant = object
        new_x = int((event.x - self.grid_origin_x) / self.grid_size)
        new_y = int((event.y - self.grid_origin_y) / self.grid_size)
        self.grid_manager.move_grid_pos(self.grid_clicked_x, self.grid_clicked_y, new_x, new_y, is_entity=True)

    def move_servant(self, entity, old_x, old_y, new_x, new_y):
        move_x = (new_x - old_x) * self.grid_size
        move_y = (new_y - old_y) * self.grid_size
        for image in self.image_ref_array:
            if image['Name'] == entity['Name']:
                image_ref = image['Image']
                self.canvas.move(image_ref, move_x, move_y)
        self.turn_tracker.next_turn()

    def new_turn_display(self, turn, entity_name, colour):
        text = str("Turn " + str(turn) + " - " + str(entity_name))
        self.canvas.itemconfigure(self.turn_counter_text, text=text, fill=colour)
