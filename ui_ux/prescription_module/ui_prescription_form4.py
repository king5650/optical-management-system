# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prescription_formZfEMrj.ui'
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
        self.centralwidget.setStyleSheet(u"border: 2px solid #d1d5db;\n"
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

        self.refferenceID = QLabel(self.date_ref)
        self.refferenceID.setObjectName(u"refferenceID")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.refferenceID.setFont(font)
        self.refferenceID.setStyleSheet(u"\n"
"border: none;\n"
"padding: 10px;\n"
"\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 9px;\n"
"padding: 8px;\n"
"color: black;\n"
"\n"
"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.refferenceID)


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
        self.label_9.setStyleSheet(u"border: none;\n"
"                font-size: 1.125em; /* text-lg */\n"
"              font-weight: 700;   /* font-semibold */\n"
"                color: #2d3748;  /*text-gray-800 */")

        self.horizontalLayout_4.addWidget(self.label_9)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(22)
        self.gridLayout.setVerticalSpacing(8)
        self.doc_name = QLineEdit(self.doctor_info)
        self.doc_name.setObjectName(u"doc_name")
        self.doc_name.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 9px;\n"
"padding: 8px;\n"
"color: black;\n"
"}")

        self.gridLayout.addWidget(self.doc_name, 1, 0, 1, 1)

        self.label_6 = QLabel(self.doctor_info)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 27))
        self.label_6.setMaximumSize(QSize(16777215, 33))
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"\n"
"border: none;\n"
"padding: 4px;")

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.reg_no = QLineEdit(self.doctor_info)
        self.reg_no.setObjectName(u"reg_no")
        self.reg_no.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 9px;\n"
"padding: 8px;\n"
"color: black;\n"
"}")

        self.gridLayout.addWidget(self.reg_no, 1, 1, 1, 1)

        self.label_7 = QLabel(self.doctor_info)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 27))
        self.label_7.setMaximumSize(QSize(16777215, 33))
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"\n"
"border: none;\n"
"padding: 4px;")

        self.gridLayout.addWidget(self.label_7, 0, 1, 1, 1)

        self.specialization = QLineEdit(self.doctor_info)
        self.specialization.setObjectName(u"specialization")
        self.specialization.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 9px;\n"
"padding: 8px;\n"
"color: black;\n"
"}")

        self.gridLayout.addWidget(self.specialization, 1, 2, 1, 1)

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
"               background-color: #eff6ff; /* bg-blue-50 */\n"
"                border-radius: 8px; /* rounded-lg */\n"
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
"border: none;\n"
"\n"
"                font-size: 1.125em; /* text-lg */\n"
"              font-weight: 700;   /* font-semibold */\n"
"                color: #2d3748;  /*text-gray-800 */")

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
"\n"
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
"\n"
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
        self.label_16.setStyleSheet(u"\n"
"\n"
"border: none;\n"
"padding: 3px;\n"
"background-color: none;\n"
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
"                background-color: none; /*#eff6ff;  bg-blue-50 */\n"
"                border-radius: 8px; /* rounded-lg */\n"
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
"              font-weight: 700;   /* font-semibold */\n"
"                color: #2d3748;  /*text-gray-800 */\n"
"")

        self.horizontalLayout_5.addWidget(self.label_18)


        self.verticalLayout.addWidget(self.frame)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(14)
        self.gridLayout_3.setVerticalSpacing(1)
        self.axe_og = QLineEdit(self.prescription_info)
        self.axe_og.setObjectName(u"axe_og")
        self.axe_og.setMinimumSize(QSize(0, 28))
        font5 = QFont()
        font5.setPointSize(12)
        self.axe_og.setFont(font5)
        self.axe_og.setStyleSheet(u"                width: 100%;\n"
"                padding:  8px; /* px-2 py-1 */\n"
"                border: 1px solid #cbd5e0; /* border-gray-300 */\n"
"                border-radius: 9px; /* rounded-button */\n"
"                font-size: 0.875em; /* text-sm */\n"
"                margin-top: 2px; /* mt-6 */\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")

        self.gridLayout_3.addWidget(self.axe_og, 2, 3, 1, 1)

        self.sphere_od = QLineEdit(self.prescription_info)
        self.sphere_od.setObjectName(u"sphere_od")
        self.sphere_od.setMinimumSize(QSize(0, 28))
        self.sphere_od.setFont(font5)
        self.sphere_od.setStyleSheet(u"                width: 100%;\n"
"                padding:  8px; /* px-2 py-1 */\n"
"                border: 1px solid #cbd5e0; /* border-gray-300 */\n"
"                border-radius: 9px; /* rounded-button */\n"
"                font-size: 0.875em; /* text-sm */\n"
"                margin-top: 2px; /* mt-6 */\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")

        self.gridLayout_3.addWidget(self.sphere_od, 1, 1, 1, 1)

        self.label_25 = QLabel(self.prescription_info)
        self.label_25.setObjectName(u"label_25")
        font6 = QFont()
        font6.setBold(True)
        self.label_25.setFont(font6)
        self.label_25.setStyleSheet(u"                padding: 10px; /* px-3 py-3 */\n"
"                white-space: nowrap;\n"
"				color: black;\n"
"                border-bottom: 1px solid #e5e7eb; /* divide-gray-200 */\n"
"                background-color: white; /* bg-white */\n"
"                border: none;\n"
"                font-weight: 900; /* font-medium */")

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

        self.axe_od = QLineEdit(self.prescription_info)
        self.axe_od.setObjectName(u"axe_od")
        self.axe_od.setMinimumSize(QSize(0, 28))
        self.axe_od.setFont(font5)
        self.axe_od.setStyleSheet(u"                width: 100%;\n"
"                padding:  8px; /* px-2 py-1 */\n"
"                border: 1px solid #cbd5e0; /* border-gray-300 */\n"
"                border-radius: 9px; /* rounded-button */\n"
"                font-size: 0.875em; /* text-sm */\n"
"                margin-top: 2px; /* mt-6 */\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")

        self.gridLayout_3.addWidget(self.axe_od, 1, 3, 1, 1)

        self.addition_od = QLineEdit(self.prescription_info)
        self.addition_od.setObjectName(u"addition_od")
        self.addition_od.setMinimumSize(QSize(0, 28))
        self.addition_od.setFont(font5)
        self.addition_od.setStyleSheet(u"                width: 100%;\n"
"                padding:  8px; /* px-2 py-1 */\n"
"                border: 1px solid #cbd5e0; /* border-gray-300 */\n"
"                border-radius: 9px; /* rounded-button */\n"
"                font-size: 0.875em; /* text-sm */\n"
"                margin-top: 2px; /* mt-6 */\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")

        self.gridLayout_3.addWidget(self.addition_od, 1, 4, 1, 1)

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

        self.addition_og = QLineEdit(self.prescription_info)
        self.addition_og.setObjectName(u"addition_og")
        self.addition_og.setMinimumSize(QSize(0, 28))
        self.addition_og.setFont(font5)
        self.addition_og.setStyleSheet(u"                width: 100%;\n"
"                padding:  8px; /* px-2 py-1 */\n"
"                border: 1px solid #cbd5e0; /* border-gray-300 */\n"
"                border-radius: 9px; /* rounded-button */\n"
"                font-size: 0.875em; /* text-sm */\n"
"                margin-top: 2px; /* mt-6 */\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")

        self.gridLayout_3.addWidget(self.addition_og, 2, 4, 1, 1)

        self.cyl_og = QLineEdit(self.prescription_info)
        self.cyl_og.setObjectName(u"cyl_og")
        self.cyl_og.setMinimumSize(QSize(0, 28))
        self.cyl_og.setFont(font5)
        self.cyl_og.setStyleSheet(u"                width: 100%;\n"
"                padding:  8px; /* px-2 py-1 */\n"
"                border: 1px solid #cbd5e0; /* border-gray-300 */\n"
"                border-radius: 9px; /* rounded-button */\n"
"                font-size: 0.875em; /* text-sm */\n"
"                margin-top: 2px; /* mt-6 */\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")

        self.gridLayout_3.addWidget(self.cyl_og, 2, 2, 1, 1)

        self.cyl_od = QLineEdit(self.prescription_info)
        self.cyl_od.setObjectName(u"cyl_od")
        self.cyl_od.setMinimumSize(QSize(0, 28))
        self.cyl_od.setFont(font5)
        self.cyl_od.setStyleSheet(u"                width: 100%;\n"
"                padding:  8px; /* px-2 py-1 */\n"
"                border: 1px solid #cbd5e0; /* border-gray-300 */\n"
"                border-radius: 9px; /* rounded-button */\n"
"                font-size: 0.875em; /* text-sm */\n"
"                margin-top: 2px; /* mt-6 */\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")

        self.gridLayout_3.addWidget(self.cyl_od, 1, 2, 1, 1)

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

        self.sphere_og = QLineEdit(self.prescription_info)
        self.sphere_og.setObjectName(u"sphere_og")
        self.sphere_og.setMinimumSize(QSize(0, 28))
        self.sphere_og.setFont(font5)
        self.sphere_og.setStyleSheet(u"                width: 100%;\n"
"                padding:  8px; /* px-2 py-1 */\n"
"                border: 1px solid #cbd5e0; /* border-gray-300 */\n"
"                border-radius: 9px; /* rounded-button */\n"
"                font-size: 0.875em; /* text-sm */\n"
"\n"
"                margin-top: 2px; /* mt-6 */\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;")

        self.gridLayout_3.addWidget(self.sphere_og, 2, 1, 1, 1)

        self.label_24 = QLabel(self.prescription_info)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font6)
        self.label_24.setStyleSheet(u"                padding: 10px; /* px-3 py-3 */\n"
"                white-space: nowrap;\n"
"				color: black;\n"
"                border-bottom: 1px solid #e5e7eb; /* divide-gray-200 */\n"
"                background-color: white; /* bg-white */\n"
"                border: none;\n"
"                font-weight: 900; /* font-medium */\n"
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
        self.vision_type.setStyleSheet(u"\n"
"				color: black;\n"
"\n"
"                font-weight: 800; /* font-medium */")
        self.vision_type.setFrameShape(QFrame.StyledPanel)
        self.vision_type.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.vision_type)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_26 = QLabel(self.vision_type)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font4)
        self.label_26.setStyleSheet(u"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 900; /* font-medium */\n"
"                color: #4a5568; /* text-gray-700 */\n"
"                margin-bottom: 8px; /* mb-2 */\n"
"border: none;")

        self.verticalLayout_6.addWidget(self.label_26)

        self.Myopie = QCheckBox(self.vision_type)
        self.Myopie.setObjectName(u"Myopie")
        self.Myopie.setFont(font)
        self.Myopie.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"")

        self.verticalLayout_6.addWidget(self.Myopie)

        self.Hypermetropie = QCheckBox(self.vision_type)
        self.Hypermetropie.setObjectName(u"Hypermetropie")
        self.Hypermetropie.setFont(font)
        self.Hypermetropie.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"")

        self.verticalLayout_6.addWidget(self.Hypermetropie)

        self.Astigmatisme = QCheckBox(self.vision_type)
        self.Astigmatisme.setObjectName(u"Astigmatisme")
        self.Astigmatisme.setFont(font)
        self.Astigmatisme.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"")

        self.verticalLayout_6.addWidget(self.Astigmatisme)

        self.Emmetropie = QCheckBox(self.vision_type)
        self.Emmetropie.setObjectName(u"Emmetropie")
        self.Emmetropie.setFont(font)
        self.Emmetropie.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"")

        self.verticalLayout_6.addWidget(self.Emmetropie)

        self.presbytie = QCheckBox(self.vision_type)
        self.presbytie.setObjectName(u"presbytie")
        self.presbytie.setFont(font)
        self.presbytie.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */")

        self.verticalLayout_6.addWidget(self.presbytie)


        self.horizontalLayout_2.addWidget(self.vision_type)

        self.lens_type = QFrame(self.widget)
        self.lens_type.setObjectName(u"lens_type")
        self.lens_type.setMinimumSize(QSize(172, 0))
        self.lens_type.setMaximumSize(QSize(181, 16777215))
        self.lens_type.setStyleSheet(u"\n"
"				color: black;\n"
"\n"
"                font-weight: 800; /* font-medium */")
        self.lens_type.setFrameShape(QFrame.StyledPanel)
        self.lens_type.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.lens_type)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_27 = QLabel(self.lens_type)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font4)
        self.label_27.setStyleSheet(u"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 900; /* font-medium */\n"
"                color: #4a5568; /* text-gray-700 */\n"
"                margin-bottom: 8px; /* mb-2 */\n"
"border: none;")

        self.verticalLayout_7.addWidget(self.label_27)

        self.Mineraux = QCheckBox(self.lens_type)
        self.Mineraux.setObjectName(u"Mineraux")
        self.Mineraux.setFont(font)
        self.Mineraux.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"")

        self.verticalLayout_7.addWidget(self.Mineraux)

        self.Organiques = QCheckBox(self.lens_type)
        self.Organiques.setObjectName(u"Organiques")
        self.Organiques.setFont(font)
        self.Organiques.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"")

        self.verticalLayout_7.addWidget(self.Organiques)

        self.Polycarbonates = QCheckBox(self.lens_type)
        self.Polycarbonates.setObjectName(u"Polycarbonates")
        self.Polycarbonates.setFont(font)
        self.Polycarbonates.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"")

        self.verticalLayout_7.addWidget(self.Polycarbonates)


        self.horizontalLayout_2.addWidget(self.lens_type)

        self.tine_option = QFrame(self.widget)
        self.tine_option.setObjectName(u"tine_option")
        self.tine_option.setMinimumSize(QSize(160, 0))
        self.tine_option.setMaximumSize(QSize(170, 16777215))
        self.tine_option.setStyleSheet(u"\n"
"				color: black;\n"
"\n"
"                font-weight: 800; /* font-medium */")
        self.tine_option.setFrameShape(QFrame.StyledPanel)
        self.tine_option.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.tine_option)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_30 = QLabel(self.tine_option)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font4)
        self.label_30.setStyleSheet(u"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 900; /* font-medium */\n"
"                color: #4a5568; /* text-gray-700 */\n"
"                margin-bottom: 8px; /* mb-2 */\n"
"border: none;")

        self.verticalLayout_8.addWidget(self.label_30)

        self.Blanc = QCheckBox(self.tine_option)
        self.Blanc.setObjectName(u"Blanc")
        self.Blanc.setFont(font)
        self.Blanc.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"")

        self.verticalLayout_8.addWidget(self.Blanc)

        self.Gris = QCheckBox(self.tine_option)
        self.Gris.setObjectName(u"Gris")
        self.Gris.setFont(font)
        self.Gris.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
" ")

        self.verticalLayout_8.addWidget(self.Gris)

        self.Antireflet = QCheckBox(self.tine_option)
        self.Antireflet.setObjectName(u"Antireflet")
        self.Antireflet.setFont(font)
        self.Antireflet.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"")

        self.verticalLayout_8.addWidget(self.Antireflet)

        self.bleue_protect = QCheckBox(self.tine_option)
        self.bleue_protect.setObjectName(u"bleue_protect")
        self.bleue_protect.setFont(font)
        self.bleue_protect.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"")

        self.verticalLayout_8.addWidget(self.bleue_protect)

        self.Photochromique = QCheckBox(self.tine_option)
        self.Photochromique.setObjectName(u"Photochromique")
        self.Photochromique.setFont(font)
        self.Photochromique.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
" ")

        self.verticalLayout_8.addWidget(self.Photochromique)


        self.horizontalLayout_2.addWidget(self.tine_option)

        self.focus_type = QFrame(self.widget)
        self.focus_type.setObjectName(u"focus_type")
        self.focus_type.setMinimumSize(QSize(160, 0))
        self.focus_type.setMaximumSize(QSize(170, 16777215))
        self.focus_type.setStyleSheet(u"\n"
"				color: black;\n"
"\n"
"                font-weight: 800; /* font-medium */")
        self.focus_type.setFrameShape(QFrame.StyledPanel)
        self.focus_type.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.focus_type)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_32 = QLabel(self.focus_type)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font4)
        self.label_32.setStyleSheet(u"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 900; /* font-medium */\n"
"                color: #4a5568; /* text-gray-700 */\n"
"                margin-bottom: 8px; /* mb-2 */\n"
"border: none;")

        self.verticalLayout_9.addWidget(self.label_32)

        self.Unifocaux = QCheckBox(self.focus_type)
        self.Unifocaux.setObjectName(u"Unifocaux")
        self.Unifocaux.setFont(font)
        self.Unifocaux.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"")

        self.verticalLayout_9.addWidget(self.Unifocaux)

        self.Bifocaux = QCheckBox(self.focus_type)
        self.Bifocaux.setObjectName(u"Bifocaux")
        self.Bifocaux.setFont(font)
        self.Bifocaux.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
" ")

        self.verticalLayout_9.addWidget(self.Bifocaux)

        self.Progressifs = QCheckBox(self.focus_type)
        self.Progressifs.setObjectName(u"Progressifs")
        self.Progressifs.setFont(font)
        self.Progressifs.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"      ")

        self.verticalLayout_9.addWidget(self.Progressifs)


        self.horizontalLayout_2.addWidget(self.focus_type)

        self.port_type = QFrame(self.widget)
        self.port_type.setObjectName(u"port_type")
        self.port_type.setMinimumSize(QSize(155, 0))
        self.port_type.setMaximumSize(QSize(164, 16777215))
        self.port_type.setStyleSheet(u"\n"
"				color: black;\n"
"\n"
"                font-weight: 800; /* font-medium */")
        self.port_type.setFrameShape(QFrame.StyledPanel)
        self.port_type.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.port_type)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_33 = QLabel(self.port_type)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font4)
        self.label_33.setStyleSheet(u"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 900; /* font-medium */\n"
"                color: #4a5568; /* text-gray-700 */\n"
"                margin-bottom: 8px; /* mb-2 */\n"
"border: none;")

        self.verticalLayout_10.addWidget(self.label_33)

        self.Constant = QCheckBox(self.port_type)
        self.Constant.setObjectName(u"Constant")
        self.Constant.setFont(font)
        self.Constant.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"")

        self.verticalLayout_10.addWidget(self.Constant)

        self.Lecture = QCheckBox(self.port_type)
        self.Lecture.setObjectName(u"Lecture")
        self.Lecture.setFont(font)
        self.Lecture.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"")

        self.verticalLayout_10.addWidget(self.Lecture)


        self.horizontalLayout_2.addWidget(self.port_type)

        self.port_type_2 = QFrame(self.widget)
        self.port_type_2.setObjectName(u"port_type_2")
        self.port_type_2.setMinimumSize(QSize(157, 0))
        self.port_type_2.setMaximumSize(QSize(165, 16777215))
        self.port_type_2.setStyleSheet(u"\n"
"				color: black;\n"
"\n"
"                font-weight: 800; /* font-medium */")
        self.port_type_2.setFrameShape(QFrame.StyledPanel)
        self.port_type_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.port_type_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_34 = QLabel(self.port_type_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font4)
        self.label_34.setStyleSheet(u"                font-size: 0.875em; /* text-sm */\n"
"                font-weight: 900; /* font-medium */\n"
"                color: #4a5568; /* text-gray-700 */\n"
"                margin-bottom: 8px; /* mb-2 */\n"
"border: none;")

        self.verticalLayout_11.addWidget(self.label_34)

        self.Normal = QCheckBox(self.port_type_2)
        self.Normal.setObjectName(u"Normal")
        self.Normal.setFont(font)
        self.Normal.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"")

        self.verticalLayout_11.addWidget(self.Normal)

        self.fort_indice = QCheckBox(self.port_type_2)
        self.fort_indice.setObjectName(u"fort_indice")
        self.fort_indice.setFont(font)
        self.fort_indice.setStyleSheet(u"                width: 16px;\n"
"                height: 16px;\n"
"                border: none; /* 1px solid #9ca3af; border-gray-400 or similar */\n"
"                border-radius: 4px;\n"
"                margin-right: 8px; /* mr-2 */\n"
"")

        self.verticalLayout_11.addWidget(self.fort_indice)


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
        self.save_btn.setFont(font6)
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
        self.preview_btn.setFont(font6)
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
        self.clear_btn.setFont(font6)
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
        self.print_btn.setFont(font6)
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
        self.refferenceID.setText(QCoreApplication.translate("MainWindow", u"xxxxxxxxxxxx", None))
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
        self.Myopie.setText(QCoreApplication.translate("MainWindow", u"Myopie", None))
        self.Hypermetropie.setText(QCoreApplication.translate("MainWindow", u"Hypermetropie", None))
        self.Astigmatisme.setText(QCoreApplication.translate("MainWindow", u"Astigmatisme", None))
        self.Emmetropie.setText(QCoreApplication.translate("MainWindow", u"Emmetropie", None))
        self.presbytie.setText(QCoreApplication.translate("MainWindow", u"Presbytie", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Lens Type", None))
        self.Mineraux.setText(QCoreApplication.translate("MainWindow", u"Mineraux", None))
        self.Organiques.setText(QCoreApplication.translate("MainWindow", u"Organiques", None))
        self.Polycarbonates.setText(QCoreApplication.translate("MainWindow", u"Polycarbonates", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Tint Options", None))
        self.Blanc.setText(QCoreApplication.translate("MainWindow", u"Blanc", None))
        self.Gris.setText(QCoreApplication.translate("MainWindow", u"Gris", None))
        self.Antireflet.setText(QCoreApplication.translate("MainWindow", u"Antireflet", None))
        self.bleue_protect.setText(QCoreApplication.translate("MainWindow", u"Bleue protect", None))
        self.Photochromique.setText(QCoreApplication.translate("MainWindow", u"Photochromique", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Focus Type", None))
        self.Unifocaux.setText(QCoreApplication.translate("MainWindow", u"Unifocaux", None))
        self.Bifocaux.setText(QCoreApplication.translate("MainWindow", u"Bifocaux", None))
        self.Progressifs.setText(QCoreApplication.translate("MainWindow", u"Progressifs", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Port Type", None))
        self.Constant.setText(QCoreApplication.translate("MainWindow", u"Constant", None))
        self.Lecture.setText(QCoreApplication.translate("MainWindow", u"Lecture", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Index Type", None))
        self.Normal.setText(QCoreApplication.translate("MainWindow", u"Normal", None))
        self.fort_indice.setText(QCoreApplication.translate("MainWindow", u"Fort indice", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.preview_btn.setText(QCoreApplication.translate("MainWindow", u"preview", None))
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.print_btn.setText(QCoreApplication.translate("MainWindow", u"print", None))
    # retranslateUi

