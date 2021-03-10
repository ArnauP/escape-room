from PyQt5.QtCore import QObject

from ..views.main_view import MainView
from ..utils.utils import *
from ..constants import *


class MainController(QObject):

    def __init__(self):
        QObject.__init__(self)
        self.__view = MainView(self)
    
    def confirm_credentials(self, username, password):
        if password == EXPECTED_PASSWORD:
            self.__view.on_right_credentials()
            # TODO: Show all the inner view
        else:
            self.__view.on_wrong_credentials()
