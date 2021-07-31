import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QLabel


class Toolbar_Items:
    def __init__(self, parent=None):
        self.parent = parent

        icon_library = os.getcwd() + '/icons/'

        self.save_btn = QAction(QIcon(icon_library + "save.svg"), "", self.parent)
        self.save_btn.setStatusTip('Save the file.')
        self.save_btn.triggered.connect(lambda: self.parent.file_save())

        self.undo_btn = QAction(QIcon(icon_library + "undo.svg"), "", self.parent)
        self.undo_btn.setStatusTip('Undo the latest change.')
        self.undo_btn.setVisible(True)
        self.undo_btn.triggered.connect(self.parent.editor.undo)

        self.redo_btn = QAction(QIcon(icon_library + "redo.svg"), "", self.parent)
        self.redo_btn.setStatusTip('Redo the latest change.')
        self.redo_btn.setVisible(True)
        self.redo_btn.triggered.connect(self.parent.editor.redo)

        self.copy_btn = QAction(QIcon(icon_library + "copy.svg"), "", self.parent)
        self.copy_btn.setStatusTip('Copy the selected text.')
        self.copy_btn.setVisible(True)
        self.copy_btn.triggered.connect(self.parent.editor.copy)

        self.paste_btn = QAction(QIcon(icon_library + "paste.svg"), "", self.parent)
        self.paste_btn.setStatusTip('Paste the selected text.')
        self.paste_btn.setVisible(True)
        self.paste_btn.triggered.connect(self.parent.editor.paste)

        self.cut_btn = QAction(QIcon(icon_library + "cut.svg"), "", self.parent)
        self.cut_btn.setStatusTip('Cut the selected text.')
        self.cut_btn.setVisible(True)
        self.cut_btn.triggered.connect(self.parent.editor.cut)

        self.bold_btn = QAction(QIcon(icon_library + "bold.svg"), "", self.parent)
        self.bold_btn.setStatusTip('Make the selected text bold.')
        self.bold_btn.triggered.connect(self.parent.text_bold)

        self.italic_btn = QAction(QIcon(icon_library + "italic.svg"), "", self.parent)
        self.italic_btn.setStatusTip('Italicize the selected text.')
        self.italic_btn.triggered.connect(self.parent.text_italic)

        self.underline_btn = QAction(QIcon(icon_library + "underline.svg"), "", self.parent)
        self.underline_btn.setStatusTip('Underline the selected text.')
        self.underline_btn.triggered.connect(self.parent.text_underline)

        self.time_date = QAction(QIcon(icon_library + "time_date.svg"), "", self.parent)
        self.time_date.setStatusTip('Get the current time and date on the text editor.')
        self.time_date.triggered.connect(self.parent.time_func)

        self.find_replace = QAction(QIcon(icon_library + "find_replace.svg"), "", self.parent)
        self.find_replace.setStatusTip('Find and Replace.')
        self.find_replace.triggered.connect(self.parent.find_replace_func)

        self.left_align_btn = QAction(QIcon(icon_library + "left_align.svg"), "", self.parent)
        self.left_align_btn.setStatusTip('Align the text to left.')
        self.left_align_btn.triggered.connect(lambda: self.parent.editor.setAlignment(Qt.AlignLeft))

        self.center_align_btn = QAction(QIcon(icon_library + "center_alignment.svg"), "", self.parent)
        self.center_align_btn.setStatusTip('Align the text to center.')
        self.center_align_btn.triggered.connect(lambda: self.parent.editor.setAlignment(Qt.AlignCenter))

        self.right_align_btn = QAction(QIcon(icon_library + "right_align.svg"), "", self.parent)
        self.right_align_btn.setStatusTip('Align the text to right.')
        self.right_align_btn.triggered.connect(lambda: self.parent.editor.setAlignment(Qt.AlignRight))