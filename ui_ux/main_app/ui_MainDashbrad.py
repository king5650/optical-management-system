# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainDashbradOpWOkx.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import images_rc
import icons_rc
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1161, 647)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, -1, 1337, 868))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_widget = QWidget(self.layoutWidget)
        self.icon_widget.setObjectName(u"icon_widget")
        self.icon_widget.setMinimumSize(QSize(80, 0))
        self.icon_widget.setMaximumSize(QSize(80, 16777215))
        self.icon_widget.setStyleSheet(u"QWidget{\n"
"	border: none;\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.icon_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(self.icon_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u":/thumb-1920-1273703.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(28)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 39, -1, -1)
        self.dashboard1 = QPushButton(self.icon_widget)
        self.dashboard1.setObjectName(u"dashboard1")
        self.dashboard1.setStyleSheet(u"\n"
"QPushButton:checked{\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"	width: 30px;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/test/icons/speed_64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard1.setIcon(icon)
        self.dashboard1.setIconSize(QSize(29, 29))
        self.dashboard1.setCheckable(True)
        self.dashboard1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.dashboard1)

        self.patientForm1 = QPushButton(self.icon_widget)
        self.patientForm1.setObjectName(u"patientForm1")
        self.patientForm1.setStyleSheet(u"QPushButton:checked{\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"	width: 30px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/test/icons/hospital_bed_64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.patientForm1.setIcon(icon1)
        self.patientForm1.setIconSize(QSize(29, 29))
        self.patientForm1.setCheckable(True)
        self.patientForm1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.patientForm1)

        self.medicalReport1 = QPushButton(self.icon_widget)
        self.medicalReport1.setObjectName(u"medicalReport1")
        self.medicalReport1.setStyleSheet(u"QPushButton:checked{\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"	width: 30px;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/test/icons/report_card_64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.medicalReport1.setIcon(icon2)
        self.medicalReport1.setIconSize(QSize(29, 29))
        self.medicalReport1.setCheckable(True)
        self.medicalReport1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.medicalReport1)

        self.receipt1 = QPushButton(self.icon_widget)
        self.receipt1.setObjectName(u"receipt1")
        self.receipt1.setStyleSheet(u"QPushButton:checked{\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"	width: 30px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/test/icons/receipt_64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.receipt1.setIcon(icon3)
        self.receipt1.setIconSize(QSize(29, 29))
        self.receipt1.setCheckable(True)
        self.receipt1.setAutoExclusive(True)

        self.verticalLayout_3.addWidget(self.receipt1)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 397, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_12 = QPushButton(self.icon_widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"QPushButton:checked{\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"	width: 30px;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/receipt_64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon4)
        self.pushButton_12.setIconSize(QSize(29, 29))
        self.pushButton_12.setCheckable(True)
        self.pushButton_12.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.pushButton_12)

        self.logout1 = QPushButton(self.icon_widget)
        self.logout1.setObjectName(u"logout1")
        self.logout1.setStyleSheet(u"QPushButton:checked{\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"	width: 30px;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/exit_64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout1.setIcon(icon5)
        self.logout1.setIconSize(QSize(29, 29))
        self.logout1.setCheckable(True)
        self.logout1.setAutoExclusive(True)

        self.verticalLayout_4.addWidget(self.logout1)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.gridLayout.addWidget(self.icon_widget, 0, 0, 1, 1)

        self.icon_text_widget = QWidget(self.layoutWidget)
        self.icon_text_widget.setObjectName(u"icon_text_widget")
        self.icon_text_widget.setMinimumSize(QSize(280, 0))
        self.icon_text_widget.setMaximumSize(QSize(400, 16777215))
        self.icon_text_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"	height: 30px;\n"
"	border: none;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.icon_text_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(25, -1, -1, -1)
        self.label_2 = QLabel(self.icon_text_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/thumb-1920-1273703.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_text_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(28)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(17, 35, -1, -1)
        self.dashboard2 = QPushButton(self.icon_text_widget)
        self.dashboard2.setObjectName(u"dashboard2")
        self.dashboard2.setStyleSheet(u"QPushButton{\n"
"	padding-left: -88px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: white;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.dashboard2.setIcon(icon)
        self.dashboard2.setIconSize(QSize(29, 29))
        self.dashboard2.setCheckable(True)
        self.dashboard2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard2)

        self.patientForm2 = QPushButton(self.icon_text_widget)
        self.patientForm2.setObjectName(u"patientForm2")
        self.patientForm2.setStyleSheet(u"QPushButton{\n"
"	padding-left: -85px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: white;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.patientForm2.setIcon(icon1)
        self.patientForm2.setIconSize(QSize(29, 29))
        self.patientForm2.setCheckable(True)
        self.patientForm2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.patientForm2)

        self.medicalReport2 = QPushButton(self.icon_text_widget)
        self.medicalReport2.setObjectName(u"medicalReport2")
        self.medicalReport2.setStyleSheet(u"QPushButton{\n"
"	padding-left: -40px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: white;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.medicalReport2.setIcon(icon2)
        self.medicalReport2.setIconSize(QSize(29, 29))
        self.medicalReport2.setCheckable(True)
        self.medicalReport2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.medicalReport2)

        self.receipt2 = QPushButton(self.icon_text_widget)
        self.receipt2.setObjectName(u"receipt2")
        self.receipt2.setStyleSheet(u"QPushButton{\n"
"	padding-left: -80px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: white;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.receipt2.setIcon(icon3)
        self.receipt2.setIconSize(QSize(29, 29))
        self.receipt2.setCheckable(True)
        self.receipt2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.receipt2)


        self.verticalLayout_6.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 397, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(29)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_11 = QPushButton(self.icon_text_widget)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u"QPushButton{\n"
"	padding-left: -60px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: white;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.pushButton_11.setIcon(icon5)
        self.pushButton_11.setIconSize(QSize(29, 29))
        self.pushButton_11.setCheckable(True)
        self.pushButton_11.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.pushButton_11)

        self.logout2 = QPushButton(self.icon_text_widget)
        self.logout2.setObjectName(u"logout2")
        self.logout2.setStyleSheet(u"QPushButton{\n"
"	padding-left: -60px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: white;\n"
"	border-radius: 3px;\n"
"	color: black;\n"
"}")
        self.logout2.setIcon(icon5)
        self.logout2.setIconSize(QSize(29, 29))
        self.logout2.setCheckable(True)
        self.logout2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.logout2)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.icon_text_widget, 0, 1, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.header_widget = QWidget(self.layoutWidget)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.header_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"border: none;")
        icon6 = QIcon()
        icon6.addFile(u":/icons/test/icons/menu_64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(45, 59))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 25, -1, 25)
        self.label = QLabel(self.header_widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.label.setFont(font1)

        self.verticalLayout_7.addWidget(self.label)

        self.label_5 = QLabel(self.header_widget)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(103, 103, 103);")

        self.verticalLayout_7.addWidget(self.label_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_7)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(320, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 25, -1)
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(19, 31))
        self.lineEdit.setMaximumSize(QSize(16777215, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 20px;\n"
"	border: 1px solid gray;\n"
"border-radius: 10px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_6 = QLabel(self.header_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(40, 40))
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setPixmap(QPixmap(u":/thumb-1920-1273703.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_6)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_8.addWidget(self.header_widget)

        self.main_widget = QWidget(self.layoutWidget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setMinimumSize(QSize(841, 741))
        self.main_widget.setMaximumSize(QSize(841, 741))
        self.main_widget.setStyleSheet(u"")
        self.stackedWidget = QStackedWidget(self.main_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 841, 741))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(190, 230, 49, 16))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(290, 260, 49, 16))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(150, 200, 341, 20))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(220, 270, 251, 41))
        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_8.addWidget(self.main_widget)


        self.gridLayout.addLayout(self.verticalLayout_8, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.dashboard2.toggled.connect(self.dashboard1.setChecked)
        self.patientForm2.toggled.connect(self.patientForm1.setChecked)
        self.medicalReport2.toggled.connect(self.medicalReport1.setChecked)
        self.receipt2.toggled.connect(self.receipt1.setChecked)
        self.pushButton_11.toggled.connect(self.pushButton_12.setChecked)
        self.logout2.toggled.connect(self.logout1.setChecked)
        self.pushButton.toggled.connect(self.icon_text_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_widget.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.dashboard1.setText("")
        self.patientForm1.setText("")
        self.medicalReport1.setText("")
        self.receipt1.setText("")
        self.pushButton_12.setText("")
        self.logout1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Optical", None))
        self.dashboard2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.patientForm2.setText(QCoreApplication.translate("MainWindow", u"Patients", None))
        self.medicalReport2.setText(QCoreApplication.translate("MainWindow", u"Medical report", None))
        self.receipt2.setText(QCoreApplication.translate("MainWindow", u"Receipt", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.logout2.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hello user", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Welcome back user", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search here", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"home", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"patient", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"report", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"receipt", None))
    # retranslateUi

