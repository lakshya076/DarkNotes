from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QAction


class ModeMenu_Items:
    def __init__(self, parent=None):
        self.parent = parent

        self.light_mode_action = QAction(QIcon(), "Light Mode", self.parent)
        self.light_mode_action.setStatusTip("Switch to Light Mode")
        self.light_mode_action.triggered.connect(self.parent.light_mode)
        self.light_mode_action.setShortcut(QKeySequence('Ctrl+Shift+L'))

        self.dark_mode_action = QAction(QIcon(), "Dark Mode", self.parent)
        self.dark_mode_action.setStatusTip("Switch to Dark Mode")
        self.dark_mode_action.triggered.connect(self.parent.dark_mode)
        self.dark_mode_action.setShortcut(QKeySequence('Ctrl+Shift+D'))
