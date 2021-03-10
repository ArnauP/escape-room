from PyQt5.QtCore import QObject

from ..views.terminal_view import TerminalView
from ..views.main_view import MainView
from ..utils.utils import *
from ..constants import *


class MainController(QObject):

    def __init__(self):
        QObject.__init__(self)
        self.__view = MainView(self)
        self.__prompt = None
    
    def confirm_credentials(self, username, password):
        if password == EXPECTED_PASSWORD:
            self.__view.on_right_credentials()
            # TODO: Show all prompts
            self.init_command_prompts()
        else:
            self.__view.on_wrong_credentials()
    
    def init_command_prompts(self):
        self.__prompt = TerminalView(self, 'Server prompt', True)
    
    def close_all_promts(self):
        if self.__prompt:
            self.__prompt.close()
