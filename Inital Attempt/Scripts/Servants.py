import json

from Scripts import GlobalLibrary

GlobalLibrary.initalise(__file__)


def get_servant(name):
    file_path = str("Servants/" + name + ".json")
    with open(file_path, 'r', encoding="utf8") as file_ref:
        file_json = json.load(file_ref)  # Load file into JSON module
        file_json.update({"Level": 1})
        file_json.update({"Allied": False})
        return file_json


def get_player_servants(servant_database):
    player_servants = servant_database
    servant_list = []
    for i in range(0, 3):
        servant = player_servants["Servants"][int(player_servants["ActiveServants"][i])]
        file_path = str("Servants/" + servant + ".json")
        with open(file_path, 'r', encoding="utf8") as file_ref:
            json_ref = json.load(file_ref)  # Load file into JSON module
            servant_level = int(player_servants["Levels"][int(player_servants["ActiveServants"][i])])
            json_ref["HP"] = int(int(json_ref["HP"]) * (1 + (servant_level / 30)))
            json_ref["ATK"] = int(int(json_ref["ATK"]) * (1 + (servant_level / 30)))
            json_ref.update({"Level": servant_level})
            json_ref.update({"Allied": True})
            servant_list.append(json_ref)
    servant1 = servant_list[0]
    servant2 = servant_list[1]
    servant3 = servant_list[2]
    return servant1, servant2, servant3
