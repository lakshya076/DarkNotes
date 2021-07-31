
from PyQt5.QtGui import QKeySequence, QIcon
from PyQt5.QtWidgets import QAction


class FileMenu_Items:
    def __init__(self, parent=None):
        self.parent = parent

        self.new_file_action = QAction(QIcon(), "New file", self.parent)
        self.new_file_action.setStatusTip("New file")
        self.new_file_action.triggered.connect(self.parent.file_new)
        self.new_file_action.setShortcut(QKeySequence('Ctrl+N'))

        self.open_file_action = QAction(QIcon(), "Open file...", self.parent)
        self.open_file_action.setStatusTip("Open file")
        self.open_file_action.triggered.connect(self.parent.file_open)
        self.open_file_action.setShortcut(QKeySequence('Ctrl+O'))

        self.save_file_action = QAction(QIcon(), "Save", self.parent)
        self.save_file_action.setStatusTip("Save current page")
        self.save_file_action.triggered.connect(self.parent.file_save)
        self.save_file_action.setShortcut(QKeySequence('Ctrl+S'))

        self.saveas_file_action = QAction(QIcon(), "Save As...", self.parent)
        self.saveas_file_action.setStatusTip("Save current page to specified file")
        self.saveas_file_action.triggered.connect(self.parent.file_saveas)
        self.saveas_file_action.setShortcut(QKeySequence('Ctrl+Shift+S'))

        self.md_mode_action = QAction(QIcon(), "Markdown Mode", self.parent)
        self.md_mode_action.setStatusTip("Enter the markdown mode. (Still in beta)")
        self.md_mode_action.triggered.connect(self.parent.md_mode)
        self.md_mode_action.setShortcut(QKeySequence('Ctrl+Shift+M'))

        self.print_action = QAction(QIcon(), "Print...", self.parent)
        self.print_action.setStatusTip("Print current page")
        self.print_action.triggered.connect(self.parent.file_print)
        self.print_action.setShortcut(QKeySequence('Ctrl+P'))

        self.export = QAction(QIcon(), "Export as PDF...", self.parent)
        self.export.setStatusTip("Export the document in pdf format.")
        self.export.triggered.connect(self.parent.export_pdf)
        self.export.setShortcut(QKeySequence('Ctrl+Shift+E'))

        self.exit_action = QAction(QIcon(), "Exit", self.parent)
        self.exit_action.setStatusTip("Exit DarkNotes")
        self.exit_action.triggered.connect(self.parent.exit)
        self.exit_action.setShortcut('Alt+F4')
