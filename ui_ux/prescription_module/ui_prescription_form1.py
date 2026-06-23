# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prescription_formChLqNX.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import static_rc
import static_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1388, 1526)
        MainWindow.setMinimumSize(QSize(9, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"position: relative;\n"
"display: inline-block;\n"
"width: 18px;\n"
"height: 18px;\n"
"border: 2px solid #d1d5db;\n"
"border-radius: 4px;\n"
"background-color: #f9fafb;")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.header_seaction = QWidget(self.centralwidget)
        self.header_seaction.setObjectName(u"header_seaction")
        self.header_seaction.setMinimumSize(QSize(1320, 110))
        self.header_seaction.setStyleSheet(u"\n"
"\n"
"#header_seaction{\n"
"                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, /* Horizontal gradient */\n"
"                                        stop: 0 #eff6ff, stop: 1 #dbeafe); /* from-blue-50 to-blue-100 */\n"
"                border-bottom: 1px solid #e5e7eb; /* border-gray-200 */\n"
"               padding: 1.5em;   /*p-6 in Tailwind (6 * 0.25rem = 1.5rem) */\n"
"border-color: #4285F4;\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.header_seaction)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.header_seaction)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(50, 50))
        self.label.setMaximumSize(QSize(100, 100))
        self.label.setSizeIncrement(QSize(0, 0))
        self.label.setStyleSheet(u"border: none;\n"
"\n"
"                width: 3em; /* w-12 in Tailwind (12 * 0.25rem = 3rem) */\n"
"                height: 3em; /* h-12 in Tailwind */\n"
"                background-color: QColor(0, 123, 255); /* Approximate for bg-primary - replace with your actual primary color */\n"
"                border-radius: 50%;\n"
"  \n"
"                color: white;\n"
"                margin-right: 0.75em; /* mr-3 in Tailwind (3 * 0.25rem = 0.75rem) */\n"
"                font-size: 1.2em; /* Adjust as needed */")
        self.label.setPixmap(QPixmap(u":/logo/logo1.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label, 0, Qt.AlignLeft)

        self.date_ref = QFrame(self.header_seaction)
        self.date_ref.setObjectName(u"date_ref")
        self.date_ref.setMinimumSize(QSize(262, 40))
        self.date_ref.setMaximumSize(QSize(452, 16777215))
        self.date_ref.setStyleSheet(u"padding: 4px;\n"
"border: none;\n"
"background-color: none;\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.date_ref.setFrameShape(QFrame.StyledPanel)
        self.date_ref.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.date_ref)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.date_ref)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"                margin-left: 0.5em; /* ml-2 in Tailwind (2 * 0.25rem = 0.5rem) */\n"
"                color: #4b5563; /* Approximate for text-gray-600 */\n"
"                font-weight: 500; /* font-medium */\n"
"border: none;\n"
"padding: 4px;")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.dateTimeEdit = QDateTimeEdit(self.date_ref)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setStyleSheet(u"\n"
"border: none;\n"
"padding: 10px;\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 9px;\n"
"padding: 8px;\n"
"color: black;\n"
"\n"
"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dateTimeEdit)

        self.label_3 = QLabel(self.date_ref)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"                margin-left: 0.5em; /* ml-2 in Tailwind (2 * 0.25rem = 0.5rem) */\n"
"                color: #4b5563; /* Approximate for text-gray-600 */\n"
"                font-weight: 500; /* font-medium */\n"
"border: none;\n"
"padding: 4px;")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.date_ref)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"\n"
"border: none;\n"
"padding: 10px;\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 9px;\n"
"padding: 8px;\n"
"color: black;\n"
"\n"
"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_4)


        self.verticalLayout_5.addLayout(self.formLayout)


        self.horizontalLayout_6.addWidget(self.date_ref, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.header_seaction)

        self.doctor_info = QFrame(self.centralwidget)
        self.doctor_info.setObjectName(u"doctor_info")
        self.doctor_info.setMinimumSize(QSize(1320, 135))
        self.doctor_info.setStyleSheet(u"\n"
"#doctor_info{\n"
"/*padding: 10px;*/\n"
"border-radius: 15px;\n"
"background-color: #f9fafb;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.doctor_info.setFrameShape(QFrame.StyledPanel)
        self.doctor_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.doctor_info)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.doctor_info)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(120, 20))
        self.frame_3.setMaximumSize(QSize(16777215, 42))
        self.frame_3.setStyleSheet(u"border: none;\n"
"background-color: none;")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(50, 25))
        self.label_5.setMaximumSize(QSize(50, 30))
        self.label_5.setStyleSheet(u"border: none;")
        self.label_5.setPixmap(QPixmap(u":/logo/images/doctor_male_40px.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"border: none")

        self.horizontalLayout_4.addWidget(self.label_9)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(22)
        self.gridLayout.setVerticalSpacing(8)
        self.lineEdit = QLineEdit(self.doctor_info)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 9px;\n"
"padding: 8px;\n"
"color: black;\n"
"}")

        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.label_6 = QLabel(self.doctor_info)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 27))
        self.label_6.setMaximumSize(QSize(16777215, 33))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"\n"
"border: none;\n"
"padding: 4px;")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.doctor_info)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 9px;\n"
"padding: 8px;\n"
"color: black;\n"
"}")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.label_7 = QLabel(self.doctor_info)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 27))
        self.label_7.setMaximumSize(QSize(16777215, 33))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"\n"
"border: none;\n"
"padding: 4px;")

        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.doctor_info)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 9px;\n"
"padding: 8px;\n"
"color: black;\n"
"}")

        self.gridLayout.addWidget(self.lineEdit_3, 1, 2, 1, 1)

        self.label_8 = QLabel(self.doctor_info)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 27))
        self.label_8.setMaximumSize(QSize(16777215, 33))
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"\n"
"border: none;\n"
"padding: 4px;")

        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout_4.addWidget(self.doctor_info)

        self.patient_info = QFrame(self.centralwidget)
        self.patient_info.setObjectName(u"patient_info")
        self.patient_info.setMinimumSize(QSize(1323, 258))
        self.patient_info.setMaximumSize(QSize(16777215, 242))
        self.patient_info.setStyleSheet(u"\n"
"#patient_info{\n"
"\n"
"                background-color: #eff6ff; /* bg-blue-50 */\n"
"                border-radius: 8px; /* rounded-lg */\n"
" \n"
"                margin-bottom: 24px; /* mb-6 */\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 9px;\n"
"padding: 8px;\n"
"color: black;\n"
"}\n"
"\n"
"")
        self.patient_info.setFrameShape(QFrame.StyledPanel)
        self.patient_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.patient_info)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.patient_info)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(400, 42))
        self.frame_2.setMaximumSize(QSize(16777215, 32))
        self.frame_2.setStyleSheet(u"border: none;\n"
"background-color: none;\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(52, 31))
        self.label_10.setMaximumSize(QSize(43, 31))
        self.label_10.setStyleSheet(u"border: none;\n"
"                font-size: 1.5em; /* ri-lg */\n"
"                margin-right: 8px; /* mr-2 */\n"
"                color: QColor(0, 123, 255); /* Approximate for text-primary */\n"
"  background-color: #eff6ff;")
        self.label_10.setPixmap(QPixmap(u":/logo/images/user_40px.png"))
        self.label_10.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(120, 20))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"border: none;  \n"
"background-color: #eff6ff;\n"
"")

        self.horizontalLayout_3.addWidget(self.label_11)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(13)
        self.gridLayout_2.setVerticalSpacing(9)
        self.Profession = QLineEdit(self.patient_info)
        self.Profession.setObjectName(u"Profession")
        self.Profession.setMinimumSize(QSize(0, 40))
        self.Profession.setMaximumSize(QSize(16777215, 43))
        font2 = QFont()
        font2.setPointSize(11)
        self.Profession.setFont(font2)

        self.gridLayout_2.addWidget(self.Profession, 1, 2, 1, 1)

        self.label_13 = QLabel(self.patient_info)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 26))
        self.label_13.setMaximumSize(QSize(16777215, 5))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(False)
        self.label_13.setFont(font3)
        self.label_13.setStyleSheet(u"border: none;\n"
"padding: 4px;\n"
"background-color: none;\n"
"                display: block;\n"
"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 500; /* font-medium */\n"
"                color: #4a5568; /* text-gray-700 */\n"
"                margin-bottom: 4px; /* mb-1 */")

        self.gridLayout_2.addWidget(self.label_13, 0, 1, 1, 1)

        self.label_12 = QLabel(self.patient_info)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 27))
        self.label_12.setMaximumSize(QSize(16777215, 2))
        self.label_12.setFont(font3)
        self.label_12.setStyleSheet(u"border: none;\n"
"padding: 6px;\n"
"background-color: none;\n"
"\n"
"                display: block;\n"
"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 500; /* font-medium */\n"
"                color: #4a5568; /* text-gray-700 */\n"
"                margin-bottom: 4px; /* mb-1 */")

        self.gridLayout_2.addWidget(self.label_12, 0, 0, 1, 1)

        self.p_name = QLineEdit(self.patient_info)
        self.p_name.setObjectName(u"p_name")
        self.p_name.setMinimumSize(QSize(0, 40))
        self.p_name.setMaximumSize(QSize(16777215, 40))
        self.p_name.setFont(font2)

        self.gridLayout_2.addWidget(self.p_name, 1, 0, 1, 1)

        self.label_15 = QLabel(self.patient_info)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(0, 28))
        self.label_15.setMaximumSize(QSize(16777215, 8))
        self.label_15.setFont(font3)
        self.label_15.setStyleSheet(u"border: none;\n"
"padding: 6px;\n"
"background-color: none;\n"
"                display: block;\n"
"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 500; /* font-medium */\n"
"                color: #4a5568; /* text-gray-700 */\n"
"                margin-bottom: 4px; /* mb-1 */")

        self.gridLayout_2.addWidget(self.label_15, 0, 3, 1, 1)

        self.p_contact = QLineEdit(self.patient_info)
        self.p_contact.setObjectName(u"p_contact")
        self.p_contact.setMinimumSize(QSize(0, 40))
        self.p_contact.setMaximumSize(QSize(16777215, 40))
        self.p_contact.setFont(font2)

        self.gridLayout_2.addWidget(self.p_contact, 1, 1, 1, 1)

        self.label_14 = QLabel(self.patient_info)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 28))
        self.label_14.setMaximumSize(QSize(16777215, 19))
        self.label_14.setFont(font3)
        self.label_14.setStyleSheet(u"border: none;\n"
"padding: 6px;\n"
"background-color: none;\n"
"                display: block;\n"
"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 500; /* font-medium */\n"
"                color: #4a5568; /* text-gray-700 */\n"
"                margin-bottom: 4px; /* mb-1 */")

        self.gridLayout_2.addWidget(self.label_14, 0, 2, 1, 1)

        self.sex = QLineEdit(self.patient_info)
        self.sex.setObjectName(u"sex")
        self.sex.setMinimumSize(QSize(0, 40))
        self.sex.setMaximumSize(QSize(16777215, 40))
        self.sex.setFont(font2)

        self.gridLayout_2.addWidget(self.sex, 1, 3, 1, 1)

        self.label_16 = QLabel(self.patient_info)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(61, 29))
        self.label_16.setMaximumSize(QSize(22, 1))
        self.label_16.setFont(font3)
        self.label_16.setStyleSheet(u"/*border: none;\n"
"padding: 10px;\n"
"background-color: none;\n"
"                display: block;\n"
"                font-size: 0.875em;  text-sm */\n"
"                /*font-weight: 500;  font-medium */\n"
"               /* color: #4a5568;  text-gray-700 */\n"
"                /*margin-bottom: 4px;  mb-1 */\n"
"\n"
"border: none;\n"
"padding: 3px;\n"
"background-color: none;\n"
"\n"
"                display: block;\n"
"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 500; /* font-medium */\n"
"                color: #4a5568; /* text-gray-700 */\n"
"                margin-bottom: 4px; /* mb-1 */")

        self.gridLayout_2.addWidget(self.label_16, 2, 0, 1, 1)

        self.age = QLineEdit(self.patient_info)
        self.age.setObjectName(u"age")
        self.age.setMinimumSize(QSize(0, 40))
        self.age.setMaximumSize(QSize(16777215, 40))
        self.age.setFont(font2)

        self.gridLayout_2.addWidget(self.age, 3, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.verticalLayout_4.addWidget(self.patient_info)

        self.prescription_info = QFrame(self.centralwidget)
        self.prescription_info.setObjectName(u"prescription_info")
        self.prescription_info.setMinimumSize(QSize(1319, 240))
        self.prescription_info.setMaximumSize(QSize(16777215, 16777215))
        self.prescription_info.setStyleSheet(u"#prescription_info{\n"
"/*padding: 10px;\n"
"border-radius: 15px;*/\n"
"                background-color: none; /*#eff6ff;  bg-blue-50 */\n"
"                border-radius: 8px; /* rounded-lg */\n"
"\n"
"                margin-bottom: 24px; /* mb-6 */\n"
"border: None;\n"
"}")
        self.prescription_info.setFrameShape(QFrame.StyledPanel)
        self.prescription_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.prescription_info)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.prescription_info)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(425, 28))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setStyleSheet(u"border: none;\n"
"background-color: none;\n"
"/*background-color: rgb(85, 255, 255);*/\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(50, 40))
        self.label_17.setMaximumSize(QSize(50, 40))
        self.label_17.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"font-size: 1.5em; /* ri-lg */\n"
"                margin-right: 8px; /* mr-2 */\n"
"                color: QColor(0, 123, 255); /* Approximate for text-primary */")
        self.label_17.setPixmap(QPixmap(u":/logo/images/eye.png"))
        self.label_17.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(120, 9))
        self.label_18.setMaximumSize(QSize(16777215, 23))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        self.label_18.setFont(font4)
        self.label_18.setStyleSheet(u"border: none;\n"
"  background-color: none;\n"
"                font-size: 1.125em; /* text-lg */\n"
"              font-weight: 600;   /* font-semibold */\n"
"                color: #2d3748;  /*text-gray-800 */\n"
"                /*margin-bottom: 12px;  mb-3 \n"
"                display: flex;\n"
"                align-items: center;*/")

        self.horizontalLayout_5.addWidget(self.label_18)


        self.verticalLayout.addWidget(self.frame)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(14)
        self.gridLayout_3.setVerticalSpacing(1)
        self.og_axl = QLineEdit(self.prescription_info)
        self.og_axl.setObjectName(u"og_axl")
        self.og_axl.setMinimumSize(QSize(0, 28))
        font5 = QFont()
        font5.setPointSize(12)
        self.og_axl.setFont(font5)
        self.og_axl.setStyleSheet(u"                width: 100%;\n"
"                padding:  8px; /* px-2 py-1 */\n"
"                border: 1px solid #cbd5e0; /* border-gray-300 */\n"
"                border-radius: 9px; /* rounded-button */\n"
"                font-size: 0.875em; /* text-sm */\n"
"                margin-top: 2px; /* mt-6 */\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")

        self.gridLayout_3.addWidget(self.og_axl, 2, 3, 1, 1)

        self.od_sphere = QLineEdit(self.prescription_info)
        self.od_sphere.setObjectName(u"od_sphere")
        self.od_sphere.setMinimumSize(QSize(0, 28))
        self.od_sphere.setFont(font5)
        self.od_sphere.setStyleSheet(u"                width: 100%;\n"
"                padding:  8px; /* px-2 py-1 */\n"
"                border: 1px solid #cbd5e0; /* border-gray-300 */\n"
"                border-radius: 9px; /* rounded-button */\n"
"                font-size: 0.875em; /* text-sm */\n"
"\n"
"                margin-top: 2px; /* mt-6 */\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")

        self.gridLayout_3.addWidget(self.od_sphere, 1, 1, 1, 1)

        self.label_25 = QLabel(self.prescription_info)
        self.label_25.setObjectName(u"label_25")
        font6 = QFont()
        font6.setBold(False)
        self.label_25.setFont(font6)
        self.label_25.setStyleSheet(u"                padding: 10px; /* px-3 py-3 */\n"
"                white-space: nowrap;\n"
"\n"
"                border-bottom: 1px solid #e5e7eb; /* divide-gray-200 */\n"
"                background-color: white; /* bg-white */\n"
"\n"
"\n"
"  \n"
"                border: none;\n"
"")

        self.gridLayout_3.addWidget(self.label_25, 2, 0, 1, 1)

        self.label_23 = QLabel(self.prescription_info)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 36))
        self.label_23.setMaximumSize(QSize(16777215, 29))
        self.label_23.setStyleSheet(u"                background-color: #f9fafb; /* bg-gray-50 */\n"
"                color: #6b7280; /* text-gray-500 */\n"
"                font-size: 0.75em; /* text-xs */\n"
"                font-weight: 500; /* font-medium */\n"
"                text-align: left;\n"
"                padding: 12px; /* px-3 py-3 */\n"
"                letter-spacing: 0.025em; /* tracking-wider */\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_23, 0, 4, 1, 1)

        self.label_20 = QLabel(self.prescription_info)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 34))
        self.label_20.setMaximumSize(QSize(16777215, 22))
        self.label_20.setStyleSheet(u"                background-color: #f9fafb; /* bg-gray-50 */\n"
"                color: #6b7280; /* text-gray-500 */\n"
"                font-size: 0.75em; /* text-xs */\n"
"                font-weight: 500; /* font-medium */\n"
"                text-align: left;\n"
"                padding: 12px; /* px-3 py-3 */\n"
"                letter-spacing: 0.025em; /* tracking-wider */\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_20, 0, 1, 1, 1)

        self.od_axl = QLineEdit(self.prescription_info)
        self.od_axl.setObjectName(u"od_axl")
        self.od_axl.setMinimumSize(QSize(0, 28))
        self.od_axl.setFont(font5)
        self.od_axl.setStyleSheet(u"                width: 100%;\n"
"                padding:  8px; /* px-2 py-1 */\n"
"                border: 1px solid #cbd5e0; /* border-gray-300 */\n"
"                border-radius: 9px; /* rounded-button */\n"
"                font-size: 0.875em; /* text-sm */\n"
"\n"
"                margin-top: 2px; /* mt-6 */\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")

        self.gridLayout_3.addWidget(self.od_axl, 1, 3, 1, 1)

        self.od_addition = QLineEdit(self.prescription_info)
        self.od_addition.setObjectName(u"od_addition")
        self.od_addition.setMinimumSize(QSize(0, 28))
        self.od_addition.setFont(font5)
        self.od_addition.setStyleSheet(u"                width: 100%;\n"
"                padding:  8px; /* px-2 py-1 */\n"
"                border: 1px solid #cbd5e0; /* border-gray-300 */\n"
"                border-radius: 9px; /* rounded-button */\n"
"                font-size: 0.875em; /* text-sm */\n"
"                margin-top: 2px; /* mt-6 */\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")

        self.gridLayout_3.addWidget(self.od_addition, 1, 4, 1, 1)

        self.label_22 = QLabel(self.prescription_info)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 24))
        self.label_22.setMaximumSize(QSize(16777215, 37))
        self.label_22.setStyleSheet(u"                background-color: #f9fafb; /* bg-gray-50 */\n"
"                color: #6b7280; /* text-gray-500 */\n"
"                font-size: 0.75em; /* text-xs */\n"
"                font-weight: 500; /* font-medium */\n"
"                text-align: left;\n"
"                padding: 12px; /* px-3 py-3 */\n"
"                letter-spacing: 0.025em; /* tracking-wider */\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_22, 0, 3, 1, 1)

        self.og_addition = QLineEdit(self.prescription_info)
        self.og_addition.setObjectName(u"og_addition")
        self.og_addition.setMinimumSize(QSize(0, 28))
        self.og_addition.setFont(font5)
        self.og_addition.setStyleSheet(u"                width: 100%;\n"
"                padding:  8px; /* px-2 py-1 */\n"
"                border: 1px solid #cbd5e0; /* border-gray-300 */\n"
"                border-radius: 9px; /* rounded-button */\n"
"                font-size: 0.875em; /* text-sm */\n"
"                margin-top: 2px; /* mt-6 */\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")

        self.gridLayout_3.addWidget(self.og_addition, 2, 4, 1, 1)

        self.og_cyl = QLineEdit(self.prescription_info)
        self.og_cyl.setObjectName(u"og_cyl")
        self.og_cyl.setMinimumSize(QSize(0, 28))
        self.og_cyl.setFont(font5)
        self.og_cyl.setStyleSheet(u"                width: 100%;\n"
"                padding:  8px; /* px-2 py-1 */\n"
"                border: 1px solid #cbd5e0; /* border-gray-300 */\n"
"                border-radius: 9px; /* rounded-button */\n"
"                font-size: 0.875em; /* text-sm */\n"
"                margin-top: 2px; /* mt-6 */\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")

        self.gridLayout_3.addWidget(self.og_cyl, 2, 2, 1, 1)

        self.od_cyl = QLineEdit(self.prescription_info)
        self.od_cyl.setObjectName(u"od_cyl")
        self.od_cyl.setMinimumSize(QSize(0, 28))
        self.od_cyl.setFont(font5)
        self.od_cyl.setStyleSheet(u"                width: 100%;\n"
"                padding:  8px; /* px-2 py-1 */\n"
"                border: 1px solid #cbd5e0; /* border-gray-300 */\n"
"                border-radius: 9px; /* rounded-button */\n"
"                font-size: 0.875em; /* text-sm */\n"
"                margin-top: 2px; /* mt-6 */\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")

        self.gridLayout_3.addWidget(self.od_cyl, 1, 2, 1, 1)

        self.label_19 = QLabel(self.prescription_info)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 12))
        self.label_19.setMaximumSize(QSize(16777215, 12))
        self.label_19.setStyleSheet(u"                background-color: #f9fafb; /* bg-gray-50 */\n"
"                color: #6b7280; /* text-gray-500 */\n"
"                font-size: 0.75em; /* text-xs */\n"
"                font-weight: 500; /* font-medium */\n"
"                text-align: left;\n"
"                padding: 12px; /* px-3 py-3 */\n"
"                letter-spacing: 0.025em; /* tracking-wider */\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_19, 0, 0, 1, 1)

        self.og_sphere = QLineEdit(self.prescription_info)
        self.og_sphere.setObjectName(u"og_sphere")
        self.og_sphere.setMinimumSize(QSize(0, 28))
        self.og_sphere.setFont(font5)
        self.og_sphere.setStyleSheet(u"                width: 100%;\n"
"                padding:  8px; /* px-2 py-1 */\n"
"                border: 1px solid #cbd5e0; /* border-gray-300 */\n"
"                border-radius: 9px; /* rounded-button */\n"
"                font-size: 0.875em; /* text-sm */\n"
"\n"
"                margin-top: 2px; /* mt-6 */\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")

        self.gridLayout_3.addWidget(self.og_sphere, 2, 1, 1, 1)

        self.label_24 = QLabel(self.prescription_info)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font6)
        self.label_24.setStyleSheet(u"                padding: 10px; /* px-3 py-3 */\n"
"                white-space: nowrap;\n"
"\n"
"                border-bottom: 1px solid #e5e7eb; /* divide-gray-200 */\n"
"                background-color: white; /* bg-white */\n"
"\n"
"\n"
"  \n"
"                border: none;\n"
"\n"
"\n"
"\n"
"                font-weight: 500; /* font-medium */\n"
"")

        self.gridLayout_3.addWidget(self.label_24, 1, 0, 1, 1)

        self.label_21 = QLabel(self.prescription_info)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 20))
        self.label_21.setMaximumSize(QSize(16777215, 36))
        self.label_21.setStyleSheet(u"                background-color: #f9fafb; /* bg-gray-50 */\n"
"                color: #6b7280; /* text-gray-500 */\n"
"                font-size: 0.75em; /* text-xs */\n"
"                font-weight: 500; /* font-medium */\n"
"                text-align: left;\n"
"                padding: 12px; /* px-3 py-3 */\n"
"                letter-spacing: 0.025em; /* tracking-wider */\n"
"border: none;")

        self.gridLayout_3.addWidget(self.label_21, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_3)


        self.verticalLayout_4.addWidget(self.prescription_info)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(1316, 209))
        self.widget.setMaximumSize(QSize(16777215, 227))
        self.widget.setStyleSheet(u"border-radius: 10px;\n"
"border:none;")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.vision_type = QFrame(self.widget)
        self.vision_type.setObjectName(u"vision_type")
        self.vision_type.setMinimumSize(QSize(169, 0))
        self.vision_type.setMaximumSize(QSize(190, 16777215))
        self.vision_type.setFrameShape(QFrame.StyledPanel)
        self.vision_type.setFrameShadow(QFrame.Raised)
        self.label_26 = QLabel(self.vision_type)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(10, 10, 121, 31))
        self.label_26.setFont(font4)
        self.label_26.setStyleSheet(u"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 900; /* font-medium */\n"
"                color: #4a5568; /* text-gray-700 */\n"
"                margin-bottom: 8px; /* mb-2 */\n"
"border: none;")
        self.checkBox = QCheckBox(self.vision_type)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(10, 50, 121, 20))
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"                display: flex;\n"
"                align-items: center;\n"
"                justify-content: center;")
        self.checkBox_2 = QCheckBox(self.vision_type)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(10, 80, 121, 20))
        self.checkBox_2.setFont(font)
        self.checkBox_2.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"                display: flex;\n"
"                align-items: center;\n"
"                justify-content: center;")
        self.checkBox_3 = QCheckBox(self.vision_type)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(10, 110, 121, 20))
        self.checkBox_3.setFont(font)
        self.checkBox_3.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"                display: flex;\n"
"                align-items: center;\n"
"                justify-content: center;")
        self.checkBox_4 = QCheckBox(self.vision_type)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(10, 140, 121, 20))
        self.checkBox_4.setFont(font)
        self.checkBox_4.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"                display: flex;\n"
"                align-items: center;\n"
"                justify-content: center;")

        self.horizontalLayout_2.addWidget(self.vision_type)

        self.lens_type = QFrame(self.widget)
        self.lens_type.setObjectName(u"lens_type")
        self.lens_type.setMinimumSize(QSize(172, 0))
        self.lens_type.setMaximumSize(QSize(181, 16777215))
        self.lens_type.setFrameShape(QFrame.StyledPanel)
        self.lens_type.setFrameShadow(QFrame.Raised)
        self.label_27 = QLabel(self.lens_type)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(10, 10, 121, 31))
        self.label_27.setFont(font4)
        self.label_27.setStyleSheet(u"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 900; /* font-medium */\n"
"                color: #4a5568; /* text-gray-700 */\n"
"                margin-bottom: 8px; /* mb-2 */\n"
"border: none;")
        self.checkBox_5 = QCheckBox(self.lens_type)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(10, 50, 121, 20))
        self.checkBox_5.setFont(font)
        self.checkBox_5.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"                display: flex;\n"
"                align-items: center;\n"
"                justify-content: center;")
        self.checkBox_6 = QCheckBox(self.lens_type)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(10, 80, 121, 20))
        self.checkBox_6.setFont(font)
        self.checkBox_6.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"                display: flex;\n"
"                align-items: center;\n"
"                justify-content: center;")
        self.checkBox_7 = QCheckBox(self.lens_type)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(10, 110, 121, 20))
        self.checkBox_7.setFont(font)
        self.checkBox_7.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"                display: flex;\n"
"                align-items: center;\n"
"                justify-content: center;")

        self.horizontalLayout_2.addWidget(self.lens_type)

        self.tine_option = QFrame(self.widget)
        self.tine_option.setObjectName(u"tine_option")
        self.tine_option.setMinimumSize(QSize(160, 0))
        self.tine_option.setMaximumSize(QSize(170, 16777215))
        self.tine_option.setFrameShape(QFrame.StyledPanel)
        self.tine_option.setFrameShadow(QFrame.Raised)
        self.label_30 = QLabel(self.tine_option)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 10, 121, 31))
        self.label_30.setFont(font4)
        self.label_30.setStyleSheet(u"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 900; /* font-medium */\n"
"                color: #4a5568; /* text-gray-700 */\n"
"                margin-bottom: 8px; /* mb-2 */\n"
"border: none;")
        self.checkBox_16 = QCheckBox(self.tine_option)
        self.checkBox_16.setObjectName(u"checkBox_16")
        self.checkBox_16.setGeometry(QRect(10, 50, 121, 20))
        self.checkBox_16.setFont(font)
        self.checkBox_16.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"                display: flex;\n"
"                align-items: center;\n"
"                justify-content: center;")
        self.checkBox_17 = QCheckBox(self.tine_option)
        self.checkBox_17.setObjectName(u"checkBox_17")
        self.checkBox_17.setGeometry(QRect(10, 80, 121, 20))
        self.checkBox_17.setFont(font)
        self.checkBox_17.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"                display: flex;\n"
"                align-items: center;\n"
"                justify-content: center;")
        self.checkBox_18 = QCheckBox(self.tine_option)
        self.checkBox_18.setObjectName(u"checkBox_18")
        self.checkBox_18.setGeometry(QRect(10, 110, 121, 20))
        self.checkBox_18.setFont(font)
        self.checkBox_18.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"                display: flex;\n"
"                align-items: center;\n"
"                justify-content: center;")
        self.checkBox_19 = QCheckBox(self.tine_option)
        self.checkBox_19.setObjectName(u"checkBox_19")
        self.checkBox_19.setGeometry(QRect(10, 140, 121, 20))
        self.checkBox_19.setFont(font)
        self.checkBox_19.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"                display: flex;\n"
"                align-items: center;\n"
"                justify-content: center;")
        self.checkBox_20 = QCheckBox(self.tine_option)
        self.checkBox_20.setObjectName(u"checkBox_20")
        self.checkBox_20.setGeometry(QRect(10, 170, 131, 20))
        self.checkBox_20.setFont(font)
        self.checkBox_20.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"                display: flex;\n"
"                align-items: center;\n"
"                justify-content: center;")

        self.horizontalLayout_2.addWidget(self.tine_option)

        self.focus_type = QFrame(self.widget)
        self.focus_type.setObjectName(u"focus_type")
        self.focus_type.setMinimumSize(QSize(160, 0))
        self.focus_type.setMaximumSize(QSize(170, 16777215))
        self.focus_type.setFrameShape(QFrame.StyledPanel)
        self.focus_type.setFrameShadow(QFrame.Raised)
        self.label_32 = QLabel(self.focus_type)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 10, 121, 31))
        self.label_32.setFont(font4)
        self.label_32.setStyleSheet(u"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 900; /* font-medium */\n"
"                color: #4a5568; /* text-gray-700 */\n"
"                margin-bottom: 8px; /* mb-2 */\n"
"border: none;")
        self.checkBox_26 = QCheckBox(self.focus_type)
        self.checkBox_26.setObjectName(u"checkBox_26")
        self.checkBox_26.setGeometry(QRect(10, 50, 121, 20))
        self.checkBox_26.setFont(font)
        self.checkBox_26.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"                display: flex;\n"
"                align-items: center;\n"
"                justify-content: center;")
        self.checkBox_27 = QCheckBox(self.focus_type)
        self.checkBox_27.setObjectName(u"checkBox_27")
        self.checkBox_27.setGeometry(QRect(10, 80, 121, 20))
        self.checkBox_27.setFont(font)
        self.checkBox_27.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"                display: flex;\n"
"                align-items: center;\n"
"                justify-content: center;")
        self.checkBox_28 = QCheckBox(self.focus_type)
        self.checkBox_28.setObjectName(u"checkBox_28")
        self.checkBox_28.setGeometry(QRect(10, 110, 121, 20))
        self.checkBox_28.setFont(font)
        self.checkBox_28.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"                display: flex;\n"
"                align-items: center;\n"
"                justify-content: center;")

        self.horizontalLayout_2.addWidget(self.focus_type)

        self.port_type = QFrame(self.widget)
        self.port_type.setObjectName(u"port_type")
        self.port_type.setMinimumSize(QSize(155, 0))
        self.port_type.setMaximumSize(QSize(164, 16777215))
        self.port_type.setFrameShape(QFrame.StyledPanel)
        self.port_type.setFrameShadow(QFrame.Raised)
        self.label_33 = QLabel(self.port_type)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(10, 10, 121, 31))
        self.label_33.setFont(font4)
        self.label_33.setStyleSheet(u"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 900; /* font-medium */\n"
"                color: #4a5568; /* text-gray-700 */\n"
"                margin-bottom: 8px; /* mb-2 */\n"
"border: none;")
        self.checkBox_29 = QCheckBox(self.port_type)
        self.checkBox_29.setObjectName(u"checkBox_29")
        self.checkBox_29.setGeometry(QRect(10, 50, 121, 20))
        self.checkBox_29.setFont(font)
        self.checkBox_29.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"                display: flex;\n"
"                align-items: center;\n"
"                justify-content: center;")
        self.checkBox_30 = QCheckBox(self.port_type)
        self.checkBox_30.setObjectName(u"checkBox_30")
        self.checkBox_30.setGeometry(QRect(10, 80, 121, 20))
        self.checkBox_30.setFont(font)
        self.checkBox_30.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"                display: flex;\n"
"                align-items: center;\n"
"                justify-content: center;")

        self.horizontalLayout_2.addWidget(self.port_type)

        self.port_type_2 = QFrame(self.widget)
        self.port_type_2.setObjectName(u"port_type_2")
        self.port_type_2.setMinimumSize(QSize(157, 0))
        self.port_type_2.setMaximumSize(QSize(165, 16777215))
        self.port_type_2.setFrameShape(QFrame.StyledPanel)
        self.port_type_2.setFrameShadow(QFrame.Raised)
        self.label_34 = QLabel(self.port_type_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(10, 10, 121, 31))
        self.label_34.setFont(font4)
        self.label_34.setStyleSheet(u"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 900; /* font-medium */\n"
"                color: #4a5568; /* text-gray-700 */\n"
"                margin-bottom: 8px; /* mb-2 */\n"
"border: none;")
        self.checkBox_31 = QCheckBox(self.port_type_2)
        self.checkBox_31.setObjectName(u"checkBox_31")
        self.checkBox_31.setGeometry(QRect(10, 50, 121, 20))
        self.checkBox_31.setFont(font)
        self.checkBox_31.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"                display: flex;\n"
"                align-items: center;\n"
"                justify-content: center;")
        self.checkBox_32 = QCheckBox(self.port_type_2)
        self.checkBox_32.setObjectName(u"checkBox_32")
        self.checkBox_32.setGeometry(QRect(10, 80, 121, 20))
        self.checkBox_32.setFont(font)
        self.checkBox_32.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"                display: flex;\n"
"                align-items: center;\n"
"                justify-content: center;")

        self.horizontalLayout_2.addWidget(self.port_type_2)


        self.verticalLayout_4.addWidget(self.widget)

        self.action_button = QFrame(self.centralwidget)
        self.action_button.setObjectName(u"action_button")
        self.action_button.setMinimumSize(QSize(767, 79))
        self.action_button.setMaximumSize(QSize(500, 62))
        self.action_button.setStyleSheet(u"\n"
"border-radius: 10px;\n"
"border: None;\n"
"  ")
        self.action_button.setFrameShape(QFrame.StyledPanel)
        self.action_button.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.action_button)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.save_btn = QPushButton(self.action_button)
        self.save_btn.setObjectName(u"save_btn")
        font7 = QFont()
        font7.setBold(True)
        self.save_btn.setFont(font7)
        self.save_btn.setStyleSheet(u"                padding: 8px 16px; /* px-4 py-2 */\n"
"                border-radius: 4px; /* rounded-button */\n"
"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 1000; /* font-medium */\n"
"                white-space: nowrap;\n"
"                border: none;\n"
"background-color: rgb(163, 163, 163);")
        icon = QIcon()
        icon.addFile(u":/logo/images/save_40px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_btn.setIcon(icon)
        self.save_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.save_btn)

        self.preview_btn = QPushButton(self.action_button)
        self.preview_btn.setObjectName(u"preview_btn")
        self.preview_btn.setFont(font7)
        self.preview_btn.setStyleSheet(u"                padding: 8px 16px; /* px-4 py-2 */\n"
"                border-radius: 4px; /* rounded-button */\n"
"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 1000; /* font-medium */\n"
"                white-space: nowrap;\n"
"                border: none;\n"
"background-color: rgb(163, 163, 163);")
        icon1 = QIcon()
        icon1.addFile(u":/logo/images/fine_print_48px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.preview_btn.setIcon(icon1)
        self.preview_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.preview_btn)

        self.clear_btn = QPushButton(self.action_button)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setFont(font7)
        self.clear_btn.setStyleSheet(u"                padding: 10px; /* px-4 py-2 */\n"
"                border-radius: 4px; /* rounded-button */\n"
"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 1000; /* font-medium */\n"
"                white-space: nowrap;\n"
"                border: none;\n"
"background-color: rgb(163, 163, 163);")
        icon2 = QIcon()
        icon2.addFile(u":/logo/images/clear_symbol_64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clear_btn.setIcon(icon2)
        self.clear_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.clear_btn)

        self.print_btn = QPushButton(self.action_button)
        self.print_btn.setObjectName(u"print_btn")
        self.print_btn.setFont(font7)
        self.print_btn.setStyleSheet(u"                padding: 10px; /* px-4 py-2 */\n"
"                border-radius: 4px; /* rounded-button */\n"
"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 1000; /* font-medium */\n"
"                white-space: nowrap;\n"
"                border: none;\n"
"background-color: rgb(163, 163, 163);")
        icon3 = QIcon()
        icon3.addFile(u":/logo/images/print_48px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.print_btn.setIcon(icon3)
        self.print_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.print_btn)


        self.verticalLayout_4.addWidget(self.action_button, 0, Qt.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ref No:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"xxxxxxxxxxxx", None))
        self.label_5.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Doctor Information", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Doctor Name", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Registration No.", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Specialization", None))
        self.label_10.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Patient Information", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Pateint Name", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Sex", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Profession", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Age", None))
        self.label_17.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Optical Prescription Details", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"OG (Left)", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"ADDITION", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"SPHERE", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"AXL", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"EYE", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"OD (Right)", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"CYL", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Vision Type", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Myopie", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Hypermetropie", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Astigmatisme", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Emmetropie", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Lens Type", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"Mineraux", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"Organiques", None))
        self.checkBox_7.setText(QCoreApplication.translate("MainWindow", u"Polycarbonates", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Tint Options", None))
        self.checkBox_16.setText(QCoreApplication.translate("MainWindow", u"Blanc", None))
        self.checkBox_17.setText(QCoreApplication.translate("MainWindow", u"Gris", None))
        self.checkBox_18.setText(QCoreApplication.translate("MainWindow", u"Antireflet", None))
        self.checkBox_19.setText(QCoreApplication.translate("MainWindow", u"Bleue protect", None))
        self.checkBox_20.setText(QCoreApplication.translate("MainWindow", u"Photochromique", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Focus Type", None))
        self.checkBox_26.setText(QCoreApplication.translate("MainWindow", u"Unifocaux", None))
        self.checkBox_27.setText(QCoreApplication.translate("MainWindow", u"Bifocaux", None))
        self.checkBox_28.setText(QCoreApplication.translate("MainWindow", u"Progressifs", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Port Type", None))
        self.checkBox_29.setText(QCoreApplication.translate("MainWindow", u"Constant", None))
        self.checkBox_30.setText(QCoreApplication.translate("MainWindow", u"Lecture", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Index Type", None))
        self.checkBox_31.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.checkBox_32.setText(QCoreApplication.translate("MainWindow", u"Fort indice", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.preview_btn.setText(QCoreApplication.translate("MainWindow", u"preview", None))
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.print_btn.setText(QCoreApplication.translate("MainWindow", u"print", None))
    # retranslateUi

