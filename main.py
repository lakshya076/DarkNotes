import os
import sys
import time
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QTextEdit, QWidget, QStatusBar, QToolBar, QMessageBox, \
    QFileDialog, QApplication, QMenuBar, QHBoxLayout
import platform
# file imports
from _css import dark_menu, dark_mode_css_main, light_mode_css_main, light_menu, dark_menubar_css, light_menubar_css
from find_replace_dialog import Find_Replace
from menu_items.filemenu_items_norm import FileMenu_Items
from menu_items.editmenu_items import EditMenu_Items
from menu_items.viewmenu_items import ViewMenu_Items
from menu_items.modemenu_items import ModeMenu_Items
from toolbar_items import Toolbar_Items
from markdown_ import MarkdownDN

icon_library = os.getcwd() + '/icons/'


class DarkNotes(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(DarkNotes, self).__init__(*args, **kwargs)

        self.setWindowIcon(QIcon(icon_library + 'dark_notes.png'))
        self.setFont(QFont('Calibri', 12))

        self.dark_mode_css_main = dark_mode_css_main
        self.dark_menu = dark_menu
        self.light_mode_css_main = light_mode_css_main
        self.light_menu = light_menu
        self.dark_menubar_css = dark_menubar_css
        self.light_menubar_css = light_menubar_css

        self.setStyleSheet(self.dark_mode_css_main)
        self.setGeometry(100, 100, 1200, 800)

        hbox = QHBoxLayout()
        hbox.setSpacing(1.5)

        self.editor = QTextEdit()
        self.editor.setFont(QFont('Source Code Pro', 12))
        self.editor.installEventFilter(self)

        hbox.addWidget(self.editor)
        layout = QVBoxLayout()
        layout.addLayout(hbox)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.path = None

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        self.toolbar = QToolBar()
        self.toolbar.setMovable(False)
        self.toolbar.setFixedHeight(35)
        self.toolbar.setIconSize(QSize(35, 35))
        self.addToolBar(self.toolbar)

        self.menubar = QMenuBar(self)
        self.menubar.setStyleSheet(self.dark_menubar_css)

        self.file_menu = self.menubar.addMenu("&File")
        self.file_menu.setStyleSheet(self.dark_menu)

        self.edit_menu = self.menubar.addMenu("&Edit")
        self.edit_menu.setStyleSheet(self.dark_menu)

        self.view_menu = self.menubar.addMenu("&View")
        self.view_menu.setStyleSheet(self.dark_menu)

        self.mode_menu = self.menubar.addMenu("&Mode")
        self.mode_menu.setStyleSheet(self.dark_menu)

        self.setMenuBar(self.menubar)
        self.menu_items()

        with open('mode.txt', 'r') as mode_file:
            mode = mode_file.readlines()

            try:
                if mode[0] == 'light':
                    self.light_mode()
                else:
                    self.dark_mode()
            except Exception:
                self.dark_mode()

            mode_file.close()

        self.toolbar_buttons()
        self.update_title()

    def toolbar_buttons(self):
        self.toolbar.addAction(Toolbar_Items(self).save_btn)
        self.toolbar.addAction(Toolbar_Items(self).undo_btn)
        self.toolbar.addAction(Toolbar_Items(self).redo_btn)
        self.toolbar.addAction(Toolbar_Items(self).copy_btn)
        self.toolbar.addAction(Toolbar_Items(self).paste_btn)
        self.toolbar.addAction(Toolbar_Items(self).cut_btn)
        self.toolbar.addAction(Toolbar_Items(self).bold_btn)
        self.toolbar.addAction(Toolbar_Items(self).italic_btn)
        self.toolbar.addAction(Toolbar_Items(self).underline_btn)
        self.toolbar.addAction(Toolbar_Items(self).time_date)
        self.toolbar.addAction(Toolbar_Items(self).find_replace)
        self.toolbar.addAction(Toolbar_Items(self).left_align_btn)
        self.toolbar.addAction(Toolbar_Items(self).center_align_btn)
        self.toolbar.addAction(Toolbar_Items(self).right_align_btn)

    def menu_items(self):
        # FILE MENU
        self.file_menu.addAction(FileMenu_Items(self).new_file_action)
        self.file_menu.addAction(FileMenu_Items(self).open_file_action)
        self.file_menu.addAction(FileMenu_Items(self).save_file_action)
        self.file_menu.addAction(FileMenu_Items(self).saveas_file_action)
        self.file_menu.addAction(FileMenu_Items(self).md_mode_action)
        self.file_menu.addAction(FileMenu_Items(self).print_action)
        self.file_menu.addAction(FileMenu_Items(self).export)
        self.file_menu.addAction(FileMenu_Items(self).exit_action)

        # EDIT MENU
        self.edit_menu.addAction(EditMenu_Items(self).undo_action)
        self.edit_menu.addAction(EditMenu_Items(self).redo_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(EditMenu_Items(self).left_align)
        self.edit_menu.addAction(EditMenu_Items(self).center_align)
        self.edit_menu.addAction(EditMenu_Items(self).right_align)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(EditMenu_Items(self).cut_action)
        self.edit_menu.addAction(EditMenu_Items(self).copy_action)
        self.edit_menu.addAction(EditMenu_Items(self).paste_action)
        self.edit_menu.addAction(EditMenu_Items(self).select_action)
        self.edit_menu.addAction(EditMenu_Items(self).find_replace)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(EditMenu_Items(self).bold_action)
        self.edit_menu.addAction(EditMenu_Items(self).italic_action)
        self.edit_menu.addAction(EditMenu_Items(self).underline_action)

        # VIEW MENU
        self.view_menu.addAction(ViewMenu_Items(self).time_date)
        self.view_menu.addAction(ViewMenu_Items(self).system_specs)
        self.view_menu.addSeparator()
        self.view_menu.addAction(ViewMenu_Items(self).zoom_in)
        self.view_menu.addAction(ViewMenu_Items(self).zoom_out)

        # MODE MENU
        self.mode_menu.addAction(ModeMenu_Items(self).dark_mode_action)
        self.mode_menu.addAction(ModeMenu_Items(self).light_mode_action)

    def md_mode(self):
        md_app = MarkdownDN()
        md_app.show()

    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def file_new(self):
        new_instance = DarkNotes()
        new_instance.show()

    def file_open(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                              "Text documents (*.txt);;All Files (*.*)")

        if path:
            try:
                with open(path, 'rU') as f:
                    text = f.read()

            except Exception as e:
                self.dialog_critical(str(e))

            else:
                self.path = path
                self.editor.setPlainText(text)
                self.update_title()

    def file_save(self):
        if self.path is None:
            return self.file_saveas()

        self._save_to_path(self.path)

    def file_saveas(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Text documents (*.txt)''All Files (*.*)")
        if not path:
            return 1

        self._save_to_path(path)

    def _save_to_path(self, path):
        text = self.editor.toPlainText()
        try:
            with open(path, 'w') as f:
                f.write(text)

        except Exception as e:
            self.dialog_critical(str(e))

        else:
            self.path = path
            self.update_title()

    def file_print(self):
        dlg = QPrintDialog()
        if dlg.exec_():
            self.editor.print_(dlg.printer())

    def update_title(self):
        self.setWindowTitle("%s - DarkNotes" % (os.path.basename(self.path) if self.path else "Untitled"))

    def light_mode(self):
        self.setStyleSheet(self.light_mode_css_main)
        self.file_menu.setStyleSheet(self.light_menu)
        self.edit_menu.setStyleSheet(self.light_menu)
        self.mode_menu.setStyleSheet(self.light_menu)
        self.view_menu.setStyleSheet(self.light_menu)
        self.menubar.setStyleSheet(self.light_menubar_css)

        with open('mode.txt', 'w') as mode:
            mode.write('light')
            mode.close()

    def dark_mode(self):
        self.setStyleSheet(self.dark_mode_css_main)
        self.file_menu.setStyleSheet(self.dark_menu)
        self.edit_menu.setStyleSheet(self.dark_menu)
        self.mode_menu.setStyleSheet(self.dark_menu)
        self.view_menu.setStyleSheet(self.dark_menu)
        self.menubar.setStyleSheet(self.dark_menubar_css)

        with open('mode.txt', 'w') as mode:
            mode.write('dark')
            mode.close()

    def text_bold(self):
        try:
            if self.editor.fontWeight() != QFont.Bold:
                self.editor.setFontWeight(QFont.Bold)
                return
            self.editor.setFontWeight(QFont.Normal)
        except Exception:
            pass

    def text_italic(self):
        text = self.editor.fontItalic()
        self.editor.setFontItalic(not (text))

    def text_underline(self):
        text = self.editor.fontUnderline()
        self.editor.setFontUnderline(not (text))

    def time_func(self):
        textvalue = self.editor.toPlainText()
        td = str(time.asctime())
        self.editor.setText(f'{textvalue}\n{td}')

    def find_replace_func(self):
        __win__ = Find_Replace(self)
        __win__.show()

    def sysinf(self):
        existing = self.editor.toPlainText()
        system = platform.uname()
        sysinfo = str(f"System: {system.system}\n"
                      f"System Name: {system.node}\n"
                      f"Release: {system.release}\n"
                      f"Version: {system.version}\n"
                      f"Machine: {system.machine}\n"
                      f"Processor: {system.processor}")
        self.editor.setText(f'{existing}\n{sysinfo}')

    def export_pdf(self):
        try:
            f_name, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF file (.pdf);;All files()")
            FORMAT = f_name + ".pdf"
            if f_name != '':
                printer = QPrinter(QPrinter.HighResolution)
                printer.setOutputFormat(QPrinter.PdfFormat)
                printer.setOutputFileName(FORMAT)
                self.main.document().print_(printer)
        except Exception:
            pass

    def exit(self):
        sys.exit()

    def closeEvent(self, event):
        if self.path is None:
            text = self.editor.toPlainText()
            if text == '' and self.path is None:
                event.accept()
            else:
                reply = QMessageBox.question(self, 'Save File', 'Do you want to save changes to Untitled?',
                                             QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)

                if reply == QMessageBox.Save:
                    path_file = self.file_save()

                    if path_file == 1:
                        event.ignore()
                    else:
                        event.accept()
                        print('Window closed')

                elif reply == QMessageBox.Discard:
                    event.accept()

                elif reply == QMessageBox.Cancel:
                    event.ignore()

        elif self.path is not None:
            app_text = self.editor.toPlainText()
            with open(self.path, 'r') as file_text:
                var_file_text = file_text.read()

                if app_text == var_file_text:
                    event.accept()
                elif app_text != var_file_text:
                    file_name = self.path.split("/")
                    reply = QMessageBox.question(self, 'Save File',
                                                 f"Do you want to save changes to {str(file_name[-1])}?",
                                                 QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)

                    if reply == QMessageBox.Save:
                        path_file = self.file_save()
                        if path_file == 1:
                            event.ignore()
                        else:
                            event.accept()
                            print('Window closed')

                    elif reply == QMessageBox.Discard:
                        event.accept()

                    elif reply == QMessageBox.Cancel:
                        event.ignore()

                file_text.close()

    def zoom(self, delta):
        if delta < 0:
            self.editor.zoomOut(2)
        elif delta > 0:
            self.editor.zoomIn(2)

    def wheelEvent(self, event):
        if event.modifiers() and Qt.ControlModifier:
            self.zoom(event.angleDelta().y())
        else:
            self.editor.wheelEvent(self, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = DarkNotes()
    win.show()
    sys.exit(app.exec_())
