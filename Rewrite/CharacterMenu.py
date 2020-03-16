import json

import TkOverrides as Tko


# noinspection PyUnusedLocal,PyUnusedLocal,PyUnusedLocal,PyUnusedLocal,PyUnusedLocal
class CharacterMenu:
    def __init__(self, window_base):
        # Assign variables
        self.window_base = window_base
        self.window_x = self.window_base.winfo_screenwidth()
        self.window_y = self.window_base.winfo_screenheight()
        self.window_base.update_window_title("Menu")
        self.current_bio = None
        self.servant_list = []
        self.bio_background = None
        self.bio_text = None

        # Create canvas
        self.cv_banner = Tko.Canvas(self.window_base, width=self.window_x, height=100, bd=0, highlightthickness=0,
                                    relief='ridge', bg="#444444")
        self.cv_banner.set_grid(1, 1, 2, 1, sticky="n")
        self.cv_list = Tko.Canvas(self.window_base, width=self.window_x / 2, height=self.window_y - 100, bd=0,
                                  highlightthickness=0, relief='ridge', bg="#333333")
        self.cv_list.set_grid(1, 2, 1, 1, sticky="sw")
        self.cv_info = Tko.Canvas(self.window_base, width=self.window_x / 2, height=self.window_y - 100, bd=0,
                                  highlightthickness=0, relief='ridge', bg="#333333")
        self.cv_info.set_grid(2, 2, 1, 1, sticky="se")

        self.cv_info.create_text(self.window_x, self.window_y, "by Louis Mayes", "nw", "#000000", size=15)

        # Create Buttons
        self.cv_banner.quit_button = self.cv_banner.create_button(10, 10, "Quit", function=self.quit)
        self.cv_banner.battle_button = self.cv_banner.create_button(self.window_x - 110, 10, "Battle",
                                                                    function=self.battle)
        self.cv_list.create_button(10, 10, "Refresh List", function=self.update_servant_list)
        # Run Interface
        self.window_base.mainloop()

    @staticmethod
    def quit(event):
        quit()

    def battle(self, event):
        print("open map select the battle")
        self.cv_info.destroy()
        self.cv_banner.destroy()
        self.cv_list.destroy()
        self.window_base.open_cover_screen()

    def update_servant_list(self, event):
        self.servant_list = []
        servant_list = []
        for servant_name in self.window_base.databases.get_servants()['Servants']:
            servant_list.append(servant_name)
            if len(servant_list) >= 10:
                self.servant_list.append(servant_list)
                servant_list = []
        self.servant_list.append(servant_list)
        self.update_servant_list_page(0, "")

    def update_servant_list_page(self, page, event):
        list_y = 0
        for name in self.servant_list[page]:
            ListItem(self, Servant(name), list_y)
            list_y += 1
            if list_y >= 10:
                list_y = 0

    def show_servant_bio(self, servant, event):
        if isinstance(self.current_bio, list):
            for item in self.current_bio:
                self.cv_info.delete(item)
        self.current_bio = []

        self.bio_background = self.cv_info.create_rectangle(50, 50, self.cv_info.winfo_width() - 50, 500,
                                                            fill="#555555")
        self.current_bio.append(self.bio_background)
        self.bio_text = self.cv_info.create_text(60, 55, text=servant.name, anchor="nw", colour="#ffffff", size=30)
        self.current_bio.append(self.bio_text)
        self.bio_desc_title = self.cv_info.create_text(60, 130, text="Description", anchor="nw", colour="#ffffff", size=22)
        self.current_bio.append(self.bio_desc_title)
        self.bio_desc = self.cv_info.create_text(60, 160, text=servant.description, anchor="nw", colour="#ffffff",
                                                       size=15, width=560)
        self.current_bio.append(self.bio_desc)
        self.bio_noblephantasm_title = self.cv_info.create_text(60, 350, text="Noble Phantasm", anchor="nw", colour="#ffffff",
                                                       size=22)
        self.current_bio.append(self.bio_noblephantasm_title)
        self.bio_noblephantasm = self.cv_info.create_text(60, 380, text=servant.noble_phantasm, anchor="nw", colour="#ffffff", size=15)
        self.current_bio.append(self.bio_noblephantasm)


class ListItem:
    def __init__(self, parent, servant, list_y):
        canvas = parent.cv_list
        self.servant = servant
        canvas.create_button(canvas.winfo_rootx() + (canvas.winfo_width() / 2) - 100,
                             canvas.winfo_rooty() + 35 * list_y, servant.name, 200,
                             function=lambda event: parent.show_servant_bio(servant, event))


class Servant:
    def __init__(self, name):
        try:
            with open(str("Servants/" + name + ".json"), 'r', encoding="utf8") as servant_file:
                servant_info = json.load(servant_file)
                # String/Lore Data
                self.name = name
                self.noble_phantasm = servant_info['NP']
                self.icon_small = servant_info['IconSmall']
                self.icon_large = servant_info['IconLarge']
                self.title = servant_info['Title']
                self.description = servant_info['Desc']
                self.class_type = servant_info['Class']
                self.ranking = servant_info['Ranking']
                self.np_class = servant_info['NPClass']
                # Statistics
                self.max_health = servant_info['HP']
                self.attack = servant_info['Attack']
                self.move = servant_info['Move']
        except KeyError:
            print("oof")
