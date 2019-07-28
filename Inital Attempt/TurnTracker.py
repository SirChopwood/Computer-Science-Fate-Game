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
        self.TurnCounterDict.update({1: self.player_stats.ServantSlotOne})
        self.TurnCounterDict.update({2: self.player_stats.ServantSlotTwo})
        self.TurnCounterDict.update({3: self.player_stats.ServantSlotThree})
        self.TurnCounterDict.update({4: "Enemy Test"})

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
        self.GUI.new_turn_display(self.OverallTurnCounter, self.TurnCounterDict[self.CurrentTurnCounter], colour=colour)