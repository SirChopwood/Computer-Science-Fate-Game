from Scripts import GlobalLibrary

GlobalLibrary.initalise(__file__)


class Main:

    def __init__(self, grid_manager, GUI):
        GlobalLibrary.initalise(Main.__name__)
        self.grid_manager = grid_manager
        self.GUI = GUI

    def start_enemy_turn(self, entity, x, y):
        GlobalLibrary.notice(str("Enemy " + entity['Name'] + "'s turn has started!"))
        target_list = []
        for pos_y in range(len(self.grid_manager.grid)):
            for pos_x in range(len(self.grid_manager.grid[pos_y])):
                pos = self.grid_manager.grid[pos_y][pos_x]
                if isinstance(pos, dict):
                    if pos['Allied']:
                        distance = int(abs(x - pos_x) + abs(y - pos_y) / 2)
                        print(distance)
                        strength = int(((pos['HP'] + pos['ATK']) / 1000) + (pos['Range']))
                        print(strength)
                        level_gap = entity['Level'] - pos['Level']
                        print(level_gap)
                        danger_value = 10 + int(((-distance + strength) - (int(pos['CurrentHP'] / 5000))) + (level_gap / 2))
                        print(danger_value)
                        target = [pos, pos_x, pos_y, danger_value]
                        target_list.append(target)
        print(target_list)
        current_target = target
        for target in target_list:
            print(target[3], current_target[3])
            if target[3] > current_target[3]:
                current_target = target
        print(current_target)
