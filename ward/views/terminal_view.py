from PyQt5.QtWidgets import QVBoxLayout, QWidget, QComboBox, QLabel, QMainWindow, QSystemTrayIcon, QMenu, QAction, qApp, QLineEdit, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QSize, Qt, QTimer, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication
from random import randint, choice
from time import sleep
import asyncio

from ..constants import *
from ..utils.utils import *


class ShutDownThread(QThread):
    echo_msg = pyqtSignal(str)
    shut_down_done = pyqtSignal()

    def __init__(self):
        """ Constructor, setting initial variables """
        super(ShutDownThread, self).__init__()
        self.__stop = False
        self.__loop = asyncio.new_event_loop()

    def run(self):
        async def callback():
            while not self.__stop:
                self.echo_msg.emit('SYSTEM WILL BE SHUT DOWN IN 3')
                sleep(1)
                self.echo_msg.emit('SYSTEM WILL BE SHUT DOWN IN 2')
                sleep(1)
                self.echo_msg.emit('SYSTEM WILL BE SHUT DOWN IN 1')
                sleep(1)
                self.echo_msg.emit('SHUTTING DOWN THE SYSTEM...')
                sleep(2)
                self.shut_down_done.emit()

        self.__loop.run_until_complete(asyncio.wait([callback()]))
        self.__loop.stop()
        self.__loop.close()
        del self.__loop
        self.exit(0)


class TerminalView(QMainWindow):

    def __init__(self, ctrl, title, command_line=False, automatic=False, timeout=1000, position=None, prompt_type=None):
        super(TerminalView, self).__init__()
        self.__ctrl = ctrl
        self.__title = title
        self.__command_line = command_line
        self.__position = position
        self.__prompt_type = prompt_type
        self.max_lines_prompted = 18

        if automatic:
            self.__timer = QTimer()
            self.__timer.timeout.connect(self.print_status)
            self.__timer.start(timeout)

        self.build_ui()

    def build_ui(self):
        self.setWindowTitle(self.__title)
        self.setFixedSize(700, 300)

        # Init widgets
        self.main_widget = QWidget()

        self.lbl_promt = QLabel()
        self.lbl_promt.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.le_commands = QLineEdit()
        self.le_commands.setFixedSize(690, 30)

        if not self.__command_line:
            self.max_lines_prompted = 18
            self.lbl_promt.setFixedSize(690, 290)
            self.le_commands.hide()
        else:
            self.echo_command(MSG_HELP)
            self.max_lines_prompted = 14
            self.lbl_promt.setFixedSize(690, 220)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        self.main_widget.setStyleSheet(
            """
            QWidget {
                background-color: black;
            }
            QLabel {
                background-color: transparent;
                color: green;
            }
            QLineEdit {
                background-color: transparent;
                color: green;
            }
            """
        )

        # Setup layouts
        main_layout.addWidget(self.lbl_promt)
        main_layout.addWidget(self.le_commands)
        self.main_widget.setLayout(main_layout)

        self.setCentralWidget(self.main_widget)
        self.setWindowFlag(Qt.WindowCloseButtonHint, False)

        if self.__position:
            self.move_position_offset(self.__position[0], self.__position[1])

        self.show()

    def move_position_offset(self, offset_x, offset_y):
        frameGm = self.frameGeometry()
        screen = QApplication.desktop().screenNumber(QApplication.desktop().cursor().pos())
        centerPoint = QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.center().x() + offset_x, frameGm.center().y() + offset_y)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.parse_command(self.le_commands.text())
            self.le_commands.setText('')
        return super().keyPressEvent(event)

    def parse_command(self, command):
        if command == COMMAND_HELP:
            self.echo_command(MSG_HELP_RESPONSE)
        elif command == COMMAND_SYSTEM_SHUTDOWN:
            self.__shutdown_thread = ShutDownThread()
            self.__shutdown_thread.echo_msg.connect(self.echo_command)
            self.__shutdown_thread.shut_down_done.connect(self.__ctrl.system_shutdown)
            self.__shutdown_thread.start()
        elif command in COMMAND_SYSTEM_STATUS:
            self.echo_command('\n>> System status: RUNNING. \n'
                              '    Process ID: 0x5239\n'
                              '    Num. Threads: {}\n'.format(randint(20, 60)))
        elif command in COMMAND_WEAPONS_ENABLE:
            self.echo_command('\n>> Weapons already enabled.')
        elif command in COMMAND_WEAPONS_DISABLE:
            self.echo_command('\n>> Could not disable weapons.')
        elif command in COMMAND_SERVER_STATUS:
            self.echo_command('\n>> Server status: RUNNING. \n'
                              '    Status code: 200\n'
                              '    Error queue: Empty\n')
        elif command == COMMAND_SERVER_KEY:
            self.echo_command('\n>>  Downloading key...')
        elif command in COMMAND_ENGINES_START:
            self.echo_command('\n>> Engines already running.')
        elif command in COMMAND_ENGINES_STOP:
            self.echo_command('\n>> Could not stop engines.')
        else:
            self.echo_command('>> Unknown command.')

    def echo_command(self, command):
        current_lines = self.lbl_promt.text().split('\n')
        incoming_lines = command.split('\n')
        if current_lines is not None:
            total_lines = current_lines + incoming_lines
            if len(total_lines) > self.max_lines_prompted:
                allowed_lines = len(total_lines) - self.max_lines_prompted
                displayed_lines = total_lines[allowed_lines:]
            else:
                displayed_lines = total_lines
            str_displayed_lines = ''
            for line in displayed_lines:
                str_displayed_lines += '{}\n'.format(line)
        else:
            str_displayed_lines = '{}\n'.format(command)
        self.lbl_promt.setText(str_displayed_lines.replace('\n\n', '\n'))
    
    def print_status(self):
        if self.__prompt_type == TYPE_PROMPT_WEAPONS:
            self.echo_command(choice(MSG_AUTOMATIC_WEAPONS).format(
                datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S'), choice(ascii_uppercase), randint(1, 50), choice(STATUS_WEAPONS)))
        elif self.__prompt_type == TYPE_PROMPT_SERVER:
            self.echo_command(choice(MSG_AUTOMATIC_SERVER).format(
                datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S'), choice(STATUS_SERVER)))
        elif self.__prompt_type == TYPE_PROMPT_ENGINES:
            self.echo_command(choice(MSG_AUTOMATIC_ENGINES).format(
                datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S'), hex(randint(5000, 10000)).upper(), choice(STATUS_ENGINES)))
        else:
            self.echo_command('STATUS: PASS')
