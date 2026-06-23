# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pdf_printlqgcWx.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QSizePolicy,
    QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(944, 838)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"background-color: rgb(225, 225, 225);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.headerFrame = QFrame(self.centralwidget)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setMaximumSize(QSize(1500, 700))
        self.headerFrame.setCursor(QCursor(Qt.ArrowCursor))
        self.headerFrame.setStyleSheet(u"")
        self.headerFrame.setFrameShape(QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.headerFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.h1_2 = QLabel(self.headerFrame)
        self.h1_2.setObjectName(u"h1_2")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(56)
        font.setBold(True)
        self.h1_2.setFont(font)
        self.h1_2.setStyleSheet(u"color: rgb(255, 29, 244);")

        self.gridLayout_5.addWidget(self.h1_2, 0, 0, 1, 2, Qt.AlignHCenter)

        self.label_37 = QLabel(self.headerFrame)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(50, 50))
        self.label_37.setMaximumSize(QSize(50, 50))
        self.label_37.setPixmap(QPixmap(u":/logo/thumb-1920-1273703.png"))
        self.label_37.setScaledContents(True)

        self.gridLayout_5.addWidget(self.label_37, 1, 0, 2, 1)

        self.label_38 = QLabel(self.headerFrame)
        self.label_38.setObjectName(u"label_38")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_38.setFont(font1)
        self.label_38.setStyleSheet(u"color: rgb(255, 0, 127);")

        self.gridLayout_5.addWidget(self.label_38, 5, 1, 1, 1, Qt.AlignHCenter)

        self.label_39 = QLabel(self.headerFrame)
        self.label_39.setObjectName(u"label_39")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label_39.setFont(font2)

        self.gridLayout_5.addWidget(self.label_39, 1, 1, 1, 1, Qt.AlignHCenter|Qt.AlignTop)

        self.label_40 = QLabel(self.headerFrame)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(50, 50))
        self.label_40.setMaximumSize(QSize(50, 50))
        self.label_40.setStyleSheet(u"")
        self.label_40.setPixmap(QPixmap(u":/logo/thumb-1920-1273703.png"))
        self.label_40.setScaledContents(True)

        self.gridLayout_5.addWidget(self.label_40, 1, 2, 2, 1)

        self.label_41 = QLabel(self.headerFrame)
        self.label_41.setObjectName(u"label_41")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_41.setFont(font3)

        self.gridLayout_5.addWidget(self.label_41, 2, 1, 1, 1, Qt.AlignHCenter)

        self.line_2 = QFrame(self.headerFrame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_5.addWidget(self.line_2, 4, 0, 1, 3)

        self.label_42 = QLabel(self.headerFrame)
        self.label_42.setObjectName(u"label_42")
        font4 = QFont()
        font4.setFamilies([u"Monotype Corsiva"])
        font4.setPointSize(18)
        font4.setBold(True)
        font4.setItalic(True)
        self.label_42.setFont(font4)
        self.label_42.setStyleSheet(u"color: rgb(255, 0, 127);")

        self.gridLayout_5.addWidget(self.label_42, 3, 1, 1, 1, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.headerFrame)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.datefame_2 = QFrame(self.frame)
        self.datefame_2.setObjectName(u"datefame_2")
        self.datefame_2.setStyleSheet(u"")
        self.datefame_2.setFrameShape(QFrame.StyledPanel)
        self.datefame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.datefame_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.datefame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(40, 0))
        self.label_4.setMaximumSize(QSize(40, 16777215))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.label_4.setFont(font5)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.dateLabel = QLabel(self.datefame_2)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setMinimumSize(QSize(90, 0))
        self.dateLabel.setMaximumSize(QSize(90, 16777215))
        self.dateLabel.setFont(font5)

        self.horizontalLayout_5.addWidget(self.dateLabel)


        self.verticalLayout_3.addWidget(self.datefame_2, 0, Qt.AlignRight)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QPushButton{\n"
"	border-radius: 9px;\n"
"	padding: 4px;\n"
"	background-color: rgb(0, 221, 255);\n"
"	\n"
"	background-color: rgb(0, 0, 99);\n"
"	\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")

        self.verticalLayout_3.addWidget(self.frame_7, 0, Qt.AlignLeft)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        font6 = QFont()
        font6.setFamilies([u"Times New Roman"])
        font6.setBold(True)
        self.frame_5.setFont(font6)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_26 = QLabel(self.frame_5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(250, 0))
        self.label_26.setMaximumSize(QSize(200, 16777215))
        self.label_26.setFont(font5)

        self.horizontalLayout_7.addWidget(self.label_26)

        self.patientNmae_label = QLabel(self.frame_5)
        self.patientNmae_label.setObjectName(u"patientNmae_label")

        self.horizontalLayout_7.addWidget(self.patientNmae_label)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_8 = QFrame(self.frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_27 = QLabel(self.frame_8)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(40, 0))
        self.label_27.setMaximumSize(QSize(40, 16777215))
        self.label_27.setFont(font5)

        self.horizontalLayout_8.addWidget(self.label_27)

        self.patientAgeLabel = QLabel(self.frame_8)
        self.patientAgeLabel.setObjectName(u"patientAgeLabel")
        self.patientAgeLabel.setMinimumSize(QSize(40, 0))
        self.patientAgeLabel.setMaximumSize(QSize(40, 16777215))
        font7 = QFont()
        font7.setBold(True)
        self.patientAgeLabel.setFont(font7)

        self.horizontalLayout_8.addWidget(self.patientAgeLabel)

        self.label_28 = QLabel(self.frame_8)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(60, 0))
        self.label_28.setMaximumSize(QSize(60, 16777215))
        self.label_28.setFont(font5)

        self.horizontalLayout_8.addWidget(self.label_28)

        self.genderLabel = QLabel(self.frame_8)
        self.genderLabel.setObjectName(u"genderLabel")
        self.genderLabel.setMinimumSize(QSize(120, 0))
        self.genderLabel.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_8.addWidget(self.genderLabel)

        self.label_29 = QLabel(self.frame_8)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(70, 0))
        self.label_29.setMaximumSize(QSize(70, 16777215))
        self.label_29.setFont(font5)

        self.horizontalLayout_8.addWidget(self.label_29)

        self.patientProfessionLabel = QLabel(self.frame_8)
        self.patientProfessionLabel.setObjectName(u"patientProfessionLabel")
        self.patientProfessionLabel.setMinimumSize(QSize(300, 0))

        self.horizontalLayout_8.addWidget(self.patientProfessionLabel)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_9)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_30 = QLabel(self.frame_9)
        self.label_30.setObjectName(u"label_30")
        font8 = QFont()
        font8.setPointSize(11)
        font8.setBold(True)
        self.label_30.setFont(font8)

        self.gridLayout_4.addWidget(self.label_30, 0, 0, 1, 1)

        self.label_31 = QLabel(self.frame_9)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font8)

        self.gridLayout_4.addWidget(self.label_31, 0, 1, 1, 1, Qt.AlignHCenter)

        self.label_32 = QLabel(self.frame_9)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font8)

        self.gridLayout_4.addWidget(self.label_32, 0, 2, 1, 1, Qt.AlignHCenter)

        self.label_33 = QLabel(self.frame_9)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font8)

        self.gridLayout_4.addWidget(self.label_33, 0, 3, 1, 1, Qt.AlignHCenter)

        self.label_34 = QLabel(self.frame_9)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font8)

        self.gridLayout_4.addWidget(self.label_34, 0, 4, 1, 1, Qt.AlignHCenter)

        self.label_35 = QLabel(self.frame_9)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font8)

        self.gridLayout_4.addWidget(self.label_35, 1, 0, 1, 1)

        self.lineEdit_12 = QLineEdit(self.frame_9)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.gridLayout_4.addWidget(self.lineEdit_12, 1, 1, 1, 1)

        self.lineEdit_13 = QLineEdit(self.frame_9)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.gridLayout_4.addWidget(self.lineEdit_13, 1, 2, 1, 1)

        self.lineEdit_14 = QLineEdit(self.frame_9)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.gridLayout_4.addWidget(self.lineEdit_14, 1, 3, 1, 1)

        self.lineEdit_15 = QLineEdit(self.frame_9)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_4.addWidget(self.lineEdit_15, 1, 4, 1, 1)

        self.label_36 = QLabel(self.frame_9)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font8)

        self.gridLayout_4.addWidget(self.label_36, 2, 0, 1, 1)

        self.lineEdit_16 = QLineEdit(self.frame_9)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_4.addWidget(self.lineEdit_16, 2, 1, 1, 1)

        self.lineEdit_17 = QLineEdit(self.frame_9)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.gridLayout_4.addWidget(self.lineEdit_17, 2, 2, 1, 1)

        self.lineEdit_18 = QLineEdit(self.frame_9)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.gridLayout_4.addWidget(self.lineEdit_18, 2, 3, 1, 1)

        self.lineEdit_19 = QLineEdit(self.frame_9)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.gridLayout_4.addWidget(self.lineEdit_19, 2, 4, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_9)


        self.verticalLayout.addWidget(self.frame)

        self.frame_10 = QFrame(self.centralwidget)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(220, 16777215))
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_10)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_48 = QLabel(self.frame_10)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(59, 16777215))
        self.label_48.setFont(font5)

        self.gridLayout_6.addWidget(self.label_48, 2, 0, 1, 2)

        self.port = QLabel(self.frame_10)
        self.port.setObjectName(u"port")
        self.port.setMinimumSize(QSize(200, 0))

        self.gridLayout_6.addWidget(self.port, 4, 3, 1, 1)

        self.label_44 = QLabel(self.frame_10)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(40, 16777215))
        self.label_44.setFont(font5)

        self.gridLayout_6.addWidget(self.label_44, 3, 0, 1, 1)

        self.label_43 = QLabel(self.frame_10)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(40, 16777215))
        self.label_43.setFont(font5)

        self.gridLayout_6.addWidget(self.label_43, 5, 0, 1, 2)

        self.typeDeVerreLabel = QLabel(self.frame_10)
        self.typeDeVerreLabel.setObjectName(u"typeDeVerreLabel")
        self.typeDeVerreLabel.setMinimumSize(QSize(200, 0))

        self.gridLayout_6.addWidget(self.typeDeVerreLabel, 1, 3, 1, 1)

        self.label_45 = QLabel(self.frame_10)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(90, 16777215))
        self.label_45.setFont(font5)

        self.gridLayout_6.addWidget(self.label_45, 1, 0, 1, 3)

        self.label_46 = QLabel(self.frame_10)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(100, 16777215))
        self.label_46.setFont(font5)

        self.gridLayout_6.addWidget(self.label_46, 0, 0, 1, 2)

        self.ametropieLable = QLabel(self.frame_10)
        self.ametropieLable.setObjectName(u"ametropieLable")
        self.ametropieLable.setMinimumSize(QSize(200, 0))

        self.gridLayout_6.addWidget(self.ametropieLable, 0, 3, 1, 1)

        self.teintesLabel = QLabel(self.frame_10)
        self.teintesLabel.setObjectName(u"teintesLabel")
        self.teintesLabel.setMinimumSize(QSize(200, 0))

        self.gridLayout_6.addWidget(self.teintesLabel, 2, 3, 1, 1)

        self.indice = QLabel(self.frame_10)
        self.indice.setObjectName(u"indice")
        self.indice.setMinimumSize(QSize(200, 0))

        self.gridLayout_6.addWidget(self.indice, 5, 3, 1, 1)

        self.label_47 = QLabel(self.frame_10)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font5)

        self.gridLayout_6.addWidget(self.label_47, 4, 0, 1, 1)

        self.foyers = QLabel(self.frame_10)
        self.foyers.setObjectName(u"foyers")
        self.foyers.setMinimumSize(QSize(200, 0))

        self.gridLayout_6.addWidget(self.foyers, 3, 3, 1, 1)


        self.verticalLayout.addWidget(self.frame_10)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.h1_2.setText(QCoreApplication.translate("MainWindow", u"NGASSAM OPTIQUE", None))
        self.label_37.setText("")
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"ORDONNANCE DE LUNETTES", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Situ\u00e9 a L'Avenue Kennedy derri\u00e8re ADAMAQUA PALACE", None))
        self.label_40.setText("")
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"T\u00e9l.: (237) 699 67 50 25/620 37 69 28/651 63 06 45", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Le professionnel de la sant\u00e9 visuelle", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.dateLabel.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Nom et Prenom(Name and surname):", None))
        self.patientNmae_label.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Age:", None))
        self.patientAgeLabel.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Gender:", None))
        self.genderLabel.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Profession:", None))
        self.patientProfessionLabel.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Oeil", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Sphere", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Cyl", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Axe", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Addition", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"OD", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"OG", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Teintes:", None))
        self.port.setText("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Foyers:", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Indice:", None))
        self.typeDeVerreLabel.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Types de verre:", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Am\u00e9tropie:", None))
        self.ametropieLable.setText("")
        self.teintesLabel.setText("")
        self.indice.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Port:", None))
        self.foyers.setText("")
    # retranslateUi

