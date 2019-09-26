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
                        strength = int(((pos['HP'] + pos['ATK']) / 1000) + (pos['Range']))
                        level_gap = entity['Level'] - pos['Level']
                        danger_value = 10 + int(((-distance + strength) - (int(pos['CurrentHP'] / 5000))) + (level_gap / 2))
                        target = [pos, pos_x, pos_y, danger_value]
                        target_list.append(target)
        if len(target_list) > 0:
            current_target = target_list[0]
            for target in target_list:
                if target[3] > current_target[3]:
                    current_target = target
            if int(abs(x - current_target[1])) <= entity['Range'] and int(abs(y - current_target[2])) <= entity['Range']:
                self.GUI.servant_selected_attack(entity, current_target[0], current_target[1], current_target[2])
            elif int(abs(x - current_target[1])) <= int(entity['Move']*2) and int(abs(y - current_target[2])) <= int(entity['Move']*2):
                new_x = (x - current_target[1]) % entity['Move']
                if new_x == 0 and current_target[1] < x:
                    new_x = (x - entity['Move'])+1
                elif new_x == 0 and current_target[1] > x:
                    new_x = (x + entity['Move'])-1
                elif new_x != 0 and current_target[1] < x:
                    new_x = x - new_x
                elif new_x != 0 and current_target[1] > x:
                    new_x = x + new_x
                else:
                    new_x = x
                new_y = (y - current_target[2]) % entity['Move']
                if new_y == 0 and current_target[2] < y:
                    new_y = (y - entity['Move'])+1
                elif new_y == 0 and current_target[2] > y:
                    new_y = (y + entity['Move'])-1
                elif new_y != 0 and current_target[2] < y:
                    new_y = y - new_y
                elif new_y != 0 and current_target[2] > y:
                    new_y = y + new_y
                else:
                    new_y = y

                self.grid_manager.move_grid_pos(x, y, new_x, new_y, True)
