import json

import GlobalLibrary

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
    S_list = []
    for i in range(0,3):
        S = player_servants["Servants"][int(player_servants["ActiveServants"][i])]
        file_path = str("Servants/" + S + ".json")
        with open(file_path, 'r', encoding="utf8") as file_ref:
            json_ref = json.load(file_ref)  # Load file into JSON module
            S_level = int(player_servants["Levels"][int(player_servants["ActiveServants"][i])])
            json_ref["HP"] = int(int(json_ref["HP"]) * (1 + (S_level / 30)))
            json_ref["ATK"] = int(int(json_ref["ATK"]) * (1 + (S_level / 30)))
            json_ref.update({"Level": S_level})
            json_ref.update({"Allied": True})
            S_list.append(json_ref)
    S1 = S_list[0]
    S2 = S_list[1]
    S3 = S_list[2]
    return S1,S2,S3