from Scripts import GlobalLibrary

GlobalLibrary.initalise(__file__)


class Main:

    def __init__(self, player_stats):
        GlobalLibrary.initalise(Main.__name__)
        self.enemy_AI = None
        self.grid_manager = None
        self.player_stats = player_stats
        self.GUI = None
        self.CurrentTurnCounter = 0
        self.OverallTurnCounter = 0
        self.TurnCounterList = []

    def next_turn(self):
        if self.CurrentTurnCounter == (len(self.TurnCounterList)-1):
            self.CurrentTurnCounter = 0
        else:
            self.CurrentTurnCounter += 1
        GlobalLibrary.notice(str("Turn: " + str(self.OverallTurnCounter)))
        self.display_current_turn()

    def display_current_turn(self):
        if self.TurnCounterList[self.CurrentTurnCounter] == self.player_stats.servant_1:
            colour = "#bbbbbb"
        elif self.TurnCounterList[self.CurrentTurnCounter] == self.player_stats.servant_2:
            colour = "#bbbbbb"
        elif self.TurnCounterList[self.CurrentTurnCounter] == self.player_stats.servant_3:
            colour = "#bbbbbb"
        else:
            colour = "#997777"
            servant_data, servant_x, servant_y = self.grid_manager.find_servant(self.TurnCounterList[self.CurrentTurnCounter])
            self.enemy_AI.start_enemy_turn(servant_data, servant_x, servant_y)
        next_servant_list = []
        for i in range(0, 3):
            try:
                next_servant_list.append(self.TurnCounterList[self.CurrentTurnCounter + i])
            except IndexError:
                next_servant_list.append(
                    self.TurnCounterList[(self.CurrentTurnCounter + i) - len(self.TurnCounterList)])
        self.GUI.new_turn_display(self.OverallTurnCounter, next_servant_list, colour=colour)
