import GUI
import GlobalLibrary
import GridManager
import Mongo
import Servants

GlobalLibrary.initalise(__file__)

grid_amount = 15
grid_size = 45

main_interface = GUI.Main(grid_amount=grid_amount, grid_size=grid_size)
main_interface.draw_grid()
main_database = Mongo.Main()
main_database.sync_files()

grid_manager = GridManager.Main(grid_amount=grid_amount, grid_size=grid_size, GUI=main_interface)
main_interface.grid_manager = grid_manager

grid_manager.set_grid_pos(2, 1, Servants.get_servant("Mordred Pendragon"))
grid_manager.set_grid_pos(6, 5, Servants.get_servant("Jeanne D'arc"))
grid_manager.set_grid_pos(8, 10, Servants.get_servant("Illyasviel von Einzbern"))
grid_manager.set_grid_pos(3, 10, Servants.get_servant("Mashu Kyrielight"))
grid_manager.set_grid_pos(9, 10, Servants.get_servant("Chloe von Einzbern"))
grid_manager.set_grid_pos(8, 11, Servants.get_servant("Merlin"))
grid_manager.set_grid_pos(5, 10, Servants.get_servant("Kid Gilgamesh"))
grid_manager.set_grid_pos(1, 7, Servants.get_servant("Artoria Pendragon (Lily)"))
grid_manager.print_map()

main_interface.start_mainloop()
