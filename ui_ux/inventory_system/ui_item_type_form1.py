# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_type_form1dymYhe.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import static_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1301, 791)
        Form.setStyleSheet(u"background-color: rgb(88, 162, 157);\n"
"color: rgb(255, 255, 255);")
        self.horizontalLayout_4 = QHBoxLayout(Form)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.item_type = QWidget(Form)
        self.item_type.setObjectName(u"item_type")
        self.verticalLayout_6 = QVBoxLayout(self.item_type)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.item_type)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(200, 16777215))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.item_type)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QComboBox{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"	width: 90px;\n"
"	font-weight: 900;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.select_category = QComboBox(self.frame_4)
        self.select_category.setObjectName(u"select_category")
        self.select_category.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.select_category, 0, 1, 1, 1)

        self.category_type_name = QLineEdit(self.frame_4)
        self.category_type_name.setObjectName(u"category_type_name")

        self.gridLayout_2.addWidget(self.category_type_name, 1, 1, 1, 1)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame_5)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.add_item_type = QPushButton(self.frame_5)
        self.add_item_type.setObjectName(u"add_item_type")
        icon = QIcon()
        icon.addFile(u":/logo/images/plus_48px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_item_type.setIcon(icon)
        self.add_item_type.setIconSize(QSize(32, 32))

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.add_item_type)

        self.delete_item_type = QPushButton(self.frame_5)
        self.delete_item_type.setObjectName(u"delete_item_type")
        icon1 = QIcon()
        icon1.addFile(u":/logo/images/delete_100px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_item_type.setIcon(icon1)
        self.delete_item_type.setIconSize(QSize(32, 32))

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.delete_item_type)

        self.edit_item_type = QPushButton(self.frame_5)
        self.edit_item_type.setObjectName(u"edit_item_type")
        icon2 = QIcon()
        icon2.addFile(u":/logo/images/update_left_rotation_64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_item_type.setIcon(icon2)
        self.edit_item_type.setIconSize(QSize(32, 32))

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.edit_item_type)


        self.formLayout_3.setLayout(0, QFormLayout.LabelRole, self.formLayout_2)


        self.horizontalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.item_type)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"#frame_3{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"	\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.table_item_type_display = QTableWidget(self.frame_3)
        if (self.table_item_type_display.columnCount() < 3):
            self.table_item_type_display.setColumnCount(3)
        font1 = QFont()
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.table_item_type_display.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.table_item_type_display.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.table_item_type_display.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_item_type_display.setObjectName(u"table_item_type_display")
        self.table_item_type_display.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_2.addWidget(self.table_item_type_display)


        self.verticalLayout_6.addWidget(self.frame_3)


        self.horizontalLayout_4.addWidget(self.item_type)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFont(font1)
        self.line.setAutoFillBackground(False)
        self.line.setFrameShadow(QFrame.Raised)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QFrame.VLine)

        self.horizontalLayout_4.addWidget(self.line)

        self.item_category = QWidget(Form)
        self.item_category.setObjectName(u"item_category")
        self.item_category.setMaximumSize(QSize(473, 496))
        self.verticalLayout_5 = QVBoxLayout(self.item_category)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_6 = QFrame(self.item_category)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(138, 16777215))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_2.setFont(font2)

        self.horizontalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.item_category)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"\n"
"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	color: rgb(0, 0, 0);\n"
"	width: 90px;\n"
"	font-weight: 900;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.category_name = QLineEdit(self.frame_10)
        self.category_name.setObjectName(u"category_name")

        self.horizontalLayout_2.addWidget(self.category_name)


        self.verticalLayout_3.addWidget(self.frame_10)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.frame_9)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.delete_category = QPushButton(self.frame_9)
        self.delete_category.setObjectName(u"delete_category")
        self.delete_category.setIcon(icon1)
        self.delete_category.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.delete_category, 0, 1, 1, 1)

        self.add_categoty = QPushButton(self.frame_9)
        self.add_categoty.setObjectName(u"add_categoty")
        self.add_categoty.setIcon(icon)
        self.add_categoty.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.add_categoty, 0, 0, 1, 1)

        self.edit_category = QPushButton(self.frame_9)
        self.edit_category.setObjectName(u"edit_category")
        self.edit_category.setIcon(icon2)
        self.edit_category.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.edit_category, 0, 2, 1, 1)


        self.formLayout_4.setLayout(0, QFormLayout.FieldRole, self.gridLayout)


        self.verticalLayout_3.addWidget(self.frame_9)


        self.verticalLayout_5.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.item_category)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.categor_table_display = QTableWidget(self.frame_8)
        if (self.categor_table_display.columnCount() < 2):
            self.categor_table_display.setColumnCount(2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.categor_table_display.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.categor_table_display.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        self.categor_table_display.setObjectName(u"categor_table_display")
        self.categor_table_display.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"font: 700 9pt \"Segoe UI\";")

        self.verticalLayout_4.addWidget(self.categor_table_display)


        self.verticalLayout_5.addWidget(self.frame_8)


        self.horizontalLayout_4.addWidget(self.item_category)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"ADD ITEM TYPES", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"SELECT ITEM", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"TYPE NAME", None))
        self.add_item_type.setText(QCoreApplication.translate("Form", u"ADD", None))
        self.delete_item_type.setText(QCoreApplication.translate("Form", u"DELETE", None))
        self.edit_item_type.setText(QCoreApplication.translate("Form", u"UPDATE", None))
        ___qtablewidgetitem = self.table_item_type_display.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.table_item_type_display.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"TYPE NAME", None));
        ___qtablewidgetitem2 = self.table_item_type_display.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"CATEGORY", None));
        self.label_2.setText(QCoreApplication.translate("Form", u"ADD CATEGORY", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"CATEGORY NAME:", None))
        self.delete_category.setText(QCoreApplication.translate("Form", u"DELETE", None))
        self.add_categoty.setText(QCoreApplication.translate("Form", u"ADD", None))
        self.edit_category.setText(QCoreApplication.translate("Form", u"UPDATE", None))
        ___qtablewidgetitem3 = self.categor_table_display.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Name", None));
        ___qtablewidgetitem4 = self.categor_table_display.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Date_added", None));
    # retranslateUi

