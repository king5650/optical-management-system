# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenbaWtjV.ui'
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
    QSizePolicy, QWidget)
import static_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(582, 422)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(0, 60, 400, 200))
        self.main_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0.267, x2:1, y2:0.471, stop:0 rgba(2, 101, 195, 255), stop:1 rgba(44, 47, 132, 255));\n"
"border-radius: 20px;\n"
"border-bottom: 5px solid  rgb(2, 127, 196);\n"
"border-right: 5px solid rgb(44, 47, 132);\n"
"border-top: 5px solid rgb(2, 127, 196);\n"
"border-left: 5px solid rgb(2, 127, 196);\n"
"")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.logframe = QFrame(self.main_frame)
        self.logframe.setObjectName(u"logframe")
        self.logframe.setGeometry(QRect(0, 10, 91, 51))
        self.logframe.setStyleSheet(u"image: url(:/logo/images/visible_40px.png);\n"
"background-color: none;\n"
"border: none;")
        self.logframe.setFrameShape(QFrame.StyledPanel)
        self.logframe.setFrameShadow(QFrame.Raised)
        self.middle_cricle_frame = QFrame(self.main_frame)
        self.middle_cricle_frame.setObjectName(u"middle_cricle_frame")
        self.middle_cricle_frame.setGeometry(QRect(40, 20, 400, 400))
        self.middle_cricle_frame.setStyleSheet(u"background-color: none;\n"
"/*border: 10px solid   rgb(255, 255, 255);*/\n"
"border: 10px solid   rgb(44, 47, 134);\n"
"border-radius: 200px;\n"
"")
        self.middle_cricle_frame.setFrameShape(QFrame.StyledPanel)
        self.middle_cricle_frame.setFrameShadow(QFrame.Raised)
        self.shoes_border_frame = QFrame(self.centralwidget)
        self.shoes_border_frame.setObjectName(u"shoes_border_frame")
        self.shoes_border_frame.setGeometry(QRect(330, 10, 250, 250))
        self.shoes_border_frame.setStyleSheet(u"border: 7px solid rgb(2, 127, 196);\n"
"border-radius: 20px;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(48, 51, 145, 255), stop:1 rgba(2, 127, 196, 84));")
        self.shoes_border_frame.setFrameShape(QFrame.StyledPanel)
        self.shoes_border_frame.setFrameShadow(QFrame.Raised)
        self.shoe_frame = QFrame(self.centralwidget)
        self.shoe_frame.setObjectName(u"shoe_frame")
        self.shoe_frame.setGeometry(QRect(260, -20, 321, 331))
        self.shoe_frame.setStyleSheet(u"image: url(:/logo/logo1.png);\n"
"background-color: none;\n"
"/*background-color: transparent;*/\n"
"border: none;\n"
"")
        self.shoe_frame.setFrameShape(QFrame.StyledPanel)
        self.shoe_frame.setFrameShadow(QFrame.Raised)
        self.more_info_frame = QFrame(self.centralwidget)
        self.more_info_frame.setObjectName(u"more_info_frame")
        self.more_info_frame.setGeometry(QRect(0, 250, 401, 171))
        self.more_info_frame.setStyleSheet(u"/*background-color: rgb(255, 255, 255); background-color: rgb(21, 28, 74);*/\n"
"\n"
"background-color: rgb(44, 47, 134);\n"
"border-radius: 20px;\n"
"border: 5px solid rgb(2, 127, 196);")
        self.more_info_frame.setFrameShape(QFrame.StyledPanel)
        self.more_info_frame.setFrameShadow(QFrame.Raised)
        self.app_info = QLabel(self.more_info_frame)
        self.app_info.setObjectName(u"app_info")
        self.app_info.setGeometry(QRect(0, 140, 271, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        self.app_info.setFont(font)
        self.app_info.setStyleSheet(u"border: none;\n"
"background-color: transparent;")
        self.app_info.setAlignment(Qt.AlignCenter)
        self.loading_status = QLabel(self.more_info_frame)
        self.loading_status.setObjectName(u"loading_status")
        self.loading_status.setGeometry(QRect(50, 20, 281, 61))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(False)
        self.loading_status.setFont(font1)
        self.loading_status.setStyleSheet(u"border: none;\n"
"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.loading_status.setAlignment(Qt.AlignCenter)
        self.loading_progress = QLabel(self.more_info_frame)
        self.loading_progress.setObjectName(u"loading_progress")
        self.loading_progress.setGeometry(QRect(230, 70, 91, 31))
        font2 = QFont()
        font2.setPointSize(10)
        self.loading_progress.setFont(font2)
        self.loading_progress.setStyleSheet(u"border: none;\n"
"background-color: transparent;\n"
"color: rgb(255, 255, 255);")
        self.welcome_label = QLabel(self.centralwidget)
        self.welcome_label.setObjectName(u"welcome_label")
        self.welcome_label.setGeometry(QRect(50, 191, 349, 91))
        font3 = QFont()
        font3.setFamilies([u"Algerian"])
        font3.setPointSize(30)
        font3.setBold(False)
        self.welcome_label.setFont(font3)
        self.welcome_label.setStyleSheet(u"border-left: 20px solid rgb(44, 47, 134);\n"
"border-right: 25px solid rgb(44, 47, 134);\n"
"border-bottom: 30px solid rgb(44, 47, 134);\n"
"border-radius: 30px;\n"
"color: rgb(255, 255, 255);")
        self.welcome_label.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.shoes_border_frame.raise_()
        self.more_info_frame.raise_()
        self.main_frame.raise_()
        self.welcome_label.raise_()
        self.shoe_frame.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.app_info.setText(QCoreApplication.translate("MainWindow", u"Optical system Design  by kiven@", None))
        self.loading_status.setText(QCoreApplication.translate("MainWindow", u"Initializing Optical System..", None))
        self.loading_progress.setText(QCoreApplication.translate("MainWindow", u"Please Wait........", None))
        self.welcome_label.setText(QCoreApplication.translate("MainWindow", u"WELCOME", None))
    # retranslateUi

