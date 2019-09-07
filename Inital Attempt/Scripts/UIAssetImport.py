import os
import random

from PIL import Image, ImageTk

from Scripts import GlobalLibrary

GlobalLibrary.initalise(__file__)


class Battle:

    def __init__(self, GUI, grid_size):
        GlobalLibrary.initalise(Battle.__name__)

        # INTERFACE ASSETS
        GUI.logo_image = self.image_resize("Pictures/Logo.png", int(GUI.monitor_resolution_x / 10),
                                           int(GUI.monitor_resolution_y / 10))
        GUI.ui_servant_select_stats_bg = self.image("Pictures/UI/ServantSelectStats.png")
        GUI.ui_turn_order_bg = self.image("Pictures/UI/TurnOrder.png")
        GUI.ui_move_icon = self.image_resize("Pictures/UI/MoveIcon.png", grid_size, grid_size)
        GUI.ui_attack_icon = self.image_resize("Pictures/UI/AttackIcon.png", grid_size, grid_size)

        # CLASS LOGOS
        GUI.ui_class_saber = self.image("Pictures/Classes/Saber.png")
        GUI.ui_class_archer = self.image("Pictures/Classes/Archer.png")
        GUI.ui_class_lancer = self.image("Pictures/Classes/Lancer.png")
        GUI.ui_class_caster = self.image("Pictures/Classes/Caster.png")
        GUI.ui_class_rider = self.image("Pictures/Classes/Rider.png")
        GUI.ui_class_assassin = self.image("Pictures/Classes/Assassin.png")
        GUI.ui_class_ruler = self.image("Pictures/Classes/Ruler.png")
        GUI.ui_class_shielder = self.image("Pictures/Classes/Shielder.png")
        GUI.ui_class_berserker = self.image("Pictures/Classes/Berserker.png")

        # TERRAIN TILES
        GUI.ui_tiles_chaldea = {}
        GUI.ui_tiles_chaldea.update(
            {"Single": self.image_resize("Pictures/Terrain/Chaldea/Single.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"X": self.image_resize("Pictures/Terrain/Chaldea/X.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"Straight_H": self.image_resize("Pictures/Terrain/Chaldea/Straight_H.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"Straight_V": self.image_resize("Pictures/Terrain/Chaldea/Straight_V.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"Floor": self.image_resize("Pictures/Terrain/Chaldea/Floor.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"Corner_BR": self.image_resize("Pictures/Terrain/Chaldea/Corner_BR.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"Corner_BL": self.image_resize("Pictures/Terrain/Chaldea/Corner_BL.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"Corner_TR": self.image_resize("Pictures/Terrain/Chaldea/Corner_TR.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"Corner_TL": self.image_resize("Pictures/Terrain/Chaldea/Corner_TL.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"T_RBL": self.image_resize("Pictures/Terrain/Chaldea/T_RBL.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"T_RTL": self.image_resize("Pictures/Terrain/Chaldea/T_RTL.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"T_TLB": self.image_resize("Pictures/Terrain/Chaldea/T_TLB.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"T_TRB": self.image_resize("Pictures/Terrain/Chaldea/T_TRB.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"End_T": self.image_resize("Pictures/Terrain/Chaldea/End_T.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"End_B": self.image_resize("Pictures/Terrain/Chaldea/End_B.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"End_L": self.image_resize("Pictures/Terrain/Chaldea/End_L.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"End_R": self.image_resize("Pictures/Terrain/Chaldea/End_R.png", grid_size, grid_size)})
        GlobalLibrary.notice("Battle Graphical Assets Imported")

    def image(self, file_path):
        image_reference = Image.open(file_path)
        image_reference = ImageTk.PhotoImage(image_reference)
        return image_reference

    def image_resize(self, file_path, x, y):
        image_reference = Image.open(file_path)
        image_reference = image_reference.resize((x, y), Image.ANTIALIAS)
        image_reference = ImageTk.PhotoImage(image_reference)
        return image_reference

    def image_scale(self, file_path, scale):
        image_reference = Image.open(file_path)
        scale_x = int(image_reference.size[0] * scale)
        scale_y = int(image_reference.size[1] * scale)
        image_reference = image_reference.resize((scale_x, scale_y), Image.ANTIALIAS)
        image_reference = ImageTk.PhotoImage(image_reference)
        return image_reference


class Cover:

    def __init__(self, GUI):
        GlobalLibrary.initalise(Cover.__name__)

        # INTERFACE ASSETS
        GUI.wallpaper = self.image_resize(
            str("Pictures/Wallpapers/" + random.choice(os.listdir("Pictures/Wallpapers"))), GUI.monitor_resolution_x,
            GUI.monitor_resolution_y)
        GUI.logo_image = self.image_resize("Pictures/Logo.png", int(GUI.monitor_resolution_x / 4),
                                           int(GUI.monitor_resolution_y / 4))
        GUI.ui_click_to_start = self.image_scale("Pictures/UI/ClickToStart.png", 0.5)
        GlobalLibrary.notice("Menu Graphical Assets Imported")

    def image(self, file_path):
        image_reference = Image.open(file_path)
        image_reference = ImageTk.PhotoImage(image_reference)
        return image_reference

    def image_resize(self, file_path, x, y):
        image_reference = Image.open(file_path)
        image_reference = image_reference.resize((x, y), Image.ANTIALIAS)
        image_reference = ImageTk.PhotoImage(image_reference)
        return image_reference

    def image_scale(self, file_path, scale):
        image_reference = Image.open(file_path)
        scale_x = int(image_reference.size[0] * scale)
        scale_y = int(image_reference.size[1] * scale)
        image_reference = image_reference.resize((scale_x, scale_y), Image.ANTIALIAS)
        image_reference = ImageTk.PhotoImage(image_reference)
        return image_reference


class Menu:

    def __init__(self, GUI):
        GlobalLibrary.initalise(Menu.__name__)

        # INTERFACE ASSETS
        GUI.logo_image = self.image_resize("Pictures/Logo.png", int(GUI.monitor_resolution_x / 10),
                                           int(GUI.monitor_resolution_y / 10))
        GUI.ui_servant_list = self.image("Pictures/UI/ServantList.png")
        GUI.ui_servant_bio = self.image("Pictures/UI/ServantBio.png")
        GUI.ui_fight_button = self.image("Pictures/UI/FightButton.png")
        GUI.ui_team_list = self.image("Pictures/UI/TeamList.png")

        # CLASS LOGOS
        GUI.ui_class_saber = self.image_scale("Pictures/Classes/Saber.png", 0.7)
        GUI.ui_class_archer = self.image_scale("Pictures/Classes/Archer.png", 0.7)
        GUI.ui_class_lancer = self.image_scale("Pictures/Classes/Lancer.png", 0.7)
        GUI.ui_class_caster = self.image_scale("Pictures/Classes/Caster.png", 0.7)
        GUI.ui_class_rider = self.image_scale("Pictures/Classes/Rider.png", 0.7)
        GUI.ui_class_assassin = self.image_scale("Pictures/Classes/Assassin.png", 0.7)
        GUI.ui_class_ruler = self.image_scale("Pictures/Classes/Ruler.png", 0.7)
        GUI.ui_class_shielder = self.image_scale("Pictures/Classes/Shielder.png", 0.7)
        GUI.ui_class_berserker = self.image_scale("Pictures/Classes/Berserker.png", 0.7)

        GlobalLibrary.notice("Menu Graphical Assets Imported")

    def image(self, file_path):
        image_reference = Image.open(file_path)
        image_reference = ImageTk.PhotoImage(image_reference)
        return image_reference

    def image_resize(self, file_path, x, y):
        image_reference = Image.open(file_path)
        image_reference = image_reference.resize((x, y), Image.ANTIALIAS)
        image_reference = ImageTk.PhotoImage(image_reference)
        return image_reference

    def image_scale(self, file_path, scale):
        image_reference = Image.open(file_path)
        scale_x = int(image_reference.size[0] * scale)
        scale_y = int(image_reference.size[1] * scale)
        image_reference = image_reference.resize((scale_x, scale_y), Image.ANTIALIAS)
        image_reference = ImageTk.PhotoImage(image_reference)
        return image_reference


def get_servant_icon(entity, x, y):
    image_reference = Image.open(entity['Icon'])
    image_reference = image_reference.resize((x, y), Image.ANTIALIAS)
    image_reference = ImageTk.PhotoImage(image_reference)
    return image_reference

def image(file_path):
    image_reference = Image.open(file_path)
    image_reference = ImageTk.PhotoImage(image_reference)
    return image_reference

def image_resize(file_path, x, y):
    image_reference = Image.open(file_path)
    image_reference = image_reference.resize((x, y), Image.ANTIALIAS)
    image_reference = ImageTk.PhotoImage(image_reference)
    return image_reference

def image_scale(file_path, scale):
    image_reference = Image.open(file_path)
    scale_x = int(image_reference.size[0] * scale)
    scale_y = int(image_reference.size[1] * scale)
    image_reference = image_reference.resize((scale_x, scale_y), Image.ANTIALIAS)
    image_reference = ImageTk.PhotoImage(image_reference)
    return image_reference