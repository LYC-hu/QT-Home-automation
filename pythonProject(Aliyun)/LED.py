# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LED.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(625, 472)
        self.LED1ON = QtWidgets.QPushButton(Form)
        self.LED1ON.setGeometry(QtCore.QRect(150, 30, 93, 28))
        self.LED1ON.setObjectName("LED1ON")
        self.LED1OFF = QtWidgets.QPushButton(Form)
        self.LED1OFF.setGeometry(QtCore.QRect(240, 30, 93, 28))
        self.LED1OFF.setObjectName("LED1OFF")
        self.previous = QtWidgets.QPushButton(Form)
        self.previous.setGeometry(QtCore.QRect(100, 200, 93, 28))
        self.previous.setObjectName("previous")
        self.LED2ON = QtWidgets.QPushButton(Form)
        self.LED2ON.setGeometry(QtCore.QRect(150, 60, 93, 28))
        self.LED2ON.setObjectName("LED2ON")
        self.LED2OFF = QtWidgets.QPushButton(Form)
        self.LED2OFF.setGeometry(QtCore.QRect(240, 60, 93, 28))
        self.LED2OFF.setObjectName("LED2OFF")
        self.LED3ON = QtWidgets.QPushButton(Form)
        self.LED3ON.setGeometry(QtCore.QRect(150, 90, 93, 28))
        self.LED3ON.setObjectName("LED3ON")
        self.LED3OFF = QtWidgets.QPushButton(Form)
        self.LED3OFF.setGeometry(QtCore.QRect(240, 90, 93, 28))
        self.LED3OFF.setObjectName("LED3OFF")
        self.LED4ON = QtWidgets.QPushButton(Form)
        self.LED4ON.setGeometry(QtCore.QRect(150, 120, 93, 28))
        self.LED4ON.setObjectName("LED4ON")
        self.LED4OFF = QtWidgets.QPushButton(Form)
        self.LED4OFF.setGeometry(QtCore.QRect(240, 120, 93, 28))
        self.LED4OFF.setObjectName("LED4OFF")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 30, 111, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(11, 64, 111, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 101, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 91, 31))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        self.previous.clicked.connect(Form.go_con_panel) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.LED1ON.setText(_translate("Form", "ON"))
        self.LED1OFF.setText(_translate("Form", "OFF"))
        self.previous.setText(_translate("Form", "返回"))
        self.LED2ON.setText(_translate("Form", "ON"))
        self.LED2OFF.setText(_translate("Form", "OFF"))
        self.LED3ON.setText(_translate("Form", "ON"))
        self.LED3OFF.setText(_translate("Form", "OFF"))
        self.LED4ON.setText(_translate("Form", "ON"))
        self.LED4OFF.setText(_translate("Form", "OFF"))
        self.label.setText(_translate("Form", "前排灯LED_1"))
        self.label_2.setText(_translate("Form", "中前排灯LED_2"))
        self.label_3.setText(_translate("Form", "中后排灯LED_3"))
        self.label_4.setText(_translate("Form", "后排灯LED_4"))
