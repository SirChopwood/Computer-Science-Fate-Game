import json
import os
import pymongo
import socket
from PIL import ImageTk

import TkOverrides as Tko


class CoverScreen:
    def __init__(self, window_base):
        # Assign variables
        self.window_base = window_base
        self.window_x = self.window_base.winfo_screenwidth()
        self.window_y = self.window_base.winfo_screenheight()
        self.window_base.update_window_title("Click to Start!")

        # Create canvas
        self.canvas = Tko.Canvas(self.window_base, width=self.window_x, height=self.window_y, bd=0,
                                 highlightthickness=0, relief='ridge', bg="#999999")
        self.canvas.pack()
        # Create Wallpaper
        self.canvas.create_text(0, 0, text=str(__name__), anchor="nw")
        self.cover_image = ImageTk.PhotoImage(file='Graphics\CoverImage.png')
        self.canvas.create_image(0, 0, image=self.cover_image, anchor="nw")
        # Create Texts
        self.canvas.create_text(self.window_x * 0.1, self.window_y * 0.9, "Click to Start", "sw", "#000000", size=45)
        self.canvas.create_text(self.window_x * 0.99, self.window_y * 0.99, "by Louis Mayes", "se", "#000000", size=15)

        # Bind mouse to move to menu
        self.canvas.bind("<Button-1>", self.click)

        self.window_base.mainloop()

    def click(self, event):
        self.window_base.databases = Databases()  # Load databases
        self.canvas.destroy()  # Destroy existing interface
        self.window_base.open_character_menu()  # Open new interface

class Databases:
    def __init__(self):
        self.reload_databases()
        self.sync_files()

    def reload_databases(self):
        self.IP = socket.gethostbyname(socket.gethostname())  # Assign device IP
        mongodb = pymongo.MongoClient(  # Connect to MongoDB
            "mongodb+srv://FateGameClient:bWcLUFH0J6nT6fQr@fategame-uhen9.mongodb.net/test?retryWrites=true&w"
            "=majority")
        collection_ref = mongodb['fate']  # Open the Collection "fate"
        self.all_servants = collection_ref['servants']  # Open the database "Servants"
        collection_ref = mongodb['playerdata']  # Open the Collection "playerdata"
        self.inventory = collection_ref['playerinventory']  # Open the Database "playerinventory"
        self.servants = collection_ref['playerservants']  # Open the Database "playerservants"

        if self.get_servants() is None:
            self.create_account()

    def sync_files(self):
        for database_document in self.all_servants.find():  # Iterate through every Document in Servant Database
            file_directory = "Servants/"
            file_path = str(
                file_directory + database_document['Name'] + ".json")  # Set relative file path for selected Servant

            if os.path.isfile(path=file_path):  # Check is selected Servant has a local file
                print("File Found - " + file_path)

                with open(file_path, 'r', encoding="utf8") as file_ref:
                    file_json = json.load(file_ref)  # Load file into JSON module

                database_document['_id'] = str(database_document['_id'])  # Converts the ID value to string

                if database_document == file_json:  # Checks if files match exactly
                    print("File Matched - " + file_path)
                else:
                    print("File Didn't Match - " + file_path)
                    os.remove(file_path)  # Delete the old file
                    with open(file_path, 'w') as file_ref:  # Create a new file
                        json.dump(obj=database_document, fp=file_ref, ensure_ascii=False, indent=2)  # Write to file
                    print("File Updated - " + file_path)
            else:
                print("File Not Found - " + file_path)
                database_document['_id'] = str(database_document['_id'])  # Converts the ID value to string
                if not os.path.isdir(file_directory):
                    os.mkdir(file_directory)
                with open(file_path, 'w') as file_ref:  # Create a new file
                    json.dump(obj=database_document, fp=file_ref, ensure_ascii=False, indent=2)  # Write to file
                print("File Created - " + file_path)
        print("File Sync Complete!")

    def get_inventory(self):
        search_query = {"IP": self.IP}
        search_result = self.inventory.find_one(search_query)
        return search_result

    def get_servants(self):
        search_query = {"IP": self.IP}
        search_result = self.servants.find_one(search_query)
        return search_result

    def set_servants(self, servant_database):
        search_query = {"IP": self.IP}
        self.servants.find_one_and_replace(search_query, servant_database)

    def create_account(self):
        self.servants.insert_one({"IP": self.IP, "Servants": ["Mashu Kyrielight", "Mordred Pendragon", "Illyasviel von Einzbern"], "Levels": [1, 1, 1], "ActiveServants": [1, 2, 3]})
