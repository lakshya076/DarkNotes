import os
import sys
import time
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import QSize, Qt
import getpass
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QTextEdit, QWidget, QStatusBar, QToolBar, QMessageBox, \
    QFileDialog, QMenuBar, QSplitter
import platform
from markdown import markdown
# file imports
from _css import dark_menu, dark_mode_css_main, light_mode_css_main, light_menu, dark_menubar_css, light_menubar_css
from find_replace_dialog import Find_Replace
from menu_items.filemenu_itemsmd import FileMenu_ItemsMD
from menu_items.editmenu_items import EditMenu_Items
from menu_items.viewmenu_items import ViewMenu_Items
from menu_items.modemenu_items import ModeMenu_Items
from toolbar_items import Toolbar_Items

icon_library = os.getcwd() + '/icons/'


class MarkdownDN(QMainWindow):
    def __init__(self):
        super(MarkdownDN, self).__init__()

        self.dark_mode_css_main = dark_mode_css_main
        self.dark_menu = dark_menu
        self.light_mode_css_main = light_mode_css_main
        self.light_menu = light_menu
        self.dark_menubar_css = dark_menubar_css
        self.light_menubar_css = light_menubar_css

        self.setWindowTitle('Markdown Mode - DarkNotes')
        self.setWindowIcon(QIcon(icon_library + 'dark_notes.png'))
        self.setFont(QFont('Source Code Pro', 14))
        self.setStyleSheet(self.dark_mode_css_main)
        self.setGeometry(200, 200, 1200, 800)

        self.path = None

        layout = QVBoxLayout()

        self.editor = QTextEdit()
        self.editor.textChanged.connect(self.md_html_cont)

        self.webview = QWebEngineView()

        with open('markdown_dn/mode.txt', 'r') as mode_file:
            content = mode_file.readlines()

            try:
                if content[0] == 'dark':
                    with open('markdown_dn/webview_components/webview_defaulthtml.html', 'r') as webview_default_file:
                        default_html = webview_default_file.read()
                        self.webview.setHtml(default_html)
                        webview_default_file.close()

                elif content[0] == 'light':
                    with open('markdown_dn/webview_components/webview_default_light.html',
                              'r') as webview_default_file_light:
                        default_html = webview_default_file_light.read()
                        self.webview.setHtml(default_html)
                        webview_default_file_light.close()

            except:
                with open('markdown_dn/webview_components/webview_defaulthtml.html', 'r') as webview_default_file:
                    default_html = webview_default_file.read()
                    self.webview.setHtml(default_html)
                    webview_default_file.close()

            mode_file.close()

        self.splitter = QSplitter()
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.addWidget(self.editor)
        self.splitter.addWidget(self.webview)

        layout.addWidget(self.splitter)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

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

        with open('markdown_dn/mode.txt', 'r') as mode_file:
            mode = mode_file.readlines()

            try:
                if mode[0] == 'light':
                    self.light_mode()
                else:
                    self.dark_mode()
            except Exception:
                self.dark_mode()

            mode_file.close()

        self.update_title()
        self.toolbar_buttons()

    def md_html_cont(self):
        text = self.editor.toPlainText()
        markdown_text = markdown(text)

        html_layout_white = f'''
                <!DOCTYPE html>
                <html lang="en">
                <style>
                    a:link {{
                        color: #92d0e3
                    }}

                    a:hover {{
                        color: #1aefef
                    }}

                    a:visited {{
                        color: #be57fa
                    }}

                    body {{
                        font-family: 'Operator Mono', 'Source Code Pro', Menlo, Monaco, Consolas, Courier New, monospace;
                        font-size: 18px;
                    }}

                    div{{
                        word-wrap: break-word;
                    }}
                </style>
                <body>
                    <div class="markdown">
                        {markdown_text}
                    </div>
                </body>
                </html>
                '''

        html_layout_dark = f'''
                <!DOCTYPE html>
                <html lang="en">
                <style>
                    a:link {{
                        color: #92d0e3
                    }}

                    a:hover {{
                        color: #1aefef
                    }}

                    a:visited {{
                        color: #be57fa
                    }}

                    body {{
                        background-color: #292929;
                        color: #ffffff;
                        font-family: 'Operator Mono', 'Source Code Pro', Menlo, Monaco, Consolas, Courier New, monospace;
                        font-size: 18px;
                    }}

                    div{{
                        word-wrap: break-word;
                    }}
                </style>
                <body>
                    <div class="markdown">
                        {markdown_text}
                    </div>
                </body>
                </html>
                '''

        user = getpass.getuser()
        dir_path = f'C:/Users/{user}/appdata/Roaming/DarkNotesMarkdown'
        file_path = f'C:\\Users\\{user}\\appdata\\Roaming\\DarkNotesMarkdown\\mdtemp.html'

        try:
            os.mkdir(dir_path)

            with open(file_path, 'w') as md_file:
                with open('markdown_dn\\mode.txt', 'r') as mode_file:
                    content = mode_file.readlines()
                    try:
                        if content[0] == 'dark':
                            md_file.write(html_layout_dark)
                            md_file.close()
                        elif content[0] == 'light':
                            md_file.write(html_layout_white)
                            md_file.close()

                    except:
                        md_file.write(html_layout_dark)
                        md_file.close()

                    mode_file.close()

            with open(file_path, 'r') as md2html_file:
                file_read = md2html_file.read()
                self.webview.setHtml(file_read)

        except FileExistsError:
            file_path = f'C:\\Users\\{user}\\appdata\\Roaming\\DarkNotesMarkdown\\mdtemp.html'
            with open(file_path, 'w') as md_file:
                md_file.write(html_layout_dark)
                md_file.close()

            with open(file_path, 'r') as md2html_file:
                file_read = md2html_file.read()
                self.webview.setHtml(file_read)

        except FileNotFoundError:
            os.mkdir(dir_path)

        if text == '':
            with open('markdown_dn/webview_components/webview_defaulthtml.html', 'r') as webview_default_file:
                default_html = webview_default_file.read()
                self.webview.setHtml(default_html)
                webview_default_file.close()

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
        self.file_menu.addAction(FileMenu_ItemsMD(self).new_file_action)
        self.file_menu.addAction(FileMenu_ItemsMD(self).open_file_action)
        self.file_menu.addAction(FileMenu_ItemsMD(self).save_file_action)
        self.file_menu.addAction(FileMenu_ItemsMD(self).saveas_file_action)
        self.file_menu.addAction(FileMenu_ItemsMD(self).print_action)
        self.file_menu.addAction(FileMenu_ItemsMD(self).export)
        self.file_menu.addAction(FileMenu_ItemsMD(self).exit_action)

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

    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def file_new(self):
        new_instance = MarkdownDN()
        new_instance.show()

    def file_open(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                              "Markdown Files (*.md, *.markdown);;HTML Files (*.html, *.htm);; All Files (*.*)")

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
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Markdown File (*.md, *.markdown)")
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
            self.webview.print_(dlg.printer())

    def update_title(self):
        self.setWindowTitle("%s - DarkNotesMarkdown" % (os.path.basename(self.path) if self.path else "Untitled"))

    def light_mode(self):
        self.setStyleSheet(self.light_mode_css_main)
        self.file_menu.setStyleSheet(self.light_menu)
        self.edit_menu.setStyleSheet(self.light_menu)
        self.mode_menu.setStyleSheet(self.light_menu)
        self.view_menu.setStyleSheet(self.light_menu)
        self.menubar.setStyleSheet(self.light_menubar_css)

        with open('markdown_dn/mode.txt', 'w') as mode:
            mode.write('light')
            mode.close()

    def dark_mode(self):
        self.setStyleSheet(self.dark_mode_css_main)
        self.file_menu.setStyleSheet(self.dark_menu)
        self.edit_menu.setStyleSheet(self.dark_menu)
        self.mode_menu.setStyleSheet(self.dark_menu)
        self.view_menu.setStyleSheet(self.dark_menu)
        self.menubar.setStyleSheet(self.dark_menubar_css)

        with open('markdown_dn/mode.txt', 'w') as mode:
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
