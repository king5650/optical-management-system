# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar1KjnKaF.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)
import resource_rc
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1149, 681)
        MainWindow.setStyleSheet(u"/*= Style for mainwindow START\n"
"  ==================================================== */\n"
"	#MainWindow {\n"
"		background-color: #fff;\n"
"	}\n"
"QMenuBar {\n"
"    background-color: rgb(49, 58, 70); /* Dark background */\n"
"    padding: 5px 10px; /* Adjust padding for better spacing */\n"
"    color: rgb(230, 230, 230); /* Slightly softer white for text */\n"
"    font: 575 9pt \"Segoe UI\"; /* Use a slightly lighter weight for better readability */\n"
"    border-bottom: 1px solid rgb(60, 70, 85); /* Subtle bottom border for separation */\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background: transparent; /* Make menu bar items transparent by default */\n"
"    padding: 5px 15px;\n"
"    margin: 2px 5px; /* Add some margin around items */\n"
"    border-radius: 4px; /* Slightly rounded corners for items */\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background-color: rgba(58, 139, 212, 50); /* Secondary Blue (Medium) with slight transparency on selection */\n"
"}\n"
"\n"
"QMenuBar::item:pressed {\n"
""
                        "    background-color: rgba(15, 76, 129, 80); /* Dark Blue with slight transparency on press */\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: rgb(245, 245, 245); /* Light background for the menu */\n"
"    border: 1px solid rgb(200, 200, 200);\n"
"    margin: 2px; /* Small margin around the menu */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background: transparent;\n"
"    padding: 8px 25px;\n"
"    color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: rgba(58, 139, 212, 30); /* Light highlight on selection */\n"
"}\n"
"\n"
"QMenu::item:disabled {\n"
"    color: rgb(150, 150, 150);\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 1px;\n"
"    background: rgb(220, 220, 220);\n"
"    margin: 5px 0;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}\n"
"\n"
"QMenu::icon {\n"
"    margin-right: 8px;\n"
"}\n"
"  /*QMenuBar{	\n"
"	background-color: rgb(49, 58, 70);\n"
"	padding: 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	font:"
                        " 700 9pt \"Segoe UI\";\n"
"}\n"
"\n"
"QMenu:hover {\n"
"    border: 2px solid #3A8BD4; /* Secondary Blue (Medium) *\n"
"    background-color: #E6EDF2; /* Keep background consistent on hover *\n"
"}\n"
"QMenu::chunk {\n"
"    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #3A8BD4, stop:1 #0F4C81); /* Gradient for the chunk\n"
"    border-radius: 8px;\n"
"   transition: background-color 0.3s ease-in-out; \n"
"}\n"
"*/\n"
"/*= END\n"
"\n"
"\n"
"  ==================================================== */\n"
"\n"
"/*= Style for button to change menu style START\n"
"  ==================================================== */\n"
"	#change_btn {\n"
"		padding: 5px;\n"
"		border: none;\n"
"		width: 30px;\n"
"		height: 30px;\n"
"	}\n"
"/*= END\n"
"  ==================================================== */\n"
"\n"
"/*= Style for header widget START\n"
"  ==================================================== */\n"
"	#widget {\n"
"		background-color: #f9fafd;\n"
"	}\n"
"/*= END\n"
"  ==========================="
                        "========================= */\n"
"\n"
"/*= Style for menu with icon only START\n"
"  ==================================================== */\n"
"  	/* style for widget */\n"
"	#icon_only_widget {\n"
"		background-color: #313a46;\n"
"		width:50px;\n"
"	}\n"
"\n"
"    /* style for QPushButton and QLabel */\n"
"	#icon_only_widget QPushButton, QLabel {\n"
"		height:50px;\n"
"		border:none;\n"
"		/* border-bottom: 1px solid #b0b0b0; */\n"
"	}\n"
"\n"
"	#icon_only_widget QPushButton:hover {\n"
"		background-color: rgba( 86, 101, 115, 0.5);\n"
"	}\n"
"\n"
"	/* style for logo image */\n"
"	#logo_label_1 {\n"
"		padding: 5px\n"
"	}\n"
"/*= END\n"
"  ==================================================== */\n"
"\n"
"/*= Style for menu with icon and text START\n"
"  ==================================================== */\n"
"	/* style for widget */\n"
"	#full_menu_widget {\n"
"		background-color: #313a46;\n"
"	}\n"
"\n"
"	/* style for QPushButton */\n"
"	#full_menu_widget QPushButton {\n"
"		border:none;\n"
"		border-radius"
                        ": 3px;\n"
"		text-align: left;\n"
"		padding: 8px 0 8px 15px;\n"
"		color: #788596;\n"
"	}\n"
"\n"
"	#full_menu_widget QPushButton:hover {\n"
"		background-color: rgba( 86, 101, 115, 0.5);\n"
"	}\n"
"\n"
"	#full_menu_widget QPushButton:checked {\n"
"		color: #fff;\n"
"	}\n"
"\n"
"	/* style for logo image */\n"
"	#logo_label_2 {\n"
"		padding: 5px;\n"
"		color: #fff;\n"
"	}\n"
"\n"
"	/* style for APP title */\n"
"	#logo_label_3 {\n"
"		padding-right: 10px;\n"
"		color: #fff;\n"
"	}\n"
"/*= END\n"
"  ==================================================== */\n"
"\n"
"/*= Style for search button START\n"
"  ==================================================== */\n"
"	#search_btn {\n"
"		border: none;\n"
"	}\n"
"/*= END\n"
"  ==================================================== */\n"
"\n"
"/*= Style for search input START\n"
"  ==================================================== */\n"
"	#search_input {\n"
"		border: none;\n"
"		padding: 5px 10px;\n"
"	}\n"
"\n"
"	#search_input:focus {\n"
"		background-color: #70B9FE"
                        ";\n"
"	}\n"
"/*= END\n"
"  ==================================================== */\n"
"\n"
"/*= Style for user information button START\n"
"  ==================================================== */\n"
"	#user_btn {\n"
"		border: none;\n"
"	}\n"
"/*= END\n"
"  ==================================================== */")
        self.actionRefresh_Data = QAction(MainWindow)
        self.actionRefresh_Data.setObjectName(u"actionRefresh_Data")
        self.actionImport_Restore_Backup = QAction(MainWindow)
        self.actionImport_Restore_Backup.setObjectName(u"actionImport_Restore_Backup")
        self.actionExport_Save_As = QAction(MainWindow)
        self.actionExport_Save_As.setObjectName(u"actionExport_Save_As")
        self.actionPrint = QAction(MainWindow)
        self.actionPrint.setObjectName(u"actionPrint")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionEdit = QAction(MainWindow)
        self.actionEdit.setObjectName(u"actionEdit")
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionClear = QAction(MainWindow)
        self.actionClear.setObjectName(u"actionClear")
        self.actionToggle_Sidebar = QAction(MainWindow)
        self.actionToggle_Sidebar.setObjectName(u"actionToggle_Sidebar")
        self.actionToggle_Theme = QAction(MainWindow)
        self.actionToggle_Theme.setObjectName(u"actionToggle_Theme")
        self.actionhow_Dashboard_Widgets = QAction(MainWindow)
        self.actionhow_Dashboard_Widgets.setObjectName(u"actionhow_Dashboard_Widgets")
        self.actionWhatsApp_Automation = QAction(MainWindow)
        self.actionWhatsApp_Automation.setObjectName(u"actionWhatsApp_Automation")
        self.actionInventory_Report = QAction(MainWindow)
        self.actionInventory_Report.setObjectName(u"actionInventory_Report")
        self.actionSchedule_Message = QAction(MainWindow)
        self.actionSchedule_Message.setObjectName(u"actionSchedule_Message")
        self.actionChange_Password = QAction(MainWindow)
        self.actionChange_Password.setObjectName(u"actionChange_Password")
        self.actionLogout = QAction(MainWindow)
        self.actionLogout.setObjectName(u"actionLogout")
        self.actionPayment_History = QAction(MainWindow)
        self.actionPayment_History.setObjectName(u"actionPayment_History")
        self.actionPayment_History_2 = QAction(MainWindow)
        self.actionPayment_History_2.setObjectName(u"actionPayment_History_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.verticalLayout_3 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.logo_label_1 = QLabel(self.icon_only_widget)
        self.logo_label_1.setObjectName(u"logo_label_1")
        self.logo_label_1.setMinimumSize(QSize(50, 50))
        self.logo_label_1.setMaximumSize(QSize(50, 50))
        self.logo_label_1.setPixmap(QPixmap(u":/icon/icon/Logo.png"))
        self.logo_label_1.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.logo_label_1)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.home_btn_1 = QPushButton(self.icon_only_widget)
        self.home_btn_1.setObjectName(u"home_btn_1")
        icon = QIcon()
        icon.addFile(u":/icon/icon/home-4-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icon/icon/home-4-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.home_btn_1.setIcon(icon)
        self.home_btn_1.setIconSize(QSize(20, 20))
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_btn_1)

        self.dashborad_btn_1 = QPushButton(self.icon_only_widget)
        self.dashborad_btn_1.setObjectName(u"dashborad_btn_1")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/dashboard-5-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/icon/icon/dashboard-5-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.dashborad_btn_1.setIcon(icon1)
        self.dashborad_btn_1.setIconSize(QSize(20, 20))
        self.dashborad_btn_1.setCheckable(True)
        self.dashborad_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashborad_btn_1)

        self.orders_btn_1 = QPushButton(self.icon_only_widget)
        self.orders_btn_1.setObjectName(u"orders_btn_1")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/activity-feed-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/icon/icon/activity-feed-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.orders_btn_1.setIcon(icon2)
        self.orders_btn_1.setIconSize(QSize(20, 20))
        self.orders_btn_1.setCheckable(True)
        self.orders_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.orders_btn_1)

        self.products_btn_1 = QPushButton(self.icon_only_widget)
        self.products_btn_1.setObjectName(u"products_btn_1")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icon/product-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icon/icon/product-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.products_btn_1.setIcon(icon3)
        self.products_btn_1.setIconSize(QSize(20, 20))
        self.products_btn_1.setCheckable(True)
        self.products_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.products_btn_1)

        self.customers_btn_1 = QPushButton(self.icon_only_widget)
        self.customers_btn_1.setObjectName(u"customers_btn_1")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icon/group-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icon/icon/group-48.ico", QSize(), QIcon.Normal, QIcon.On)
        self.customers_btn_1.setIcon(icon4)
        self.customers_btn_1.setIconSize(QSize(20, 20))
        self.customers_btn_1.setCheckable(True)
        self.customers_btn_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.customers_btn_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 375, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.exit_btn_1 = QPushButton(self.icon_only_widget)
        self.exit_btn_1.setObjectName(u"exit_btn_1")
        icon5 = QIcon()
        icon5.addFile(u":/icon/icon/close-window-64.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn_1.setIcon(icon5)
        self.exit_btn_1.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.exit_btn_1)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_5 = QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 40))
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.change_btn = QPushButton(self.widget)
        self.change_btn.setObjectName(u"change_btn")
        icon6 = QIcon()
        icon6.addFile(u":/icon/icon/menu-4-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.change_btn.setIcon(icon6)
        self.change_btn.setIconSize(QSize(14, 14))
        self.change_btn.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.change_btn)

        self.horizontalSpacer = QSpacerItem(236, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.horizontalLayout_4.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(232, 232, 232);")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_4 = QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_5 = QGridLayout(self.page_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_6 = QGridLayout(self.page_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_7 = QGridLayout(self.page_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_8 = QGridLayout(self.page_7)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.stackedWidget.addWidget(self.page_7)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)

        self.full_menu_widget = QWidget(self.centralwidget)
        self.full_menu_widget.setObjectName(u"full_menu_widget")
        self.verticalLayout_4 = QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.logo_label_2 = QLabel(self.full_menu_widget)
        self.logo_label_2.setObjectName(u"logo_label_2")
        self.logo_label_2.setMinimumSize(QSize(40, 40))
        self.logo_label_2.setMaximumSize(QSize(40, 40))
        self.logo_label_2.setPixmap(QPixmap(u":/icon/icon/Logo.png"))
        self.logo_label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.logo_label_2)

        self.logo_label_3 = QLabel(self.full_menu_widget)
        self.logo_label_3.setObjectName(u"logo_label_3")
        font = QFont()
        font.setPointSize(15)
        self.logo_label_3.setFont(font)

        self.horizontalLayout_2.addWidget(self.logo_label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.home_btn_2 = QPushButton(self.full_menu_widget)
        self.home_btn_2.setObjectName(u"home_btn_2")
        self.home_btn_2.setIcon(icon)
        self.home_btn_2.setIconSize(QSize(14, 14))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_btn_2)

        self.dashborad_btn_2 = QPushButton(self.full_menu_widget)
        self.dashborad_btn_2.setObjectName(u"dashborad_btn_2")
        icon7 = QIcon()
        icon7.addFile(u":/icon/icon/group-32.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.dashborad_btn_2.setIcon(icon7)
        self.dashborad_btn_2.setIconSize(QSize(14, 14))
        self.dashborad_btn_2.setCheckable(True)
        self.dashborad_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashborad_btn_2)

        self.orders_btn_2 = QPushButton(self.full_menu_widget)
        self.orders_btn_2.setObjectName(u"orders_btn_2")
        self.orders_btn_2.setIcon(icon2)
        self.orders_btn_2.setIconSize(QSize(14, 14))
        self.orders_btn_2.setCheckable(True)
        self.orders_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.orders_btn_2)

        self.products_btn_2 = QPushButton(self.full_menu_widget)
        self.products_btn_2.setObjectName(u"products_btn_2")
        self.products_btn_2.setIcon(icon3)
        self.products_btn_2.setIconSize(QSize(14, 14))
        self.products_btn_2.setCheckable(True)
        self.products_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.products_btn_2)

        self.customers_btn_2 = QPushButton(self.full_menu_widget)
        self.customers_btn_2.setObjectName(u"customers_btn_2")
        self.customers_btn_2.setIcon(icon4)
        self.customers_btn_2.setIconSize(QSize(14, 14))
        self.customers_btn_2.setCheckable(True)
        self.customers_btn_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.customers_btn_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 373, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.exit_btn_2 = QPushButton(self.full_menu_widget)
        self.exit_btn_2.setObjectName(u"exit_btn_2")
        self.exit_btn_2.setIcon(icon5)
        self.exit_btn_2.setIconSize(QSize(14, 14))

        self.verticalLayout_4.addWidget(self.exit_btn_2)


        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1149, 41))
        self.menuFiles = QMenu(self.menuBar)
        self.menuFiles.setObjectName(u"menuFiles")
        self.menuEdit = QMenu(self.menuBar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menuBar)
        self.menuView.setObjectName(u"menuView")
        self.menuTools = QMenu(self.menuBar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuUser = QMenu(self.menuBar)
        self.menuUser.setObjectName(u"menuUser")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFiles.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.menuBar.addAction(self.menuUser.menuAction())
        self.menuFiles.addAction(self.actionRefresh_Data)
        self.menuFiles.addSeparator()
        self.menuFiles.addAction(self.actionImport_Restore_Backup)
        self.menuFiles.addAction(self.actionExport_Save_As)
        self.menuFiles.addSeparator()
        self.menuFiles.addAction(self.actionPrint)
        self.menuFiles.addSeparator()
        self.menuFiles.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionEdit)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addAction(self.actionClear)
        self.menuView.addAction(self.actionToggle_Sidebar)
        self.menuView.addAction(self.actionToggle_Theme)
        self.menuView.addAction(self.actionhow_Dashboard_Widgets)
        self.menuTools.addAction(self.actionWhatsApp_Automation)
        self.menuTools.addAction(self.actionInventory_Report)
        self.menuTools.addAction(self.actionSchedule_Message)
        self.menuTools.addAction(self.actionPayment_History_2)
        self.menuUser.addAction(self.actionChange_Password)
        self.menuUser.addAction(self.actionLogout)

        self.retranslateUi(MainWindow)
        self.change_btn.toggled.connect(self.icon_only_widget.setVisible)
        self.change_btn.toggled.connect(self.full_menu_widget.setHidden)
        self.home_btn_1.toggled.connect(self.home_btn_2.setChecked)
        self.dashborad_btn_1.toggled.connect(self.dashborad_btn_2.setChecked)
        self.orders_btn_1.toggled.connect(self.orders_btn_2.setChecked)
        self.products_btn_1.toggled.connect(self.products_btn_2.setChecked)
        self.customers_btn_1.toggled.connect(self.customers_btn_2.setChecked)
        self.home_btn_2.toggled.connect(self.home_btn_1.setChecked)
        self.dashborad_btn_2.toggled.connect(self.dashborad_btn_1.setChecked)
        self.orders_btn_2.toggled.connect(self.orders_btn_1.setChecked)
        self.products_btn_2.toggled.connect(self.products_btn_1.setChecked)
        self.customers_btn_2.toggled.connect(self.customers_btn_1.setChecked)
        self.exit_btn_2.clicked.connect(MainWindow.close)
        self.exit_btn_1.clicked.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionRefresh_Data.setText(QCoreApplication.translate("MainWindow", u"Refresh Data", None))
        self.actionImport_Restore_Backup.setText(QCoreApplication.translate("MainWindow", u"Import/Restore Backup", None))
        self.actionExport_Save_As.setText(QCoreApplication.translate("MainWindow", u"Export/Save As", None))
        self.actionPrint.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionEdit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.actionClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.actionToggle_Sidebar.setText(QCoreApplication.translate("MainWindow", u"Toggle Sidebar", None))
        self.actionToggle_Theme.setText(QCoreApplication.translate("MainWindow", u"Toggle Theme", None))
        self.actionhow_Dashboard_Widgets.setText(QCoreApplication.translate("MainWindow", u"how Dashboard Widgets", None))
        self.actionWhatsApp_Automation.setText(QCoreApplication.translate("MainWindow", u"WhatsApp Automation", None))
        self.actionInventory_Report.setText(QCoreApplication.translate("MainWindow", u"Inventory Report", None))
        self.actionSchedule_Message.setText(QCoreApplication.translate("MainWindow", u"Schedule Message", None))
        self.actionChange_Password.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.actionPayment_History.setText(QCoreApplication.translate("MainWindow", u"Payment History", None))
        self.actionPayment_History_2.setText(QCoreApplication.translate("MainWindow", u"Payment History", None))
        self.logo_label_1.setText("")
        self.home_btn_1.setText("")
        self.dashborad_btn_1.setText("")
        self.orders_btn_1.setText("")
        self.products_btn_1.setText("")
        self.customers_btn_1.setText("")
        self.exit_btn_1.setText("")
        self.change_btn.setText("")
        self.logo_label_2.setText("")
        self.logo_label_3.setText(QCoreApplication.translate("MainWindow", u"Sidebar", None))
        self.home_btn_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.dashborad_btn_2.setText(QCoreApplication.translate("MainWindow", u"Patients", None))
        self.orders_btn_2.setText(QCoreApplication.translate("MainWindow", u"Medical Reports", None))
        self.products_btn_2.setText(QCoreApplication.translate("MainWindow", u"Inventory", None))
        self.customers_btn_2.setText(QCoreApplication.translate("MainWindow", u"WhatsApp", None))
        self.exit_btn_2.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.menuFiles.setTitle(QCoreApplication.translate("MainWindow", u"Files", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools ", None))
        self.menuUser.setTitle(QCoreApplication.translate("MainWindow", u"User", None))
    # retranslateUi

