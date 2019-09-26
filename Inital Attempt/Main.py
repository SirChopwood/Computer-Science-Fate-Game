import socket

from Scripts import CoverGUI, GlobalLibrary

GlobalLibrary.initalise(__file__)

user_device_name = socket.gethostname()
user_IP = socket.gethostbyname(socket.gethostname())
GlobalLibrary.debug(str(user_device_name + " | " + user_IP))
cover_interface = CoverGUI.Main(user_IP)
cover_interface.start_mainloop()
cover_gui = CoverGUI.Main()