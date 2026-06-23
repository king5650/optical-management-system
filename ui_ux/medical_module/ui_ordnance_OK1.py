# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ordnance_OKLKYsUg.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import static_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(961, 824)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(209, 209, 209);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerFrame = QFrame(self.centralwidget)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setMaximumSize(QSize(1500, 700))
        self.headerFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.headerFrame.setStyleSheet(u"")
        self.headerFrame.setFrameShape(QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.headerFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.h1 = QLabel(self.headerFrame)
        self.h1.setObjectName(u"h1")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(56)
        font.setBold(True)
        self.h1.setFont(font)
        self.h1.setStyleSheet(u"color: rgb(255, 29, 244);")

        self.gridLayout_2.addWidget(self.h1, 0, 0, 1, 2, Qt.AlignHCenter)

        self.label_8 = QLabel(self.headerFrame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(90, 50))
        self.label_8.setMaximumSize(QSize(90, 50))
        self.label_8.setPixmap(QPixmap(u":/logo/images/logo.png"))
        self.label_8.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 2, 1)

        self.label_11 = QLabel(self.headerFrame)
        self.label_11.setObjectName(u"label_11")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"color: rgb(255, 0, 127);")

        self.gridLayout_2.addWidget(self.label_11, 5, 1, 1, 1, Qt.AlignHCenter)

        self.label = QLabel(self.headerFrame)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label.setFont(font2)

        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.label_9 = QLabel(self.headerFrame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(80, 50))
        self.label_9.setMaximumSize(QSize(90, 50))
        self.label_9.setStyleSheet(u"")
        self.label_9.setPixmap(QPixmap(u":/logo/images/logo.png"))
        self.label_9.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_9, 1, 2, 2, 1)

        self.label_2 = QLabel(self.headerFrame)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_2.setFont(font3)

        self.gridLayout_2.addWidget(self.label_2, 2, 1, 1, 1, Qt.AlignHCenter)

        self.line = QFrame(self.headerFrame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 4, 0, 1, 3)

        self.label_10 = QLabel(self.headerFrame)
        self.label_10.setObjectName(u"label_10")
        font4 = QFont()
        font4.setFamilies([u"Monotype Corsiva"])
        font4.setPointSize(18)
        font4.setBold(True)
        font4.setItalic(True)
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"color: rgb(255, 0, 127);")

        self.gridLayout_2.addWidget(self.label_10, 3, 1, 1, 1, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.headerFrame)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.datefame = QFrame(self.frame)
        self.datefame.setObjectName(u"datefame")
        self.datefame.setStyleSheet(u"")
        self.datefame.setFrameShape(QFrame.StyledPanel)
        self.datefame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.datefame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.date = QLabel(self.datefame)
        self.date.setObjectName(u"date")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.date.setFont(font5)

        self.horizontalLayout.addWidget(self.date)

        self.label_3 = QLabel(self.datefame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(120, 0))
        self.label_3.setMaximumSize(QSize(120, 16777215))
        self.label_3.setFont(font5)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.datefame, 0, Qt.AlignRight)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QPushButton{\n"
"	border-radius: 9px;\n"
"	padding: 4px;\n"
"	background-color: rgb(0, 221, 255);\n"
"	\n"
"	background-color: rgb(0, 0, 99);\n"
"	\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.saveButton = QPushButton(self.frame_6)
        self.saveButton.setObjectName(u"saveButton")
        font6 = QFont()
        font6.setBold(True)
        self.saveButton.setFont(font6)
        icon = QIcon()
        icon.addFile(u":/logo/images/save_100px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveButton.setIcon(icon)
        self.saveButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.saveButton)

        self.pirintBUtton = QPushButton(self.frame_6)
        self.pirintBUtton.setObjectName(u"pirintBUtton")
        self.pirintBUtton.setFont(font3)
        icon1 = QIcon()
        icon1.addFile(u":/logo/images/print_100px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pirintBUtton.setIcon(icon1)
        self.pirintBUtton.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.pirintBUtton)


        self.verticalLayout_2.addWidget(self.frame_6, 0, Qt.AlignLeft)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)

        self.horizontalLayout_2.addWidget(self.label_5, 0, Qt.AlignLeft)

        self.patientName = QLineEdit(self.frame_2)
        self.patientName.setObjectName(u"patientName")

        self.horizontalLayout_2.addWidget(self.patientName)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font5)

        self.horizontalLayout_3.addWidget(self.label_6)

        self.pateintage = QLineEdit(self.frame_3)
        self.pateintage.setObjectName(u"pateintage")
        self.pateintage.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_3.addWidget(self.pateintage)

        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)

        self.horizontalLayout_3.addWidget(self.label_7)

        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(150, 0))
        self.comboBox.setMaximumSize(QSize(102, 16777215))

        self.horizontalLayout_3.addWidget(self.comboBox)

        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font5)

        self.horizontalLayout_3.addWidget(self.label_12)

        self.patientprofesion = QLineEdit(self.frame_3)
        self.patientprofesion.setObjectName(u"patientprofesion")
        self.patientprofesion.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.patientprofesion)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        font7 = QFont()
        font7.setPointSize(11)
        font7.setBold(True)
        self.label_13.setFont(font7)

        self.gridLayout.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font7)

        self.gridLayout.addWidget(self.label_14, 0, 1, 1, 1, Qt.AlignHCenter)

        self.label_15 = QLabel(self.frame_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font7)

        self.gridLayout.addWidget(self.label_15, 0, 2, 1, 1, Qt.AlignHCenter)

        self.label_16 = QLabel(self.frame_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font7)

        self.gridLayout.addWidget(self.label_16, 0, 3, 1, 1, Qt.AlignHCenter)

        self.label_17 = QLabel(self.frame_4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font7)

        self.gridLayout.addWidget(self.label_17, 0, 4, 1, 1, Qt.AlignHCenter)

        self.label_18 = QLabel(self.frame_4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font7)

        self.gridLayout.addWidget(self.label_18, 1, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.frame_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 1, 1, 1, 1)

        self.lineEdit_5 = QLineEdit(self.frame_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 1, 2, 1, 1)

        self.lineEdit_6 = QLineEdit(self.frame_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 1, 3, 1, 1)

        self.lineEdit_7 = QLineEdit(self.frame_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout.addWidget(self.lineEdit_7, 1, 4, 1, 1)

        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font7)

        self.gridLayout.addWidget(self.label_19, 2, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.frame_4)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout.addWidget(self.lineEdit_8, 2, 1, 1, 1)

        self.lineEdit_9 = QLineEdit(self.frame_4)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout.addWidget(self.lineEdit_9, 2, 2, 1, 1)

        self.lineEdit_10 = QLineEdit(self.frame_4)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.gridLayout.addWidget(self.lineEdit_10, 2, 3, 1, 1)

        self.lineEdit_11 = QLineEdit(self.frame_4)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout.addWidget(self.lineEdit_11, 2, 4, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)

        self.frame_5 = QFrame(self.centralwidget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(400, 0))
        self.frame_5.setMaximumSize(QSize(550, 16777215))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(11)
        self.checkBox_14 = QCheckBox(self.frame_5)
        self.checkBox_14.setObjectName(u"checkBox_14")

        self.gridLayout_3.addWidget(self.checkBox_14, 3, 3, 1, 1)

        self.checkBox_11 = QCheckBox(self.frame_5)
        self.checkBox_11.setObjectName(u"checkBox_11")

        self.gridLayout_3.addWidget(self.checkBox_11, 2, 5, 1, 1)

        self.checkBox_2 = QCheckBox(self.frame_5)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout_3.addWidget(self.checkBox_2, 0, 4, 1, 1)

        self.checkBox_17 = QCheckBox(self.frame_5)
        self.checkBox_17.setObjectName(u"checkBox_17")

        self.gridLayout_3.addWidget(self.checkBox_17, 4, 3, 1, 1)

        self.checkBox_9 = QCheckBox(self.frame_5)
        self.checkBox_9.setObjectName(u"checkBox_9")

        self.gridLayout_3.addWidget(self.checkBox_9, 2, 3, 1, 1)

        self.checkBox_15 = QCheckBox(self.frame_5)
        self.checkBox_15.setObjectName(u"checkBox_15")

        self.gridLayout_3.addWidget(self.checkBox_15, 3, 4, 1, 1)

        self.checkBox_18 = QCheckBox(self.frame_5)
        self.checkBox_18.setObjectName(u"checkBox_18")

        self.gridLayout_3.addWidget(self.checkBox_18, 4, 4, 1, 1)

        self.checkBox_7 = QCheckBox(self.frame_5)
        self.checkBox_7.setObjectName(u"checkBox_7")

        self.gridLayout_3.addWidget(self.checkBox_7, 1, 4, 1, 1)

        self.checkBox = QCheckBox(self.frame_5)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_3.addWidget(self.checkBox, 0, 3, 1, 1)

        self.checkBox_19 = QCheckBox(self.frame_5)
        self.checkBox_19.setObjectName(u"checkBox_19")

        self.gridLayout_3.addWidget(self.checkBox_19, 5, 3, 1, 1)

        self.checkBox_16 = QCheckBox(self.frame_5)
        self.checkBox_16.setObjectName(u"checkBox_16")

        self.gridLayout_3.addWidget(self.checkBox_16, 3, 5, 1, 1)

        self.checkBox_6 = QCheckBox(self.frame_5)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.gridLayout_3.addWidget(self.checkBox_6, 1, 3, 1, 1)

        self.label_25 = QLabel(self.frame_5)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(100, 0))
        self.label_25.setMaximumSize(QSize(100, 16777215))
        self.label_25.setFont(font5)

        self.gridLayout_3.addWidget(self.label_25, 5, 0, 1, 2)

        self.label_20 = QLabel(self.frame_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(100, 0))
        self.label_20.setMaximumSize(QSize(100, 16777215))
        self.label_20.setFont(font5)

        self.gridLayout_3.addWidget(self.label_20, 0, 0, 1, 3)

        self.checkBox_13 = QCheckBox(self.frame_5)
        self.checkBox_13.setObjectName(u"checkBox_13")

        self.gridLayout_3.addWidget(self.checkBox_13, 2, 7, 1, 1)

        self.checkBox_4 = QCheckBox(self.frame_5)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout_3.addWidget(self.checkBox_4, 0, 6, 1, 1)

        self.label_21 = QLabel(self.frame_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(100, 0))
        self.label_21.setMaximumSize(QSize(100, 16777215))
        self.label_21.setFont(font5)

        self.gridLayout_3.addWidget(self.label_21, 1, 0, 1, 3)

        self.label_22 = QLabel(self.frame_5)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(100, 0))
        self.label_22.setMaximumSize(QSize(100, 16777215))
        self.label_22.setFont(font5)

        self.gridLayout_3.addWidget(self.label_22, 2, 0, 1, 2)

        self.label_24 = QLabel(self.frame_5)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(100, 0))
        self.label_24.setMaximumSize(QSize(100, 16777215))
        self.label_24.setFont(font5)

        self.gridLayout_3.addWidget(self.label_24, 4, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.frame_5)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_3.addWidget(self.checkBox_3, 0, 5, 1, 1)

        self.checkBox_8 = QCheckBox(self.frame_5)
        self.checkBox_8.setObjectName(u"checkBox_8")

        self.gridLayout_3.addWidget(self.checkBox_8, 1, 5, 1, 1)

        self.checkBox_10 = QCheckBox(self.frame_5)
        self.checkBox_10.setObjectName(u"checkBox_10")

        self.gridLayout_3.addWidget(self.checkBox_10, 2, 4, 1, 1)

        self.checkBox_20 = QCheckBox(self.frame_5)
        self.checkBox_20.setObjectName(u"checkBox_20")

        self.gridLayout_3.addWidget(self.checkBox_20, 5, 4, 1, 1)

        self.label_23 = QLabel(self.frame_5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(100, 0))
        self.label_23.setMaximumSize(QSize(100, 16777215))
        self.label_23.setFont(font5)

        self.gridLayout_3.addWidget(self.label_23, 3, 0, 1, 1)

        self.checkBox_12 = QCheckBox(self.frame_5)
        self.checkBox_12.setObjectName(u"checkBox_12")

        self.gridLayout_3.addWidget(self.checkBox_12, 2, 6, 1, 1)

        self.checkBox_5 = QCheckBox(self.frame_5)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.gridLayout_3.addWidget(self.checkBox_5, 0, 7, 1, 1)


        self.verticalLayout.addWidget(self.frame_5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.h1.setText(QCoreApplication.translate("MainWindow", u"NGASSAM OPTIQUE", None))
        self.label_8.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"ORDONNANCE DE LUNETTES", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Situ\u00e9 a L'Avenue Kennedy derri\u00e8re ADAMAQUA PALACE", None))
        self.label_9.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"T\u00e9l.: (237) 699 67 50 25/620 37 69 28/651 63 06 45", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Le professionnel de la sant\u00e9 visuelle", None))
        self.date.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.saveButton.setText("")
        self.pirintBUtton.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Nom et Prenom(Name and surname):", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Age:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Gender:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Profession:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Oeil", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Sphere", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Cyl", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Axe", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Addition", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"OD", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"OG", None))
        self.checkBox_14.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_11.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_17.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_9.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_15.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_18.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_19.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_16.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Indice:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Am\u00e9tropie:", None))
        self.checkBox_13.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Types de verre:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Teintes:", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Port:", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_8.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_10.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_20.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Foyers:", None))
        self.checkBox_12.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
    # retranslateUi

