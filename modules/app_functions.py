# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *

# WITH ACCESS TO MAIN WINDOW WIDGETS
# ///////////////////////////////////////////////////////////////


class AppFunctions(MainWindow):
    def setThemeHack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #aa63ff;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #aa63ff;"
        Settings.MENU_SELECTED_STYLESHEET = """
        border-left: 22px solid qlineargradient(spread:pad, x1:0, y1:0.471591, x2:0.326, y2:0.472, stop:0 rgba(254, 121, 199, 255), stop:0.573684 rgba(170, 85, 255, 255), stop:0.631579 rgba(170, 85, 255, 0));
        background-color: rgb(50, 50, 50);
        """

        # SET MANUAL STYLES
        self.ui.lineEdit.setStyleSheet("background-color: #aa63ff;") if self.ui.lineEdit else None
        self.ui.pushButton.setStyleSheet("background-color: #aa63ff;") if self.ui.pushButton else None
        self.ui.plainTextEdit.setStyleSheet("background-color: #aa63ff;") if self.ui.plainTextEdit else None
        self.ui.tableWidget.setStyleSheet(
            "QScrollBar:vertical { background: #aa63ff; } QScrollBar:horizontal { background: #aa63ff; }") if self.ui.tableWidget else None
        self.ui.scrollArea.setStyleSheet(
            "QScrollBar:vertical { background: #aa63ff; } QScrollBar:horizontal { background: #aa63ff; }") if self.ui.scrollArea else None
        self.ui.comboBox.setStyleSheet("background-color: #aa63ff;") if self.ui.comboBox else None
        self.ui.horizontalScrollBar.setStyleSheet("background-color: #aa63ff;") if self.ui.horizontalScrollBar else None
        self.ui.verticalScrollBar.setStyleSheet("background-color: #aa63ff;") if self.ui.verticalScrollBar else None
        self.ui.commandLinkButton.setStyleSheet("color: #aa63ff;") if self.ui.commandLinkButton else None
