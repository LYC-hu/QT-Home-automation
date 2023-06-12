from time import sleep

import curtain
import control_panel_action
import sys
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class curtainaction(curtain.Ui_Form, QMainWindow):
    def __init__(self):
        super(curtain.Ui_Form, self).__init__()
        super().__init__()
        self.setupUi(self)

        self.curtain_1.sliderReleased.connect(self.curtain_1_change) #滑块控制
        self.curtain_1_num.valueChanged.connect(self.num_change)    #数字控制
        self.previous.clicked.connect(self.go_con_panel)


    def curtain_1_change(self):
        self.curtain_1_num.setValue(self.curtain_1.value())
        size = self.curtain_1.value()
        t2 = threading.Thread(target=control_panel_action.Curtain_1_PositionChange(size))
        t2.start()
        t2.join()

    def num_change(self):
        self.curtain_1.setValue(self.curtain_1_num.value())
        digital_num = self.curtain_1.value()
        t2 = threading.Thread(target=control_panel_action.Curtain_1_PositionChange(digital_num))
        t2.start()
        t2.join()

    def go_con_panel(self): #返回前一页
        self.control_panel=control_panel_action.controlpanelactions()
        self.control_panel.show()
        self.close()