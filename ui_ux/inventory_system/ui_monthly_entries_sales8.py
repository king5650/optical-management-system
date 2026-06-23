# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'monthly_entries1DRfcxk.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import static_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1234, 790)
        Form.setStyleSheet(u"QWidget{\n"
"background-color: rgb(88, 162, 157);\n"
"\n"
"}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 283))
        self.frame_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 9, 1, 6)
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(500, 196))
        self.frame_6.setMaximumSize(QSize(525, 250))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(136, 16777215))
        self.label_13.setFont(font)

        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(136, 16777215))
        self.label_14.setFont(font)

        self.gridLayout_3.addWidget(self.label_14, 2, 0, 1, 1)

        self.items_types = QComboBox(self.frame_6)
        self.items_types.setObjectName(u"items_types")
        self.items_types.setMaximumSize(QSize(253, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.items_types.setFont(font1)

        self.gridLayout_3.addWidget(self.items_types, 3, 1, 1, 1)

        self.category = QComboBox(self.frame_6)
        self.category.setObjectName(u"category")
        self.category.setMaximumSize(QSize(253, 16777215))
        self.category.setFont(font1)

        self.gridLayout_3.addWidget(self.category, 2, 1, 1, 1)

        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(136, 16777215))
        self.label_15.setFont(font)

        self.gridLayout_3.addWidget(self.label_15, 3, 0, 1, 1)

        self.years = QComboBox(self.frame_6)
        self.years.setObjectName(u"years")
        self.years.setMaximumSize(QSize(253, 16777215))
        self.years.setFont(font1)

        self.gridLayout_3.addWidget(self.years, 1, 1, 1, 1)

        self.months = QComboBox(self.frame_6)
        self.months.setObjectName(u"months")
        self.months.setMaximumSize(QSize(253, 16777215))
        self.months.setFont(font1)

        self.gridLayout_3.addWidget(self.months, 0, 1, 1, 1)

        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(136, 16777215))
        self.label_16.setFont(font)

        self.gridLayout_3.addWidget(self.label_16, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_6)

        self.horizontalSpacer = QSpacerItem(70, 18, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(153, 266))
        self.frame_5.setMaximumSize(QSize(430, 349))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_6.addWidget(self.label_5, 0, 0, 1, 1)

        self.sale_entries = QComboBox(self.frame_5)
        self.sale_entries.setObjectName(u"sale_entries")
        self.sale_entries.setFont(font1)

        self.gridLayout_6.addWidget(self.sale_entries, 0, 1, 1, 1)

        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 30))
        self.label_6.setMaximumSize(QSize(16777215, 39))
        self.label_6.setFont(font)

        self.gridLayout_6.addWidget(self.label_6, 1, 0, 1, 1)

        self.globalamount = QLabel(self.frame_5)
        self.globalamount.setObjectName(u"globalamount")
        self.globalamount.setMinimumSize(QSize(0, 26))
        self.globalamount.setMaximumSize(QSize(16777215, 52))
        self.globalamount.setFont(font)

        self.gridLayout_6.addWidget(self.globalamount, 1, 1, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_6)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)

        self.label_12 = QLabel(self.frame_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout_2.addWidget(self.label_12, 6, 0, 1, 1)

        self.label_11 = QLabel(self.frame_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout_2.addWidget(self.label_11, 5, 0, 1, 1)


        self.verticalLayout_8.addLayout(self.gridLayout_2)


        self.horizontalLayout.addWidget(self.frame_5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(132, 16777215))
        self.frame_4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"	width: 90px;\n"
"	font-weight: 900;\n"
"}\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.filter_button = QPushButton(self.frame_4)
        self.filter_button.setObjectName(u"filter_button")
        self.filter_button.setMaximumSize(QSize(100, 16777215))
        icon = QIcon()
        icon.addFile(u":/logo/images/filter_100px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.filter_button.setIcon(icon)
        self.filter_button.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.filter_button)

        self.export_button = QPushButton(self.frame_4)
        self.export_button.setObjectName(u"export_button")
        self.export_button.setMaximumSize(QSize(107, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/logo/images/export_24px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.export_button.setIcon(icon1)
        self.export_button.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.export_button)

        self.radio_pdf = QRadioButton(self.frame_4)
        self.radio_pdf.setObjectName(u"radio_pdf")
        font2 = QFont()
        font2.setBold(True)
        self.radio_pdf.setFont(font2)
        self.radio_pdf.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.radio_pdf)

        self.radio_csv = QRadioButton(self.frame_4)
        self.radio_csv.setObjectName(u"radio_csv")
        self.radio_csv.setFont(font2)
        self.radio_csv.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.radio_csv)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(Form)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(self.frame_3)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
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
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font1)
        self.tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-weight: 900;")

        self.verticalLayout.addWidget(self.tableWidget)


        self.verticalLayout_3.addWidget(self.frame_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Monthly Entries/ sales", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Month: ", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Items:", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"Types:", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"Years", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"sale/entry", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"total amount Global", None))
        self.globalamount.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"Profit made", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.filter_button.setText(QCoreApplication.translate("Form", u"Filter", None))
        self.export_button.setText(QCoreApplication.translate("Form", u"Export ", None))
        self.radio_pdf.setText(QCoreApplication.translate("Form", u"PDF", None))
        self.radio_csv.setText(QCoreApplication.translate("Form", u"CSV", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Month", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Item", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Unit Price", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Stock Quantity", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Total Amount", None));
    # retranslateUi

