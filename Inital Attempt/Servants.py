import json
import GlobalLibrary

GlobalLibrary.initalise(__file__)


def get_servant(name):
    file_path = str("Servants/" + name + ".json")
    with open(file_path, 'r', encoding="utf8") as file_ref:
        file_json = json.load(file_ref)  # Load file into JSON module
        return file_json
