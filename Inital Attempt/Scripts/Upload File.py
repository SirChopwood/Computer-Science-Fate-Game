import json
import os

import bson
import pymongo


class ServantDatabase:

    def __init__(self):
        print(ServantDatabase.__name__)
        print("Connecting to Mongo Server!")
        try:
            self.server_ref = pymongo.MongoClient(
                "mongodb+srv://SirChopwood:ChangeMe1@fategame-uhen9.mongodb.net/test?retryWrites=true&w"
                "=majority")
        except pymongo.errors.AutoReconnect:
            print("Connection Failed, Reconnecting!")
        except pymongo.errors.ConnectionFailure:
            print("Connection Failed!")
        self.collection_ref = self.server_ref['fate']  # Open the Collection "fate"
        self.database_servants = self.collection_ref['servants']  # Open the Database "servants"

    def find_servant(self):
        servant_name = input("Servant Name: ")
        search_query = {"Name": servant_name}
        search_result = self.database_servants.find_one(search_query)
        print(search_result)

    def update_servant(self):
        servant_name = input("Servant Name: ")
        file_path = str(
            "Servants/" + servant_name + ".json")  # Set relative file path for selected Servant

        if os.path.isfile(path=file_path):  # Check is selected Servant has a local file
            print("File Found - " + file_path)
            with open(file_path, 'r', encoding="utf8") as file_ref:
                print(file_ref)
                file_json = json.load(file_ref)  # Load file into JSON module
                print(file_json)
                file_json["_id"] = bson.objectid.ObjectId(file_json["_id"])
                self.database_servants.delete_one({"Name": servant_name})
                self.database_servants.insert_one(file_json)

                print("File Uploaded")


SDB = ServantDatabase()
SDB.update_servant()
