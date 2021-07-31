dark_menu = """
        QMenu {
            background-color: #242323;   
            border: 1px solid black;
            margin: 2px;
        }
        QMenu::item:selected { 
            background-color: #404040;
            color: #e8e3e3;
        }
        QMenu::separator {
            height: 2px;
            background: #7d7878;
            margin-left: 10px;
            margin-right: 5px;
        }
        """

light_menu = """
        QMenu {
            background-color: #ffffff;   
            border: 1px solid black;
            margin: 2px;
        }
        QMenu::item:selected { 
            background-color: #bab6b6;
            color: #212121;
        }
        QMenu::item:hover{
            background-color: #ffffff
        }
        QMenu::separator {
            height: 2px;
            background: #2b2929;
            margin-left: 10px;
            margin-right: 5px;
        }
        """

dark_mode_css_main = """
        background-color: #212121; 
        color: #ffffff;
        QTextEdit{
            background-color: #212121;
        }
        """

light_mode_css_main = """
        background-color: #ffffff; 
        color: #000000;
        """

dark_menubar_css = """
        QMenuBar {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #292828, stop:1 #292828);
            spacing: 3px; /* spacing between menu bar items */
        }
        
        QMenuBar::item {
            padding: 1px 4px;
            border-radius: 4px;
        }
        
        QMenuBar::item:selected {
            background: #292828;
        }
        
        QMenuBar::item:pressed {
            background: #515151;
        }
        """

light_menubar_css = """
        QMenuBar {
            background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                              stop:0 #ffffff, stop:1 #ffffff);
            spacing: 3px; /* spacing between menu bar items */
        }
        
        QMenuBar::item {
            padding: 1px 4px;
            border-radius: 4px;
        }
        
        QMenuBar::item:selected {
            background: #ffffff;
        }
        
        QMenuBar::item:pressed {
            background: #ccc8c8;
        }
        """