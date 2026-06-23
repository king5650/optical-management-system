# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginqbRrzd.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QWidget)
# import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1005, 845)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(90, 10, 721, 771))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 681, 711))
        self.label.setStyleSheet(u"border-image: url(:/images/dark-theme-02.jpg);\n"
"border-radius: 30px;\n"
"")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 681, 701))
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1715909, stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
"border-radius: 30px;\n"
"")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 30, 601, 641))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);\n"
"border-radius: 20px;")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(290, 90, 171, 41))
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgba(255, 255, 255, 210);")
        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(100, 280, 511, 41))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.textEdit.setFont(font2)
        self.textEdit.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: None;\n"
"border-bottom: 2px solid rgba(105, 118,132,255);\n"
"color: rgba(255, 255, 255, 230);\n"
"padding-bottom: 7px;")
        self.textEdit_2 = QTextEdit(self.widget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(100, 380, 511, 41))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.textEdit_2.setFont(font3)
        self.textEdit_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: None;\n"
"border-bottom: 2px solid rgba(105, 118,132,255);\n"
"color: rgba(255, 255, 255, 230);\n"
"padding-bottom: 7px;")
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 510, 251, 51))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"QPushButton#pushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 255));\n"
"color: rgba(255, 255, 255, 210);\n"
"border-radius: 5px;\n"
"\n"
"}\n"
"QPushButton#pushButton:Hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 255));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"padding-left: 5px;\n"
"padding-top: 5px;\n"
"background-color: rgba(105, 118, 132, 255)\n"
"\n"
"\n"
"}\n"
"\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1005, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"LOG IN", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

