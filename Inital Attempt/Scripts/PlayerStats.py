from Scripts import GlobalLibrary, Servants

GlobalLibrary.initalise(__file__)


class Main:

    def __init__(self, servant_database):
        GlobalLibrary.initalise(Main.__name__)
        self.servant_1 = servant_database['Servants'][int(servant_database['ActiveServants'][0])]
        self.servant_2 = servant_database['Servants'][int(servant_database['ActiveServants'][1])]
        self.servant_3 = servant_database['Servants'][int(servant_database['ActiveServants'][2])]
        self.set_servant_references(servant_database)

    def set_servant_references(self, servant_database):
        self.servant_ref_1, self.servant_ref_2, self.servant_ref_3 = Servants.get_player_servants(servant_database)
