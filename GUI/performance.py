# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'performance.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(574, 434)
        Form.setMinimumSize(QtCore.QSize(574, 434))
        Form.setMaximumSize(QtCore.QSize(574, 434))
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 621, 461))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(-6, 0, 621, 451))
        self.label.setStyleSheet("border-image: url(:/image/background.jpg)")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(200, 120, 161, 51))
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setStyleSheet("background-color: rgba(85, 255, 255, 200);\n"
"font: 75 22pt \"Times New Roman\";\n"
"border-radius: 15px;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 330, 91, 31))
        self.pushButton_6.setStyleSheet(".QPushButton{\n"
"background-color: rgb(202, 87, 242);\n"
"font: 16pt \"Cooper Black\";\n"
"border-radius: 15px;\n"
"color: black; \n"
"border: 2px solid rgb(202, 87, 242);\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"  background-color: rgb(255, 170, 255);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget)
        self.pushButton_7.setGeometry(QtCore.QRect(340, 330, 91, 31))
        self.pushButton_7.setStyleSheet(".QPushButton{\n"
"background-color: rgb(202, 87, 242);\n"
"font: 16pt \"Cooper Black\";\n"
"border-radius: 15px;\n"
"color: black; \n"
"border: 2px solid rgb(202, 87, 242);\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"  background-color: rgb(255, 170, 255);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 180, 444, 116))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setObjectName("layout")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.layout.addWidget(self.label_7, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_9.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.layout.addWidget(self.label_9, 0, QtCore.Qt.AlignRight)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.layout.addWidget(self.label_10, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_2.addLayout(self.layout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setStyleSheet("font: 75 18pt \"Times New Roman\";")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "Performance"))
        self.pushButton_6.setText(_translate("Form", "Menu"))
        self.pushButton_7.setText(_translate("Form", "Details"))
        self.label_7.setText(_translate("Form", "Number of records:"))
        self.label_9.setText(_translate("Form", "Average score:"))
        self.label_10.setText(_translate("Form", "Average time spent:"))
        self.label_12.setText(_translate("Form", "nil"))
        self.label_11.setText(_translate("Form", "nil / 10"))
        self.label_8.setText(_translate("Form", "nil seconds"))
import res_rc
