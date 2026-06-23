# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_inventorysAzJTFX.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1056, 645)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(88, 162, 157);")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(1038, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(20)
        font.setBold(True)
        self.label_8.setFont(font)

        self.verticalLayout.addWidget(self.label_8, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"\n"
"padding: 10px;\n"
"\n"
"}\n"
"\n"
"#frame_3{\n"
"	height: 80px;\n"
"	border-radius: 20px;\n"
"	background-color: rgb(81, 161, 134);\n"
"	padding-left: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"QPushButton{\n"
"	color: white;\n"
"	border-radius: 9px;\n"
"	border: 2px solid white;\n"
"	background-color: rgb(0, 0, 99);\n"
"	padding: 2px;\n"
"	height: 20px;\n"
"	font: 700 11pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"	background-color: rgb(255, 98, 46);\n"
"}\n"
"\n"
"QComboBox::hover{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QSpinBox::hover{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(30, 20, 30, 20)
        self.itemsSelect = QComboBox(self.frame_2)
        self.itemsSelect.setObjectName(u"itemsSelect")
        self.itemsSelect.setMinimumSize(QSize(200, 0))
        self.itemsSelect.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.itemsSelect, 0, 3, 1, 1)

        self.itemtype = QComboBox(self.frame_2)
        self.itemtype.setObjectName(u"itemtype")
        self.itemtype.setMaximumSize(QSize(300, 16777215))

        self.gridLayout.addWidget(self.itemtype, 1, 3, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(90, 0))
        self.label.setMaximumSize(QSize(40, 16777215))
        font1 = QFont()
        font1.setBold(True)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(90, 0))
        self.label_4.setMaximumSize(QSize(40, 16777215))
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(90, 0))
        self.label_2.setMaximumSize(QSize(40, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_2.setFont(font2)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(110, 0))
        self.label_3.setMaximumSize(QSize(40, 16777215))
        self.label_3.setFont(font1)

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.itemAmount = QLineEdit(self.frame_2)
        self.itemAmount.setObjectName(u"itemAmount")

        self.gridLayout.addWidget(self.itemAmount, 3, 3, 1, 1)

        self.itemquant = QLineEdit(self.frame_2)
        self.itemquant.setObjectName(u"itemquant")

        self.gridLayout.addWidget(self.itemquant, 4, 3, 1, 1)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.opticalAccessoryName = QLineEdit(self.frame_2)
        self.opticalAccessoryName.setObjectName(u"opticalAccessoryName")

        self.gridLayout.addWidget(self.opticalAccessoryName, 2, 3, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setContentsMargins(30, 20, 30, 20)
        self.pushButton_8 = QPushButton(self.frame_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(100, 0))
        self.pushButton_8.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_8, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 0))
        self.pushButton.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.pushButton, 4, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 0))
        self.pushButton_2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.pushButton_7 = QPushButton(self.frame_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(100, 0))
        self.pushButton_7.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_7, 3, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.frame_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(100, 0))
        self.pushButton_9.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_2.addWidget(self.pushButton_9, 2, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout_3)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(360, 120))
        self.frame_3.setMaximumSize(QSize(350, 77))
        self.frame_3.setStyleSheet(u"\n"
"\n"
"#label_5,#label_6{\n"
"	color: rgb(255, 255, 255);\n"
"border-radius:1px;\n"
"}\n"
"#totalpriceLabel,#totalstockLabel{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(2)
        self.gridLayout_5.setVerticalSpacing(19)
        self.gridLayout_5.setContentsMargins(2, 2, 2, 2)
        self.totalstockLabel = QLabel(self.frame_3)
        self.totalstockLabel.setObjectName(u"totalstockLabel")
        self.totalstockLabel.setFont(font2)

        self.gridLayout_5.addWidget(self.totalstockLabel, 0, 1, 1, 1)

        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        self.label_6.setFont(font3)

        self.gridLayout_5.addWidget(self.label_6, 1, 0, 1, 1)

        self.totalpriceLabel = QLabel(self.frame_3)
        self.totalpriceLabel.setObjectName(u"totalpriceLabel")
        self.totalpriceLabel.setFont(font2)

        self.gridLayout_5.addWidget(self.totalpriceLabel, 1, 1, 1, 1)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)

        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(88, 162, 157);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableWidget = QTableWidget(self.frame_4)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_4.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ITEMS INVENTOTY ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Type", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"quantity", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Item", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"amount", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.totalstockLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Total Amount:", None))
        self.totalpriceLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Total Stock:", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Type", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Date_Added", None));
    # retranslateUi

