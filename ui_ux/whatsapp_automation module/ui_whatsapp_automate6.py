# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'whatsapp-automate1MwNlEf.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
    QFormLayout, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListView, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
import static_rc
import static_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1132, 815)
        MainWindow.setStyleSheet(u"/* --- Define the \"Oceanic Professional\" Color Palette --- */\n"
"/* You can replace these variables with actual hex values in Qt Designer if preferred,\n"
"   or define them as custom properties if your Qt Designer version supports it.\n"
"   For direct copy-paste, it's often easier to just replace them. */\n"
"\n"
"/* Primary Blue (Dark): A deep, rich navy/ocean blue \u2013 strong and trustworthy */\n"
"/* #0F4C81 */\n"
"/* Secondary Blue (Medium): A vibrant yet calm mid-tone blue \u2013 good for primary buttons, active states */\n"
"/* #3A8BD4 */\n"
"/* Accent Blue (Light): A soft, airy blue \u2013 for subtle highlights, backgrounds, inactive states */\n"
"/* #7FC8E8 */\n"
"/* Neutral (Light Gray): Clean and professional background/card color */\n"
"/* #E6EDF2 */\n"
"/* Neutral (Dark Gray/Text): Readable text, dark elements */\n"
"/* #34495E */\n"
"/* White Text: For text on dark backgrounds */\n"
"/* #FFFFFF */\n"
"\n"
"\n"
"/* --- MainWindow (or centralWidget if applying to background) --- */\n"
"/* App"
                        "ly this to the MainWindow's stylesheet property */\n"
"QMainWindow {\n"
"    background-color: #E6EDF2; /* Neutral (Light Gray) */\n"
"}\n"
"/* If you prefer to apply to centralWidget, set its background */\n"
"QWidget#centralwidget {\n"
"    background-color: #E6EDF2; /* Neutral (Light Gray) */\n"
"}\n"
"\n"
"\n"
"/* --- header_part (QWidget) --- */\n"
"QWidget#header_part {\n"
"    background-color: #0F4C81; /* Primary Blue (Dark) */\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"/* --- label (Title in Header) --- */\n"
"QLabel#label {\n"
"    color: #FFFFFF; /* White Text */\n"
"}\n"
"\n"
"\n"
"/* --- details (QWidget) and actionbuttons (QFrame) --- */\n"
"/* These frames are set to match the main window background for a seamless look */\n"
"QWidget#details,\n"
"QFrame#actionbuttons,\n"
"QFrame#frame_box {\n"
"    background-color: #E6EDF2; /* Neutral (Light Gray) */\n"
"    border: none; /* Ensure no default borders */\n"
"}\n"
"\n"
"\n"
"/* --- message_box (QTextEdit) --- */\n"
"QTextEdit#message_box {\n"
" "
                        "   background-color: #FFFFFF; /* White Text */\n"
"    border: 1px solid #34495E; /* Neutral (Dark Gray) */\n"
"    border-radius: 5px;\n"
"    color: #34495E; /* Neutral (Dark Gray) */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"\n"
"/* --- list_message_sent (QListView) --- */\n"
"QListView#list_message_sent {\n"
"    background-color: #FFFFFF; /* White Text */\n"
"    border: 1px solid #34495E; /* Neutral (Dark Gray) */\n"
"    border-radius: 5px;\n"
"    color: #34495E; /* Neutral (Dark Gray) */\n"
"}\n"
"\n"
"\n"
"/* --- send_message (QPushButton) & cancel_message (QPushButton) & search_btn (QPushButton) --- */\n"
"QPushButton {\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: #0F4C81; /* Primary Blue (Dark) */\n"
"    padding: 8px 15px;\n"
"    font-weight: bold;\n"
"    color: #FFFFFF; /* White Text */\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #3A8BD4; /* Secondary Blue (Medium) - Hover effect */\n"
"}\n"
"\n"
"\n"
"/* --- all_checkBox (QCheckBox) & customize_checkBox (Q"
                        "CheckBox) --- */\n"
"QCheckBox {\n"
"    color: #34495E; /* Neutral (Dark Gray) */\n"
"}\n"
"\n"
"\n"
"/* --- dateTimeEdit (QDateTimeEdit) --- */\n"
"QDateTimeEdit#dateTimeEdit {\n"
"    background-color: #FFFFFF; /* White Text */\n"
"    border: 1px solid #34495E; /* Neutral (Dark Gray) */\n"
"    border-radius: 5px;\n"
"    color: #34495E; /* Neutral (Dark Gray) */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"\n"
"/* --- group_name_input (QLineEdit) --- */\n"
"QLineEdit#group_name_input {\n"
"    background-color: #FFFFFF; /* White Text */\n"
"    border: 1px solid #34495E; /* Neutral (Dark Gray) */\n"
"    border-radius: 5px;\n"
"    color: #34495E; /* Neutral (Dark Gray) */\n"
"    padding: 5px;\n"
"}\n"
"\n"
"\n"
"/* --- group_dropdown (QComboBox) --- */\n"
"QComboBox#group_dropdown {\n"
"    background-color: #FFFFFF; /* White Text */\n"
"    border: 1px solid #34495E; /* Neutral (Dark Gray) */\n"
"    border-radius: 5px;\n"
"    color: #34495E; /* Neutral (Dark Gray) */\n"
"    padding: 5px;\n"
"}\n"
"QComboBox"
                        "#group_dropdown::drop-down {\n"
"    border: 0px; /* Remove default arrow border */\n"
"}\n"
"/* You might need to add a custom arrow image if the default disappears or doesn't match */\n"
"/* QComboBox::down-arrow {\n"
"    image: url(:/icons/images/arrow_down_50px.png);\n"
"    width: 20px; height: 20px;\n"
"} */\n"
"QComboBox#group_dropdown:hover {\n"
"    border: 1px solid #3A8BD4; /* Secondary Blue (Medium) - Hover effect for border */\n"
"}\n"
"QComboBox#group_dropdown::on { /* Style when dropdown is open */\n"
"    border: 1px solid #3A8BD4; /* Secondary Blue (Medium) */\n"
"}\n"
"QComboBox#group_dropdown QAbstractItemView { /* Styles for the dropdown list itself */\n"
"    border: 1px solid #34495E; /* Neutral (Dark Gray) */\n"
"    border-radius: 5px;\n"
"    background-color: #FFFFFF; /* White Text */\n"
"    selection-background-color: #7FC8E8; /* Accent Blue (Light) */\n"
"    color: #34495E; /* Neutral (Dark Gray) */\n"
"}\n"
"\n"
"\n"
"/* --- search_bar (QLineEdit) --- */\n"
"QLineEdit#search_bar"
                        " {\n"
"    border: 1px solid #34495E; /* Neutral (Dark Gray) */\n"
"    border-radius: 5px;\n"
"    color: #34495E; /* Neutral (Dark Gray) */\n"
"    padding: 9px;\n"
"    background-color: #FFFFFF; /* White Text */\n"
"    selection-background-color: #7FC8E8; /* Accent Blue (Light) */\n"
"}\n"
"\n"
"\n"
"/* --- tableWidget (QTableWidget) --- */\n"
"QTableWidget#tableWidget {\n"
"    background-color: #FFFFFF; /* White Text */\n"
"    border: 1px solid #34495E; /* Neutral (Dark Gray) */\n"
"    border-radius: 5px;\n"
"    gridline-color: #E6EDF2; /* Neutral (Light Gray) - Lighter grid lines */\n"
"    color: #34495E; /* Neutral (Dark Gray) */\n"
"}\n"
"QHeaderView::section { /* Style for table headers */\n"
"    background-color: #0F4C81; /* Primary Blue (Dark) */\n"
"    color: #FFFFFF; /* White Text */\n"
"    padding: 5px;\n"
"    border: 1px solid #E6EDF2; /* Neutral (Light Gray) */\n"
"    border-bottom: 2px solid #3A8BD4; /* Secondary Blue (Medium) - Accent line */\n"
"}\n"
"QTableWidget::item {\n"
"    "
                        "padding: 5px;\n"
"}\n"
"QTableWidget::item:selected {\n"
"    background-color: #7FC8E8; /* Accent Blue (Light) - Selected item background */\n"
"    color: #34495E; /* Neutral (Dark Gray) */\n"
"}\n"
"\n"
"\n"
"/* --- progressBar (QProgressBar) --- */\n"
"QProgressBar#progressBar {\n"
"    border: 2px solid #0F4C81; /* Primary Blue (Dark) */\n"
"    border-radius: 10px;\n"
"    background-color: #E6EDF2; /* Neutral (Light Gray) */\n"
"    text-align: center;\n"
"    color: #34495E; /* Neutral (Dark Gray) */\n"
"    font-weight: bold;\n"
"    padding: 2px;\n"
"    /* Transitions are not directly supported in QSS for Qt Designer preview,\n"
"       but they will work at runtime if applied programmatically or via a compiled stylesheet. */\n"
"    /* transition: all 0.3s ease-in-out; */\n"
"}\n"
"QProgressBar#progressBar:hover {\n"
"    border: 2px solid #3A8BD4; /* Secondary Blue (Medium) */\n"
"    background-color: #E6EDF2; /* Keep background consistent on hover */\n"
"}\n"
"QProgressBar#progressBar::chunk {\n"
""
                        "    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #3A8BD4, stop:1 #0F4C81); /* Gradient for the chunk */\n"
"    border-radius: 8px;\n"
"    /* transition: background-color 0.3s ease-in-out; */\n"
"}\n"
"\n"
"\n"
"/* --- statusLabel (QLabel) --- */\n"
"QLabel#statusLabel {\n"
"    background-color: #0F4C81; /* Primary Blue (Dark) */\n"
"    color: #FFFFFF; /* White Text */\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"    font-weight: bold;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #F2F4F7;")
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
"")

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
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.list_message_sent.setFont(font1)

        self.horizontalLayout_2.addWidget(self.list_message_sent)


        self.horizontalLayout_3.addWidget(self.frame_box)

        self.actionbuttons = QFrame(self.details)
        self.actionbuttons.setObjectName(u"actionbuttons")
        self.actionbuttons.setMinimumSize(QSize(153, 71))
        self.actionbuttons.setMaximumSize(QSize(224, 16777215))
        self.actionbuttons.setFrameShape(QFrame.StyledPanel)
        self.actionbuttons.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.actionbuttons)
        self.formLayout.setObjectName(u"formLayout")
        self.send_message = QPushButton(self.actionbuttons)
        self.send_message.setObjectName(u"send_message")
        self.send_message.setMinimumSize(QSize(103, 0))
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.send_message.setFont(font2)
        self.send_message.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(0, 0, 99);\n"
"	padding: 5px;\n"
"	font-weight: 900;\n"
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
        self.cancel_message.setFont(font2)
        self.cancel_message.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(0, 0, 99);\n"
"	padding: 5px;\n"
"	font-weight: 900;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/logo/images/clear_symbol_48px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancel_message.setIcon(icon1)
        self.cancel_message.setIconSize(QSize(25, 25))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.cancel_message)

        self.all_checkBox = QCheckBox(self.actionbuttons)
        self.all_checkBox.setObjectName(u"all_checkBox")
        self.all_checkBox.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.all_checkBox)

        self.customize_checkBox = QCheckBox(self.actionbuttons)
        self.customize_checkBox.setObjectName(u"customize_checkBox")
        self.customize_checkBox.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.customize_checkBox)

        self.dateTimeEdit = QDateTimeEdit(self.actionbuttons)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        font3 = QFont()
        font3.setBold(True)
        self.dateTimeEdit.setFont(font3)

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.dateTimeEdit)

        self.group_name_input = QLineEdit(self.actionbuttons)
        self.group_name_input.setObjectName(u"group_name_input")
        self.group_name_input.setFont(font1)
        self.group_name_input.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"padding: 10px;\n"
"border-radius: 4px;")

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.group_name_input)

        self.group_dropdown = QComboBox(self.actionbuttons)
        self.group_dropdown.setObjectName(u"group_dropdown")
        self.group_dropdown.setFont(font1)

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.group_dropdown)


        self.horizontalLayout_3.addWidget(self.actionbuttons)


        self.verticalLayout_2.addWidget(self.details)

        self.patient_table = QWidget(self.centralwidget)
        self.patient_table.setObjectName(u"patient_table")
        self.patient_table.setMinimumSize(QSize(1053, 445))
        self.patient_table.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.patient_table)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.patient_table)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 44))
        self.frame.setStyleSheet(u"background-color: none;\n"
"border: none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.search_bar = QLineEdit(self.frame)
        self.search_bar.setObjectName(u"search_bar")
        self.search_bar.setStyleSheet(u"border: 1px solod black;\n"
"border-radius: 3px;\n"
"color: rgb(0, 0, 0);\n"
"padding: 9px;\n"
"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.search_bar)

        self.search_btn = QPushButton(self.frame)
        self.search_btn.setObjectName(u"search_btn")
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(True)
        self.search_btn.setFont(font4)
        self.search_btn.setStyleSheet(u"QPushButton{\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	background-color: rgb(0, 0, 99);\n"
"	padding: 5px;\n"
"color: white\n"
"}")

        self.horizontalLayout_4.addWidget(self.search_btn)


        self.verticalLayout.addWidget(self.frame)

        self.tableWidget = QTableWidget(self.patient_table)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
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
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font3);
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font3)
        self.tableWidget.setTabletTracking(False)
        self.tableWidget.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.tableWidget)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, -1, -1, -1)
        self.progressBar = QProgressBar(self.patient_table)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(661, 41))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 2px solid #3498db; /* Border color */\n"
"    border-radius: 10px; /* Rounded corners for the main bar */\n"
"    background-color: #ecf0f1; /* Background color of the empty part */\n"
"    text-align: center; /* Center the percentage text */\n"
"    color: #2c3e50; /* Color of the percentage text */\n"
"    font-weight: bold; /* Make the text bold */\n"
"    padding: 2px; /* Padding inside the progress bar */\n"
"   /* transition: all 0.3s ease-in-out;  Smooth transition for hover effects */\n"
"}\n"
"\n"
"QProgressBar:hover {\n"
"    border: 2px solid #2980b9; /* Darker border on hover */\n"
"    background-color: #e0e0e0; /* Slightly darker background on hover */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #1abc9c, stop:1 #16a085); /* Gradient for the chunk */\n"
"    border-radius: 8px; /* Rounded corners for the chunk (slightly smaller than main bar) */\n"
"     /*transition: background-color 0.3s ease-in-out;"
                        " Smooth transition for chunk color */\n"
"}\n"
"\n"
"/* Optional: Different chunk color on hover (if you want the chunk to change on hover of the *chunk* itself, which is less common for progress bars) */\n"
"QProgressBar::chunk:hover {\n"
"    /* This might not be noticeable as the chunk's size changes dynamically. */\n"
"    /* Consider if this truly adds value to the UX of a progress bar. */\n"
"    /* background-color: #27ae60; */\n"
"}")
        self.progressBar.setValue(24)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.progressBar)

        self.statusLabel = QLabel(self.patient_table)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setMinimumSize(QSize(233, 41))
        self.statusLabel.setMaximumSize(QSize(428, 16777215))
        self.statusLabel.setStyleSheet(u"background-color: rgb(35, 94, 255);\n"
"color: white;\n"
"padding-left: 10px;")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.statusLabel)


        self.verticalLayout.addLayout(self.formLayout_2)


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
        self.all_checkBox.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.customize_checkBox.setText(QCoreApplication.translate("MainWindow", u"Customize", None))
        self.search_bar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search patient here.................................................................", None))
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"checkbox", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Contact", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Profession", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"loading", None))
    # retranslateUi

