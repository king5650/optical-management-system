# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patient_medical_reportListQDqBOW.ui'
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
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(965, 587)
        Form.setMinimumSize(QSize(959, 0))
        Form.setStyleSheet(u"background-color: rgb(88, 162, 157);")
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(946, 0))
        self.frame.setMaximumSize(QSize(1, 1100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(959, 0))
        self.frame_2.setStyleSheet(u"\n"
"QLabel{\n"
"	color:  white;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(30, -1, -1, -1)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(70, 0))
        self.label_6.setMaximumSize(QSize(70, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.label_6.setFont(font1)

        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)

        self.p_address = QLabel(self.frame_2)
        self.p_address.setObjectName(u"p_address")

        self.gridLayout.addWidget(self.p_address, 1, 3, 1, 1)

        self.p_name = QLabel(self.frame_2)
        self.p_name.setObjectName(u"p_name")

        self.gridLayout.addWidget(self.p_name, 0, 1, 1, 1)

        self.p_contact = QLabel(self.frame_2)
        self.p_contact.setObjectName(u"p_contact")

        self.gridLayout.addWidget(self.p_contact, 2, 3, 1, 1)

        self.p_age = QLabel(self.frame_2)
        self.p_age.setObjectName(u"p_age")

        self.gridLayout.addWidget(self.p_age, 0, 3, 1, 1)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(70, 0))
        self.label_8.setMaximumSize(QSize(70, 16777215))
        self.label_8.setFont(font1)

        self.gridLayout.addWidget(self.label_8, 0, 2, 1, 1)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(70, 0))
        self.label_9.setMaximumSize(QSize(70, 16777215))
        self.label_9.setFont(font1)

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.p_gender = QLabel(self.frame_2)
        self.p_gender.setObjectName(u"p_gender")

        self.gridLayout.addWidget(self.p_gender, 1, 1, 1, 1)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(70, 0))
        self.label_11.setMaximumSize(QSize(70, 16777215))
        self.label_11.setFont(font1)

        self.gridLayout.addWidget(self.label_11, 1, 2, 1, 1)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(70, 0))
        self.label_12.setMaximumSize(QSize(70, 16777215))
        self.label_12.setFont(font1)

        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)

        self.p_mail = QLabel(self.frame_2)
        self.p_mail.setObjectName(u"p_mail")

        self.gridLayout.addWidget(self.p_mail, 2, 1, 1, 1)

        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(70, 0))
        self.label_14.setMaximumSize(QSize(70, 16777215))
        self.label_14.setFont(font1)

        self.gridLayout.addWidget(self.label_14, 2, 2, 1, 1)

        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(90, 0))
        self.label_15.setMaximumSize(QSize(90, 16777215))
        self.label_15.setFont(font1)

        self.gridLayout.addWidget(self.label_15, 3, 0, 1, 1)

        self.p_profession = QLabel(self.frame_2)
        self.p_profession.setObjectName(u"p_profession")

        self.gridLayout.addWidget(self.p_profession, 3, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_6 = QFrame(Form)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QPushButton{\n"
"	border-radius: 9px;\n"
"	padding: 4px;\n"
"\n"
"	background-color: rgb(0, 0, 99);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(179, 179, 179);\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(33, -1, -1, -1)
        self.saveButton = QPushButton(self.frame_6)
        self.saveButton.setObjectName(u"saveButton")
        font2 = QFont()
        font2.setBold(True)
        self.saveButton.setFont(font2)
        icon = QIcon()
        icon.addFile(u":/newPrefix/images/eye_diseases_64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveButton.setIcon(icon)
        self.saveButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.saveButton)

        self.pirintBUtton = QPushButton(self.frame_6)
        self.pirintBUtton.setObjectName(u"pirintBUtton")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.pirintBUtton.setFont(font3)
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/images/delete_100px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pirintBUtton.setIcon(icon1)
        self.pirintBUtton.setIconSize(QSize(24, 24))

        self.horizontalLayout_4.addWidget(self.pirintBUtton)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(961, 0))
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"#tableWidget, table, th{\n"
"	color: red;\n"
"}")
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSortingEnabled(True)

        self.verticalLayout_3.addWidget(self.tableWidget)


        self.verticalLayout_4.addWidget(self.frame_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Patient Medical Report", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Name:", None))
        self.p_address.setText("")
        self.p_name.setText("")
        self.p_contact.setText("")
        self.p_age.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"Age:", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Gender:", None))
        self.p_gender.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"Address:", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Email:", None))
        self.p_mail.setText("")
        self.label_14.setText(QCoreApplication.translate("Form", u"Contact:", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Profession", None))
        self.p_profession.setText("")
        self.saveButton.setText(QCoreApplication.translate("Form", u"View", None))
        self.pirintBUtton.setText(QCoreApplication.translate("Form", u"delete", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"New Column", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"date_created", None));
    # retranslateUi

