from PyQt5.QtCore import QObject

from ..views.main_view import MainView
from ..utils.utils import *
from ..constants import *


class MainController(QObject):

    def __init__(self):
        QObject.__init__(self)
        self.__view = MainView(self)
