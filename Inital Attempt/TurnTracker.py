import GlobalLibrary

GlobalLibrary.initalise(__file__)


class Main:

    def __init__(self, player_stats):
        GlobalLibrary.initalise(Main.__name__)
        self.player_stats = player_stats
        self.GUI = None
        self.CurrentTurnCounter = 1
        self.OverallTurnCounter = 1
        self.TurnCounterDict = {}

    def next_turn(self):
        GlobalLibrary.notice(str("Turn: " + str(self.OverallTurnCounter)))
        if self.CurrentTurnCounter == len(self.TurnCounterDict):
            self.CurrentTurnCounter = 1
            self.OverallTurnCounter += 1
        else:
            self.CurrentTurnCounter += 1
        self.display_current_turn()

    def display_current_turn(self):
        if self.TurnCounterDict[self.CurrentTurnCounter] == self.player_stats.ServantSlotOne:
            colour = "#8888ff"
        elif self.TurnCounterDict[self.CurrentTurnCounter] == self.player_stats.ServantSlotTwo:
            colour = "#8888ff"
        elif self.TurnCounterDict[self.CurrentTurnCounter] == self.player_stats.ServantSlotThree:
            colour = "#8888ff"
        else:
            colour = "#ff8888"
        next_servant_list = []
        for i in range(0, 3):
            try:
                next_servant_list.append(self.TurnCounterDict[self.CurrentTurnCounter + i])
            except KeyError:
                next_servant_list.append(self.TurnCounterDict[(self.CurrentTurnCounter + i) - len(self.TurnCounterDict)])
        self.GUI.new_turn_display(self.OverallTurnCounter, next_servant_list, colour=colour)