import GlobalLibrary
GlobalLibrary.initalise(__file__)

class Main:

    def __init__(self):
        GlobalLibrary.initalise(Main.__name__)
        self.ServantSlotOne = "Mordred Pendragon"
        self.ServantSlotTwo = "Illyasviel von Einzbern"
        self.ServantSlotThree = "Astolfo"