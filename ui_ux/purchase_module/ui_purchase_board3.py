# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'purchase_board1CbGVih.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)
import static_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1326, 904)
        Form.setStyleSheet(u"#Form, #frame_2 ,#frame_3, #frame_4, #frame_6, #frame_7, #frame, #frame_5{\n"
"background-color: rgb(88, 162, 157);\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit, QComboBox{\n"
"color: black;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QLineEdit, QComboBox, #toolButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"#toolButton{\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(1308, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(60, 60))
        self.label_6.setMaximumSize(QSize(60, 60))
        self.label_6.setPixmap(QPixmap(u":/logo/images/9827180.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_6, 0, Qt.AlignHCenter)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(234, 0))
        self.label.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(60, 60))
        self.label_2.setMaximumSize(QSize(60, 60))
        self.label_2.setPixmap(QPixmap(u":/logo/images/9827180.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(1200, 300))
        self.frame_2.setMaximumSize(QSize(2000, 300))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(700, 0))
        self.frame_4.setMaximumSize(QSize(700, 16777215))
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 4px;\n"
"	height: 20px;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QComboBox{\n"
"	border-radius: 4px;\n"
"	height: 20px;\n"
"	padding: 5px;\n"
"\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.category = QComboBox(self.frame_4)
        self.category.setObjectName(u"category")

        self.gridLayout.addWidget(self.category, 0, 1, 1, 1)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.quantity = QLineEdit(self.frame_4)
        self.quantity.setObjectName(u"quantity")

        self.gridLayout.addWidget(self.quantity, 2, 1, 1, 1)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)

        self.item_types = QComboBox(self.frame_4)
        self.item_types.setObjectName(u"item_types")

        self.gridLayout.addWidget(self.item_types, 1, 1, 1, 1)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.unit_price = QLineEdit(self.frame_4)
        self.unit_price.setObjectName(u"unit_price")
        self.unit_price.setReadOnly(True)

        self.gridLayout.addWidget(self.unit_price, 0, 3, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_4, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(550, 0))
        self.frame_3.setMaximumSize(QSize(550, 16777215))
        self.frame_3.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 4px;\n"
"	height: 20px;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"QComboBox{\n"
"	border-radius: 4px;\n"
"	height: 20px;\n"
"	padding: 5px;\n"
"\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setContentsMargins(5, 0, -1, -1)
        self.patient_name = QComboBox(self.frame_3)
        self.patient_name.setObjectName(u"patient_name")

        self.gridLayout_2.addWidget(self.patient_name, 0, 1, 1, 1)

        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 0))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.label_10.setFont(font2)

        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)

        self.p_contact = QLineEdit(self.frame_3)
        self.p_contact.setObjectName(u"p_contact")
        self.p_contact.setReadOnly(True)

        self.gridLayout_2.addWidget(self.p_contact, 3, 1, 1, 1)

        self.p_email = QLineEdit(self.frame_3)
        self.p_email.setObjectName(u"p_email")
        self.p_email.setReadOnly(True)

        self.gridLayout_2.addWidget(self.p_email, 1, 1, 1, 1)

        self.toolButton = QToolButton(self.frame_3)
        self.toolButton.setObjectName(u"toolButton")

        self.gridLayout_2.addWidget(self.toolButton, 0, 2, 1, 1)

        self.p_gender = QLineEdit(self.frame_3)
        self.p_gender.setObjectName(u"p_gender")
        self.p_gender.setReadOnly(True)

        self.gridLayout_2.addWidget(self.p_gender, 4, 1, 1, 1)

        self.p_address = QLineEdit(self.frame_3)
        self.p_address.setObjectName(u"p_address")
        self.p_address.setReadOnly(True)

        self.gridLayout_2.addWidget(self.p_address, 2, 1, 1, 1)

        self.p_age = QLineEdit(self.frame_3)
        self.p_age.setObjectName(u"p_age")
        self.p_age.setReadOnly(True)

        self.gridLayout_2.addWidget(self.p_age, 5, 1, 1, 1)

        self.label_11 = QLabel(self.frame_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)

        self.gridLayout_2.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_12 = QLabel(self.frame_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)

        self.gridLayout_2.addWidget(self.label_12, 4, 0, 1, 1)

        self.label_13 = QLabel(self.frame_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)

        self.gridLayout_2.addWidget(self.label_13, 5, 0, 1, 1)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_3, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_5 = QFrame(Form)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(1267, 0))
        self.frame_5.setStyleSheet(u"\n"
"\n"
"#tableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"#tableWidget::hover{\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"#tableWidget::select{\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: rgb(214, 214, 214);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(self.frame_5)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(13)
        font3.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        __qtablewidgetitem1.setBackground(QColor(255, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        __qtablewidgetitem2.setBackground(QColor(255, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        __qtablewidgetitem3.setBackground(QColor(255, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")
        font4 = QFont()
        font4.setKerning(False)
        self.tableWidget.setFont(font4)
        self.tableWidget.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(14, 163, 255);")
        self.tableWidget.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.tableWidget)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(Form)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(1291, 0))
        self.frame_6.setMaximumSize(QSize(1500, 16777215))
        self.frame_6.setStyleSheet(u"QLineEdit{\n"
"	border-radius: 4px;\n"
"	height: 20px;\n"
"	padding: 5px;\n"
"\n"
"}\n"
"\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_24 = QLabel(self.frame_6)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setPixmap(QPixmap(u":/logo/images/sales_performance_50px.png"))
        self.label_24.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_24, 1, 2, 1, 1)

        self.VAT_on_lens = QLineEdit(self.frame_6)
        self.VAT_on_lens.setObjectName(u"VAT_on_lens")
        font5 = QFont()
        font5.setPointSize(12)
        self.VAT_on_lens.setFont(font5)
        self.VAT_on_lens.setReadOnly(True)

        self.gridLayout_3.addWidget(self.VAT_on_lens, 2, 1, 1, 1)

        self.amount_given = QLineEdit(self.frame_6)
        self.amount_given.setObjectName(u"amount_given")
        self.amount_given.setFont(font5)

        self.gridLayout_3.addWidget(self.amount_given, 1, 5, 1, 1)

        self.label_23 = QLabel(self.frame_6)
        self.label_23.setObjectName(u"label_23")
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        self.label_23.setFont(font6)

        self.gridLayout_3.addWidget(self.label_23, 1, 3, 1, 1)

        self.VAT_on_frame = QLineEdit(self.frame_6)
        self.VAT_on_frame.setObjectName(u"VAT_on_frame")
        self.VAT_on_frame.setFont(font5)
        self.VAT_on_frame.setReadOnly(True)

        self.gridLayout_3.addWidget(self.VAT_on_frame, 1, 1, 1, 1)

        self.total_balance = QLineEdit(self.frame_6)
        self.total_balance.setObjectName(u"total_balance")
        self.total_balance.setFont(font5)
        self.total_balance.setReadOnly(True)

        self.gridLayout_3.addWidget(self.total_balance, 0, 5, 1, 1)

        self.VAT_on_aceessory = QLineEdit(self.frame_6)
        self.VAT_on_aceessory.setObjectName(u"VAT_on_aceessory")
        self.VAT_on_aceessory.setFont(font5)
        self.VAT_on_aceessory.setReadOnly(True)

        self.gridLayout_3.addWidget(self.VAT_on_aceessory, 3, 1, 1, 1)

        self.label_21 = QLabel(self.frame_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font6)

        self.gridLayout_3.addWidget(self.label_21, 0, 3, 1, 1)

        self.label_22 = QLabel(self.frame_6)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setPixmap(QPixmap(u":/logo/images/payment_history_50px.png"))
        self.label_22.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_22, 0, 2, 1, 1)

        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font6)

        self.gridLayout_3.addWidget(self.label_17, 3, 0, 1, 1)

        self.total_amount_without_tax = QLineEdit(self.frame_6)
        self.total_amount_without_tax.setObjectName(u"total_amount_without_tax")
        self.total_amount_without_tax.setFont(font5)
        self.total_amount_without_tax.setReadOnly(True)

        self.gridLayout_3.addWidget(self.total_amount_without_tax, 0, 1, 1, 1)

        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font6)

        self.gridLayout_3.addWidget(self.label_16, 2, 0, 1, 1)

        self.label_20 = QLabel(self.frame_6)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setPixmap(QPixmap(u":/logo/images/stack_of_money_48px.png"))
        self.label_20.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label_20, 2, 2, 1, 1)

        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font6)

        self.gridLayout_3.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_19 = QLabel(self.frame_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font6)

        self.gridLayout_3.addWidget(self.label_19, 2, 3, 1, 1)

        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font6)

        self.gridLayout_3.addWidget(self.label_15, 1, 0, 1, 1)

        self.total_VAT_on_items = QLineEdit(self.frame_6)
        self.total_VAT_on_items.setObjectName(u"total_VAT_on_items")
        self.total_VAT_on_items.setFont(font5)
        self.total_VAT_on_items.setReadOnly(True)

        self.gridLayout_3.addWidget(self.total_VAT_on_items, 4, 1, 1, 1)

        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font6)

        self.gridLayout_3.addWidget(self.label_18, 4, 0, 1, 1)

        self.change_to_give = QLineEdit(self.frame_6)
        self.change_to_give.setObjectName(u"change_to_give")
        self.change_to_give.setFont(font5)
        self.change_to_give.setReadOnly(True)

        self.gridLayout_3.addWidget(self.change_to_give, 2, 5, 1, 1)


        self.horizontalLayout_2.addLayout(self.gridLayout_3)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"QPushButton{\n"
"	border-radius: 9px;\n"
"	padding: 8px;\n"
"	font-weight: 900px;\n"
"	background-color: rgb(0, 0, 99);\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(179, 179, 179);\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.validate = QPushButton(self.frame_7)
        self.validate.setObjectName(u"validate")
        font7 = QFont()
        font7.setBold(True)
        self.validate.setFont(font7)
        icon = QIcon()
        icon.addFile(u":/logo/images/ok_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.validate.setIcon(icon)
        self.validate.setIconSize(QSize(32, 32))

        self.gridLayout_4.addWidget(self.validate, 1, 2, 1, 1)

        self.receipt_print = QPushButton(self.frame_7)
        self.receipt_print.setObjectName(u"receipt_print")
        self.receipt_print.setFont(font7)
        icon1 = QIcon()
        icon1.addFile(u":/logo/images/print_100px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.receipt_print.setIcon(icon1)
        self.receipt_print.setIconSize(QSize(32, 32))

        self.gridLayout_4.addWidget(self.receipt_print, 1, 4, 1, 1)

        self.add_to_cart = QPushButton(self.frame_7)
        self.add_to_cart.setObjectName(u"add_to_cart")
        font8 = QFont()
        font8.setPointSize(9)
        font8.setBold(True)
        self.add_to_cart.setFont(font8)
        icon2 = QIcon()
        icon2.addFile(u":/logo/images/add_shopping_cart_48px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_to_cart.setIcon(icon2)
        self.add_to_cart.setIconSize(QSize(32, 32))

        self.gridLayout_4.addWidget(self.add_to_cart, 1, 1, 1, 1)

        self.delete_from_cart = QPushButton(self.frame_7)
        self.delete_from_cart.setObjectName(u"delete_from_cart")
        self.delete_from_cart.setFont(font7)
        icon3 = QIcon()
        icon3.addFile(u":/logo/images/delete_100px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_from_cart.setIcon(icon3)
        self.delete_from_cart.setIconSize(QSize(32, 32))

        self.gridLayout_4.addWidget(self.delete_from_cart, 1, 3, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_4, 0, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_6.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"Purchase Borad", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Category", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Quantity", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Unit Price", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Item type", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Address", None))
        self.toolButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Contact", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Email", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Gender", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Age", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Patient Name", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Quantity", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Items", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Unit Price", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Total Price", None));
        self.label_24.setText("")
        self.label_23.setText(QCoreApplication.translate("Form", u"Given Amount", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"Total Balance", None))
        self.label_22.setText("")
        self.label_17.setText(QCoreApplication.translate("Form", u"VAT on Accessory:", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"VAT on Lens:", None))
        self.label_20.setText("")
        self.label_14.setText(QCoreApplication.translate("Form", u"Total without Tax:", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"Change", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"VAT on Frames:", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"Total VAT:", None))
        self.validate.setText(QCoreApplication.translate("Form", u"Validate", None))
        self.receipt_print.setText(QCoreApplication.translate("Form", u"Print", None))
        self.add_to_cart.setText(QCoreApplication.translate("Form", u"Add", None))
        self.delete_from_cart.setText(QCoreApplication.translate("Form", u"Remove", None))
    # retranslateUi

