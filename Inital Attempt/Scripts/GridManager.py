import ast

from Scripts import GlobalLibrary, Servants

GlobalLibrary.initalise(__file__)


class Main:

    def __init__(self, grid_amount, grid_size, GUI, turn_tracker):
        GlobalLibrary.initalise(Main.__name__)
        self.GUI = GUI
        self.grid_size = int(grid_size)
        self.grid_amount = int(grid_amount)
        self.grid = []
        self.turn_tracker = turn_tracker
        for i in range(0, grid_amount):
            self.grid.append(["#"] * self.grid_amount)

    def print_grid(self):
        for i in range(len(self.grid)):
            print(self.grid[i])

    def get_grid_pos(self, x, y):
        try:
            entity = self.grid[y][x]
            return entity
        except IndexError:
            return

    def find_servant(self, servant_name):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                pos = self.grid[y][x]
                if isinstance(pos, dict):
                    if pos['Name'] == servant_name:
                        return pos, x, y

    def set_grid_pos(self, x, y, entity, redraw):
        self.grid[y][x] = entity
        if redraw:
            if not isinstance(entity, str):
                self.GUI.draw_servant(entity=entity, pos_x=x, pos_y=y, grid_snap=True, scale=None)

    def spawn_player_servants(self, servant_database):
        S1, S2, S3 = Servants.get_player_servants(servant_database)
        for y in range(self.grid_amount):
            for x in range(self.grid_amount):
                if not isinstance(self.grid[y][x], dict):
                    if (self.grid[y][x]) == "Marker_Start_Pos1":
                        self.set_grid_pos(x, y, S1, True)
                    if (self.grid[y][x]) == "Marker_Start_Pos2":
                        self.set_grid_pos(x, y, S2, True)
                    if (self.grid[y][x]) == "Marker_Start_Pos3":
                        self.set_grid_pos(x, y, S3, True)
        self.turn_tracker.TurnCounterList.append(S1["Name"])
        self.turn_tracker.TurnCounterList.append(S2["Name"])
        self.turn_tracker.TurnCounterList.append(S3["Name"])

    def move_grid_pos(self, old_x, old_y, new_x, new_y, is_entity):
        entity = self.grid[old_y][old_x]
        self.grid[old_y][old_x] = "#"
        self.grid[new_y][new_x] = entity
        if is_entity:
            self.GUI.move_servant(entity, old_x, old_y, new_x, new_y)

    def display_grid_graphics(self):
        for y in range(self.grid_amount):
            for x in range(self.grid_amount):
                if not isinstance(self.grid[y][x], dict):
                    if (self.grid[y][x]) == "#" or "Marker" in (self.grid[y][x]):
                        tile_image = self.GUI.ui_tiles_chaldea['Floor']
                    else:
                        tile_image = self.GUI.ui_tiles_chaldea[(self.grid[y][x])]
                    self.GUI.grid_graphics = []
                    self.GUI.grid_graphics.append(
                        self.GUI.canvas.create_image((self.GUI.grid_origin_x + (self.grid_size * x)),
                                                     (self.GUI.grid_origin_y + (self.grid_size * y)), image=tile_image,
                                                     anchor="nw"))

    def load_map(self, map_name, player_servants):
        map_path = str("Maps/" + map_name + ".txt")
        y = 0
        with open(map_path, "r") as map_file:
            for map_line in map_file.readlines():
                map_line = ast.literal_eval(map_line)
                x = 0
                for tile_value in map_line:
                    self.set_grid_pos(x, y, tile_value, False)
                    x += 1
                y += 1
        self.display_grid_graphics()
        self.spawn_player_servants(player_servants)
        enemy_path = str("Maps/" + map_name + "_Enemies.txt")
        with open(enemy_path, "r") as enemy_file:
            for enemy_line in enemy_file.readlines():
                enemy_line = ast.literal_eval(enemy_line)
                self.set_grid_pos(enemy_line[0], enemy_line[1], Servants.get_enemy_servant(enemy_line[2], enemy_line[3]), True)
                self.turn_tracker.TurnCounterList.append(enemy_line[2])
