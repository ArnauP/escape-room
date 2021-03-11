from PyQt5.QtWidgets import QVBoxLayout, QWidget, QComboBox, QLabel, QMainWindow, QSystemTrayIcon, QMenu, QAction, qApp, QLineEdit, QPushButton
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
        self.setWindowTitle('Control Panel')
        self.setFixedSize(300, 400)

        # Init widgets
        self.main_widget = QWidget()

        self.img_container = QLabel(self.main_widget)
        img = QPixmap(PATH_ICON)
        self.img_container.setPixmap(img.scaled(QSize(100, 100)))
        self.img_container.setStyleSheet(
            """
            margin-bottom: 30px;
            padding-left: 30px;
            """
            )

        self.lbl_username = QLabel('Username')
        self.le_username = QLineEdit('Admin')
        self.lbl_password = QLabel('Password')
        self.le_password = QLineEdit(EXPECTED_PASSWORD)
        self.le_password.setEchoMode(QLineEdit.Password)

        self.lbl_error = QLabel()
        self.lbl_error.setStyleSheet(
            """
            color: red;
            margin-top: 10px;
            padding-left: 10px;
            """
        )
        self.lbl_error.hide()

        self.btn_confirm = QPushButton('Confirm')
        self.btn_confirm.clicked.connect(self.on_confirmation)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        # Setup layouts
        main_layout.addWidget(self.img_container)
        main_layout.addWidget(self.lbl_username)
        main_layout.addWidget(self.le_username)
        main_layout.addWidget(self.lbl_password)
        main_layout.addWidget(self.le_password)
        main_layout.addWidget(self.lbl_error)
        main_layout.addWidget(self.btn_confirm)
        self.main_widget.setLayout(main_layout)

        self.setCentralWidget(self.main_widget)

        self.show()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            self.on_confirmation()
        return super().keyPressEvent(event)

    def reset_view(self, keep_pwd=True):
        self.le_username.setEnabled(True)
        self.le_password.setEnabled(True)
        self.btn_confirm.setEnabled(True)
        if not keep_pwd:
            self.le_password.setText('')
        self.lbl_error.setText('')
        self.lbl_error.hide()
    
    def on_confirmation(self):
        if self.__ctrl.allow_connections:
            self.reset_view()
            self.__ctrl.confirm_credentials(username=self.le_username.text(),
                                            password=self.le_password.text())
        else:
            self.lbl_error.setText('Server did not respond.')
            self.lbl_error.show()
    
    def on_wrong_credentials(self):
        self.lbl_error.setText('Wrong credentials')
        self.lbl_error.show()
    
    def on_right_credentials(self):
        self.le_username.setEnabled(False)
        self.le_password.setEnabled(False)
        self.btn_confirm.setEnabled(False)

    def closeEvent(self, event):
        self.__ctrl.close_all_promts()
