import os
import random

import GlobalLibrary
from PIL import Image, ImageTk

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
        GlobalLibrary.notice("Graphical Assets Imported")

    def image(self, file_path):
        image_reference = Image.open(file_path)
        image_reference = ImageTk.PhotoImage(image_reference)
        return image_reference

    def image_resize(self, file_path, x, y):
        image_reference = Image.open(file_path)
        image_reference = image_reference.resize((x, y), Image.ANTIALIAS)
        image_reference = ImageTk.PhotoImage(image_reference)
        return image_reference


class Menu:

    def __init__(self, GUI):
        GlobalLibrary.initalise(Menu.__name__)

        # INTERFACE ASSETS
        GUI.wallpaper = self.image_resize(
            str("Pictures/Wallpapers/" + random.choice(os.listdir("Pictures/Wallpapers"))), GUI.monitor_resolution_x,
            GUI.monitor_resolution_y)
        GUI.logo_image = self.image_resize("Pictures/Logo.png", int(GUI.monitor_resolution_x / 4),
                                           int(GUI.monitor_resolution_y / 4))

    def image(self, file_path):
        image_reference = Image.open(file_path)
        image_reference = ImageTk.PhotoImage(image_reference)
        return image_reference

    def image_resize(self, file_path, x, y):
        image_reference = Image.open(file_path)
        image_reference = image_reference.resize((x, y), Image.ANTIALIAS)
        image_reference = ImageTk.PhotoImage(image_reference)
        return image_reference
