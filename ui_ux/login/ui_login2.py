# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login1UGYqMu.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QWidget)
import static_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(675, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(614, 700))
        MainWindow.setMaximumSize(QSize(675, 700))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"background-color: rgb(18, 30, 38);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-50, -40, 736, 775))
        self.frame.setMinimumSize(QSize(736, 0))
        self.frame.setMaximumSize(QSize(478, 16777215))
        self.frame.setStyleSheet(u"background-color: rgb(14, 21, 25);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 40, 681, 711))
        self.label_5.setStyleSheet(u"border-image: url(:/images/images/dark-theme-02.jpg);\n"
"border-radius: 30px;\n"
"")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(50, 40, 681, 701))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"background-color: rgba(0, 0, 0, 100);\n"
"border-radius: 20px;")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 40, 681, 711))
        font1 = QFont()
        font1.setPointSize(11)
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1715909, stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
"border-radius: 30px;\n"
"")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(330, 120, 171, 41))
        font2 = QFont()
        font2.setPointSize(25)
        font2.setBold(True)
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: rgba(255, 255, 255, 255);\n"
"background-color: none;")
        self.textEdit_3 = QTextEdit(self.frame)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(140, 310, 511, 41))
        sizePolicy.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.textEdit_3.setFont(font3)
        self.textEdit_3.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: None;\n"
"border-bottom: 2px solid rgba(105, 118,132,255);\n"
"color: rgba(255, 255, 255, 255);\n"
"padding-bottom: 7px;")
        self.textEdit_4 = QTextEdit(self.frame)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(140, 410, 511, 41))
        sizePolicy.setHeightForWidth(self.textEdit_4.sizePolicy().hasHeightForWidth())
        self.textEdit_4.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.textEdit_4.setFont(font4)
        self.textEdit_4.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: None;\n"
"border-bottom: 2px solid rgba(105, 118,132,255);\n"
"color: rgba(255, 255, 255, 255);\n"
"padding-bottom: 7px;")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(250, 550, 251, 51))
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

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_5.setText("")
        self.label_7.setText("")
        self.label_6.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"LOG IN", None))
        self.textEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User Name", None))
        self.textEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

