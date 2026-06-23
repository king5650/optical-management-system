# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'whatsapp-automateMYOhSg.ui'
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
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)
import static_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1071, 815)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.header_part = QWidget(self.centralwidget)
        self.header_part.setObjectName(u"header_part")
        self.header_part.setMinimumSize(QSize(500, 80))
        self.header_part.setStyleSheet(u"background-color: rgb(88, 162, 157);\n"
"")
        self.horizontalLayout = QHBoxLayout(self.header_part)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.header_part)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(70, 70))
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/logo/images/whatsapp_48px.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.label = QLabel(self.header_part)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(312, 30))
        self.label.setMaximumSize(QSize(303, 16777215))
        font = QFont()
        font.setFamilies([u"Segoe UI Light"])
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-weight: 900;")

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.header_part)

        self.details = QWidget(self.centralwidget)
        self.details.setObjectName(u"details")
        self.details.setMinimumSize(QSize(700, 260))
        self.details.setStyleSheet(u"")
        self.horizontalLayout_3 = QHBoxLayout(self.details)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_box = QFrame(self.details)
        self.frame_box.setObjectName(u"frame_box")
        self.frame_box.setFrameShape(QFrame.StyledPanel)
        self.frame_box.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_box)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.message_box = QTextEdit(self.frame_box)
        self.message_box.setObjectName(u"message_box")
        self.message_box.setMinimumSize(QSize(478, 0))

        self.horizontalLayout_2.addWidget(self.message_box)

        self.list_message_sent = QListView(self.frame_box)
        self.list_message_sent.setObjectName(u"list_message_sent")
        self.list_message_sent.setMinimumSize(QSize(367, 0))

        self.horizontalLayout_2.addWidget(self.list_message_sent)


        self.horizontalLayout_3.addWidget(self.frame_box)

        self.actionbuttons = QFrame(self.details)
        self.actionbuttons.setObjectName(u"actionbuttons")
        self.actionbuttons.setMinimumSize(QSize(120, 71))
        self.actionbuttons.setFrameShape(QFrame.StyledPanel)
        self.actionbuttons.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.actionbuttons)
        self.formLayout.setObjectName(u"formLayout")
        self.send_message = QPushButton(self.actionbuttons)
        self.send_message.setObjectName(u"send_message")
        self.send_message.setMinimumSize(QSize(103, 0))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.send_message.setFont(font1)
        self.send_message.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(0, 0, 99);\n"
"	padding: 5px;\n"
"	font-weight: 1200;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/logo/images/ok_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.send_message.setIcon(icon)
        self.send_message.setIconSize(QSize(25, 25))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.send_message)

        self.cancel_message = QPushButton(self.actionbuttons)
        self.cancel_message.setObjectName(u"cancel_message")
        self.cancel_message.setMinimumSize(QSize(104, 0))
        self.cancel_message.setFont(font1)
        self.cancel_message.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(0, 0, 99);\n"
"	padding: 5px;\n"
"	font-weight: 1200;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/logo/images/clear_symbol_48px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancel_message.setIcon(icon1)
        self.cancel_message.setIconSize(QSize(25, 25))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.cancel_message)

        self.checkBox = QCheckBox(self.actionbuttons)
        self.checkBox.setObjectName(u"checkBox")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.checkBox.setFont(font2)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.checkBox)

        self.checkBox_2 = QCheckBox(self.actionbuttons)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setFont(font2)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.checkBox_2)

        self.dateTimeEdit = QDateTimeEdit(self.actionbuttons)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        font3 = QFont()
        font3.setBold(True)
        self.dateTimeEdit.setFont(font3)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.dateTimeEdit)


        self.horizontalLayout_3.addWidget(self.actionbuttons)


        self.verticalLayout_2.addWidget(self.details)

        self.patient_table = QWidget(self.centralwidget)
        self.patient_table.setObjectName(u"patient_table")
        self.patient_table.setMinimumSize(QSize(1053, 445))
        self.patient_table.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.patient_table)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(self.patient_table)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setTabletTracking(False)
        self.tableWidget.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.tableWidget)


        self.verticalLayout_2.addWidget(self.patient_table)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"AUTOMATED SYSTEM", None))
        self.send_message.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.cancel_message.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Customize", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Contact", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Profession", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
    # retranslateUi

