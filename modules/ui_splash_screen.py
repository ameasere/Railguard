# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
from .resources_rc import *
class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(691, 400)
        icon = QIcon()
        icon.addFile(u":/images/railguard.ico", QSize(), QIcon.Normal, QIcon.Off)
        SplashScreen.setWindowIcon(icon)
        SplashScreen.setStyleSheet(u"")
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {	\n"
"	background-color: rgb(0, 9, 31);\n"
"	color: rgb(220, 220, 220);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(0, 90, 661, 61))
        font = QFont()
        font.setFamilies([u"Inter"])
        font.setPointSize(38)
        font.setBold(True)
        font.setItalic(False)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: #aa84f0;\n"
"background-color: transparent;\n"
"font: 600 38pt \"Inter\";\n"
"")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(0, 150, 661, 31))
        font1 = QFont()
        font1.setFamilies([u"Inter"])
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(98, 114, 164);\n"
"background-color: transparent;\n"
"font: 600 14pt \"Inter\";")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(50, 280, 561, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	background-color: #00091f;\n"
"	color: rgb(230, 230, 230);\n"
"	border: none;\n"
"	border-style: none;\n"
"	border-color: #00091f;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"	font: 650 10pt \"Inter\";\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.466, x2:0.858, y2:0.494091, stop:0 rgba(0, 9, 31, 255), stop:0.789773 rgba(112, 87, 158, 255), stop:1 rgba(157, 122, 222, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(0, 320, 671, 21))
        font2 = QFont()
        font2.setFamilies([u"Inter Light"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_loading.setFont(font2)
        self.label_loading.setStyleSheet(u"color: rgb(98, 114, 164);\n"
"background-color: transparent;\n"
"font: 400 10pt \"Inter Light\";")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.selectMap = QPushButton(self.dropShadowFrame)
        self.selectMap.setObjectName(u"selectMap")
        self.selectMap.setGeometry(QRect(290, 350, 91, 25))
        self.selectMap.setMinimumSize(QSize(20, 20))
        self.selectMap.setFont(font2)
        self.selectMap.setCursor(QCursor(Qt.PointingHandCursor))
        self.selectMap.setStyleSheet(u"#selectMap {\n"
"background-color: #aa84f0;\n"
"font: 450 10pt \"Inter Light\";\n"
"}\n"
"#selectMap::pressed {\n"
"background-color: rgb(182, 170, 240);\n"
"font: 450 10pt \"Inter Light\";\n"
"}\n"
"QPushButton {\n"
"	border: 2px solid #aa84f0;\n"
"	color: #fff;\n"
"	border-radius: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(199, 152, 240);\n"
"	color: #fff;\n"
"	border: rgb(199, 152, 240);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(182, 170, 240);\n"
"	color: #fff;\n"
"	border: rgb(182, 170, 240);\n"
"}")
        self.selectMap.setFlat(False)
        self.label_title_2 = QLabel(self.dropShadowFrame)
        self.label_title_2.setObjectName(u"label_title_2")
        self.label_title_2.setGeometry(QRect(0, 310, 671, 71))
        self.label_title_2.setFont(font)
        self.label_title_2.setStyleSheet(u"background-color: qlineargradient(spread:reflect, x1:0.501, y1:0, x2:0.516455, y2:1, stop:0.340909 rgba(0, 9, 31, 255), stop:1 rgba(77, 77, 113, 255));\n"
"")
        self.label_title_2.setAlignment(Qt.AlignCenter)
        self.label_title_2.raise_()
        self.label_title.raise_()
        self.label_description.raise_()
        self.progressBar.raise_()
        self.label_loading.raise_()
        self.selectMap.raise_()

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"Railguard", None))
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p>Railguard</p></body></html>", None))
        self.label_description.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p>SUPERVISED SIGNALLING</p></body></html>", None))
        self.label_loading.setText(QCoreApplication.translate("SplashScreen", u"Loading...", None))
        self.selectMap.setText(QCoreApplication.translate("SplashScreen", u"Exit", None))
        self.label_title_2.setText(QCoreApplication.translate("SplashScreen", u"<html><head/><body><p><br/></p></body></html>", None))
    # retranslateUi

