import GlobalLibrary
from PIL import Image, ImageTk

GlobalLibrary.initalise(__file__)


class Main:

    def __init__(self, GUI, grid_size):
        GlobalLibrary.initalise(Main.__name__)

        # INTERFACE ASSETS
        GUI.ui_servant_select_stats_bg = self.import_image("Pictures/UI/ServantSelectStats.png")
        GUI.ui_turn_order_bg = self.import_image("Pictures/UI/TurnOrder.png")
        GUI.ui_move_icon = self.import_image_resize("Pictures/UI/MoveIcon.png", grid_size, grid_size)
        GUI.ui_attack_icon = self.import_image_resize("Pictures/UI/AttackIcon.png", grid_size, grid_size)

        # CLASS LOGOS
        GUI.ui_class_saber = self.import_image("Pictures/Classes/Saber.png")
        GUI.ui_class_archer = self.import_image("Pictures/Classes/Archer.png")
        GUI.ui_class_lancer = self.import_image("Pictures/Classes/Lancer.png")
        GUI.ui_class_caster = self.import_image("Pictures/Classes/Caster.png")
        GUI.ui_class_rider = self.import_image("Pictures/Classes/Rider.png")
        GUI.ui_class_assassin = self.import_image("Pictures/Classes/Assassin.png")
        GUI.ui_class_ruler = self.import_image("Pictures/Classes/Ruler.png")
        GUI.ui_class_shielder = self.import_image("Pictures/Classes/Shielder.png")
        GUI.ui_class_berserker = self.import_image("Pictures/Classes/Berserker.png")

        # TERRAIN TILES
        GUI.ui_tiles_chaldea = {}
        GUI.ui_tiles_chaldea.update(
            {"Single": self.import_image_resize("Pictures/Terrain/Chaldea/Single.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"X": self.import_image_resize("Pictures/Terrain/Chaldea/X.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"Straight_H": self.import_image_resize("Pictures/Terrain/Chaldea/Straight_H.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"Straight_V": self.import_image_resize("Pictures/Terrain/Chaldea/Straight_V.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"Floor": self.import_image_resize("Pictures/Terrain/Chaldea/Floor.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"Corner_BR": self.import_image_resize("Pictures/Terrain/Chaldea/Corner_BR.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"Corner_BL": self.import_image_resize("Pictures/Terrain/Chaldea/Corner_BL.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"Corner_TR": self.import_image_resize("Pictures/Terrain/Chaldea/Corner_TR.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"Corner_TL": self.import_image_resize("Pictures/Terrain/Chaldea/Corner_TL.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"T_RBL": self.import_image_resize("Pictures/Terrain/Chaldea/T_RBL.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"T_RTL": self.import_image_resize("Pictures/Terrain/Chaldea/T_RTL.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"T_TLB": self.import_image_resize("Pictures/Terrain/Chaldea/T_TLB.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"T_TRB": self.import_image_resize("Pictures/Terrain/Chaldea/T_TRB.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"End_T": self.import_image_resize("Pictures/Terrain/Chaldea/End_T.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"End_B": self.import_image_resize("Pictures/Terrain/Chaldea/End_B.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"End_L": self.import_image_resize("Pictures/Terrain/Chaldea/End_L.png", grid_size, grid_size)})
        GUI.ui_tiles_chaldea.update(
            {"End_R": self.import_image_resize("Pictures/Terrain/Chaldea/End_R.png", grid_size, grid_size)})

        print(GUI.ui_tiles_chaldea)
        print(GUI.ui_tiles_chaldea['Straight_H'])

    def import_image(self, file_path):
        image_reference = Image.open(file_path)
        image_reference = ImageTk.PhotoImage(image_reference)
        return image_reference

    def import_image_resize(self, file_path, x, y):
        image_reference = Image.open(file_path)
        image_reference = image_reference.resize((x, y), Image.ANTIALIAS)
        image_reference = ImageTk.PhotoImage(image_reference)
        return image_reference
