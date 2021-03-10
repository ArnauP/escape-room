from PyQt5.QtWidgets import QVBoxLayout, QWidget, QComboBox, QLabel, QMainWindow, QSystemTrayIcon, QMenu, QAction, qApp, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize, Qt, QTimer

from ..constants import *
from ..utils.utils import *


class TerminalView(QMainWindow):

    def __init__(self, ctrl, title, command_line):
        super(TerminalView, self).__init__()
        self.__ctrl = ctrl
        self.__title = title
        self.__command_line = command_line

        self.__timer = QTimer()
        self.__timer.timeout.connect(self.print_status)
        self.__timer.start(2000)

        self.build_ui()

    def build_ui(self):
        self.setWindowTitle(self.__title)
        self.setFixedSize(700, 300)

        # Init widgets
        self.main_widget = QWidget()

        self.lbl_promt = QLabel()
        self.lbl_promt.setFixedSize(690, 250)
        self.lbl_promt.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.le_commands = QLineEdit()
        self.le_commands.setFixedSize(690, 30)

        if not self.__command_line:
            self.__command_line.hide()

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        # Setup layouts
        main_layout.addWidget(self.lbl_promt)
        main_layout.addWidget(self.le_commands)
        self.main_widget.setLayout(main_layout)

        self.setCentralWidget(self.main_widget)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)

        self.show()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.send_command(self.le_commands.text())
            self.le_commands.setText('')
        return super().keyPressEvent(event)

    def send_command(self, command):
        self.lbl_promt.setText('{}{}\n'.format(self.lbl_promt.text(), command))
    
    def print_status(self):
        self.send_command('STATUS: GOOD')
     