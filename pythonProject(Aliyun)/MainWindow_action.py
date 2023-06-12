import sys
import untitled
import control_panel_action
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5 import QtWidgets
import threading
#主窗口的实现
class MainWindowaction(untitled.Ui_Form, QMainWindow):
    def __init__(self):
        super(untitled.Ui_Form, self).__init__()
        self.setupUi(self)

        self.start.clicked.connect(self.open_btn_clicked)
    def open_btn_clicked(self):
        self.control_panel = control_panel_action.controlpanelactions()
        self.control_panel.show()   #显示控制面板

        global t1    # 建立线程t1：mqtt连接阿里云物联网平台
        t1 = threading.Thread(target=control_panel_action.mqtt_connect_aliyun_iot_platform, )
        t1.start()

        self.close()    #关闭旧窗口

if __name__ == '__main__':

    app = QApplication(sys.argv)

    demo_window = MainWindowaction()

    demo_window.show()

    sys.exit(app.exec_())
