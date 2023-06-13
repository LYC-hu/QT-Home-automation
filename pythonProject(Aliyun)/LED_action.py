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

        self.LED1ON.clicked.connect(self.turn_1_on)
        self.LED1OFF.clicked.connect(self.turn_1_off)

        self.LED2ON.clicked.connect(self.turn_2_on)
        self.LED2OFF.clicked.connect(self.turn_2_off)

        self.LED3ON.clicked.connect(self.turn_3_on)
        self.LED3OFF.clicked.connect(self.turn_3_off)

        self.LED4ON.clicked.connect(self.turn_4_on)
        self.LED4OFF.clicked.connect(self.turn_4_off)

        self.previous.clicked.connect(self.go_con_panel)



    def turn_1_on(self):
        t2 = threading.Thread(target=control_panel_action.LED_1_On, )
        t2.start()
        t2.join()


    def turn_1_off(self):
        t2 = threading.Thread(target=control_panel_action.LED_1_Off, )
        t2.start()
        t2.join()

    def turn_2_on(self):
        t2 = threading.Thread(target=control_panel_action.LED_2_On, )
        t2.start()
        t2.join()


    def turn_2_off(self):
        t2 = threading.Thread(target=control_panel_action.LED_2_Off, )
        t2.start()
        t2.join()

    def turn_3_on(self):
        t2 = threading.Thread(target=control_panel_action.LED_3_On, )
        t2.start()
        t2.join()


    def turn_3_off(self):
        t2 = threading.Thread(target=control_panel_action.LED_3_Off, )
        t2.start()
        t2.join()

    def turn_4_on(self):
        t2 = threading.Thread(target=control_panel_action.LED_4_On, )
        t2.start()
        t2.join()


    def turn_4_off(self):
        t2 = threading.Thread(target=control_panel_action.LED_4_Off, )
        t2.start()
        t2.join()

    def go_con_panel(self): #返回前一页
        self.control_panel=control_panel_action.controlpanelactions()
        self.control_panel.show()
        self.close()