# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LOGINFORM1xZUIKH.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import static_rc
import static_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1261, 580)
        MainWindow.setMinimumSize(QSize(1212, 500))
        MainWindow.setMaximumSize(QSize(1266, 580))
        MainWindow.setStyleSheet(u"background-color: rgb(82, 115, 227);\n"
"border-radius: 2px;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(880, 320))
        self.centralwidget.setMaximumSize(QSize(16777215, 543))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(1000, 550))
        self.widget.setMaximumSize(QSize(1252, 574))
        self.widget.setStyleSheet(u"background-color: rgb(82, 115, 227);\n"
"border-radius: 2px;\n"
"height: 400px;\n"
"width: 500px;")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(1224, 516))
        self.frame.setMaximumSize(QSize(1202, 516))
        self.frame.setStyleSheet(u"background-color: rgb(230, 230, 230);\n"
"border-radius: 10px;\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1221, 510))
        self.label.setMinimumSize(QSize(0, 500))
        self.label.setMaximumSize(QSize(16777215, 510))
        self.label.setStyleSheet(u"border-radius: 10px;\n"
"")
        self.label.setPixmap(QPixmap(u":/images/images/Mask Group 3.png"))
        self.label.setScaledContents(True)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(560, 0, 652, 466))
        self.frame_2.setStyleSheet(u"background-color: rgb(230, 230, 230);\n"
"border-radius: 10px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(200, 99))
        self.label_2.setMaximumSize(QSize(150, 88))
        self.label_2.setPixmap(QPixmap(u":/logo/logo1.png"))
        self.label_2.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(634, 71))
        self.label_3.setMaximumSize(QSize(150, 71))
        self.label_3.setStyleSheet(u"font-weight: 900;\n"
"font-size: 61px;\n"
"padding:2px;\n"
"color: black;")

        self.verticalLayout_4.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(264, 38))
        self.label_4.setMaximumSize(QSize(271, 36))
        font = QFont()
        font.setFamilies([u"SimSun-ExtB"])
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"font-weight: 900;\n"
"font-size: 20px;\n"
"padding:2px;")

        self.verticalLayout_4.addWidget(self.label_4, 0, Qt.AlignHCenter)

        self.user_details = QFrame(self.frame_2)
        self.user_details.setObjectName(u"user_details")
        self.user_details.setMinimumSize(QSize(610, 222))
        self.user_details.setMaximumSize(QSize(567, 214))
        font1 = QFont()
        font1.setBold(True)
        self.user_details.setFont(font1)
        self.user_details.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(239, 136, 43);\n"
"}\n"
"\n"
"#lineEdit_3{\n"
"background-color: rgb(239, 136, 43);\n"
"\n"
"}")
        self.user_details.setFrameShape(QFrame.StyledPanel)
        self.user_details.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.user_details)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(37)
        self.label_5 = QLabel(self.user_details)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(52, 44))
        self.label_5.setMaximumSize(QSize(30, 58))
        self.label_5.setPixmap(QPixmap(u":/logo/images/user_filled_50px.png"))
        self.label_5.setScaledContents(True)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_3 = QLineEdit(self.user_details)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(500, 44))
        self.lineEdit_3.setMaximumSize(QSize(500, 38))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.lineEdit_3.setFont(font2)
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border-bottom: 2px solid gray;")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_3)

        self.label_6 = QLabel(self.user_details)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(52, 44))
        self.label_6.setMaximumSize(QSize(30, 58))
        self.label_6.setStyleSheet(u"color: red;")
        self.label_6.setPixmap(QPixmap(u":/logo/images/password_24px.png"))
        self.label_6.setScaledContents(True)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.lineEdit_2 = QLineEdit(self.user_details)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(500, 44))
        self.lineEdit_2.setMaximumSize(QSize(500, 38))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.lineEdit_2.setFont(font3)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border-bottom: 2px solid gray;")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)


        self.verticalLayout_3.addLayout(self.formLayout)

        self.pushButton = QPushButton(self.user_details)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(200, 51))
        self.pushButton.setMaximumSize(QSize(200, 55))
        font4 = QFont()
        font4.setFamilies([u"SimSun-ExtG"])
        font4.setPointSize(18)
        font4.setBold(True)
        self.pushButton.setFont(font4)
        self.pushButton.setStyleSheet(u"#pushButton{\n"
"background-color: rgb(82, 115, 227);\n"
"color: white;\n"
"font-weight: 900px;\n"
"}\n"
"\n"
"#pushButton:hover{\n"
"	background-color: rgb(42, 44, 125);\n"
"color: white;\n"
"font-weight: 900px;\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.user_details)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"NGASSAM OPTIQUE", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"welcome To GSB soft", None))
        self.label_5.setText("")
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"        enter user name/ nom d'utilisateur", None))
        self.label_6.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"        password/ mote de pass", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
    # retranslateUi

