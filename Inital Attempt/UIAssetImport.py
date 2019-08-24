from PIL import Image, ImageTk
import GlobalLibrary

GlobalLibrary.initalise(__file__)


class Main:

    def __init__(self, GUI, grid_size):
        GlobalLibrary.initalise(Main.__name__)

        ui_servant_select_stats_bg = Image.open("Pictures/UI/ServantSelectStats.png")
        ui_servant_select_stats_bg = ImageTk.PhotoImage(ui_servant_select_stats_bg)
        GUI.ui_servant_select_stats_bg = ui_servant_select_stats_bg

        ui_turn_order_bg = Image.open("Pictures/UI/TurnOrder.png")
        ui_turn_order_bg = ImageTk.PhotoImage(ui_turn_order_bg)
        GUI.ui_turn_order_bg = ui_turn_order_bg

        ui_move_icon = Image.open("Pictures/UI/MoveIcon.png")
        ui_move_icon = ui_move_icon.resize((grid_size, grid_size), Image.ANTIALIAS)
        ui_move_icon = ImageTk.PhotoImage(ui_move_icon)
        GUI.ui_move_icon = ui_move_icon

        ui_attack_icon = Image.open("Pictures/UI/AttackIcon.png")
        ui_attack_icon = ui_attack_icon.resize((grid_size, grid_size), Image.ANTIALIAS)
        ui_attack_icon = ImageTk.PhotoImage(ui_attack_icon)
        GUI.ui_attack_icon = ui_attack_icon