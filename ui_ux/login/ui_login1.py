# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login1OGXQed.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)
import static_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1148, 875)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(805, 0))
        self.widget.setMaximumSize(QSize(805, 16777215))
        self.widget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(750, 0))
        self.frame.setMaximumSize(QSize(780, 16777215))
        self.frame.setStyleSheet(u"")
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
        self.label_6.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1715909, stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
"border-radius: 30px;\n"
"")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(330, 120, 171, 41))
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"color: rgba(255, 255, 255, 210);")
        self.textEdit_3 = QTextEdit(self.frame)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(140, 310, 511, 41))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.textEdit_3.setFont(font2)
        self.textEdit_3.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: None;\n"
"border-bottom: 2px solid rgba(105, 118,132,255);\n"
"color: rgba(255, 255, 255, 230);\n"
"padding-bottom: 7px;")
        self.textEdit_4 = QTextEdit(self.frame)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(140, 410, 511, 41))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.textEdit_4.setFont(font3)
        self.textEdit_4.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: None;\n"
"border-bottom: 2px solid rgba(105, 118,132,255);\n"
"color: rgba(255, 255, 255, 230);\n"
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

        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.widget, 0, Qt.AlignHCenter)

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

