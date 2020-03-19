rom PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

import os
import sys


class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        QBtn = QDialogButtonBox.submit  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        title = QLabel("Oxygen")
        font = title.font()
        font.setPointSize(20)
        title.setFont(font)

        layout.addWidget(title)

        logo = QLabel()
        logo.setPixmap(QPixmap(os.path.join('Images', 'oxogo.png')))
        layout.addWidget(logo)

        layout.addWidget(QLabel("Version 1.0.0"))
        layout.addWidget(QLabel("Copyright."))

        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)















class SettingsWindow(QDialog):
    def __inita__(self, *args, **kwargs):
        super(SettingsWindow, self).__inita__(*args, **kwargs)

        QBtnz = QDialogzButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonzBox(QBtnz)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        titlez = QLabel("Choose you prefered search engine")
        fontz.setPointSize(20)
        title.setFont(fontz)

        layout.addWidget(title)

        logoz = QLabel()
        logoz.setPixmap(QPixmap(os.path.join("/Users/David/Desktop/O2/Images/", 'oxogo.png')))
        layout.addWidget(logoz)

        layout.addWidget(QLabel("Version 1.0.0"))
        layout.addWidget(QLabel("Copyright."))

        for p in range(0, layout.count()):
            layout.itemAt(p).setAlignment(Qt.AlignHCenter)

        layout.addWidget(self.buttonBox)

        self.setLayout(layout)




































       


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://duckduckgo.com/"))

        self.browser.urlChanged.connect(self.update_urlbar)
        #self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(16, 16))
        self.addToolBar(navtb)

        back_btn = QAction(QIcon(os.path.join('/Users/David/Desktop/O2/Images/', 'arrow-180.png')), "Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        next_btn = QAction(QIcon(os.path.join('/Users/David/Desktop/O2/Images/', 'arrow-000.png')), "Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        reload_btn = QAction(QIcon(os.path.join("/Users/David/Desktop/O2/Images/", 'arrow-circle-315.png')), "Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        home_btn = QAction(QIcon(os.path.join('/Users/David/Desktop/O2/Images/', 'haus.png')), "Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        navtb.addSeparator()

        self.httpsicon = QLabel()
        self.httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-nossl.png')))
        navtb.addWidget(self.httpsicon)

        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

       

        li_btn = QAction(QIcon(os.path.join('/Users/David/Desktop/O2/Images/', 'pfpf.png')), "Login to O2", self)
        li_btn.setStatusTip("Login to oygen browser")
        li_btn.triggered.connect(self.navigate_home)
        navtb.addAction(li_btn)




        his_btn = QAction(QIcon(os.path.join('/Users/David/Desktop/O2/Images/', 'klok.png')), "History", self)
        his_btn.setStatusTip("View browsing history")
        his_btn.triggered.connect(self.navigate_home)
        navtb.addAction(his_btn)

        #------------------------------
        file_menu = self.menuBar().addMenu("&File")

        open_file_action = QAction(QIcon(os.path.join('images', 'disk--arrow.png')), "Open file...", self)
        open_file_action.setStatusTip("Open from file")
        open_file_action.triggered.connect(self.open_file)
        file_menu.addAction(open_file_action)

        save_file_action = QAction(QIcon(os.path.join('images', 'disk--pencil.png')), "Save Page As...", self)
        save_file_action.setStatusTip("Save current page to file")
        save_file_action.triggered.connect(self.save_file)
        file_menu.addAction(save_file_action)

        print_action = QAction(QIcon(os.path.join('images', 'printer.png')), "Print...", self)
        print_action.setStatusTip("Print current page")
        print_action.triggered.connect(self.print_page)
        file_menu.addAction(print_action)


        settings_menu = self.menuBar().addMenu("&Settings")
        settings_action = QAction(QIcon(os.path.join('images', 'question.png')),"Choose your default search engine!", self)
        settings_action.setStatusTip("Choose your default search engine.")
        settings_menu.addAction(settings_action)

        #navigate_mozarella_action = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "Choose your default search engine", self)
        #navigate_mozarella_action.setStatusTip("Go to Browser Homepage")
        #navigate_mozarella_action.triggered.connect(self.navigate_mozarella)
        #settings_menu.addAction(navigate_mozarella_action)



        help_menu = self.menuBar().addMenu("&Help")

        about_action = QAction(QIcon(os.path.join('images', 'question.png')), "About Browser", self)
        about_action.setStatusTip("Find out more about Browser")  # Hungry!
        about_action.triggered.connect(self.about)
        help_menu.addAction(about_action)

        navigate_mozarella_action = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "Browser Homepage", self)
        navigate_mozarella_action.setStatusTip("Go to Browser Homepage")
        navigate_mozarella_action.triggered.connect(self.navigate_mozarella)
        help_menu.addAction(navigate_mozarella_action)

        self.show()

        self.setWindowIcon(QIcon(os.path.join( 'oxogo.png')))


        #//////////////////////////////////////

        help_menu = self.menuBar().addMenu("&Email")

        about_action = QAction(QIcon(os.path.join('images', 'question.png')), "About Browser", self)
       

        navigate_mozarella_action = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "Gmail", self)
        navigate_mozarella_action.setStatusTip("Gmail")
        navigate_mozarella_action.triggered.connect(self.navigate_mozarella)
        help_menu.addAction(navigate_mozarella_action)

        self.show()

        navigate_parm_action = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "Yahoo mail", self)
        navigate_parm_action.setStatusTip("Yahoo mail")
        navigate_parm_action.triggered.connect(self.navigate_parm)
        help_menu.addAction(navigate_parm_action)

        self.show()

        self.setWindowIcon(QIcon(os.path.join( 'oxogo.png')))



     

        #///////////////////////////////


        help_menu = self.menuBar().addMenu("&Configure Browser")

        about_action = QAction(QIcon(os.path.join('images', 'question.png')), "About Browser", self)
       

        navigate_mozarella_action = QAction(QIcon(os.path.join('images', 'lifebuoy.png')), "Layout", self)
        navigate_mozarella_action.setStatusTip("Layout")
        navigate_mozarella_action.triggered.connect(self.navigate_mozarella)
        help_menu.addAction(navigate_mozarella_action)

        self.show()

        self.setWindowIcon(QIcon(os.path.join("/Users/David/Desktop/O2/Images/", 'oxogo.png')))




