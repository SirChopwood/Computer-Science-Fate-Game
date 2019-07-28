import json
import os
import sys

import GlobalLibrary
import pymongo

GlobalLibrary.initalise(__file__)


# FateGameClient bWcLUFH0J6nT6fQr
class Main:

    def __init__(self):
        GlobalLibrary.initalise(Main.__name__)
        GlobalLibrary.notice("Connecting to Mongo Server!")
        try:
            self.server_ref = pymongo.MongoClient(
                "mongodb+srv://FateGameClient:bWcLUFH0J6nT6fQr@fategame-uhen9.mongodb.net/test?retryWrites=true&w=majority")
        except pymongo.errors.AutoReconnect:
            GlobalLibrary.error("Connection Failed, Reconnecting!")
        except pymongo.errors.ConnectionFailure:
            GlobalLibrary.error("Connection Failed!")
        self.collection_ref = self.server_ref['fate']  # Open the Collection "fate"
        self.database_servants = self.collection_ref['servants']  # Open the Database "servants"

    def find_servant(self, servant_name):
        search_query = {"Name": servant_name}
        search_result = self.database_servants.find_one(search_query)
        return search_result

    def sync_files(self):
        try:
            for database_document in self.database_servants.find():  # Iterate through every Document in Servant Database
                file_path = str(
                    "Servants/" + database_document['Name'] + ".json")  # Set relative file path for selected Servant

                if os.path.isfile(path=file_path):  # Check is selected Servant has a local file
                    GlobalLibrary.debug("File Found - " + file_path)

                    with open(file_path, 'r', encoding="utf8") as file_ref:
                        file_json = json.load(file_ref)  # Load file into JSON module

                    database_document['_id'] = str(database_document['_id'])  # Converts the ID value to string

                    if database_document == file_json:  # Checks if files match exactly
                        GlobalLibrary.debug("File Matched - " + file_path)
                    else:
                        GlobalLibrary.debug("File Didn't Match - " + file_path)
                        os.remove(file_path)  # Delete the old file
                        with open(file_path, 'w') as file_ref:  # Create a new file
                            json.dump(obj=database_document, fp=file_ref, ensure_ascii=False, indent=2)  # Write to file
                        GlobalLibrary.debug("File Updated - " + file_path)
                else:
                    GlobalLibrary.debug("File Not Found - " + file_path)
                    database_document['_id'] = str(database_document['_id'])  # Converts the ID value to string
                    with open(file_path, 'w') as file_ref:  # Create a new file
                        json.dump(obj=database_document, fp=file_ref, ensure_ascii=False, indent=2)  # Write to file
                    GlobalLibrary.debug("File Created - " + file_path)
            GlobalLibrary.notice("File Sync Complete!")
        except pymongo.errors.ServerSelectionTimeoutError:  # Error if connection times out
            GlobalLibrary.error("Connection Failed")
            sys.exit()
