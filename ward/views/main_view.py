from PyQt5.QtWidgets import QVBoxLayout, QWidget, QComboBox, QLabel, QMainWindow, QSystemTrayIcon, QMenu, QAction, qApp
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize, Qt

from ..constants import *
from ..utils.utils import *


class MainView(QMainWindow):

    def __init__(self, ctrl):
        super(MainView, self).__init__()
        self.__ctrl = ctrl
        self.build_ui()

    def build_ui(self):
        self.setWindowTitle('User login')
        self.setFixedSize(100, 100)

        # Init widgets
        self.main_widget = QWidget()

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        # Setup layouts
        self.main_widget.setLayout(main_layout)

        self.setCentralWidget(self.main_widget)

        self.show()
     