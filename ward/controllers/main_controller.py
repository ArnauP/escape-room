from PyQt5.QtCore import QObject

from ..views.terminal_view import TerminalView
from ..views.main_view import MainView
from ..utils.utils import *
from ..constants import *


class MainController(QObject):

    def __init__(self):
        QObject.__init__(self)
        self.__view = MainView(self)
        self.__allow_connections = True
        self.__prompt_info_1 = None
        self.__prompt_info_2 = None
        self.__prompt_info_3 = None
        self.__prompt_info_4 = None
        self.__prompt_commands = None
    
    def confirm_credentials(self, username, password):
        if username == EXPECTED_USERNAME and password == EXPECTED_PASSWORD:
            self.__view.on_right_credentials()
            self.init_command_prompts()
        else:
            self.__view.on_wrong_credentials()
    
    def init_command_prompts(self):
        self.__prompt_info_1 = TerminalView(self, 'Server prompt',
                                            command_line=False, automatic=True, timeout=1500, position=[-900, -400], 
                                            prompt_type='server')
        self.__prompt_info_2 = TerminalView(self, 'Weapons prompt',
                                            command_line=False, automatic=True, timeout=1200, position=[-900, 100], 
                                            prompt_type='weapons')
        self.__prompt_info_3 = TerminalView(self, 'Engines prompt',
                                            command_line=False, automatic=True, timeout=1000, position=[100, -400], 
                                            prompt_type='engines')
        self.__prompt_commands = TerminalView(self, 'System prompt',
                                              command_line=True, automatic=False, position=[100, 100])

    def system_shutdown(self):
        self.__allow_connections = False
        self.close_all_promts()
        self.__view.reset_view(keep_pwd=False)

    def close_all_promts(self):
        if self.__prompt_info_1:
            self.__prompt_info_1.close()
        if self.__prompt_info_2:
            self.__prompt_info_2.close()
        if self.__prompt_info_3:
            self.__prompt_info_3.close()
        if self.__prompt_info_4:
            self.__prompt_info_4.close()
        if self.__prompt_commands:
            self.__prompt_commands.close()

    @property
    def allow_connections(self):
        return self.__allow_connections
