import socket

import GUI
import GlobalLibrary
import GridManager
import Mongo
import Servants
import TurnTracker
import PlayerStats

GlobalLibrary.initalise(__file__)

user_device_name = socket.gethostname()
user_IP = socket.gethostbyname(user_device_name)
GlobalLibrary.debug(str(user_device_name + " | " + user_IP))
grid_amount = 20
grid_size = 50
player_stats = PlayerStats.Main()
turn_tracker = TurnTracker.Main(player_stats=player_stats)
main_interface = GUI.Main(grid_amount=grid_amount, grid_size=grid_size, turn_tracker=turn_tracker, player_stats=player_stats)
main_interface.draw_grid()
turn_tracker.GUI = main_interface
servant_database = Mongo.ServantDatabase()
servant_database.sync_files()
player_database = Mongo.PlayerDatabase()
player_servants = player_database.find_player_servants(user_IP)
player_inventory = player_database.find_player_inventory(user_IP)
grid_manager = GridManager.Main(grid_amount=grid_amount, grid_size=grid_size, GUI=main_interface)
main_interface.grid_manager = grid_manager
#grid_manager.set_grid_pos(0,0, "Corner_BR")
grid_manager.load_map("Chaldea 1-1")
grid_manager.display_grid_graphics()

S1, S2, S3 = Servants.get_player_servants(player_servants)
grid_manager.set_grid_pos(2, 4, S1)
grid_manager.set_grid_pos(2, 5, S2)
grid_manager.set_grid_pos(2, 6, S3)
grid_manager.set_grid_pos(4, 4, Servants.get_servant("Merlin"))
turn_tracker.TurnCounterDict.update({1: S1["Name"]})
turn_tracker.TurnCounterDict.update({2: S2["Name"]})
turn_tracker.TurnCounterDict.update({3: S3["Name"]})
turn_tracker.display_current_turn()
#grid_manager.print_grid()
main_interface.start_mainloop()
