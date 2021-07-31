import re
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit, QLabel, QCheckBox, QGridLayout, QWidget, QVBoxLayout, \
    QHBoxLayout


class Find_Replace(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.parent = parent
        self.last_match = None

        self.find_button = QPushButton("Find", self)
        self.find_button.clicked.connect(self.find)

        self.replace_button = QPushButton("Replace", self)
        self.replace_button.clicked.connect(self.replace)

        self.all_button = QPushButton("Replace all", self)
        self.all_button.clicked.connect(self.replace_all)

        self.find_field = QLineEdit(self)
        self.find_field.resize(250, 50)

        self.replace_field = QLineEdit(self)
        self.replace_field.resize(250, 50)

        self.find_text = QLabel('Find what: ', self)

        self.replace_text = QLabel('Replace with: ', self)

        options_label = QLabel("Options: ", self)

        self.case_sens = QCheckBox("Case sensitive", self)
        self.whole_words = QCheckBox("Whole words", self)

        self.main_layout = QVBoxLayout()

        self.find_layout_left = QHBoxLayout()
        self.find_layout_left.addWidget(self.find_text)
        self.find_layout_left.addWidget(self.find_field)

        self.replace_layout_left = QHBoxLayout()
        self.replace_layout_left.addWidget(self.replace_text)
        self.replace_layout_left.addWidget(self.replace_field)

        self.left_ver_layout = QVBoxLayout()
        self.left_ver_layout.addLayout(self.find_layout_left)
        self.left_ver_layout.addLayout(self.replace_layout_left)

        self.right_ver_layout = QVBoxLayout()
        self.right_ver_layout.addWidget(self.find_button)
        self.right_ver_layout.addWidget(self.replace_button)
        self.right_ver_layout.addWidget(self.all_button)

        self.top_hor_layout = QHBoxLayout()
        self.top_hor_layout.addLayout(self.left_ver_layout)
        self.top_hor_layout.addLayout(self.right_ver_layout)

        self.bottom_hor_layout = QHBoxLayout()
        self.bottom_hor_layout.addWidget(options_label)
        self.bottom_hor_layout.addWidget(self.whole_words)
        self.bottom_hor_layout.addWidget(self.case_sens)

        self.main_layout.addLayout(self.top_hor_layout)
        self.main_layout.addLayout(self.bottom_hor_layout)

        self.setWindowTitle("Find & Replace")
        self.setLayout(self.main_layout)

    def find(self):
        text = self.parent.editor.toPlainText()
        query = self.find_field.text()

        # If the 'Whole Words' checkbox is checked, we need to append
        # and prepend a non-alphanumeric character
        if self.whole_words.isChecked():
            query = r'\W' + query + r'\W'

        flags = 0 if self.case_sens.isChecked() else re.I
        pattern = re.compile(query, flags)

        start = self.last_match.start() + 1 if self.last_match else 0
        self.last_match = pattern.search(text, start)

        if self.last_match:
            start = self.last_match.start()
            end = self.last_match.end()

            if self.whole_words.isChecked():
                start += 1
                end -= 1

            self.move_cursor(start, end)

        else:
            self.parent.editor.move_cursor(QTextCursor.End)

    def replace(self):
        cursor = self.parent.editor.textCursor()

        if self.last_match and cursor.hasSelection():
            cursor.insertText(self.replace_field.text())
            self.parent.editor.setTextCursor(cursor)

    def replace_all(self):
        self.last_match = None
        self.find()

        while self.last_match:
            self.replace()
            self.find()

    def move_cursor(self, start, end):
        cursor = self.parent.editor.textCursor()
        cursor.setPosition(start)
        cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, end - start)
        self.parent.editor.setTextCursor(cursor)
