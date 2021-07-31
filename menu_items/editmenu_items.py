from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QAction


class EditMenu_Items:
    def __init__(self, parent=None):
        self.parent = parent

        self.undo_action = QAction(QIcon(), "Undo", self.parent)
        self.undo_action.setStatusTip("Undo last change")
        self.undo_action.triggered.connect(self.parent.editor.undo)
        self.undo_action.setShortcut(QKeySequence('Ctrl+Z'))

        self.redo_action = QAction(QIcon(), "Redo", self.parent)
        self.redo_action.setStatusTip("Redo last change")
        self.redo_action.triggered.connect(self.parent.editor.redo)
        self.redo_action.setShortcut(QKeySequence('Ctrl+Y'))

        self.left_align = QAction(QIcon(), "Align Left", self.parent)
        self.left_align.setStatusTip("Align the text to left.")
        self.left_align.triggered.connect(lambda: self.parent.editor.setAlignment(Qt.AlignLeft))
        self.left_align.setShortcut('Ctrl+L')

        self.center_align = QAction(QIcon(), "Align Center", self.parent)
        self.center_align.setStatusTip("Align the text to center.")
        self.center_align.triggered.connect(lambda: self.parent.editor.setAlignment(Qt.AlignCenter))
        self.center_align.setShortcut('Ctrl+E')

        self.right_align = QAction(QIcon(), "Align Right", self.parent)
        self.right_align.setStatusTip("Align the text to right.")
        self.right_align.triggered.connect(lambda: self.parent.editor.setAlignment(Qt.AlignRight))
        self.right_align.setShortcut('Ctrl+R')

        self.cut_action = QAction(QIcon(), "Cut", self.parent)
        self.cut_action.setStatusTip("Cut selected text")
        self.cut_action.triggered.connect(self.parent.editor.cut)
        self.cut_action.setShortcut(QKeySequence('Ctrl+X'))

        self.copy_action = QAction(QIcon(), "Copy", self.parent)
        self.copy_action.setStatusTip("Copy selected text")
        self.copy_action.triggered.connect(self.parent.editor.copy)
        self.copy_action.setShortcut(QKeySequence('Ctrl+C'))

        self.paste_action = QAction(QIcon(), "Paste", self.parent)
        self.paste_action.setStatusTip("Paste from clipboard")
        self.paste_action.triggered.connect(self.parent.editor.paste)
        self.paste_action.setShortcut(QKeySequence('Ctrl+V'))

        self.select_action = QAction(QIcon(), "Select all", self.parent)
        self.select_action.setStatusTip("Select all text")
        self.select_action.triggered.connect(self.parent.editor.selectAll)
        self.select_action.setShortcut(QKeySequence('Ctrl+A'))

        self.find_replace = QAction(QIcon(), "Find | Replace", self.parent)
        self.find_replace.setStatusTip("Find and replace text...")
        self.find_replace.triggered.connect(self.parent.find_replace_func)
        self.find_replace.setShortcut(QKeySequence('Ctrl+F'))

        self.bold_action = QAction(QIcon(), "Bold", self.parent)
        self.bold_action.setStatusTip("Make the selected text bold")
        self.bold_action.triggered.connect(self.parent.text_bold)
        self.bold_action.setCheckable(True)
        self.bold_action.setChecked(False)
        self.bold_action.setShortcut(QKeySequence('Ctrl+B'))

        self.italic_action = QAction(QIcon(), "Italic", self.parent)
        self.italic_action.setStatusTip("Italicize selected text")
        self.italic_action.triggered.connect(self.parent.text_italic)
        self.italic_action.setCheckable(True)
        self.italic_action.setChecked(False)
        self.italic_action.setShortcut(QKeySequence('Ctrl+I'))

        self.underline_action = QAction(QIcon(), "Underline", self.parent)
        self.underline_action.setStatusTip("Underline selected text")
        self.underline_action.triggered.connect(self.parent.text_underline)
        self.underline_action.setCheckable(True)
        self.underline_action.setChecked(False)
        self.underline_action.setShortcut(QKeySequence('Ctrl+U'))
