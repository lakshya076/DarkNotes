from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QAction


class ViewMenu_Items:
    def __init__(self, parent=None):
        self.parent = parent

        self.time_date = QAction(QIcon(), "Date/Time", self.parent)
        self.time_date.setStatusTip("Enter the time and date in editor")
        self.time_date.setShortcut('Alt+T')
        self.time_date.triggered.connect(self.parent.time_func)

        self.system_specs = QAction("PC specs", self.parent)
        self.system_specs.triggered.connect(self.parent.sysinf)
        self.system_specs.setShortcut('Alt+S')

        self.zoom_in = QAction("Zoom In", self.parent)
        self.zoom_in.triggered.connect(lambda: self.parent.editor.zoomIn(2))
        self.zoom_in.setShortcut('Ctrl+=')

        self.zoom_out = QAction("Zoom Out", self.parent)
        self.zoom_out.triggered.connect(lambda: self.parent.editor.zoomOut(2))
        self.zoom_out.setShortcut('Ctrl+-')
