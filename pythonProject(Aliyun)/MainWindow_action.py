import sys
import ast
import json
import login
import register
import untitled
import control_panel_action
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QMessageBox
from PyQt5 import QtWidgets
import threading
#元组存放用户登录名、密码
login_user = {"LYC": "123"}

#此函数用于读取文件到元组中
def txt_read(files):
    txt_dict = {}
    fopen = open(files)
    for line in fopen.readlines():
        line = str(line).replace("\n", "")  # 注意，必须是双引号，找了大半个小时，发现是这个问题
        # split（）函数用法，逗号前面是以什么来分割，后面是分割成n+1个部分，且以数组形式从0开始
        txt_dict[line.split(' ', 1)[0]] = line.split(' ', 1)[1]

    fopen.close()
    return txt_dict

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

#注册页面
class Main_register(register.Ui_Form,QWidget):
    def __init__(self):
        super(Main_register,self).__init__()
        self.setupUi(self)
        # self.login = Main_login()
        self.Register_sure.clicked.connect(self.Sign_in)
        self.Return.clicked.connect(self.Goto_Login)
    def Sign_in(self):
        Username = self.NewUsername.text()
        Passwd = self.NewPasswd.text()
        Passwd_sure = self.NewPasswd_2.text()
        if Username == "" or Passwd_sure == "" or Passwd == "" or Passwd_sure != Passwd or len(Username.split(' ')) > 1:
            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '所填信息不规范或不完整或两次密码输入错误!')
            msg_box.exec_()
        else:

            with open("login.txt","a+") as f:
               f.write(Username+" "+Passwd+"\n")
            msg_box = QMessageBox(QMessageBox.Warning, "注册提示", "尊贵的用户，您已注册成功！")
            msg_box.exec_()
    def Goto_Login(self):
        self.login = Main_login()
        self.login.show()
        self.close()


#登录界面
class Main_login(QWidget,login.Ui_Form):
    def __init__(self):
        super(Main_login, self).__init__()
        self.setupUi(self)
        self.main = MainWindowaction()
        self.Res = Main_register()
        self.login.clicked.connect(self.confirm)
        self.register_2.clicked.connect(self.Register)



    def confirm(self):
        flag = 0
        # print(self.Ufilename.text())
        Username = self.Ufilename.text()
        # print(self.Passwd.text())
        Passwd = self.Passwd.text()

       #将login.txt记录的注册用户信息读到元组中
        login_user = txt_read('login.txt')
        #判断是否在注册信息字典中
        if Username in login_user.keys():
            if login_user[Username] == Passwd:
                    flag =1
        if flag:#flag为1账号密码正确，进入主窗口
            # main = MainWindowaction()#实例化主窗口函数
            self.main.show()#打开新窗口
            # self.hide()#关闭当前登录窗口
        else :
            msg_box = QMessageBox(QMessageBox.Warning, 'Warning', '账户名或密码错误!')
            msg_box.exec_()
    def Register(self):
        self.Res.show()#打开注册界面
        self.close()






if __name__ == '__main__':

    app = QApplication(sys.argv)

    # demo_window = MainWindowaction()

    # demo_window.show()
    login_window = Main_login()
    login_window.show()

    sys.exit(app.exec_())
