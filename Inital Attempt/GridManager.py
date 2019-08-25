import GlobalLibrary
import ast

GlobalLibrary.initalise(__file__)


class Main:

    def __init__(self, grid_amount, grid_size, GUI):
        self.GUI = GUI
        self.grid_size = int(grid_size)
        self.grid_amount = int(grid_amount)
        self.grid = []
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

    def set_grid_pos(self, x, y, entity):
        self.grid[y][x] = entity
        if not isinstance(entity, str):
            self.GUI.draw_servant(entity=entity, pos_x=x, pos_y=y, grid_snap=True, scale=None)

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
                    if (self.grid[y][x]) == "#":
                        tile_image = self.GUI.ui_tiles_chaldea['Floor']
                    else:
                        print((self.grid[y][x]))
                        tile_image = self.GUI.ui_tiles_chaldea[(self.grid[y][x])]
                    self.GUI.grid_graphics = []
                    self.GUI.grid_graphics.append(self.GUI.canvas.create_image((self.GUI.grid_origin_x + (self.grid_size*x)), (self.GUI.grid_origin_y + (self.grid_size*y)), image=tile_image, anchor="nw"))

    def load_map(self, map_name):
        map_path = str("Maps/"+map_name+".txt")
        y = 0
        with open(map_path, "r") as map_file:
            for map_line in map_file.readlines():
                map_line = ast.literal_eval(map_line)
                x = 0
                for tile_value in map_line:
                    self.set_grid_pos(x, y, tile_value)
                    x += 1
                y += 1