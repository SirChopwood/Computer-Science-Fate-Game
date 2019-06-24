import GUI
import Mongo
import Servants
import json
import GridManager
import GlobalLibrary

GlobalLibrary.initalise(__file__)


grid_amount = 15
grid_size = 45


main_interface = GUI.Main(grid_amount=grid_amount, grid_size=grid_size)
main_interface.draw_grid()
#main_database = Mongo.Main()
#main_database.sync_files()


grid_manager = GridManager.Main(grid_amount=grid_amount, grid_size=grid_size, GUI=main_interface)
grid_manager.print_map()
grid_manager.set_grid_pos(4,2,Servants.get_servant("Mordred Pendragon"))
grid_manager.set_grid_pos(5,2,Servants.get_servant("Jeanne D'arc"))
grid_manager.print_map()



main_interface.start_mainloop()
