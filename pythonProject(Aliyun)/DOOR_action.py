import DOOR
import control_panel_action
import sys
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class DOORaction(DOOR.Ui_Form, QMainWindow):
    def __init__(self):
        super(DOOR.Ui_Form, self).__init__()
        super().__init__()
        self.setupUi(self)

        self.OPEN_FRONT.clicked.connect(self.Front_open)
        self.CLOSE_FRONT.clicked.connect(self.Front_close)

        self.OPEN_FRONT.clicked.connect(self.Back_open)
        self.CLOSE_FRONT.clicked.connect(self.Back_close)

        self.previous.clicked.connect(self.go_con_panel)

    # 门的开关
    def Front_open(self):
        t2 = threading.Thread(target=control_panel_action.Front_Door_Open(), )
        t2.start()
        t2.join()

    def Front_close(self):
        t2 = threading.Thread(target=control_panel_action.Front_Door_Close(), )
        t2.start()
        t2.join()

    def Back_open(self):
        t2 = threading.Thread(target=control_panel_action.Back_Door_Open(), )
        t2.start()
        t2.join()

    def Back_close(self):
        t2 = threading.Thread(target=control_panel_action.Back_Door_Close(), )
        t2.start()
        t2.join()


    def go_con_panel(self): #返回前一页
        self.control_panel=control_panel_action.controlpanelactions()
        self.control_panel.show()
        self.close()