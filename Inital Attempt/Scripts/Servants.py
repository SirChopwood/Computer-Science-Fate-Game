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
    GlobalLibrary.debug(str(player_servants["ActiveServants"]))
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
            json_ref.update({"CurrentHP": int(int(json_ref["HP"]) * (1 + (servant_level / 30)))})
            json_ref.update({"CurrentNP": 0})
            servant_list.append(json_ref)
    servant1 = servant_list[0]
    servant2 = servant_list[1]
    servant3 = servant_list[2]
    return servant1, servant2, servant3


def get_all_player_servants(servant_database):
    servant_list = []
    servant_list_master = []
    for i in range(len(servant_database["Servants"])):
        try:
            servant = servant_database["Servants"][i]
            file_path = str("Servants/" + servant + ".json")
            with open(file_path, 'r', encoding="utf8") as file_ref:
                json_ref = json.load(file_ref)  # Load file into JSON module
            servant_level = int(servant_database["Levels"][i])
            json_ref["HP"] = int(int(json_ref["HP"]) * (1 + (servant_level / 30)))
            json_ref["ATK"] = int(int(json_ref["ATK"]) * (1 + (servant_level / 30)))
            json_ref.update({"Level": servant_level})
            json_ref.update({"Allied": True})
            json_ref.update({"CurrentHP": int(int(json_ref["HP"]) * (1 + (servant_level / 30)))})
            json_ref.update({"CurrentNP": 0})
            servant_list.append(json_ref)
            if len(servant_list) == 10:
                servant_list_master.append(servant_list)
                servant_list = []
        except KeyError:
            GlobalLibrary.error("Servant File Error")

    servant_list_master.append(servant_list)
    return servant_list_master


def get_enemy_servant(servant_name, level):
    file_path = str("Servants/" + servant_name + ".json")
    with open(file_path, 'r', encoding="utf8") as file_ref:
        json_ref = json.load(file_ref)  # Load file into JSON module
        json_ref["HP"] = int(int(json_ref["HP"]) * (1 + (level / 30)))
        json_ref["ATK"] = int(int(json_ref["ATK"]) * (1 + (level / 30)))
        json_ref.update({"Level": level})
        json_ref.update({"Allied": False})
        json_ref.update({"CurrentHP": int(int(json_ref["HP"]) * (1 + (level / 30)))})
        json_ref.update({"CurrentNP": 0})
        return json_ref

    