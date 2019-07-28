import GUI
import GlobalLibrary
import GridManager
import Mongo
import Servants
import TurnTracker
import PlayerStats

GlobalLibrary.initalise(__file__)

grid_amount = 15
grid_size = 45
player_stats = PlayerStats.Main()
turn_tracker = TurnTracker.Main(player_stats=player_stats)
main_interface = GUI.Main(grid_amount=grid_amount, grid_size=grid_size, turn_tracker=turn_tracker, player_stats=player_stats)
main_interface.draw_grid()
turn_tracker.GUI = main_interface
main_database = Mongo.Main()
main_database.sync_files()

grid_manager = GridManager.Main(grid_amount=grid_amount, grid_size=grid_size, GUI=main_interface)
main_interface.grid_manager = grid_manager

grid_manager.set_grid_pos(2, 4, Servants.get_servant("Mordred Pendragon"))
grid_manager.set_grid_pos(11, 5, Servants.get_servant("Jeanne D'arc"))
grid_manager.set_grid_pos(2, 5, Servants.get_servant("Illyasviel von Einzbern"))
#grid_manager.set_grid_pos(3, 10, Servants.get_servant("Mashu Kyrielight"))
#grid_manager.set_grid_pos(9, 10, Servants.get_servant("Chloe von Einzbern"))
#grid_manager.set_grid_pos(8, 11, Servants.get_servant("Merlin"))
#grid_manager.set_grid_pos(5, 10, Servants.get_servant("Kid Gilgamesh"))
#grid_manager.set_grid_pos(1, 7, Servants.get_servant("Artoria Pendragon (Lily)"))
grid_manager.set_grid_pos(2, 6, Servants.get_servant("Astolfo"))
#grid_manager.print_map()
turn_tracker.display_current_turn()
main_interface.start_mainloop()
