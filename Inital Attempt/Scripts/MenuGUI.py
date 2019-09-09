import socket
import tkinter

from Scripts import UIAssetImport, GlobalLibrary, GridManager, PlayerStats, Servants, TurnTracker, BattleGUI, Mongo

GlobalLibrary.initalise(__file__)


class Main:

    def __init__(self, window, user_IP):
        self.init_finished = False
        self.user_IP = user_IP
        self.window = window
        self.image_array = []
        self.image_ref_array = []
        self.canvases = []
        self.canvas_team_list_icons = []
        self.canvas_team_list_text_name = []
        self.canvas_team_list_text_atk = []
        self.canvas_team_list_text_hp = []
        self.canvas_team_list_text_lvl = []
        self.canvas_team_list_class = []
        self.canvas_servant_list_bg = []
        self.canvas_servant_list_text_name = []
        self.canvas_servant_list_image = []
        self.canvas_servant_list_image_ref = []
        self.servant_list_page_max = 0
        self.servant_list_page = 0
        self.servant_list = []
        self.servant_data = object
        self.canvas_servant_list_selected_bg = None
        self.selected_servant = ""
        self.monitor_resolution_x = self.window.winfo_screenwidth()
        self.monitor_resolution_y = self.window.winfo_screenheight()
        if not hasattr(self, 'canvas'):
            UIAssetImport.Menu(self)

        self.servant_database = Mongo.ServantDatabase()
        self.servant_database.sync_files()
        self.update_databases()

        # Create main Canvas
        self.window.configure(bg='#333337')

        self.create_canvas_quit()
        self.create_canvas_servant_list()
        self.create_canvas_servant_bio()
        self.create_canvas_team_list()
        self.create_canvas_battle()
        self.init_finished = True

    def start_mainloop(self):
        self.window.mainloop()

    def quit_program(self, event):
        self.window.destroy()

    def update_databases(self):
        self.player_database = Mongo.PlayerDatabase()
        user_IP = socket.gethostbyname(socket.gethostname())
        self.player_servants = self.player_database.find_player_servants(user_IP)
        self.player_stats = PlayerStats.Main(self.player_servants)
        self.player_inventory = self.player_database.find_player_inventory(user_IP)

    def create_canvas_quit(self):
        self.canvas_quit = tkinter.Canvas(self.window, width=700, height=180, bg="#333337", bd=0, highlightthickness=0,
                                          relief='ridge')
        self.canvases.append(self.canvas_quit)
        self.canvas_quit.grid(row=0, column=0, sticky="nw")
        self.canvas_quit.create_image(10, 0, image=self.logo_image, anchor="nw", tags="logo_image")
        self.canvas_quit.tag_bind("logo_image", "<Button-1>", self.quit_program)

    def create_canvas_servant_list(self):
        self.canvas_servant_list = tkinter.Canvas(self.window, width=650, height=900, bg="#333337", bd=0,
                                                  highlightthickness=0,
                                                  relief='ridge')
        self.canvases.append(self.canvas_servant_list)
        self.canvas_servant_list.grid(row=1, column=0, sticky="sw", rowspan=2)
        self.canvas_servant_list.create_image(350, 500, image=self.ui_servant_list,
                                              anchor="c", tags="servant_list")
        self.canvas_servant_list.create_image(350, 170, image=self.ui_servant_list_title, anchor="c")
        self.canvas_servant_list.create_text(350, 170, text="Servants", fill="#cccccc",
                                             font=("Coolvetica Rg", 35), anchor="c")
        self.canvas_servant_list.create_image(350, 830, image=self.ui_servant_list_button, anchor="c",
                                              tags="refresh_button")
        self.canvas_servant_list.create_image(350, 830, image=self.ui_refresh, anchor="c",
                                              tags="refresh_button")
        self.canvas_servant_list.tag_bind("refresh_button", "<Button-1>", self.reload_servant_list_event)
        self.canvas_servant_list.create_image(200, 830, image=self.ui_servant_list_button, anchor="c",
                                              tags="prev_page_button")
        self.canvas_servant_list.create_image(200, 830, image=self.ui_left_arrow, anchor="c",
                                              tags="prev_page_button")
        self.canvas_servant_list.tag_bind("prev_page_button", "<Button-1>", self.prev_page_servant_list_event)
        self.canvas_servant_list.create_image(500, 830, image=self.ui_servant_list_button, anchor="c",
                                              tags="next_page_button")
        self.canvas_servant_list.create_image(500, 830, image=self.ui_right_arrow, anchor="c",
                                              tags="next_page_button")
        self.canvas_servant_list.tag_bind("next_page_button", "<Button-1>", self.next_page_servant_list_event)
        self.reload_servant_list_event("")

    def reload_servant_list_event(self, event):
        self.update_databases()
        self.servant_list = Servants.get_all_player_servants(self.player_servants)
        self.servant_list_page_max = len(self.servant_list)
        self.update_servant_list()

    def update_servant_list_event(self, event):
        self.update_servant_list()

    def next_page_servant_list_event(self, event):
        if self.servant_list_page < self.servant_list_page_max - 1:
            self.servant_list_page += 1
        self.update_servant_list()

    def prev_page_servant_list_event(self, event):
        if self.servant_list_page > 0:
            self.servant_list_page -= 1
        self.update_servant_list()

    def update_servant_list(self):
        list_pos_y = 252
        for i in range(len(self.canvas_servant_list_bg)):
            self.canvas_servant_list.delete(self.canvas_servant_list_bg[i])
            self.canvas_servant_list.delete(self.canvas_servant_list_text_name[i])
            self.canvas_servant_list.delete(self.canvas_servant_list_image[i])
            self.canvas_servant_list.delete(self.canvas_servant_list_image_ref[i])
        for servant in self.servant_list[self.servant_list_page]:
            self.canvas_servant_list_bg.append(
                self.canvas_servant_list.create_rectangle(123, list_pos_y - 27, 580, list_pos_y + 27, fill="#2c2303",
                                                          tags=(servant['Name'], "servant_list")))
            self.canvas_servant_list_text_name.append(
                self.canvas_servant_list.create_text(180, list_pos_y, text=servant['Name'], fill="#cccccc",
                                                     font=("Coolvetica Rg", 25), anchor="w",
                                                     tags=(servant['Name'], "servant_list")))
            try:
                servant_image = UIAssetImport.get_servant_icon(servant, 50, 50)
            except FileNotFoundError:
                GlobalLibrary.error(str("Servant needs icon: " + servant['Name']))
                servant_image = UIAssetImport.image_resize("Pictures/Class-Shielder-Gold.png", 50, 50)
            self.canvas_servant_list_image_ref.append(servant_image)
            self.canvas_servant_list_image.append(
                self.canvas_servant_list.create_image(150, list_pos_y, image=servant_image, anchor="c",
                                                      tags=(servant['Name'], "servant_list")))
            list_pos_y += 55
        self.canvas_servant_list.tag_bind("servant_list", "<Button-1>", self.select_servant)

    def select_servant(self, event):
        if not self.init_finished:
            return
        if isinstance(self.canvas_servant_list_selected_bg, object):
            self.canvas_servant_list.itemconfigure(self.canvas_servant_list_selected_bg, fill="#2c2303")
        self.hide_servant_bio("")
        tag = self.canvas_servant_list.itemcget(self.canvas_servant_list.find_closest(event.x, event.y), "tags")
        tag = tag.strip(" servant_list current")
        tag = tag.strip("{")
        self.selected_servant = tag.strip("}")
        tagged_widgets = self.canvas_servant_list.find_withtag(self.selected_servant)
        for widget in tagged_widgets:
            if widget in self.canvas_servant_list_bg:
                self.canvas_servant_list.itemconfigure(widget, fill="#433607")
                self.canvas_servant_list_selected_bg = widget
                self.show_servant_bio()

    def create_canvas_servant_bio(self):
        self.canvas_servant_bio = tkinter.Canvas(self.window, width=850, height=900, bg="#333337", bd=0,
                                                 highlightthickness=0,
                                                 relief='ridge')
        self.canvases.append(self.canvas_servant_bio)
        self.canvas_servant_bio.grid(row=1, column=1, sticky="s", rowspan=2)
        self.canvas_servant_bio.bind("<Button-1>", self.hide_servant_bio)

    def show_servant_bio(self):
        for servant in self.servant_list[self.servant_list_page]:
            if servant['Name'] == self.selected_servant:
                self.servant_data = servant
        base_servant_data = Servants.get_servant(self.servant_data['Name'])
        self.canvas_servant_bio.create_image(415, 500, image=self.ui_servant_bio, anchor="c", tags="servant_bio")
        self.canvas_servant_bio.create_text(220, 280, text=self.servant_data['Name'], fill="#cccccc",
                                            font=("Coolvetica Rg", 30),
                                            anchor="w", tags="servant_bio")
        try:
            self.selected_servant_image = UIAssetImport.get_servant_icon(self.servant_data, 125, 125)
        except FileNotFoundError:
            GlobalLibrary.error("REMEMBER TO ADD ICON PATHS TO SERVANTS!!!")
            self.selected_servant_image = UIAssetImport.image_resize("Pictures/Class-Shielder-Gold.png", 125, 125)
        self.canvas_servant_bio.create_image(107, 315, image=self.selected_servant_image, anchor="c",
                                             tags="servant_bio")
        self.canvas_servant_bio.create_text(220, 320,
                                            text=str("HP: " + str(self.servant_data['HP']) + " (" + str(
                                                base_servant_data['HP']) + ")"), fill="#888888",
                                            font=("Coolvetica Rg", 15), anchor="w", tags="servant_bio")
        self.canvas_servant_bio.create_text(400, 320,
                                            text=str(
                                                "HP: " + str(self.servant_data['ATK']) + " (" + str(
                                                    base_servant_data['ATK']) + ")"), fill="#888888",
                                            font=("Coolvetica Rg", 15), anchor="w", tags="servant_bio")
        self.canvas_servant_bio.create_text(580, 320,
                                            text=str("Move: " + str(self.servant_data['Move'])), fill="#888888",
                                            font=("Coolvetica Rg", 15), anchor="w", tags="servant_bio")
        self.canvas_servant_bio.create_rectangle(215, 340, 780, 370, fill="#2c2303", tags="servant_bio")

        self.canvas_servant_bio.create_rectangle(220, 345, (self.servant_data['Level'] * ((775 - 215) / 100)) + 215,
                                                 365, fill="#433607", tags="servant_bio")
        self.canvas_servant_bio.create_text(((self.servant_data['Level'] * ((775 - 215) / 100)) / 2) + 215, 355,
                                            text=str(self.servant_data['Level']), fill="#888888",
                                            font=("Coolvetica Rg", 12), anchor="c", tags="servant_bio")
        try:
            if self.servant_data['Class'] == "Saber":
                servant_class = self.ui_class_saber
            elif self.servant_data['Class'] == "Archer":
                servant_class = self.ui_class_archer
            elif self.servant_data['Class'] == "Lancer":
                servant_class = self.ui_class_lancer
            elif self.servant_data['Class'] == "Caster":
                servant_class = self.ui_class_caster
            elif self.servant_data['Class'] == "Rider":
                servant_class = self.ui_class_rider
            elif self.servant_data['Class'] == "Assassin":
                servant_class = self.ui_class_assassin
            elif self.servant_data['Class'] == "Ruler":
                servant_class = self.ui_class_ruler
            elif self.servant_data['Class'] == "Shielder":
                servant_class = self.ui_class_shielder
            elif self.servant_data['Class'] == "Berserker":
                servant_class = self.ui_class_berserker
            self.canvas_servant_bio.create_image(740, 290, image=servant_class, anchor="c", tags="servant_bio")
        except KeyError:
            GlobalLibrary.error("REMEMBER TO ADD CLASSES TO SERVANTS")
        except UnboundLocalError:
            GlobalLibrary.error("REMEMBER TO ADD CLASSES TO SERVANTS")

        try:
            self.canvas_servant_bio.create_text(55, 425,
                                                text=str(self.servant_data['Desc']), fill="#888888",
                                                font=("Coolvetica Rg", 15),
                                                anchor="nw", justify="left", width=725, tags="servant_bio")
        except KeyError:
            GlobalLibrary.error("REMEMBER TO ADD DESCRIPTIONS TO SERVANTS")
        self.canvas_team_list.create_image(100, (int(self.canvas_team_list.cget("height")) / 2) - 160,
                                           image=self.ui_servant_list_button, anchor="c",
                                           tags=("servant_bio", "team_slot1"))
        self.canvas_team_list.create_image(100, (int(self.canvas_team_list.cget("height")) / 2) - 160,
                                           image=self.ui_right_arrow, anchor="c", tags=("servant_bio", "team_slot1"))
        self.canvas_team_list.create_image(100, (int(self.canvas_team_list.cget("height")) / 2) - 30,
                                           image=self.ui_servant_list_button, anchor="c",
                                           tags=("servant_bio", "team_slot2"))
        self.canvas_team_list.create_image(100, (int(self.canvas_team_list.cget("height")) / 2) - 30,
                                           image=self.ui_right_arrow, anchor="c", tags=("servant_bio", "team_slot2"))
        self.canvas_team_list.create_image(100, (int(self.canvas_team_list.cget("height")) / 2) + 100,
                                           image=self.ui_servant_list_button, anchor="c",
                                           tags=("servant_bio", "team_slot3"))
        self.canvas_team_list.create_image(100, (int(self.canvas_team_list.cget("height")) / 2) + 100,
                                           image=self.ui_right_arrow, anchor="c", tags=("servant_bio", "team_slot3"))
        self.canvas_team_list.tag_bind("team_slot1", "<Button-1>", self.set_player_servant)
        self.canvas_team_list.tag_bind("team_slot2", "<Button-1>", self.set_player_servant)
        self.canvas_team_list.tag_bind("team_slot3", "<Button-1>", self.set_player_servant)

    def hide_servant_bio(self, event):
        for widget in self.canvas_servant_bio.find_withtag("servant_bio"):
            self.canvas_servant_bio.delete(widget)
        for widget in self.canvas_team_list.find_withtag("servant_bio"):
            self.canvas_team_list.delete(widget)

    def set_player_servant(self, event):
        tag = self.canvas_team_list.itemcget(self.canvas_team_list.find_closest(event.x, event.y), "tags")
        tag = tag.strip(" servant_bio current}")
        slot = int(tag.strip("{team_slot"))
        for i in range(0, 2):
            servant = self.player_servants['Servants'][self.player_servants['ActiveServants'][i]]
            if self.selected_servant == servant:
                return
        for i in range(len(self.player_servants['Servants'])):
            if self.player_servants['Servants'][i] == self.selected_servant:
                self.player_servants['ActiveServants'][slot - 1] = i
                self.player_database.set_player_servants(self.user_IP, self.player_servants)
                if slot == 1:
                    self.player_stats.servant_1 = self.selected_servant
                elif slot == 2:
                    self.player_stats.servant_2 = self.selected_servant
                elif slot == 3:
                    self.player_stats.servant_3 = self.selected_servant
                self.player_stats.set_servant_references(self.player_servants)
                self.update_team_list()

    def create_canvas_team_list(self):
        self.canvas_team_list = tkinter.Canvas(self.window, width=370, height=900, bg="#333337", bd=0,
                                               highlightthickness=0,
                                               relief='ridge')
        self.canvases.append(self.canvas_team_list)
        self.canvas_team_list.grid(row=2, column=2, sticky="ne")
        self.canvas_team_list.create_image(self.canvas_team_list.cget("width"),
                                           int(self.canvas_team_list.cget("height")) / 2 - 20, image=self.ui_team_list,
                                           anchor="e")
        self.canvas_team_list_icons.append(
            self.canvas_team_list.create_image(int(self.canvas_team_list.cget("width")) - 220,
                                               (int(self.canvas_team_list.cget("height")) / 2) - 160,
                                               image=self.logo_image,
                                               anchor="w"))
        self.canvas_team_list_icons.append(
            self.canvas_team_list.create_image(int(self.canvas_team_list.cget("width")) - 220,
                                               (int(self.canvas_team_list.cget("height")) / 2) - 30,
                                               image=self.logo_image,
                                               anchor="w"))
        self.canvas_team_list_icons.append(
            self.canvas_team_list.create_image(int(self.canvas_team_list.cget("width")) - 220,
                                               (int(self.canvas_team_list.cget("height")) / 2) + 100,
                                               image=self.logo_image,
                                               anchor="w"))

        self.canvas_team_list_text_name.append(
            self.canvas_team_list.create_text(int(self.canvas_team_list.cget("width")) - 220,
                                              (int(self.canvas_team_list.cget("height")) / 2) - 110, text="DEBUG TEXT",
                                              fill="#cccccc", font=("Coolvetica Rg", 15), anchor="w"))
        self.canvas_team_list_text_name.append(
            self.canvas_team_list.create_text(int(self.canvas_team_list.cget("width")) - 220,
                                              (int(self.canvas_team_list.cget("height")) / 2) + 20, text="DEBUG TEXT",
                                              fill="#cccccc", font=("Coolvetica Rg", 15), anchor="w"))
        self.canvas_team_list_text_name.append(
            self.canvas_team_list.create_text(int(self.canvas_team_list.cget("width")) - 220,
                                              (int(self.canvas_team_list.cget("height")) / 2) + 150, text="DEBUG TEXT",
                                              fill="#cccccc", font=("Coolvetica Rg", 15), anchor="w"))

        self.canvas_team_list_class.append(
            self.canvas_team_list.create_image(int(self.canvas_team_list.cget("width")) - 120,
                                               (int(self.canvas_team_list.cget("height")) / 2) - 160,
                                               image=self.logo_image,
                                               anchor="c"))
        self.canvas_team_list_class.append(
            self.canvas_team_list.create_image(int(self.canvas_team_list.cget("width")) - 120,
                                               (int(self.canvas_team_list.cget("height")) / 2) - 30,
                                               image=self.logo_image,
                                               anchor="c"))
        self.canvas_team_list_class.append(
            self.canvas_team_list.create_image(int(self.canvas_team_list.cget("width")) - 120,
                                               (int(self.canvas_team_list.cget("height")) / 2) + 100,
                                               image=self.logo_image,
                                               anchor="c"))
        self.canvas_team_list_text_atk.append(
            self.canvas_team_list.create_text(int(self.canvas_team_list.cget("width")) - 90,
                                              (int(self.canvas_team_list.cget("height")) / 2) - 175, text="DEBUG TEXT",
                                              fill="#aaaaaa", font=("Coolvetica Rg", 15), anchor="w"))
        self.canvas_team_list_text_atk.append(
            self.canvas_team_list.create_text(int(self.canvas_team_list.cget("width")) - 90,
                                              (int(self.canvas_team_list.cget("height")) / 2 - 45), text="DEBUG TEXT",
                                              fill="#aaaaaa", font=("Coolvetica Rg", 15), anchor="w"))
        self.canvas_team_list_text_atk.append(
            self.canvas_team_list.create_text(int(self.canvas_team_list.cget("width")) - 90,
                                              (int(self.canvas_team_list.cget("height")) / 2) + 115, text="DEBUG TEXT",
                                              fill="#aaaaaa", font=("Coolvetica Rg", 15), anchor="w"))
        self.canvas_team_list_text_hp.append(
            self.canvas_team_list.create_text(int(self.canvas_team_list.cget("width")) - 90,
                                              (int(self.canvas_team_list.cget("height")) / 2) - 145, text="DEBUG TEXT",
                                              fill="#aaaaaa", font=("Coolvetica Rg", 15), anchor="w"))
        self.canvas_team_list_text_hp.append(
            self.canvas_team_list.create_text(int(self.canvas_team_list.cget("width")) - 90,
                                              (int(self.canvas_team_list.cget("height")) / 2 - 15), text="DEBUG TEXT",
                                              fill="#aaaaaa", font=("Coolvetica Rg", 15), anchor="w"))
        self.canvas_team_list_text_hp.append(
            self.canvas_team_list.create_text(int(self.canvas_team_list.cget("width")) - 90,
                                              (int(self.canvas_team_list.cget("height")) / 2) + 85, text="DEBUG TEXT",
                                              fill="#aaaaaa", font=("Coolvetica Rg", 15), anchor="w"))
        self.canvas_team_list_text_lvl.append(
            self.canvas_team_list.create_text(int(self.canvas_team_list.cget("width")) - 120,
                                              (int(self.canvas_team_list.cget("height")) / 2) - 160, text="DEBUG TEXT",
                                              fill="#aaaaaa", font=("Coolvetica Rg", 20), anchor="c"))
        self.canvas_team_list_text_lvl.append(
            self.canvas_team_list.create_text(int(self.canvas_team_list.cget("width")) - 120,
                                              (int(self.canvas_team_list.cget("height")) / 2 - 30), text="DEBUG TEXT",
                                              fill="#aaaaaa", font=("Coolvetica Rg", 20), anchor="c"))
        self.canvas_team_list_text_lvl.append(
            self.canvas_team_list.create_text(int(self.canvas_team_list.cget("width")) - 120,
                                              (int(self.canvas_team_list.cget("height")) / 2) + 100, text="DEBUG TEXT",
                                              fill="#aaaaaa", font=("Coolvetica Rg", 20), anchor="c"))
        self.update_team_list()

    def update_team_list(self):
        self.team_list_image_ref_array = []
        player_servant_list = [self.player_stats.servant_ref_1, self.player_stats.servant_ref_2,
                               self.player_stats.servant_ref_3]
        for i in range(len(player_servant_list)):
            self.team_list_image_ref_array.append(UIAssetImport.get_servant_icon(player_servant_list[i], 70, 70))
            self.canvas_team_list.itemconfigure(self.canvas_team_list_icons[i],
                                                image=self.team_list_image_ref_array[i])
            self.canvas_team_list.itemconfigure(self.canvas_team_list_text_name[i], text=player_servant_list[i]['Name'])
            self.canvas_team_list.itemconfigure(self.canvas_team_list_text_atk[i],
                                                text=str("ATK: " + str(player_servant_list[i]['ATK'])))
            self.canvas_team_list.itemconfigure(self.canvas_team_list_text_hp[i],
                                                text=str("HP: " + str(player_servant_list[i]['HP'])))
            self.canvas_team_list.itemconfigure(self.canvas_team_list_text_lvl[i], text=player_servant_list[i]['Level'])
            try:
                if player_servant_list[i]['Class'] == "Saber":
                    servant_class = self.ui_class_saber
                elif player_servant_list[i]['Class'] == "Archer":
                    servant_class = self.ui_class_archer
                elif player_servant_list[i]['Class'] == "Lancer":
                    servant_class = self.ui_class_lancer
                elif player_servant_list[i]['Class'] == "Caster":
                    servant_class = self.ui_class_caster
                elif player_servant_list[i]['Class'] == "Rider":
                    servant_class = self.ui_class_rider
                elif player_servant_list[i]['Class'] == "Assassin":
                    servant_class = self.ui_class_assassin
                elif player_servant_list[i]['Class'] == "Ruler":
                    servant_class = self.ui_class_ruler
                elif player_servant_list[i]['Class'] == "Shielder":
                    servant_class = self.ui_class_shielder
                elif player_servant_list[i]['Class'] == "Berserker":
                    servant_class = self.ui_class_berserker
            except KeyError:
                print("REMEMBER TO ADD CLASSES TO SERVANTS")
            self.canvas_team_list.itemconfigure(self.canvas_team_list_class[i], image=servant_class)

    def create_canvas_battle(self):
        self.canvas_battle = tkinter.Canvas(self.window, width=370, height=180, bg="#333337", bd=0,
                                            highlightthickness=0,
                                            relief='ridge')
        self.canvases.append(self.canvas_battle)
        self.canvas_battle.grid(row=2, column=2, sticky="se")
        self.canvas_battle.create_image(self.canvas_battle.cget("width"), self.canvas_battle.cget("height"),
                                        image=self.ui_fight_button, anchor="se", tags="fight_button")
        self.canvas_battle.create_text(int(self.canvas_battle.cget("width")) - 80,
                                       int(self.canvas_battle.cget("height")) - 37, text="BATTLE",
                                       fill="#cccccc", font=("Coolvetica Rg", 30), anchor="se", tags="fight_button")
        self.canvas_battle.tag_bind("fight_button", "<Button-1>", self.open_battle)

    def open_battle(self, event):
        for i in self.canvases:
            i.destroy()
        grid_amount = 20  # default = 20
        grid_size = 50  # default = 50
        turn_tracker = TurnTracker.Main(player_stats=self.player_stats)
        battle_interface = BattleGUI.Main(window=self.window, user_IP=self.user_IP, grid_amount=grid_amount,
                                          grid_size=grid_size, turn_tracker=turn_tracker,
                                          player_stats=self.player_stats)
        battle_interface.draw_grid()
        turn_tracker.GUI = battle_interface
        grid_manager = GridManager.Main(grid_amount=grid_amount, grid_size=grid_size, GUI=battle_interface,
                                        turn_tracker=turn_tracker)
        battle_interface.grid_manager = grid_manager
        grid_manager.load_map("Chaldea 1-1")
        grid_manager.display_grid_graphics()
        grid_manager.spawn_player_servants(self.player_servants)
        grid_manager.set_grid_pos(4, 4, Servants.get_servant("Merlin"))
        turn_tracker.display_current_turn()
        battle_interface.start_mainloop()
