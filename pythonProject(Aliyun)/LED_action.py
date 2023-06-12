import LED
import control_panel_action
import sys
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class LEDaction(LED.Ui_Form, QMainWindow):
    def __init__(self):
        super(LED.Ui_Form, self).__init__()
        super().__init__()
        self.setupUi(self)

        self.ON.clicked.connect(self.turn_on)
        self.OFF.clicked.connect(self.turn_off)
        self.previous.clicked.connect(self.go_con_panel)



    def turn_on(self):
        t2 = threading.Thread(target=control_panel_action.LED_On, )
        t2.start()
        t2.join()


    def turn_off(self):
        t2 = threading.Thread(target=control_panel_action.LED_Off, )
        t2.start()
        t2.join()


    def go_con_panel(self): #返回前一页
        self.control_panel=control_panel_action.controlpanelactions()
        self.control_panel.show()
        self.close()