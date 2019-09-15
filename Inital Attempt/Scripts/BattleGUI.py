import tkinter
import random

from PIL import Image, ImageTk

from Scripts import UIAssetImport, GlobalLibrary, MenuGUI, EnemyAI

GlobalLibrary.initalise(__file__)


class Main:

    def __init__(self, window, user_IP, grid_amount, grid_size, turn_tracker, player_stats):
        GlobalLibrary.initalise(Main.__name__)
        self.window = window
        # Set ""Global"" Variables
        self.user_IP = user_IP
        self.grid_amount = grid_amount  # Number of Boxes
        self.grid_size = grid_size  # Box Size
        self.grid_manager = None
        self.grid_clicked_x = int
        self.grid_clicked_y = int
        self.turn_tracker = turn_tracker
        self.player_stats = player_stats
        self.servant_has_moved = False
        self.image_array = []
        self.image_ref_array = []
        self.selection_array = []
        self.monitor_resolution_x = window.winfo_screenwidth()
        self.monitor_resolution_y = window.winfo_screenheight()
        self.grid_origin_x = self.monitor_resolution_x / 2 + (-int(self.grid_amount / 2) * self.grid_size)
        self.grid_origin_y = self.monitor_resolution_y / 2 + (-int(self.grid_amount / 2) * self.grid_size)
        self.selected_servant = object
        if not hasattr(self, 'canvas'):
            UIAssetImport.Battle(self, grid_size)
        # Create main Canvas
        self.canvas = tkinter.Canvas(window, width=self.monitor_resolution_x, height=self.monitor_resolution_y,
                                     bg="#333337", bd=0, highlightthickness=0, relief='ridge')
        self.canvas.pack()
        self.canvas.create_image(10, 0, image=self.logo_image, anchor="nw", tags="logo_image")
        self.canvas.tag_bind("logo_image", "<Button-1>", self.open_main_menu)

        # Set Mouse Binds
        self.canvas.bind("<Button-1>", self.click)

        self.turn_counter_bg = self.canvas.create_image(self.monitor_resolution_x, self.monitor_resolution_y,
                                                        image=self.ui_turn_order_bg, anchor="se")
        self.turn_counter_text = (
            self.canvas.create_text(self.monitor_resolution_x - 65, self.monitor_resolution_y - 88, text="DEBUG",
                                    fill="#ffffff",
                                    font=("Coolvetica Rg", 20), anchor="c", justify="center"))
        self.turn_counter_image = []
        self.turn_counter_image.append(
            self.canvas.create_image(self.monitor_resolution_x - 275, self.monitor_resolution_y - 30, image=self.logo_image,
                                     anchor="c"))
        self.turn_counter_image.append(
            self.canvas.create_image(self.monitor_resolution_x - 175, self.monitor_resolution_y - 30, image=self.logo_image,
                                     anchor="c"))
        self.turn_counter_image.append(
            self.canvas.create_image(self.monitor_resolution_x - 75, self.monitor_resolution_y - 30, image=self.logo_image,
                                     anchor="c"))

    def quit_program(self, event):
        self.window.destroy()

    def start_mainloop(self):
        self.enemy_AI = EnemyAI.Main(self.grid_manager, self)
        self.turn_tracker.enemy_AI = self.enemy_AI
        self.window.mainloop()

    def open_main_menu(self, event):
        self.canvas.destroy()
        menu_interface = MenuGUI.Main(self.window, self.user_IP)
        menu_interface.start_mainloop()

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
                                         'File': entity['Icon'],
                                         'ImageFile': new_image})  # Place image at absolute position
        else:
            self.image_ref_array.append(
                {'Name': entity['Name'], 'Image': self.canvas.create_image(pos_x, pos_y, image=new_image, anchor="nw"),
                 'File': entity['Icon'], 'ImageFile': new_image})  # Place image at absolute position

    def click(self, event):
        self.grid_clicked_x = int((event.x - self.grid_origin_x) / self.grid_size)
        self.grid_clicked_y = int((event.y - self.grid_origin_y) / self.grid_size)
        click_selection = self.grid_manager.get_grid_pos(self.grid_clicked_x, self.grid_clicked_y)

        for shape in self.selection_array:
            self.canvas.delete(shape)
        self.selection_array.clear()
        if isinstance(click_selection, dict):
            for image_ref in self.image_ref_array:
                if image_ref['Name'] == click_selection['Name'] == self.turn_tracker.TurnCounterList[
                    self.turn_tracker.CurrentTurnCounter]:
                    self.servant_selected_both(click_selection)
                elif image_ref['Name'] == click_selection['Name'] != self.turn_tracker.TurnCounterList[
                    self.turn_tracker.CurrentTurnCounter]:
                    self.selected_servant = click_selection
                    self.display_servant_stats()

    def servant_selected_both(self, click_selection):
        GlobalLibrary.notice(click_selection['Name'] + " selected.")
        self.selected_servant = click_selection
        selected_servant_move = (self.selected_servant['Move'] * 2) + 1
        selected_servant_move_start_x = (
                (self.grid_clicked_x * self.grid_size) - (self.selected_servant['Move'] * self.grid_size))
        selected_servant_move_start_y = (
                (self.grid_clicked_y * self.grid_size) - (self.selected_servant['Move'] * self.grid_size))
        for row in range(selected_servant_move):
            for column in range(selected_servant_move):
                x = int(column + (selected_servant_move_start_x / self.grid_size))
                y = int(row + (selected_servant_move_start_y / self.grid_size))
                if 0 <= x < self.grid_amount and 0 <= y < self.grid_amount:
                    if self.grid_manager.get_grid_pos(x, y) == "#":
                        x_start = selected_servant_move_start_x + (column * self.grid_size) + self.grid_origin_x
                        y_start = selected_servant_move_start_y + (row * self.grid_size) + self.grid_origin_y
                        selection_box = self.canvas.create_image(x_start, y_start, image=self.ui_move_icon,
                                                                 anchor="nw", tags="move_selection_box")
                        self.selection_array.append(selection_box)
        self.canvas.tag_bind("move_selection_box", "<Button-1>", self.servant_selected_move_click)
        selected_servant_attack = (self.selected_servant['Range'] * 2) + 1
        selected_servant_attack_start_x = (
                (self.grid_clicked_x * self.grid_size) - (self.selected_servant['Range'] * self.grid_size))
        selected_servant_attack_start_y = (
                (self.grid_clicked_y * self.grid_size) - (self.selected_servant['Range'] * self.grid_size))
        for row in range(selected_servant_attack):
            for column in range(selected_servant_attack):
                x = int(column + (selected_servant_attack_start_x / self.grid_size))
                y = int(row + (selected_servant_attack_start_y / self.grid_size))
                if 0 <= x < (self.grid_amount - 2) and 0 <= y < (self.grid_amount - 2):
                    grid_pos_ref = self.grid_manager.get_grid_pos(x, y)
                    if not isinstance(grid_pos_ref, str):
                        if grid_pos_ref['Allied'] is False:
                            x_start = (selected_servant_attack_start_x + (
                                    column * self.grid_size) + self.grid_origin_x)
                            y_start = (selected_servant_attack_start_y + (
                                    row * self.grid_size) + self.grid_origin_y)
                            selection_box = self.canvas.create_image(x_start, y_start, image=self.ui_attack_icon,
                                                                     anchor="nw", tags="attack_selection_box")
                            self.selection_array.append(selection_box)
        self.canvas.tag_bind("attack_selection_box", "<Button-1>", self.servant_selected_attack_click)
        self.display_servant_stats()

    def display_servant_stats(self):
        self.selection_array.append(
            self.canvas.create_image(self.monitor_resolution_x / 2, self.monitor_resolution_y,
                                     image=self.ui_servant_select_stats_bg, anchor="s"))
        try:
            if self.selected_servant['Class'] == "Saber":
                servant_class = self.ui_class_saber
            elif self.selected_servant['Class'] == "Archer":
                servant_class = self.ui_class_archer
            elif self.selected_servant['Class'] == "Lancer":
                servant_class = self.ui_class_lancer
            elif self.selected_servant['Class'] == "Caster":
                servant_class = self.ui_class_caster
            elif self.selected_servant['Class'] == "Rider":
                servant_class = self.ui_class_rider
            elif self.selected_servant['Class'] == "Assassin":
                servant_class = self.ui_class_assassin
            elif self.selected_servant['Class'] == "Ruler":
                servant_class = self.ui_class_ruler
            elif self.selected_servant['Class'] == "Shielder":
                servant_class = self.ui_class_shielder
            elif self.selected_servant['Class'] == "Berserker":
                servant_class = self.ui_class_berserker
        except KeyError:
            print("REMEMBER TO ADD CLASSES TO SERVANTS")

        self.selection_array.append(
            self.canvas.create_image(self.monitor_resolution_x / 2, self.monitor_resolution_y - 60,
                                     image=servant_class, anchor="c"))
        self.selection_array.append(
            self.canvas.create_text(self.monitor_resolution_x / 2, self.monitor_resolution_y - 92,
                                    text=self.selected_servant['Name'], fill="#BF9A06",
                                    font=("Coolvetica Rg", 20)))
        try:
            self.selection_array.append(
                self.canvas.create_text(self.monitor_resolution_x / 2, self.monitor_resolution_y - 62,
                                        text=str(
                                            "Level " + str(self.selected_servant['Level']) + " " +
                                            self.selected_servant[
                                                'Title']), fill="#999999",
                                        font=("Coolvetica Rg", 14)))
        except KeyError:
            print("REMEMBER TO ADD TITLES TO SERVANTS")
            self.selection_array.append(
                self.canvas.create_text(self.monitor_resolution_x / 2, self.monitor_resolution_y - 62,
                                        text=str(
                                            "Level " + str(self.selected_servant['Level']) + " Servant"),
                                        fill="#999999",
                                        font=("Coolvetica Rg", 14)))
        self.selection_array.append(
            self.canvas.create_text((self.monitor_resolution_x / 2) - 200, self.monitor_resolution_y - 32,
                                    text=str("HP " + str(self.selected_servant['CurrentHP'])), fill="#cccccc",
                                    font=("Coolvetica Rg", 20)))
        self.selection_array.append(
            self.canvas.create_text((self.monitor_resolution_x / 2), self.monitor_resolution_y - 32,
                                    text=str("ATK " + str(self.selected_servant['ATK'])), fill="#cccccc",
                                    font=("Coolvetica Rg", 20)))
        self.selection_array.append(
            self.canvas.create_text((self.monitor_resolution_x / 2) + 200, self.monitor_resolution_y - 32,
                                    text=str("Move " + str(self.selected_servant['Move'])), fill="#cccccc",
                                    font=("Coolvetica Rg", 20)))

    def servant_selected_move_click(self, event):
        self.selected_servant = object
        new_x = int((event.x - self.grid_origin_x) / self.grid_size)
        new_y = int((event.y - self.grid_origin_y) / self.grid_size)
        self.grid_manager.move_grid_pos(self.grid_clicked_x, self.grid_clicked_y, new_x, new_y, is_entity=True)
        self.turn_tracker.next_turn()

    def servant_selected_attack_click(self, event):
        new_x = int((event.x - self.grid_origin_x) / self.grid_size)
        new_y = int((event.y - self.grid_origin_y) / self.grid_size)
        servant = self.grid_manager.get_grid_pos(new_x, new_y)
        if random.randint(0,20) == 30:
            damage = int(self.selected_servant['ATK'] / 2 * (random.randint(7, 10)/10))
            servant['CurrentHP'] -= damage
            GlobalLibrary.notice(
                str(self.selected_servant['Name'] + " critted " + servant['Name'] + " for " + str(damage)))
        else:
            damage = int(self.selected_servant['ATK'] * (random.randint(7, 10)/10))
            servant['CurrentHP'] -= damage
            GlobalLibrary.notice(
                str(self.selected_servant['Name'] + " attacked " + servant['Name'] + " for " + str(damage)))
        if servant['CurrentHP'] <= 0:
            self.grid_manager.set_grid_pos(new_x, new_y, "#", True)
            for image in self.image_ref_array:
                if image['Name'] == servant['Name']:
                    image_ref = image['Image']
                    self.canvas.delete(image_ref)
            GlobalLibrary.notice(str(servant['Name'] + " has died!"))
        else:
            self.grid_manager.set_grid_pos(new_x, new_y, servant, True)
        self.turn_tracker.next_turn()

    def move_servant(self, entity, old_x, old_y, new_x, new_y):
        move_x = (new_x - old_x) * self.grid_size
        move_y = (new_y - old_y) * self.grid_size
        for image in self.image_ref_array:
            if image['Name'] == entity['Name']:
                image_ref = image['Image']
                self.canvas.move(image_ref, move_x, move_y)

    def new_turn_display(self, turn, entity_names, colour):
        for i in range(0, len(self.turn_counter_image)):
            for image_ref in self.image_ref_array:
                if image_ref['Name'] == entity_names[i]:
                    self.canvas.itemconfigure(self.turn_counter_image[i], image=image_ref["ImageFile"])
        text = str("TURN " + str(turn))
        self.canvas.itemconfigure(self.turn_counter_text, text=text, fill=colour)
