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

        ui_class_saber = Image.open("Pictures/Classes/Saber.png")
        ui_class_saber = ImageTk.PhotoImage(ui_class_saber)
        GUI.ui_class_saber = ui_class_saber

        ui_class_archer = Image.open("Pictures/Classes/Archer.png")
        ui_class_archer = ImageTk.PhotoImage(ui_class_archer)
        GUI.ui_class_archer = ui_class_archer

        ui_class_lancer = Image.open("Pictures/Classes/Lancer.png")
        ui_class_lancer = ImageTk.PhotoImage(ui_class_lancer)
        GUI.ui_class_lancer = ui_class_lancer

        ui_class_caster = Image.open("Pictures/Classes/Caster.png")
        ui_class_caster = ImageTk.PhotoImage(ui_class_caster)
        GUI.ui_class_caster = ui_class_caster

        ui_class_rider = Image.open("Pictures/Classes/Rider.png")
        ui_class_rider = ImageTk.PhotoImage(ui_class_rider)
        GUI.ui_class_rider = ui_class_rider

        ui_class_assassin = Image.open("Pictures/Classes/Assassin.png")
        ui_class_assassin = ImageTk.PhotoImage(ui_class_assassin)
        GUI.ui_class_assassin = ui_class_assassin

        ui_class_ruler = Image.open("Pictures/Classes/Ruler.png")
        ui_class_ruler = ImageTk.PhotoImage(ui_class_ruler)
        GUI.ui_class_ruler = ui_class_ruler

        ui_class_shielder = Image.open("Pictures/Classes/Shielder.png")
        ui_class_shielder = ImageTk.PhotoImage(ui_class_shielder)
        GUI.ui_class_ruler = ui_class_shielder

        ui_class_berserker = Image.open("Pictures/Classes/Berserker.png")
        ui_class_berserker = ImageTk.PhotoImage(ui_class_berserker)
        GUI.ui_class_ruler = ui_class_berserker
