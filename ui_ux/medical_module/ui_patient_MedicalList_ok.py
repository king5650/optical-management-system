# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'patient_MedicalList_okzjlnid.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import static_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1034, 689)
        MainWindow.setStyleSheet(u"              /*  background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,  Horizontal gradient\n"
"                                        stop: 0 #eff6ff, stop: 1 #dbeafe);  \n"
"background-color: rgb(88, 162, 157);*/\n"
"background-color: rgba(44, 47, 134, 200);\n"
"color: white;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	border-radius: 9px;\n"
"	padding: 4px;\n"
"	background-color: rgb(0, 221, 255);\n"
"	\n"
"	background-color: rgb(0, 0, 99);\n"
"	\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0, 50);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"Monotype Corsiva"])
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        self.label_4.setFont(font)

        self.verticalLayout_6.addWidget(self.label_4, 0, Qt.AlignHCenter)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QPushButton{\n"
"	border: 2px solid white;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(0, 0, 99);\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border: 2px solid white;\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(154, 154, 154);\n"
"	padding: 5px;\n"
"}\n"
"\n"
"#searchButton{\n"
"	border: 1px solid #000000;\n"
"	border-radius: 10px;\n"
"	color: white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 1px solid #000000;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-color: rgb(0, 0, 127);\n"
"	padding: 3px;\n"
"}\n"
"#frame_3{\n"
"	background-color: none;\n"
"border: none;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.create_form = QPushButton(self.frame_3)
        self.create_form.setObjectName(u"create_form")
        icon = QIcon()
        icon.addFile(u":/logo/images/add_list_40px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.create_form.setIcon(icon)
        self.create_form.setIconSize(QSize(26, 26))

        self.horizontalLayout_8.addWidget(self.create_form)

        self.view_prescription = QPushButton(self.frame_3)
        self.view_prescription.setObjectName(u"view_prescription")
        icon1 = QIcon()
        icon1.addFile(u":/logo/images/edit_property_64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.view_prescription.setIcon(icon1)
        self.view_prescription.setIconSize(QSize(26, 26))

        self.horizontalLayout_8.addWidget(self.view_prescription)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        icon2 = QIcon()
        icon2.addFile(u":/logo/images/synchronize_40px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QSize(26, 26))

        self.horizontalLayout_8.addWidget(self.pushButton)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalSpacer_3 = QSpacerItem(387, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(290, 0))
        self.lineEdit.setMaximumSize(QSize(290, 16777215))
        self.lineEdit.setStyleSheet(u"border: 1px solod black;\n"
"border-radius: 3px;\n"
"color: rgb(0, 0, 0);\n"
"padding: 9px;")

        self.horizontalLayout_9.addWidget(self.lineEdit)

        self.searchButton = QPushButton(self.frame_3)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setMinimumSize(QSize(70, 0))
        self.searchButton.setMaximumSize(QSize(70, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Quincy"])
        font1.setPointSize(9)
        font1.setBold(True)
        self.searchButton.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/logo/images/find_and_replace_64px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon3)

        self.horizontalLayout_9.addWidget(self.searchButton)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_9)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"#frame_4{\n"
"background-color: none;\n"
"border: none;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.tableWidget = QTableWidget(self.frame_4)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        font2 = QFont()
        font2.setBold(True)
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
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font2);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setTabletTracking(True)
        self.tableWidget.setStyleSheet(u"            QTableWidget {\n"
"                background-color: transparent;\n"
"                border: 1px solid #ccc;\n"
"                border-radius: 4px;\n"
"                gridline-color: #ccc;\n"
"                selection-background-color: rgb(0, 0, 99);\n"
"                selection-color: #ffffff;\n"
"                color: white;\n"
"				font: 800 12pt \"Manrope ExtraBold\";\n"
"            }\n"
"\n"
"            QHeaderView::section {\n"
"                background-color: rgba(44, 47, 134, 230);\n"
"                color: white;\n"
"                padding: 8px;\n"
"                border: 1px solid white;\n"
"                font-weight: 900;\n"
"            }\n"
"\n"
"            QHeaderView {\n"
"				font: 14pt \"Quincy\";\n"
"				font-weight: 900;\n"
"            }\n"
"\n"
"            QTableWidget::item:selected {\n"
"                background-color: #0078d7;\n"
"                color: white;\n"
"                font-weight: 900;\n"
"            }")
        self.tableWidget.setSortingEnabled(True)

        self.verticalLayout_7.addWidget(self.tableWidget)


        self.verticalLayout.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Medical Report/Raport medical", None))
        self.create_form.setText("")
        self.view_prescription.setText("")
        self.pushButton.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search here.........", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"search", None))
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

