import GlobalLibrary

GlobalLibrary.initalise(__file__)


class Main:

    def __init__(self, grid_amount, grid_size, GUI):
        self.GUI = GUI
        self.grid_size = int(grid_size)
        self.grid_amount = int(grid_amount)
        self.grid = []
        for i in range(0, grid_amount):
            self.grid.append(["#"] * self.grid_amount)

    def print_map(self):
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
        self.GUI.draw_servant(entity=entity, pos_x=x, pos_y=y, grid_snap=True, scale=None)

    def move_grid_pos(self, old_x, old_y, new_x, new_y, is_entity):
        entity = self.grid[old_y][old_x]
        self.grid[old_y][old_x] = "#"
        self.grid[new_y][new_x] = entity
        if is_entity:
            self.GUI.move_servant(entity, old_x, old_y, new_x, new_y)
