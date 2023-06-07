# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainrgCZLM.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QComboBox, QCommandLinkButton, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QScrollArea, QScrollBar, QSizePolicy, QSlider,
    QStackedWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
from .resources_rc import *
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(734, 413)
        MainWindow.setMinimumSize(QSize(734, 413))
        icon = QIcon()
        icon.addFile(u":/images/ssg+.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Inter Medium"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Inter Medium\";\n"
"}\n"
"#mapSelected {\n"
"	border-top-left-radius: 8px;\n"
"	border-top-right-radius: 8px;\n"
"	border-bottom-left-radius: 8px;\n"
"	border-bottom-right-radius: 8px;\n"
"}\n"
"#predictionOutput {\n"
"	border-top-left-radius: 8px;\n"
"	border-top-right-radius: 8px;\n"
"	border-bottom-left-radius: 8px;\n"
"	border-bottom-right-radius: 8px;\n"
"}\n"
"\n"
"#cpuName {\n"
"	border-top-left-radius: 8px;\n"
"	border-top-right-radius: 8px;\n"
"	border-bottom-left-radius: 8px;\n"
"	border-bottom-right-radius: 8px;\n"
"}\n"
"\n"
"#gpuName {\n"
"	border-top-left-radius: 8px;\n"
"	border-top-right-radius: 8px;\n"
"	border-bottom-left-radius: 8px;\n"
"	border-bottom-right-radius: 8px;\n"
"}\n"
"\n"
"#cudaDetected {\n"
"	border-top-left-radius: 8px;\n"
"	border-top-right-radius: 8px;\n"
"	border-bottom-left-radius: 8px;\n"
"	border-bottom-right-radius: 8px;\n"
"}\n"
"\n"
"#cudnnDetected {\n"
"	border-top-left-radius: 8px;\n"
"	border-top-right-radi"
                        "us: 8px;\n"
"	border-bottom-left-radius: 8px;\n"
"	border-bottom-right-radius: 8px;\n"
"}\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgb(239, 239, 239);\n"
"	border: 1px solid rgb(173, 170, 170);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(173, 170, 170);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {\n"
"	background-color: rgb(239, 239, 239);\n"
"	border: 1px solid rgb(239, 239, 239);\n"
"	border-top-left-radius: 8px;\n"
"	border-top-right-radius: 8px;\n"
"	border-bottom-left-radius: 8px;\n"
"	border-bottom-right-radius: 8px;\n"
"}\n"
"\n"
"/* ////////////////////////////////////////////////////////////////"
                        "/////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {\n"
"	background-color: rgb(184, 184, 184);\n"
"}\n"
"#titleLeftApp { font: 81 12pt \"Inter Medium\"; }\n"
"#titleLeftDescription { font: 8pt \"Inter Medium\"; color: #db63ff; }\n"
"\n"
"#topMenu .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"\n"
"#bottomMenu .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(35,35,38);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {\n"
"	background-color: #aa63ff;\n"
"	color: #fff;\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: solid qlineargradient(spread:pad, x1:1, y1"
                        ":0.477, x2:0, y2:0.494, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: #23242a;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:pressed { \n"
"	background-color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {\n"
"	background-color: rgb(184, 184, 184);\n"
"}\n"
"#extraTopBg {\n"
"	background-color: rgb(184, 184, 184);\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel"
                        " { color: #db63ff; }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(35,35,38); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: #db63ff; border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid qlineargradient(spread:pad, x1:1, y1:0.477, x2:0, y2:0.494, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(35,35,38);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {\n"
"	background-color: #db63ff;\n"
"	"
                        "color: #fff;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{\n"
"	background-color: rgb(184, 184, 184);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: #db63ff; border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(239, 239, 239); }\n"
"#themeSettingsTopDetail { background-color: #db63ff; }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { \n"
"background-color: rgb(184, 184, 184); }\n"
"#bottomBar QLabel "
                        "{ font-size: 11px; padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(35,35,38);\n"
"}\n"
"#contentSettings .QPushButton:pressed {\n"
"	background-color: #db63ff;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(35,35,38);\n"
"	border-bottom: 1px solid qlineargradient(spread:pad, x1:1, y1:0.477, x2:0, y2:0.494, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
""
                        "QTableWidget::item{\n"
"	border-color: qlineargradient(spread:pad, x1:1, y1:0.477, x2:0, y2:0.494, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(35,35,38);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: #db63ff;\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(35,35,38);\n"
"	max-width: 30px;\n"
"	border: 1px solid qlineargradient(spread:pad, x1:1, y1:0.477, x2:0, y2:0.494, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"	border-style: none;\n"
"    border-bottom: 1px solid qlineargradient(spread:pad, x1:1, y1:0.477, x2:0, y2:0.494, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"    border-right: 1px solid qlineargradient(spread:pad, x1:1, y1:0.477, x2:0, y2:0.494, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"QTableWidget::horizontalHeader {\n"
"	background-color: rgb(35,35,38);\n"
"}\n"
"QHeaderView::section:horizonta"
                        "l\n"
"{\n"
"    border: 1px solid qlineargradient(spread:pad, x1:1, y1:0.477, x2:0, y2:0.494, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"	background-color: rgb(35,35,38);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid qlineargradient(spread:pad, x1:1, y1:0.477, x2:0, y2:0.494, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(35,35,38);\n"
"	border-radius: 5px;\n"
"	border: 2px solid qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: #db63ff;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88)"
                        ";\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(0,94,217);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:ho"
                        "rizontal {\n"
"    background: #db63ff;\n"
"    min-width: 25px;\n"
"	border-radius: 4px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" Q"
                        "ScrollBar::handle:vertical {\n"
"	background: #db63ff;\n"
"    min-height: 25px;\n"
"	border-radius: 4px;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
""
                        "    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	borde"
                        "r: 3px solid qlineargradient(spread:pad, x1:1, y1:0.477, x2:0, y2:0.494, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid qlineargradient(spread:pad, x1:1, y1:0.477, x2:0, y2:0.494, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px;\n"
"	border-left-width: 3px;\n"
"	border-left-color: qlineargradient(spread:pad, x1:1, y1:0.477, x2:0, y2:0.494, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;\n"
"	backg"
                        "round-image: url(:/icons/images/icons/arrow-down_hover.png);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: #db63ff;\n"
"	background-color: rgb(35,35,38);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: #db63ff;\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: #db63ff;\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: #db63ff;\n"
"}\n"
"\n"
"QSlide"
                        "r::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: #aa63ff;\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: #db63ff;\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: #db63ff;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {\n"
"	color: #db63ff;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {\n"
"	color: #fff;\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {\n"
"	color: #aa63ff;\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////"
                        "////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"#pagesContainer QPushButton:pressed {\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}")
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setGeometry(QRect(10, 10, 721, 401))
        self.bgApp.setMinimumSize(QSize(721, 401))
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo_2 = QFrame(self.leftMenuFrame)
        self.topLogoInfo_2.setObjectName(u"topLogoInfo_2")
        self.topLogoInfo_2.setMinimumSize(QSize(0, 50))
        self.topLogoInfo_2.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo_2.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo_2.setFrameShadow(QFrame.Raised)
        self.topLogo_2 = QFrame(self.topLogoInfo_2)
        self.topLogo_2.setObjectName(u"topLogo_2")
        self.topLogo_2.setGeometry(QRect(10, 10, 42, 31))
        self.topLogo_2.setMinimumSize(QSize(41, 21))
        self.topLogo_2.setMaximumSize(QSize(1000, 1000))
        self.topLogo_2.setStyleSheet(u"")
        self.topLogo_2.setFrameShape(QFrame.NoFrame)
        self.topLogo_2.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogo_2)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(0, 0, 42, 31))
        self.topLogo.setMinimumSize(QSize(41, 21))
        self.topLogo.setMaximumSize(QSize(1000, 1000))
        self.topLogo.setSizeIncrement(QSize(0, 0))
        self.topLogo.setAutoFillBackground(False)
        self.topLogo.setStyleSheet(u"")
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.ssglabel = QLabel(self.topLogo)
        self.ssglabel.setObjectName(u"ssglabel")
        self.ssglabel.setGeometry(QRect(0, 5, 41, 21))
        self.ssglabel.setStyleSheet(u"")
        self.ssglabel.setPixmap(QPixmap(u":/images/ssg+.png"))
        self.ssglabel.setScaledContents(True)
        self.titleLeftApp = QLabel(self.topLogoInfo_2)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Inter Medium"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo_2)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Raleway Medium"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setStyleSheet(u"font: 57 10pt \"Raleway Medium\";")
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalMenuLayout.addWidget(self.topLogoInfo_2)

        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setStyleSheet(u"#toggleButton {\n"
"	background-color: rgb(184, 184, 184);\n"
"	background-image: url(:/icons/images/icons/menu_unhover.png);\n"
"}\n"
"#toggleButton::hover {\n"
"	background-color: rgb(184, 184, 184);\n"
"	background-image: url(:/icons/images/icons/menu_hover.png);\n"
"}\n"
"#toggleButton::pressed {\n"
"	background-color: rgb(50, 50, 50);\n"
"	background-image: url(:/icons/images/icons/menu_hover.png);\n"
"}")
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 50))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setMinimumSize(QSize(0, 250))
        self.topMenu.setStyleSheet(u"#btn_home {\n"
"	background-image: url(:/icons/images/icons/home_unhover.png);\n"
"}\n"
"#btn_home::hover {\n"
"	background-image: url(:/icons/images/icons/home_hover.png);\n"
"}\n"
"#btn_home::pressed {\n"
"	background-color: rgb(50, 50, 50);\n"
"	background-image: url(:/icons/images/icons/home_hover.png);\n"
"}\n"
"")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setAutoFillBackground(False)
        self.btn_home.setStyleSheet(u"")
        self.btn_home.setFlat(True)

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_page2 = QPushButton(self.topMenu)
        self.btn_page2.setObjectName(u"btn_page2")
        sizePolicy.setHeightForWidth(self.btn_page2.sizePolicy().hasHeightForWidth())
        self.btn_page2.setSizePolicy(sizePolicy)
        self.btn_page2.setMinimumSize(QSize(0, 45))
        self.btn_page2.setFont(font)
        self.btn_page2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page2.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_8.addWidget(self.btn_page2)

        self.btn_page3 = QPushButton(self.topMenu)
        self.btn_page3.setObjectName(u"btn_page3")
        sizePolicy.setHeightForWidth(self.btn_page3.sizePolicy().hasHeightForWidth())
        self.btn_page3.setSizePolicy(sizePolicy)
        self.btn_page3.setMinimumSize(QSize(0, 45))
        self.btn_page3.setFont(font)
        self.btn_page3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page3.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_8.addWidget(self.btn_page3)

        self.btn_page4 = QPushButton(self.topMenu)
        self.btn_page4.setObjectName(u"btn_page4")
        sizePolicy.setHeightForWidth(self.btn_page4.sizePolicy().hasHeightForWidth())
        self.btn_page4.setSizePolicy(sizePolicy)
        self.btn_page4.setMinimumSize(QSize(0, 45))
        self.btn_page4.setFont(font)
        self.btn_page4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page4.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_8.addWidget(self.btn_page4)

        self.btn_page5 = QPushButton(self.topMenu)
        self.btn_page5.setObjectName(u"btn_page5")
        sizePolicy.setHeightForWidth(self.btn_page5.sizePolicy().hasHeightForWidth())
        self.btn_page5.setSizePolicy(sizePolicy)
        self.btn_page5.setMinimumSize(QSize(0, 45))
        self.btn_page5.setFont(font)
        self.btn_page5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_page5.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_8.addWidget(self.btn_page5)


        self.verticalMenuLayout.addWidget(self.topMenu)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setStyleSheet(u"#toggleLeftBox {\n"
"	background-color: rgb(184, 184, 184);\n"
"	background-image: url(:/icons/images/icons/chevrons-right_unhover.png);\n"
"}\n"
"#toggleLeftBox::hover {\n"
"	background-color: rgb(184, 184, 184);\n"
"	background-image: url(:/icons/images/icons/chevrons-right_hover.png);\n"
"}\n"
"#toggleLeftBox::pressed {\n"
"	background-color: rgb(50, 50, 50);\n"
"	background-image: url(:/icons/images/icons/chevrons-right_hover.png);\n"
"}\n"
"")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.toggleLeftBox = QPushButton(self.bottomMenu)
        self.toggleLeftBox.setObjectName(u"toggleLeftBox")
        sizePolicy.setHeightForWidth(self.toggleLeftBox.sizePolicy().hasHeightForWidth())
        self.toggleLeftBox.setSizePolicy(sizePolicy)
        self.toggleLeftBox.setMinimumSize(QSize(0, 45))
        self.toggleLeftBox.setFont(font)
        self.toggleLeftBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleLeftBox.setLayoutDirection(Qt.LeftToRight)
        self.toggleLeftBox.setStyleSheet(u"")

        self.verticalLayout_9.addWidget(self.toggleLeftBox)


        self.verticalMenuLayout.addWidget(self.bottomMenu)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.extraLeftBox = QFrame(self.bgApp)
        self.extraLeftBox.setObjectName(u"extraLeftBox")
        self.extraLeftBox.setMinimumSize(QSize(0, 0))
        self.extraLeftBox.setMaximumSize(QSize(0, 16777215))
        self.extraLeftBox.setFrameShape(QFrame.NoFrame)
        self.extraLeftBox.setFrameShadow(QFrame.Raised)
        self.extraColumLayout = QVBoxLayout(self.extraLeftBox)
        self.extraColumLayout.setSpacing(0)
        self.extraColumLayout.setObjectName(u"extraColumLayout")
        self.extraColumLayout.setContentsMargins(0, 0, 0, 0)
        self.extraTopBg = QFrame(self.extraLeftBox)
        self.extraTopBg.setObjectName(u"extraTopBg")
        self.extraTopBg.setMinimumSize(QSize(0, 50))
        self.extraTopBg.setMaximumSize(QSize(16777215, 50))
        self.extraTopBg.setFrameShape(QFrame.NoFrame)
        self.extraTopBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.extraTopBg)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.extraTopLayout = QGridLayout()
        self.extraTopLayout.setObjectName(u"extraTopLayout")
        self.extraTopLayout.setHorizontalSpacing(10)
        self.extraTopLayout.setVerticalSpacing(0)
        self.extraTopLayout.setContentsMargins(10, -1, 10, -1)
        self.extraIcon = QFrame(self.extraTopBg)
        self.extraIcon.setObjectName(u"extraIcon")
        self.extraIcon.setMinimumSize(QSize(20, 0))
        self.extraIcon.setMaximumSize(QSize(20, 20))
        self.extraIcon.setStyleSheet(u"")
        self.extraIcon.setFrameShape(QFrame.NoFrame)
        self.extraIcon.setFrameShadow(QFrame.Raised)

        self.extraTopLayout.addWidget(self.extraIcon, 0, 0, 1, 1)

        self.extraLabel = QLabel(self.extraTopBg)
        self.extraLabel.setObjectName(u"extraLabel")
        self.extraLabel.setMinimumSize(QSize(150, 0))

        self.extraTopLayout.addWidget(self.extraLabel, 0, 1, 1, 1)

        self.extraCloseColumnBtn = QPushButton(self.extraTopBg)
        self.extraCloseColumnBtn.setObjectName(u"extraCloseColumnBtn")
        self.extraCloseColumnBtn.setMinimumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setMaximumSize(QSize(28, 28))
        self.extraCloseColumnBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.extraCloseColumnBtn.setIcon(icon1)
        self.extraCloseColumnBtn.setIconSize(QSize(20, 20))

        self.extraTopLayout.addWidget(self.extraCloseColumnBtn, 0, 2, 1, 1)


        self.verticalLayout_5.addLayout(self.extraTopLayout)


        self.extraColumLayout.addWidget(self.extraTopBg)

        self.extraContent = QFrame(self.extraLeftBox)
        self.extraContent.setObjectName(u"extraContent")
        self.extraContent.setFrameShape(QFrame.NoFrame)
        self.extraContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.extraContent)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.extraTopMenu = QFrame(self.extraContent)
        self.extraTopMenu.setObjectName(u"extraTopMenu")
        self.extraTopMenu.setFrameShape(QFrame.NoFrame)
        self.extraTopMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.extraTopMenu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.extraTopMenu)
        self.btn_share.setObjectName(u"btn_share")
        sizePolicy.setHeightForWidth(self.btn_share.sizePolicy().hasHeightForWidth())
        self.btn_share.setSizePolicy(sizePolicy)
        self.btn_share.setMinimumSize(QSize(0, 45))
        self.btn_share.setFont(font)
        self.btn_share.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_share.setLayoutDirection(Qt.LeftToRight)
        self.btn_share.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.btn_share)

        self.btn_credits = QPushButton(self.extraTopMenu)
        self.btn_credits.setObjectName(u"btn_credits")
        sizePolicy.setHeightForWidth(self.btn_credits.sizePolicy().hasHeightForWidth())
        self.btn_credits.setSizePolicy(sizePolicy)
        self.btn_credits.setMinimumSize(QSize(0, 45))
        self.btn_credits.setFont(font)
        self.btn_credits.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_credits.setLayoutDirection(Qt.LeftToRight)
        self.btn_credits.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.btn_credits)

        self.btn_more = QPushButton(self.extraTopMenu)
        self.btn_more.setObjectName(u"btn_more")
        sizePolicy.setHeightForWidth(self.btn_more.sizePolicy().hasHeightForWidth())
        self.btn_more.setSizePolicy(sizePolicy)
        self.btn_more.setMinimumSize(QSize(0, 45))
        self.btn_more.setFont(font)
        self.btn_more.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_more.setLayoutDirection(Qt.LeftToRight)
        self.btn_more.setStyleSheet(u"")

        self.verticalLayout_11.addWidget(self.btn_more)


        self.verticalLayout_12.addWidget(self.extraTopMenu, 0, Qt.AlignTop)

        self.extraCenter = QFrame(self.extraContent)
        self.extraCenter.setObjectName(u"extraCenter")
        self.extraCenter.setFrameShape(QFrame.NoFrame)
        self.extraCenter.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.extraCenter)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.credits = QTextEdit(self.extraCenter)
        self.credits.setObjectName(u"credits")
        self.credits.setMinimumSize(QSize(222, 0))
        self.credits.setStyleSheet(u"background: transparent;")
        self.credits.setFrameShape(QFrame.NoFrame)
        self.credits.setReadOnly(True)

        self.verticalLayout_10.addWidget(self.credits)


        self.verticalLayout_12.addWidget(self.extraCenter)

        self.extraBottom = QFrame(self.extraContent)
        self.extraBottom.setObjectName(u"extraBottom")
        self.extraBottom.setFrameShape(QFrame.NoFrame)
        self.extraBottom.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.extraBottom)


        self.extraColumLayout.addWidget(self.extraContent)


        self.appLayout.addWidget(self.extraLeftBox)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(659, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setStyleSheet(u"")
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setStyleSheet(u"")
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        self.titleRightInfo.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMinimumSize(QSize(10000, 0))
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font3 = QFont()
        font3.setFamilies([u"Raleway ExtraBold"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        self.titleRightInfo.setFont(font3)
        self.titleRightInfo.setStyleSheet(u"font: 81 10pt \"Raleway ExtraBold\";")
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(127, 50))
        self.rightButtons.setStyleSheet(u"#closeAppBtn {\n"
"background-color: rgb(150, 150, 150);\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"}\n"
"#closeAppBtn::hover {\n"
"background-color: rgb(101, 101, 101);\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"}\n"
"#closeAppBtn::pressed {\n"
"background-color: rgb(50, 50, 50);\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"}\n"
"\n"
"#maximizeRestoreAppBtn {\n"
"background-color: rgb(150, 150, 150);\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"}\n"
"#maximizeRestoreAppBtn::hover {\n"
"background-color: rgb(150, 150, 150);\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radiu"
                        "s: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"}\n"
"#maximizeRestoreAppBtn::pressed {\n"
"background-color: rgb(50, 50, 50);\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"}\n"
"\n"
"#minimizeAppBtn {\n"
"background-color: rgb(150, 150, 150);\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"}\n"
"#minimizeAppBtn::hover {\n"
"background-color: rgb(101, 101, 101);\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"}\n"
"#minimizeAppBtn::pressed {\n"
"background-color: rgb(50, 50, 50);\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"}\n"
"\n"
"#settingsTopBtn {\n"
"background-color: rgb(150, 150, 150);\n"
"border-top-left-radius: 8px;\n"
""
                        "border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"}\n"
"#settingsTopBtn::hover {\n"
"background-color: rgb(101, 101, 101);\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"}\n"
"#settingsTopBtn::pressed {\n"
"background-color: rgb(50, 50, 50);\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"}")
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setGeometry(QRect(15, 10, 28, 28))
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.minimizeAppBtn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon2)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))
        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setGeometry(QRect(49, 10, 28, 28))
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font4 = QFont()
        font4.setFamilies([u"Inter Medium"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font4)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.maximizeRestoreAppBtn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon3)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))
        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setGeometry(QRect(83, 10, 28, 28))
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closeAppBtn.setStyleSheet(u"")
        self.closeAppBtn.setIcon(icon1)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"#home {\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"}\n"
"\n"
"#mapSelected {\n"
"background-color: rgb(245, 245, 245);\n"
"border: 2px solid qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"#predictionOutput {\n"
"background-color: rgb(245, 245, 245);\n"
"border: 2px solid qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"}\n"
"\n"
"#cpuName {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"font: 300 8pt \"Inter Light\";\n"
"}\n"
"\n"
"#gpuName {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"font: 300 8pt \"Inter Light\";\n"
"}\n"
"\n"
"#cudaDetected {\n"
"background-color: qlineargradient(spread:pad,"
                        " x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"font: 300 10pt \"Inter Light\";\n"
"}\n"
"\n"
"#cudnnDetected {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"font: 300 10pt \"Inter Light\";\n"
"}")
        self.dashboardTitle = QLabel(self.home)
        self.dashboardTitle.setObjectName(u"dashboardTitle")
        self.dashboardTitle.setGeometry(QRect(0, 0, 631, 31))
        self.dashboardTitle.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"font: 800 20pt \"Inter\";")
        self.dashboardTitle.setLineWidth(1)
        self.dashboardTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.selectMap = QPushButton(self.home)
        self.selectMap.setObjectName(u"selectMap")
        self.selectMap.setGeometry(QRect(31, 113, 150, 30))
        self.selectMap.setMinimumSize(QSize(150, 30))
        font5 = QFont()
        font5.setFamilies([u"Inter Light"])
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        self.selectMap.setFont(font5)
        self.selectMap.setCursor(QCursor(Qt.PointingHandCursor))
        self.selectMap.setStyleSheet(u"#selectMap {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"font: 300 10pt \"Inter Light\";\n"
"}\n"
"#selectMap::pressed {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 180), stop:1 rgba(170, 85, 255, 180));\n"
"font: 300 10pt \"Inter Light\";\n"
"}")
        self.selectMap.setFlat(False)
        self.labelFrame = QFrame(self.home)
        self.labelFrame.setObjectName(u"labelFrame")
        self.labelFrame.setGeometry(QRect(0, 40, 181, 61))
        self.labelFrame.setStyleSheet(u"#labelFrame {\n"
"border: 2px solid qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"background-color: rgb(245, 245, 245);\n"
"}")
        self.labelFrame.setFrameShape(QFrame.StyledPanel)
        self.labelFrame.setFrameShadow(QFrame.Raised)
        self.statusTitle = QLabel(self.labelFrame)
        self.statusTitle.setObjectName(u"statusTitle")
        self.statusTitle.setGeometry(QRect(10, 10, 61, 16))
        self.statusTitle.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"font: 800 20pt \"Inter Extra Bold\";")
        self.statusTitle.setLineWidth(1)
        self.statusTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.status = QLabel(self.labelFrame)
        self.status.setObjectName(u"status")
        self.status.setGeometry(QRect(70, 10, 61, 16))
        self.status.setStyleSheet(u"color: #ff0000;")
        self.status.setLineWidth(1)
        self.status.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.versionTitle = QLabel(self.labelFrame)
        self.versionTitle.setObjectName(u"versionTitle")
        self.versionTitle.setGeometry(QRect(10, 30, 101, 20))
        self.versionTitle.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"font: 800 20pt \"Inter Extra Bold\";")
        self.versionTitle.setLineWidth(1)
        self.versionTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.modelVersion = QLabel(self.labelFrame)
        self.modelVersion.setObjectName(u"modelVersion")
        self.modelVersion.setGeometry(QRect(110, 30, 61, 16))
        self.modelVersion.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.modelVersion.setLineWidth(1)
        self.modelVersion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.labelFrame_2 = QFrame(self.labelFrame)
        self.labelFrame_2.setObjectName(u"labelFrame_2")
        self.labelFrame_2.setGeometry(QRect(120, 60, 181, 61))
        self.labelFrame_2.setStyleSheet(u"#labelFrame {\n"
"border: 2px solid qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"}")
        self.labelFrame_2.setFrameShape(QFrame.StyledPanel)
        self.labelFrame_2.setFrameShadow(QFrame.Raised)
        self.statusTitle_2 = QLabel(self.labelFrame_2)
        self.statusTitle_2.setObjectName(u"statusTitle_2")
        self.statusTitle_2.setGeometry(QRect(10, 10, 61, 16))
        self.statusTitle_2.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"font: 800 20pt \"Inter Extra Bold\";")
        self.statusTitle_2.setLineWidth(1)
        self.statusTitle_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.status_2 = QLabel(self.labelFrame_2)
        self.status_2.setObjectName(u"status_2")
        self.status_2.setGeometry(QRect(70, 10, 61, 16))
        self.status_2.setStyleSheet(u"")
        self.status_2.setLineWidth(1)
        self.status_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.versionTitle_2 = QLabel(self.labelFrame_2)
        self.versionTitle_2.setObjectName(u"versionTitle_2")
        self.versionTitle_2.setGeometry(QRect(10, 30, 101, 20))
        self.versionTitle_2.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"font: 800 20pt \"Inter Extra Bold\";")
        self.versionTitle_2.setLineWidth(1)
        self.versionTitle_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.modelVersion_2 = QLabel(self.labelFrame_2)
        self.modelVersion_2.setObjectName(u"modelVersion_2")
        self.modelVersion_2.setGeometry(QRect(110, 30, 61, 16))
        self.modelVersion_2.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.modelVersion_2.setLineWidth(1)
        self.modelVersion_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.line = QFrame(self.home)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 100, 16, 31))
        self.line.setStyleSheet(u"color: rgb(170, 99, 255);")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QFrame.VLine)
        self.line_9 = QFrame(self.home)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(0, 240, 16, 21))
        self.line_9.setStyleSheet(u"color: rgb(4, 239, 188)")
        self.line_9.setFrameShadow(QFrame.Plain)
        self.line_9.setLineWidth(5)
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_4 = QFrame(self.home)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setGeometry(QRect(10, 160, 21, 16))
        self.line_4.setStyleSheet(u"color: rgb(170, 99, 255);")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setLineWidth(5)
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_5 = QFrame(self.home)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(0, 200, 16, 41))
        self.line_5.setStyleSheet(u"color: rgb(4, 239, 188)")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setLineWidth(5)
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_2 = QFrame(self.home)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(10, 120, 21, 16))
        self.line_2.setStyleSheet(u"color: rgb(170, 99, 255);")
        self.line_2.setFrameShadow(QFrame.Plain)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_10 = QFrame(self.home)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(10, 250, 21, 16))
        self.line_10.setStyleSheet(u"color: rgb(4, 239, 188)")
        self.line_10.setFrameShadow(QFrame.Plain)
        self.line_10.setLineWidth(5)
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_3 = QFrame(self.home)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(0, 130, 16, 41))
        self.line_3.setStyleSheet(u"color: rgb(170, 99, 255);")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setLineWidth(5)
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_7 = QFrame(self.home)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(0, 171, 16, 30))
        self.line_7.setStyleSheet(u"color: rgb(4, 239, 188)")
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setLineWidth(5)
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_6 = QFrame(self.home)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(10, 210, 21, 16))
        self.line_6.setStyleSheet(u"color: rgb(4, 239, 188)")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setLineWidth(5)
        self.line_6.setFrameShape(QFrame.HLine)
        self.predict = QPushButton(self.home)
        self.predict.setObjectName(u"predict")
        self.predict.setGeometry(QRect(30, 153, 150, 30))
        self.predict.setMinimumSize(QSize(150, 30))
        self.predict.setFont(font5)
        self.predict.setCursor(QCursor(Qt.PointingHandCursor))
        self.predict.setStyleSheet(u"#predict {\n"
"background-color: rgb(184, 184, 184);\n"
"font: 300 10pt \"Inter Light\";\n"
"}")
        self.predict.setFlat(False)
        self.mapSelected = QLabel(self.home)
        self.mapSelected.setObjectName(u"mapSelected")
        self.mapSelected.setGeometry(QRect(30, 208, 151, 21))
        self.mapSelected.setStyleSheet(u"color: #ff0000;\n"
"")
        self.mapSelected.setLineWidth(1)
        self.mapSelected.setAlignment(Qt.AlignCenter)
        self.predictionOutput = QLabel(self.home)
        self.predictionOutput.setObjectName(u"predictionOutput")
        self.predictionOutput.setGeometry(QRect(30, 248, 151, 21))
        self.predictionOutput.setStyleSheet(u"color: #ff0000;")
        self.predictionOutput.setLineWidth(1)
        self.predictionOutput.setAlignment(Qt.AlignCenter)
        self.predictionstdout = QPlainTextEdit(self.home)
        self.predictionstdout.setObjectName(u"predictionstdout")
        self.predictionstdout.setGeometry(QRect(200, 120, 231, 151))
        self.predictionstdout.setMinimumSize(QSize(100, 100))
        self.predictionstdout.setStyleSheet(u"border: 2px solid qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"background-color: rgb(70, 70, 70);\n"
"color: #fff;")
        self.predictionstdout.setReadOnly(True)
        self.predictionOutputTitle = QLabel(self.home)
        self.predictionOutputTitle.setObjectName(u"predictionOutputTitle")
        self.predictionOutputTitle.setGeometry(QRect(200, 100, 121, 20))
        self.predictionOutputTitle.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"font: 800 20pt \"Inter Extra Bold\";")
        self.predictionOutputTitle.setLineWidth(1)
        self.predictionOutputTitle.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.labelFrame_3 = QFrame(self.home)
        self.labelFrame_3.setObjectName(u"labelFrame_3")
        self.labelFrame_3.setGeometry(QRect(450, 40, 181, 61))
        self.labelFrame_3.setStyleSheet(u"#labelFrame_3{\n"
"border: 2px solid qlineargradient(spread:pad, x1:1, y1:0.477, x2:0, y2:0.494, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"background-color: rgb(245, 245, 245);\n"
"}")
        self.labelFrame_3.setFrameShape(QFrame.StyledPanel)
        self.labelFrame_3.setFrameShadow(QFrame.Raised)
        self.statusTitle_3 = QLabel(self.labelFrame_3)
        self.statusTitle_3.setObjectName(u"statusTitle_3")
        self.statusTitle_3.setGeometry(QRect(10, 10, 161, 16))
        self.statusTitle_3.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"font: 800 20pt \"Inter Extra Bold\";")
        self.statusTitle_3.setLineWidth(1)
        self.statusTitle_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.versionTitle_3 = QLabel(self.labelFrame_3)
        self.versionTitle_3.setObjectName(u"versionTitle_3")
        self.versionTitle_3.setGeometry(QRect(10, 30, 101, 20))
        self.versionTitle_3.setStyleSheet(u"color: rgb(170, 85, 255);\n"
"font: 800 20pt \"Inter Extra Bold\";")
        self.versionTitle_3.setLineWidth(1)
        self.versionTitle_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.tensorflowVersion = QLabel(self.labelFrame_3)
        self.tensorflowVersion.setObjectName(u"tensorflowVersion")
        self.tensorflowVersion.setGeometry(QRect(110, 30, 61, 16))
        self.tensorflowVersion.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.tensorflowVersion.setLineWidth(1)
        self.tensorflowVersion.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.labelFrame_4 = QFrame(self.labelFrame_3)
        self.labelFrame_4.setObjectName(u"labelFrame_4")
        self.labelFrame_4.setGeometry(QRect(120, 60, 181, 61))
        self.labelFrame_4.setStyleSheet(u"#labelFrame {\n"
"border: 2px solid qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"border-top-left-radius: 8px;\n"
"border-top-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"border-bottom-right-radius: 8px;\n"
"}")
        self.labelFrame_4.setFrameShape(QFrame.StyledPanel)
        self.labelFrame_4.setFrameShadow(QFrame.Raised)
        self.statusTitle_4 = QLabel(self.labelFrame_4)
        self.statusTitle_4.setObjectName(u"statusTitle_4")
        self.statusTitle_4.setGeometry(QRect(10, 10, 61, 16))
        self.statusTitle_4.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"font: 800 20pt \"Inter Extra Bold\";")
        self.statusTitle_4.setLineWidth(1)
        self.statusTitle_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.status_4 = QLabel(self.labelFrame_4)
        self.status_4.setObjectName(u"status_4")
        self.status_4.setGeometry(QRect(70, 10, 61, 16))
        self.status_4.setStyleSheet(u"")
        self.status_4.setLineWidth(1)
        self.status_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.versionTitle_4 = QLabel(self.labelFrame_4)
        self.versionTitle_4.setObjectName(u"versionTitle_4")
        self.versionTitle_4.setGeometry(QRect(10, 30, 101, 20))
        self.versionTitle_4.setStyleSheet(u"color: rgb(254, 121, 199);\n"
"font: 800 20pt \"Inter Extra Bold\";")
        self.versionTitle_4.setLineWidth(1)
        self.versionTitle_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.modelVersion_4 = QLabel(self.labelFrame_4)
        self.modelVersion_4.setObjectName(u"modelVersion_4")
        self.modelVersion_4.setGeometry(QRect(110, 30, 61, 16))
        self.modelVersion_4.setStyleSheet(u"color: rgb(170, 85, 255);")
        self.modelVersion_4.setLineWidth(1)
        self.modelVersion_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.line_8 = QFrame(self.home)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(100, 340, 21, 16))
        self.line_8.setStyleSheet(u"color: rgb(4, 239, 188)")
        self.line_8.setFrameShadow(QFrame.Plain)
        self.line_8.setLineWidth(5)
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_11 = QFrame(self.home)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setGeometry(QRect(100, 380, 21, 16))
        self.line_11.setStyleSheet(u"color: rgb(4, 239, 188)")
        self.line_11.setFrameShadow(QFrame.Plain)
        self.line_11.setLineWidth(5)
        self.line_11.setFrameShape(QFrame.HLine)
        self.line_14 = QFrame(self.home)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setGeometry(QRect(90, 370, 16, 21))
        self.line_14.setStyleSheet(u"color: rgb(4, 239, 188)")
        self.line_14.setFrameShadow(QFrame.Plain)
        self.line_14.setLineWidth(5)
        self.line_14.setFrameShape(QFrame.VLine)
        self.line_15 = QFrame(self.home)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setGeometry(QRect(90, 330, 16, 41))
        self.line_15.setStyleSheet(u"color: rgb(4, 239, 188)")
        self.line_15.setFrameShadow(QFrame.Plain)
        self.line_15.setLineWidth(5)
        self.line_15.setFrameShape(QFrame.VLine)
        self.line_19 = QFrame(self.home)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setGeometry(QRect(600, 210, 21, 16))
        self.line_19.setStyleSheet(u"color: rgb(4, 239, 188)")
        self.line_19.setFrameShadow(QFrame.Plain)
        self.line_19.setLineWidth(5)
        self.line_19.setFrameShape(QFrame.HLine)
        self.line_20 = QFrame(self.home)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setGeometry(QRect(600, 250, 21, 16))
        self.line_20.setStyleSheet(u"color: rgb(4, 239, 188)")
        self.line_20.setFrameShadow(QFrame.Plain)
        self.line_20.setLineWidth(5)
        self.line_20.setFrameShape(QFrame.HLine)
        self.line_21 = QFrame(self.home)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setGeometry(QRect(610, 130, 16, 41))
        self.line_21.setStyleSheet(u"color: rgb(170, 99, 255);")
        self.line_21.setFrameShadow(QFrame.Plain)
        self.line_21.setLineWidth(5)
        self.line_21.setFrameShape(QFrame.VLine)
        self.line_22 = QFrame(self.home)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setGeometry(QRect(600, 122, 21, 20))
        self.line_22.setStyleSheet(u"color: rgb(170, 99, 255);")
        self.line_22.setFrameShadow(QFrame.Plain)
        self.line_22.setLineWidth(5)
        self.line_22.setFrameShape(QFrame.HLine)
        self.line_23 = QFrame(self.home)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setGeometry(QRect(610, 240, 16, 21))
        self.line_23.setStyleSheet(u"color: rgb(4, 239, 188)")
        self.line_23.setFrameShadow(QFrame.Plain)
        self.line_23.setLineWidth(5)
        self.line_23.setFrameShape(QFrame.VLine)
        self.line_24 = QFrame(self.home)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setGeometry(QRect(610, 200, 16, 41))
        self.line_24.setStyleSheet(u"color: rgb(4, 239, 188)")
        self.line_24.setFrameShadow(QFrame.Plain)
        self.line_24.setLineWidth(5)
        self.line_24.setFrameShape(QFrame.VLine)
        self.line_25 = QFrame(self.home)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setGeometry(QRect(610, 100, 16, 31))
        self.line_25.setStyleSheet(u"color: rgb(170, 99, 255);")
        self.line_25.setFrameShadow(QFrame.Plain)
        self.line_25.setLineWidth(5)
        self.line_25.setFrameShape(QFrame.VLine)
        self.line_26 = QFrame(self.home)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setGeometry(QRect(610, 171, 16, 30))
        self.line_26.setStyleSheet(u"color: rgb(4, 239, 188)")
        self.line_26.setFrameShadow(QFrame.Plain)
        self.line_26.setLineWidth(5)
        self.line_26.setFrameShape(QFrame.VLine)
        self.line_27 = QFrame(self.home)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setGeometry(QRect(600, 163, 21, 21))
        self.line_27.setStyleSheet(u"color: rgb(170, 99, 255);")
        self.line_27.setFrameShadow(QFrame.Plain)
        self.line_27.setLineWidth(5)
        self.line_27.setFrameShape(QFrame.HLine)
        self.cpuName = QLabel(self.home)
        self.cpuName.setObjectName(u"cpuName")
        self.cpuName.setGeometry(QRect(450, 118, 151, 31))
        self.cpuName.setStyleSheet(u"color: #fff;\n"
"")
        self.cpuName.setLineWidth(1)
        self.cpuName.setAlignment(Qt.AlignCenter)
        self.cpuName.setWordWrap(True)
        self.gpuName = QLabel(self.home)
        self.gpuName.setObjectName(u"gpuName")
        self.gpuName.setGeometry(QRect(450, 158, 151, 31))
        self.gpuName.setStyleSheet(u"color: #fff;\n"
"")
        self.gpuName.setLineWidth(1)
        self.gpuName.setAlignment(Qt.AlignCenter)
        self.gpuName.setWordWrap(True)
        self.cudaDetected = QLabel(self.home)
        self.cudaDetected.setObjectName(u"cudaDetected")
        self.cudaDetected.setGeometry(QRect(450, 208, 151, 21))
        self.cudaDetected.setStyleSheet(u"color: #fff;\n"
"")
        self.cudaDetected.setLineWidth(1)
        self.cudaDetected.setAlignment(Qt.AlignCenter)
        self.cudnnDetected = QLabel(self.home)
        self.cudnnDetected.setObjectName(u"cudnnDetected")
        self.cudnnDetected.setGeometry(QRect(450, 248, 151, 21))
        self.cudnnDetected.setStyleSheet(u"color: #fff;\n"
"")
        self.cudnnDetected.setLineWidth(1)
        self.cudnnDetected.setAlignment(Qt.AlignCenter)
        self.selectMap_2 = QPushButton(self.home)
        self.selectMap_2.setObjectName(u"selectMap_2")
        self.selectMap_2.setGeometry(QRect(240, 275, 150, 25))
        self.selectMap_2.setMinimumSize(QSize(150, 25))
        self.selectMap_2.setFont(font5)
        self.selectMap_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.selectMap_2.setStyleSheet(u"#selectMap_2{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 255), stop:1 rgba(170, 85, 255, 255));\n"
"font: 300 10pt \"Inter Light\";\n"
"}\n"
"#selectMap_2::pressed {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.471591, x2:1, y2:0.489, stop:0 rgba(254, 121, 199, 180), stop:1 rgba(170, 85, 255, 180));\n"
"font: 300 10pt \"Inter Light\";\n"
"}")
        self.selectMap_2.setFlat(False)
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.widgets)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 30))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: rgb(52, 59, 72);")

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)

        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = QCheckBox(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout.addWidget(self.row_2)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.row_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 16):
            self.tableWidget.setRowCount(16)
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font6);
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy3)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush3 = QBrush(QColor(221, 221, 221, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 255))
        brush5.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.tableWidget.setPalette(palette)
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.unusedPage3 = QWidget()
        self.unusedPage3.setObjectName(u"unusedPage3")
        self.stackedWidget.addWidget(self.unusedPage3)
        self.unusedPage2 = QWidget()
        self.unusedPage2.setObjectName(u"unusedPage2")
        self.stackedWidget.addWidget(self.unusedPage2)
        self.unusedPage1 = QWidget()
        self.unusedPage1.setObjectName(u"unusedPage1")
        self.stackedWidget.addWidget(self.unusedPage1)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_help = QPushButton(self.topMenus)
        self.btn_help.setObjectName(u"btn_help")
        sizePolicy.setHeightForWidth(self.btn_help.sizePolicy().hasHeightForWidth())
        self.btn_help.setSizePolicy(sizePolicy)
        self.btn_help.setMinimumSize(QSize(0, 45))
        self.btn_help.setFont(font)
        self.btn_help.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_help.setLayoutDirection(Qt.LeftToRight)
        self.btn_help.setStyleSheet(u"")

        self.verticalLayout_14.addWidget(self.btn_help)

        self.btn_report = QPushButton(self.topMenus)
        self.btn_report.setObjectName(u"btn_report")
        sizePolicy.setHeightForWidth(self.btn_report.sizePolicy().hasHeightForWidth())
        self.btn_report.setSizePolicy(sizePolicy)
        self.btn_report.setMinimumSize(QSize(0, 45))
        self.btn_report.setFont(font)
        self.btn_report.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_report.setLayoutDirection(Qt.LeftToRight)
        self.btn_report.setStyleSheet(u"")

        self.verticalLayout_14.addWidget(self.btn_report)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.creditsLabel = QLabel(self.bottomBar)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setGeometry(QRect(0, 0, 141, 21))
        self.creditsLabel.setMaximumSize(QSize(16777215, 21))
        font7 = QFont()
        font7.setFamilies([u"Inter Medium"])
        font7.setPointSize(9)
        font7.setBold(False)
        font7.setItalic(False)
        self.creditsLabel.setFont(font7)
        self.creditsLabel.setStyleSheet(u"font: 300 9pt \"Inter Medium\";")
        self.creditsLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setGeometry(QRect(537, 0, 101, 21))
        self.version.setStyleSheet(u"font: 300 9pt \"Inter Medium\";")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setGeometry(QRect(639, 0, 20, 22))
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SSGPlus", None))
        self.ssglabel.setText("")
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color: rgb(254, 121, 199);\">SSGPlus</span></p></body></html>", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#aa63ff;\">Home</span></p></body></html>", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_page2.setText(QCoreApplication.translate("MainWindow", u"Page 2", None))
        self.btn_page3.setText(QCoreApplication.translate("MainWindow", u"Page 3", None))
        self.btn_page4.setText(QCoreApplication.translate("MainWindow", u"Page 4", None))
        self.btn_page5.setText(QCoreApplication.translate("MainWindow", u"Page 5", None))
        self.toggleLeftBox.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.extraLabel.setText("")
#if QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Hide", None))
#endif // QT_CONFIG(tooltip)
        self.extraCloseColumnBtn.setText("")
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Share", None))
        self.btn_credits.setText(QCoreApplication.translate("MainWindow", u"Show Credits", None))
        self.btn_more.setText(QCoreApplication.translate("MainWindow", u"More", None))
        self.credits.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Inter Medium'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:12pt; font-weight:600; color:#614385;\">Credit</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; color:#516395;\">Theme by: Zeno Rocha, enigmapr0ject</span></p>\n"
"<p align=\"center\" st"
                        "yle=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; color:#516395;\">UI framework by: Wanderson M. Pimenta</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI'; font-size:9pt; color:#ffffff;\">Developed by enigmapr0ject</span></p></body></html>", None))
        self.titleRightInfo.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.dashboardTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">SSGPlus</span></p></body></html>", None))
        self.selectMap.setText(QCoreApplication.translate("MainWindow", u"Select Map", None))
        self.statusTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Overlay:</span></p></body></html>", None))
        self.status.setText(QCoreApplication.translate("MainWindow", u"Disabled", None))
        self.versionTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Model Version:</span></p></body></html>", None))
        self.modelVersion.setText("")
        self.statusTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Overlay:</span></p></body></html>", None))
        self.status_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ff0000;\">Disabled</span></p></body></html>", None))
        self.versionTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Model Version:</span></p></body></html>", None))
        self.modelVersion_2.setText("")
        self.predict.setText(QCoreApplication.translate("MainWindow", u"Predict", None))
        self.mapSelected.setText(QCoreApplication.translate("MainWindow", u"Map not selected.", None))
        self.predictionOutput.setText(QCoreApplication.translate("MainWindow", u"No predictions.", None))
        self.predictionOutputTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Prediction output</span></p></body></html>", None))
        self.statusTitle_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600;\">System Information</span></p></body></html>", None))
        self.versionTitle_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600;\">TF Version:</span></p></body></html>", None))
        self.tensorflowVersion.setText("")
        self.statusTitle_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Overlay:</span></p></body></html>", None))
        self.status_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ff0000;\">Disabled</span></p></body></html>", None))
        self.versionTitle_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Model Version:</span></p></body></html>", None))
        self.modelVersion_4.setText("")
        self.cpuName.setText(QCoreApplication.translate("MainWindow", u"CPU: ", None))
        self.gpuName.setText(QCoreApplication.translate("MainWindow", u"GPU:", None))
        self.cudaDetected.setText(QCoreApplication.translate("MainWindow", u"CUDA:", None))
        self.cudnnDetected.setText(QCoreApplication.translate("MainWindow", u"cuDNN:", None))
        self.selectMap_2.setText(QCoreApplication.translate("MainWindow", u"Open Predicted Map", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"0", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem20 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Test", None));
        ___qtablewidgetitem21 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Text", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Cell", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.btn_help.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.btn_report.setText(QCoreApplication.translate("MainWindow", u"Report Issue", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.creditsLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#aa55ff;\">Made by Puremaven</span></p></body></html>", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#aa55ff;\">Version</span><span style=\" color:#aa55ff;\"> 0.0.1</span></p></body></html>", None))
    # retranslateUi

