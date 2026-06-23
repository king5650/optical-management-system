# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'whatsapp-automate1plNHgT.ui'
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
import static_rc # Assuming this file contains your images/icons

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1132, 815)

        # --- Define the "Oceanic Professional" Color Palette ---
        # Primary Blue (Dark): A deep, rich navy/ocean blue – strong and trustworthy
        self.PRIMARY_DARK_BLUE = "#0F4C81"
        # Secondary Blue (Medium): A vibrant yet calm mid-tone blue – good for primary buttons, active states
        self.SECONDARY_MEDIUM_BLUE = "#3A8BD4"
        # Accent Blue (Light): A soft, airy blue – for subtle highlights, backgrounds, inactive states
        self.ACCENT_LIGHT_BLUE = "#7FC8E8"
        # Neutral (Light Gray): Clean and professional background/card color
        self.NEUTRAL_LIGHT_GRAY = "#E6EDF2"
        # Neutral (Dark Gray/Text): Readable text, dark elements
        self.NEUTRAL_DARK_GRAY = "#34495E"
        # White Text: For text on dark backgrounds
        self.WHITE_TEXT = "#FFFFFF"

        # Set the main window background
        MainWindow.setStyleSheet(f"background-color: {self.NEUTRAL_LIGHT_GRAY};")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        # Header Part
        self.header_part = QWidget(self.centralwidget)
        self.header_part.setObjectName(u"header_part")
        self.header_part.setMinimumSize(QSize(500, 80))
        self.header_part.setStyleSheet(f"background-color: {self.PRIMARY_DARK_BLUE};"
                                       "border-radius: 10px;") # Added border-radius for modern look
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
        self.label.setStyleSheet(f"color: {self.WHITE_TEXT};") # Text color on dark header

        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.header_part)

        # Details Part
        self.details = QWidget(self.centralwidget)
        self.details.setObjectName(u"details")
        self.details.setMinimumSize(QSize(700, 260))
        self.details.setStyleSheet(f"background-color: {self.NEUTRAL_LIGHT_GRAY};") # Set background for consistency
        self.horizontalLayout_3 = QHBoxLayout(self.details)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_box = QFrame(self.details)
        self.frame_box.setObjectName(u"frame_box")
        self.frame_box.setFrameShape(QFrame.StyledPanel)
        self.frame_box.setFrameShadow(QFrame.Raised)
        # Apply a subtle background to the frame box for visual separation
        self.frame_box.setStyleSheet(f"background-color: {self.NEUTRAL_LIGHT_GRAY}; border: none;")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_box)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        # Message Box (QTextEdit)
        self.message_box = QTextEdit(self.frame_box)
        self.message_box.setObjectName(u"message_box")
        self.message_box.setMinimumSize(QSize(478, 0))
        self.message_box.setStyleSheet(f"background-color: {self.WHITE_TEXT};"
                                       f"border: 1px solid {self.NEUTRAL_DARK_GRAY};"
                                       f"border-radius: 5px;"
                                       f"color: {self.NEUTRAL_DARK_GRAY};"
                                       f"padding: 5px;")
        self.horizontalLayout_2.addWidget(self.message_box)

        # List Message Sent (QListView)
        self.list_message_sent = QListView(self.frame_box)
        self.list_message_sent.setObjectName(u"list_message_sent")
        self.list_message_sent.setMinimumSize(QSize(367, 0))
        self.list_message_sent.setStyleSheet(f"background-color: {self.WHITE_TEXT};"
                                             f"border: 1px solid {self.NEUTRAL_DARK_GRAY};"
                                             f"border-radius: 5px;"
                                             f"color: {self.NEUTRAL_DARK_GRAY};")
        self.horizontalLayout_2.addWidget(self.list_message_sent)

        self.horizontalLayout_3.addWidget(self.frame_box)

        # Action Buttons Frame
        self.actionbuttons = QFrame(self.details)
        self.actionbuttons.setObjectName(u"actionbuttons")
        self.actionbuttons.setMinimumSize(QSize(153, 71))
        self.actionbuttons.setFrameShape(QFrame.StyledPanel)
        self.actionbuttons.setFrameShadow(QFrame.Raised)
        self.actionbuttons.setStyleSheet(f"background-color: {self.NEUTRAL_LIGHT_GRAY}; border: none;") # Consistent background
        self.formLayout = QFormLayout(self.actionbuttons)
        self.formLayout.setObjectName(u"formLayout")

        # Send Message Button
        self.send_message = QPushButton(self.actionbuttons)
        self.send_message.setObjectName(u"send_message")
        self.send_message.setMinimumSize(QSize(103, 0))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.send_message.setFont(font1)
        self.send_message.setStyleSheet(
            f"QPushButton{{"
            f"  border: none;"
            f"  border-radius: 5px;"
            f"  background-color: {self.PRIMARY_DARK_BLUE};"
            f"  padding: 8px 15px;" # Increased padding for better touch target
            f"  font-weight: bold;"
            f"  color: {self.WHITE_TEXT};"
            f"}}"
            f"QPushButton:hover{{"
            f"  background-color: {self.SECONDARY_MEDIUM_BLUE};" # Hover effect
            f"}}"
        )
        icon = QIcon()
        icon.addFile(u":/logo/images/ok_50px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.send_message.setIcon(icon)
        self.send_message.setIconSize(QSize(25, 25))
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.send_message)

        # Cancel Message Button
        self.cancel_message = QPushButton(self.actionbuttons)
        self.cancel_message.setObjectName(u"cancel_message")
        self.cancel_message.setMinimumSize(QSize(104, 0))
        self.cancel_message.setFont(font1)
        self.cancel_message.setStyleSheet(
            f"QPushButton{{"
            f"  border: none;"
            f"  border-radius: 5px;"
            f"  background-color: {self.PRIMARY_DARK_BLUE};"
            f"  padding: 8px 15px;" # Increased padding
            f"  font-weight: bold;"
            f"  color: {self.WHITE_TEXT};"
            f"}}"
            f"QPushButton:hover{{"
            f"  background-color: {self.SECONDARY_MEDIUM_BLUE};" # Hover effect
            f"}}"
        )
        icon1 = QIcon()
        icon1.addFile(u":/logo/images/clear_symbol_48px.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancel_message.setIcon(icon1)
        self.cancel_message.setIconSize(QSize(25, 25))
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.cancel_message)

        # Checkboxes
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.all_checkBox = QCheckBox(self.actionbuttons)
        self.all_checkBox.setObjectName(u"all_checkBox")
        self.all_checkBox.setFont(font2)
        self.all_checkBox.setStyleSheet(f"color: {self.NEUTRAL_DARK_GRAY};") # Text color for checkboxes
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.all_checkBox)

        self.customize_checkBox = QCheckBox(self.actionbuttons)
        self.customize_checkBox.setObjectName(u"customize_checkBox")
        self.customize_checkBox.setFont(font2)
        self.customize_checkBox.setStyleSheet(f"color: {self.NEUTRAL_DARK_GRAY};") # Text color for checkboxes
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.customize_checkBox)

        # DateTimeEdit
        self.dateTimeEdit = QDateTimeEdit(self.actionbuttons)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        font3 = QFont()
        font3.setBold(True)
        self.dateTimeEdit.setFont(font3)
        self.dateTimeEdit.setStyleSheet(f"background-color: {self.WHITE_TEXT};"
                                        f"border: 1px solid {self.NEUTRAL_DARK_GRAY};"
                                        f"border-radius: 5px;"
                                        f"color: {self.NEUTRAL_DARK_GRAY};"
                                        f"padding: 5px;")
        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.dateTimeEdit)

        # Group Name Input (QLineEdit)
        self.group_name_input = QLineEdit(self.actionbuttons)
        self.group_name_input.setObjectName(u"group_name_input")
        self.group_name_input.setFont(font2)
        self.group_name_input.setStyleSheet(f"background-color: {self.WHITE_TEXT};"
                                            f"border: 1px solid {self.NEUTRAL_DARK_GRAY};"
                                            f"border-radius: 5px;"
                                            f"color: {self.NEUTRAL_DARK_GRAY};"
                                            f"padding: 5px;")
        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.group_name_input)

        # Group Dropdown (QComboBox)
        self.group_dropdown = QComboBox(self.actionbuttons)
        self.group_dropdown.setObjectName(u"group_dropdown")
        self.group_dropdown.setFont(font2)
        self.group_dropdown.setStyleSheet(f"QComboBox{{"
                                          f"  background-color: {self.WHITE_TEXT};"
                                          f"  border: 1px solid {self.NEUTRAL_DARK_GRAY};"
                                          f"  border-radius: 5px;"
                                          f"  color: {self.NEUTRAL_DARK_GRAY};"
                                          f"  padding: 5px;"
                                          f"}}"
                                          f"QComboBox::drop-down{{"
                                          f"  border: 0px;" # Remove arrow border
                                          f"}}"
                                          f"QComboBox::down-arrow{{"
                                          f"  image: url(:/icons/images/arrow_down_50px.png);" # Placeholder for a custom arrow icon if needed
                                          f"  width: 20px; height: 20px;"
                                          f"}}"
                                          f"QComboBox:hover{{"
                                          f"  border: 1px solid {self.SECONDARY_MEDIUM_BLUE};" # Hover effect for border
                                          f"}}"
                                          f"QComboBox::on{{" # Style when dropdown is open
                                          f"  border: 1px solid {self.SECONDARY_MEDIUM_BLUE};"
                                          f"}}"
                                          f"QComboBox QAbstractItemView{{" # Styles for the dropdown list itself
                                          f"  border: 1px solid {self.NEUTRAL_DARK_GRAY};"
                                          f"  border-radius: 5px;"
                                          f"  background-color: {self.WHITE_TEXT};"
                                          f"  selection-background-color: {self.ACCENT_LIGHT_BLUE};"
                                          f"  color: {self.NEUTRAL_DARK_GRAY};"
                                          f"}}")
        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.group_dropdown)

        self.horizontalLayout_3.addWidget(self.actionbuttons)
        self.verticalLayout_2.addWidget(self.details)

        # Patient Table Part
        self.patient_table = QWidget(self.centralwidget)
        self.patient_table.setObjectName(u"patient_table")
        self.patient_table.setMinimumSize(QSize(1053, 445))
        self.patient_table.setStyleSheet(f"background-color: {self.NEUTRAL_LIGHT_GRAY};") # Consistent background
        self.verticalLayout = QVBoxLayout(self.patient_table)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.patient_table)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 44))
        self.frame.setStyleSheet(u"background-color: none;\n"
                                 u"border: none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        # Search Bar
        self.search_bar = QLineEdit(self.frame)
        self.search_bar.setObjectName(u"search_bar")
        self.search_bar.setStyleSheet(f"border: 1px solid {self.NEUTRAL_DARK_GRAY};" # Corrected "solod" to "solid"
                                       f"border-radius: 5px;"
                                       f"color: {self.NEUTRAL_DARK_GRAY};"
                                       f"padding: 9px;"
                                       f"background-color: {self.WHITE_TEXT};"
                                       f"selection-background-color: {self.ACCENT_LIGHT_BLUE};") # Selection color
        self.horizontalLayout_4.addWidget(self.search_bar)

        # Search Button
        self.search_btn = QPushButton(self.frame)
        self.search_btn.setObjectName(u"search_btn")
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(True)
        self.search_btn.setFont(font4)
        self.search_btn.setStyleSheet(
            f"QPushButton{{"
            f"  border: none;"
            f"  border-radius: 5px;"
            f"  background-color: {self.PRIMARY_DARK_BLUE};"
            f"  padding: 8px 15px;"
            f"  color: {self.WHITE_TEXT};"
            f"}}"
            f"QPushButton:hover{{"
            f"  background-color: {self.SECONDARY_MEDIUM_BLUE};" # Hover effect
            f"}}"
        )
        self.horizontalLayout_4.addWidget(self.search_btn)
        self.verticalLayout.addWidget(self.frame)

        # Table Widget
        self.tableWidget = QTableWidget(self.patient_table)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        
        # Set horizontal header item fonts and style
        header_font = QFont()
        header_font.setBold(True)
        header_font.setPointSize(10) # Adjust font size for headers if needed

        headers = ["ID", "Name", "Email", "Contact", "Address", "Profession", "Age", "Gender"]
        for i, text in enumerate(headers):
            __qtablewidgetitem = QTableWidgetItem()
            __qtablewidgetitem.setFont(header_font)
            self.tableWidget.setHorizontalHeaderItem(i, __qtablewidgetitem)
            self.tableWidget.horizontalHeaderItem(i).setText(QCoreApplication.translate("MainWindow", text, None))

        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font3) # Using existing bold font for table content
        self.tableWidget.setTabletTracking(False)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setStyleSheet(
            f"QTableWidget{{"
            f"  background-color: {self.WHITE_TEXT};"
            f"  border: 1px solid {self.NEUTRAL_DARK_GRAY};"
            f"  border-radius: 5px;"
            f"  gridline-color: {self.NEUTRAL_LIGHT_GRAY};" # Lighter grid lines
            f"  color: {self.NEUTRAL_DARK_GRAY};"
            f"}}"
            f"QHeaderView::section{{" # Style for table headers
            f"  background-color: {self.PRIMARY_DARK_BLUE};"
            f"  color: {self.WHITE_TEXT};"
            f"  padding: 5px;"
            f"  border: 1px solid {self.NEUTRAL_LIGHT_GRAY};"
            f"  border-bottom: 2px solid {self.SECONDARY_MEDIUM_BLUE};" # Accent line
            f"}}"
            f"QTableWidget::item{{"
            f"  padding: 5px;"
            f"}}"
            f"QTableWidget::item:selected{{"
            f"  background-color: {self.ACCENT_LIGHT_BLUE};" # Selected item background
            f"  color: {self.NEUTRAL_DARK_GRAY};"
            f"}}"
        )
        self.verticalLayout.addWidget(self.tableWidget)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, -1, -1, -1)

        # Progress Bar
        self.progressBar = QProgressBar(self.patient_table)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(661, 41))
        self.progressBar.setStyleSheet(
            f"QProgressBar {{"
            f"    border: 2px solid {self.PRIMARY_DARK_BLUE};"
            f"    border-radius: 10px;"
            f"    background-color: {self.NEUTRAL_LIGHT_GRAY};"
            f"    text-align: center;"
            f"    color: {self.NEUTRAL_DARK_GRAY};"
            f"    font-weight: bold;"
            f"    padding: 2px;"
            f"    transition: all 0.3s ease-in-out;"
            f"}}"
            f"QProgressBar:hover {{"
            f"    border: 2px solid {self.SECONDARY_MEDIUM_BLUE};"
            f"    background-color: {self.NEUTRAL_LIGHT_GRAY};" # Keep background consistent on hover
            f"}}"
            f"QProgressBar::chunk {{"
            f"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 {self.SECONDARY_MEDIUM_BLUE}, stop:1 {self.PRIMARY_DARK_BLUE});"
            f"    border-radius: 8px;"
            f"    transition: background-color 0.3s ease-in-out;"
            f"}}"
        )
        self.progressBar.setValue(24) # Example value

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.progressBar)

        # Status Label
        self.statusLabel = QLabel(self.patient_table)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setMinimumSize(QSize(233, 41))
        self.statusLabel.setMaximumSize(QSize(428, 16777215))
        self.statusLabel.setStyleSheet(f"background-color: {self.PRIMARY_DARK_BLUE};"
                                       f"color: {self.WHITE_TEXT};"
                                       f"border-radius: 5px;"
                                       f"padding: 5px;"
                                       f"font-weight: bold;") # Added padding and bold for better appearance
        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.statusLabel)

        self.verticalLayout.addLayout(self.formLayout_2)
        self.verticalLayout_2.addWidget(self.patient_table)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WhatsApp Automation System", None)) # Updated window title
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"WHATSAPP AUTOMATION", None)) # Capitalized for consistency
        self.send_message.setText(QCoreApplication.translate("MainWindow", u"Send Message", None)) # More descriptive
        self.cancel_message.setText(QCoreApplication.translate("MainWindow", u"Cancel Send", None)) # More descriptive
        self.all_checkBox.setText(QCoreApplication.translate("MainWindow", u"Select All Contacts", None)) # More descriptive
        self.customize_checkBox.setText(QCoreApplication.translate("MainWindow", u"Customize Message", None)) # More descriptive
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy-MM-dd hh:mm:ss", None)) # Set a common format
        self.group_name_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Group Name (Optional)", None)) # Placeholder text
        self.group_dropdown.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Group", None)) # Placeholder text
        self.search_bar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search contacts here...", None)) # More concise placeholder
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"Search Contacts", None)) # More descriptive
        
        # Table Headers - already set in setupUi, just ensuring retranslateUi aligns
        # ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        # ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        # ... (rest of the table header retranslations are handled by the loop in setupUi now)
        
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Status: Ready", None)) # Default status text
    # retranslateUi
