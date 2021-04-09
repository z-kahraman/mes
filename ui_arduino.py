# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'arduino.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QSize(700, 500))
        MainWindow.setMaximumSize(QSize(700, 500))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame {\n"
"	border:none;\n"
"	background-color: rgb(35, 35, 35);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.lbl_durum = QLabel(self.frame)
        self.lbl_durum.setObjectName(u"lbl_durum")
        self.lbl_durum.setGeometry(QRect(10, 20, 681, 81))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(20)
        self.lbl_durum.setFont(font)
        self.lbl_durum.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lbl_durum.setAlignment(Qt.AlignCenter)
        self.list_widget = QListWidget(self.frame)
        self.list_widget.setObjectName(u"list_widget")
        self.list_widget.setGeometry(QRect(10, 110, 681, 381))
        self.list_widget.setStyleSheet(u"QListWidget{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(58, 56, 56);\n"
"}")

        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Arduino ve SQLite", None))
        self.lbl_durum.setText(QCoreApplication.translate("MainWindow", u"INCOMING DATA", None))
    # retranslateUi

