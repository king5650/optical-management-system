# dashboard.py

from PySide6.QtCore import Qt, QSize, QTimer
from PySide6.QtGui import QIcon, QFont, QAction, QColor
from PySide6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QFrame, QSizePolicy, QButtonGroup, QSpacerItem,
    QGraphicsDropShadowEffect, QStackedWidget, QMenu
)
from PySide6.QtCore import QTranslator, QLocale, QEvent, QLibraryInfo

import sys
import os
import random
import requests
from PySide6.QtCore import Signal, QTranslator, QCoreApplication, QLocale


from modules.patient_module.patient_registratioin_system import PatientForm
from testform import MedicalReportForm
from modules.patient_module.patient_medicalLIst import MedicalReportSystem

from medicalrepotForms import MedicalReportForm
#from messgae_test import MessageAutomationsystem
from whatsapp_auto.main import whatsapp_automation_MainWindow 

#imported modules
#backup module
from modules.backup_module.backup_panel import BackupPanel #ok
from modules.backup_module.BACKUPSYSTEM import BackupRestoreApp#ok

#inventory system
from modules.inventory_module.inventory_system import InventorySystem #ok
from modules.inventory_module.inventory_report_viewer import InventoryReportViewer #ok
from modules.inventory_module.inventory_system_itemform_ui import ItemTypeForm #ok
from modules.inventory_module.InventoryManager_dashboard import InventoryManager #ok
from modules.inventory_module.inventory_system_itemform_ui import ItemTypeForm #ok

#patient registration system
from modules.patient_module.patient_registratioin_system import PatientForm #ok
from modules.patient_module.patient_medicalLIst import MedicalReportSystem #ok

#sales modules
from modules.sales_module.sales_puchase_board import PurchaseBoardManager #ok
#from modules.sales_module.PaymentHistoryDialog import PaymentHistoryDialog #ok
from modules.sales_module.payment_history_report import PaymentHistoryDialog #ok
from modules.sales_module.month_sales_and_exits import MonthlyReportManager #ok

from modules.main_app.home_card import MainWindow #ok

from ui_ux.main_app.ui_sidebar11  import Ui_MainWindow

from translation_manager import TranslationManager

#task schedular
# from whatsapp_auth_system_final.job_scheduler import JobScheduler
from whatsapp_auto.main import whatsapp_automation_MainWindow 
from PySide6.QtWidgets import QGraphicsBlurEffect


# ---- Theme (Dark Mode Professional) ----
THEME = {
    "bg": "none",#"#1E1E2F"
    "bg_1": "#1E1E2F",#
    "bg_2": "white",#
    # "bg": "qlineargradient(spread:pad, x1:0, y1:0.267, x2:1, y2:0.471, stop:0 rgba(2, 101, 195, 255), stop:1 rgba(44, 47, 132, 255))",    
    # "bg_alt": "#222236",
    "bg_alt": "qlineargradient(spread:pad, x1:0, y1:0.267, x2:1, y2:0.471, stop:0 rgba(2, 101, 195, 255), stop:1 rgba(44, 47, 132, 255))",  
    # "card": "#2A2A40", #background-color: rgb(44, 47, 134);
    "card": "rgb(44, 47, 134)", 
    "border": "#343454",
    "text": "#E5E7EB",
    "text_dim": "#C7CBD1",
    "muted": "#9AA0A6",
    "primary": "#3B82F6",
    "success": "#10B981",
    "warning": "#F59E0B",
    "danger": "#EF4444",
    "highlight": "#334155"
}

FONT_FAMILY = "Segoe UI, Inter, Roboto, Arial"

def apply_shadow(widget, radius=18, opacity=0.25, y_offset=6):
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(radius)
    col = QColor(0, 0, 0)
    col.setAlphaF(max(0.0, min(1.0, opacity)))
    shadow.setColor(col)
    shadow.setOffset(0, y_offset)
    widget.setGraphicsEffect(shadow)


# class SidebarButton(QPushButton):
#     def __init__(self, text, icon_char="•", parent=None):
#         super().__init__(parent)
#         self.setCheckable(True)
#         self.setCursor(Qt.PointingHandCursor)
#         self.setText(f"  {icon_char}  {text}")
#         self.setMinimumHeight(40)
#         self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
#         self.setObjectName("SidebarButton")
class SidebarButton(QPushButton):
    def __init__(self, text, icon=None, parent=None):
        super().__init__(parent)
        self.setCheckable(True)
        self.setCursor(Qt.PointingHandCursor)
        self.setText(f"  {text}")
        self.setMinimumHeight(40)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setObjectName("SidebarButton")
        if icon is not None:
            self.setIcon(icon)
            self.setIconSize(QSize(24, 24))  # Adjust size as needed

class StatCard(QFrame):
    def __init__(self, title, value, subtitle="", accent=THEME["primary"], icon_char="•", parent=None):
        super().__init__(parent)
        self.accent = accent
        self.icon_char = icon_char
        self.setObjectName("StatCard")
        self.setStyleSheet(f"""
            QFrame#StatCard {{
                background-color: {THEME['card']};
                border: 1px solid white;
                border-radius: 12px;
            }}
        """)
        apply_shadow(self, radius=28, opacity=0.2, y_offset=10)

        self.value_lbl = QLabel(value)

        lay = QVBoxLayout(self)
        lay.setContentsMargins(16, 16, 16, 16)
        lay.setSpacing(8)

        # Top row
        top = QHBoxLayout()
        top.setSpacing(8)
        icon = QLabel(self.icon_char)
        icon.setObjectName("CardIcon")
        icon.setFixedSize(28, 28)
        icon.setAlignment(Qt.AlignCenter)
        icon.setStyleSheet(f"""
            QLabel#CardIcon {{
                color: {THEME['text']};
                /*background-color: {self.accent}22;*/
                background-color: {THEME['bg_2']};
                border: 1px solid {self.accent}55;
                border-radius: 6px;
                font-size: 16px;
                font-weight: 900px;
            }}
        """)

        title_lbl = QLabel(title)
        # title_lbl.setStyleSheet(f"color: {THEME['text_dim']};")
        title_lbl.setStyleSheet(f"color: white; font-weight: 500;")
        title_font = QFont(FONT_FAMILY, 12, QFont.Medium)
        title_lbl.setFont(title_font)

        top.addWidget(icon)
        top.addWidget(title_lbl, 1)
        top.addStretch(1)

        # Value
        value_font = QFont(FONT_FAMILY, 28, QFont.DemiBold)
        self.value_lbl.setFont(value_font)
        self.value_lbl.setStyleSheet(f"color: {THEME['text']};")

        # Subtitle
        subtitle_lbl = QLabel(subtitle)
        subtitle_lbl.setStyleSheet(f"color: {THEME['bg_2']}; font-weight: 500;")
        subtitle_font = QFont(FONT_FAMILY, 12)
        subtitle_lbl.setFont(subtitle_font)

        lay.addLayout(top)
        lay.addSpacing(4)
        lay.addWidget(self.value_lbl)
        lay.addWidget(subtitle_lbl)
        lay.addStretch(1)

    def update_value(self, value: str):
        self.value_lbl.setText(value)


class Header(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Header")
        self.setStyleSheet(f"""
            QFrame#Header {{
                background-color: {THEME['bg_alt']};
                border-bottom: 1px solid {THEME['border']};
            }}
        """)
        lay = QHBoxLayout(self)
        lay.setContentsMargins(16, 10, 16, 10)
        lay.setSpacing(12)

        self.title = QLabel("Optics Dashboard")
        title_font = QFont(FONT_FAMILY, 18, QFont.DemiBold)
        self.title.setFont(title_font)
        self.title.setStyleSheet(f"color: {THEME['text']};")

        # search = QLineEdit()
        # search.setPlaceholderText("Search patients, sales, appointments…")
        # search.setClearButtonEnabled(True)
        # search.setObjectName("Search")
        # search.setMinimumWidth(320)
        # search.setStyleSheet(f"""
        #     QLineEdit#Search {{
        #         background: {THEME['bg']};
        #         color: {THEME['text']};
        #         border: 1px solid {THEME['border']};
        #         border-radius: 8px;
        #         padding: 8px 12px;
        #         selection-background-color: {THEME['primary']}AA;
        #     }}
        # """)

        spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        profile = QPushButton("User")
        profile.setCursor(Qt.PointingHandCursor)
        profile.setObjectName("Profile")
        profile.setMinimumHeight(34)
        profile.setStyleSheet(f"""
            QPushButton#Profile {{
                color: {THEME['text']};
                background: {THEME['bg']};
                border: 1px solid {THEME['border']};
                border-radius: 8px;
                padding: 6px 12px;
            }}
        """)

        lay.addWidget(self.title)
        lay.addSpacing(8)
        # lay.addWidget(search)
        lay.addItem(spacer)
        lay.addWidget(profile)

    def update_title(self, title: str):
        self.title.setText(title)
                
class Sidebar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.expanded = True
        self.full_width = 220
        self.collapsed_width = 60
        self.setFixedWidth(self.full_width)
        self.setObjectName("Sidebar")
        self.setFixedWidth(220)
        self.setStyleSheet(f"""
            QFrame#Sidebar {{
                background-color: {THEME['bg_alt']};
                border-right: 1px solid {THEME['border']};
            }}
            QPushButton#SidebarButton {{
                color: {THEME['text']};
                background-color: transparent;
                border: none;
                border-radius: 8px;
                padding: 8px 10px;
                text-align: left;
                font-size: 18px;
                font-weight: 900px;
            }}
            QPushButton#SidebarButton:hover {{
                background-color: {THEME['highlight']};
            }}
            QPushButton#SidebarButton:checked {{
                background-color: {THEME['primary']}22;
                border: 1px solid {THEME['primary']}55;
            }}
        """)

        lay = QVBoxLayout(self)
        lay.setContentsMargins(12, 16, 12, 16)
        lay.setSpacing(6)

        brand = QLabel("OptiCare")
        brand.setFont(QFont(FONT_FAMILY, 16, QFont.DemiBold))
        brand.setStyleSheet(f"color: {THEME['text']};")
        muted = QLabel("v1.0")
        muted.setStyleSheet(f"color: {THEME['muted']}; font-size: 12px;")

        lay.addWidget(brand)
        lay.addWidget(muted)
        lay.addSpacing(12)

        self.group = QButtonGroup(self)
        self.group.setExclusive(True)

        # self.btn_home = SidebarButton("Home", "🏠")
        # self.btn_patients = SidebarButton("Patients", "👤")
        # self.btn_sales = SidebarButton("Sales", "🛒")
        # self.btn_appts = SidebarButton("Appointments", "📅")
        # self.btn_settings = SidebarButton("Settings", "⚙️")
        
        from PySide6.QtGui import QIcon

        self.btn_home = SidebarButton("Home", QIcon("images/home_icon2.png"))
        self.btn_patients = SidebarButton("Patients", QIcon("images/patient_icon1.png"))
        self.btn_sales = SidebarButton("Sales", QIcon("images/sales_icon.png"))
        self.btn_medical_report = SidebarButton("Medical Rport", QIcon("images/med_rep.png"))
        self.btn_appts = SidebarButton("Appointments", QIcon("images/appointments.png"))
        self.btn_settings = SidebarButton("Settings", QIcon("images/settings.png"))
        for i, b in enumerate([
            self.btn_home, self.btn_patients, self.btn_sales,  self.btn_medical_report,
            self.btn_appts, self.btn_settings
        ]):
            lay.addWidget(b)
            self.group.addButton(b, i)

        lay.addStretch(1)

        cta = QPushButton("➕ New patient")
        cta.setCursor(Qt.PointingHandCursor)
        cta.setMinimumHeight(40)
        cta.setObjectName("CTA")
        cta.setStyleSheet(f"""
            QPushButton#CTA {{
                color: {THEME['bg']};
                background-color: {THEME['success']};
                border: none;
                border-radius: 8px;
                font-weight: 600;
            }}
        """)
        lay.addWidget(cta)
        self.btn_home.setChecked(True)


# class DashboardView(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setStyleSheet(f"background-color: {THEME['bg']};")
#         outer = QVBoxLayout(self)
#         outer.setContentsMargins(16, 16, 16, 16)
#         outer.setSpacing(16)

#         row1 = QHBoxLayout()
#         row1.setSpacing(16)

#         self.card_patients = StatCard("Patients", "0", "Total registered", THEME["primary"], "👤")
#         self.card_sales = StatCard("Sales", "0", "Sales count", THEME["success"], "🛒")
#         self.card_appts = StatCard("Appointments", "0", "Scheduled today", THEME["warning"], "📅")
#         self.card_new = StatCard("New Patient", "Loading…", "Preparing form", THEME["primary"], "➕")

#         for c in [self.card_patients, self.card_sales, self.card_appts, self.card_new]:
#             c.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
#             row1.addWidget(c)

#         outer.addLayout(row1)
#         outer.addStretch(1)

#         # Timer to simulate real-time updates
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.refresh_data)
#         self.timer.start(3000)  # every 3 seconds

#     def refresh_data(self):
#         # Simulate data updates (replace with DB/API calls in real apps)
#         self.card_patients.update_value(str(random.randint(20, 100)))
#         self.card_sales.update_value(str(random.randint(100, 500)))
#         self.card_appts.update_value(str(random.randint(5, 30)))
#         self.card_new.update_value("Ready")




class DashboardView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(f"background-color: {THEME['bg']};")
        outer = QVBoxLayout(self)
        outer.setContentsMargins(16, 16, 16, 16)
        outer.setSpacing(16)

        row1 = QHBoxLayout()
        row1.setSpacing(16)

        # Add desc_label to each StatCard
        self.card_patients = StatCard("Patients", "0", "Total registered", THEME["primary"], "👤")
        self.card_patients.desc_label = QLabel("0 patients registered.")
        self.card_patients.desc_label.setStyleSheet(f"color: {THEME['text']}; font-size: 20px; font-weight: 500;")
        self.card_patients.layout().addWidget(self.card_patients.desc_label)

        self.card_sales = StatCard("Sales", "0", "Sales count", THEME["success"], "🛒")
        self.card_sales.desc_label = QLabel("0 Sales Count.")
        self.card_sales.desc_label.setStyleSheet(f"color: {THEME['bg_2']}; font-size: 20px; font-weight: 500;")
        self.card_sales.layout().addWidget(self.card_sales.desc_label)
        
        #self.card_sales = StatCard("Sales", "0", "Sales count", THEME["success"], "🛒")
        #self.card_sales.desc_label = QLabel("0 Sales Count.")
        #self.card_sales.desc_label.setStyleSheet("color: red; font-size: 20px; font-weight: 500;")  # Custom color for desc_label
        #self.card_sales.value_lbl.setStyleSheet("color: green; font-size: 28px; font-weight: bold;")  # Custom color for value label
        # If you want to change the subtitle label color, you need to access it in StatCard and set its style there.
        #self.card_sales.layout().addWidget(self.card_sales.desc_label)                

        self.medical_rep = StatCard("Medical Report", "0", "Scheduled today", THEME["warning"], "📅")
        self.medical_rep.desc_label = QLabel("0 Medical Report.")
        self.medical_rep.desc_label.setStyleSheet(f"color: {THEME['bg_2']}; font-size: 20px; font-weight: 500;")
        self.medical_rep.layout().addWidget(self.medical_rep.desc_label)

        self.card_Inven_item = StatCard("Item Inventory", "0", "Scheduled today", THEME["warning"], "📅")
        self.card_Inven_item.desc_label = QLabel("0 Item Inventory.")
        self.card_Inven_item.desc_label.setStyleSheet(f"color: {THEME['bg_2']}; font-size: 20px; font-weight: 500;")
        self.card_Inven_item.layout().addWidget(self.card_Inven_item.desc_label)


        self.card_appts = StatCard("Appointments", "0", "Scheduled today", THEME["warning"], "📅")
        self.card_appts.desc_label = QLabel("0 appointments.")
        self.card_appts.desc_label.setStyleSheet(f"color: {THEME['bg_2']}; font-size: 20px; font-weight: 500;")
        self.card_appts.layout().addWidget(self.card_appts.desc_label)

        self.card_new = StatCard("New Patient", "Loading…", "Preparing form", THEME["primary"], "➕")

        # for c in [self.card_patients, self.card_sales, self.card_appts, self.medical_rep, self.card_Inven_item, self.card_new]:
        #     c.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        #     row1.addWidget(c)

        # Arrange cards in rows of 3
        cards = [
            self.card_patients,
            self.card_sales,
            self.card_appts,
            self.medical_rep,
            self.card_Inven_item,
            self.card_new
        ]

        for i in range(0, len(cards), 3):
            row = QHBoxLayout()
            row.setSpacing(16)
            for card in cards[i:i+3]:
                card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
                row.addWidget(card)
            outer.addLayout(row)


        outer.addLayout(row1)
        outer.addStretch(1)

        # Store cards in a list for easy access
        self.cards = [self.card_patients, self.card_sales, self.card_appts]

        # Timer to simulate real-time updates and fetch backend data
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_cards_from_backend)
        self.timer.start(3000)  # every 3 seconds

    # def update_cards_from_backend(self):
    #     try:
    #         response = requests.get("http://127.0.0.1:8000/auth/dashboard-counts/")
    #         if response.status_code == 200:
    #             data = response.json()
    #             # Update card descriptions with real data
    #             self.cards[0].desc_label.setText(f"{data.get('patient_count', 0)} patients registered.")
    #             self.cards[1].desc_label.setText(f"{data.get('sales_count', 0)} Sales Count.")
    #             self.cards[2].desc_label.setText(f"{data.get('appointment_count', 0)} appointments.")
    #         else:
    #             print("Failed to fetch dashboard data:", response.text)
    #     except Exception as e:
    #         print("Error fetching dashboard data:", e)
    def update_cards_from_backend(self):
        try:
            response = requests.get("http://127.0.0.1:8000/auth/dashboard-counts/")
            if response.status_code == 200:
                data = response.json()

                patient_count = data.get('patient_count', 0)
                sales_count = data.get('sales_count', 0)
                medical_report_count = data.get('medical_report_count', 0)
                inventory_county_count = data.get('inventory_count', 0)
                appointment_count = data.get('appointment_count', 0)

                # ✅ Update main values AND descriptions
                self.card_patients.update_value(str(patient_count))
                self.card_patients.desc_label.setText(f"{patient_count} patients registered.")

                self.card_sales.update_value(str(sales_count))
                self.card_sales.desc_label.setText(f"{sales_count} Sales Count.")
                
                self.medical_rep.update_value(str(medical_report_count))
                self.medical_rep.desc_label.setText(f"{medical_report_count} Medical report Count.")
                
                self.card_Inven_item.update_value(str(inventory_county_count))
                self.card_Inven_item.desc_label.setText(f"{inventory_county_count} Inventory Count.")
                

                self.card_appts.update_value(str(appointment_count))
                self.card_appts.desc_label.setText(f"{appointment_count} appointments.")

            else:
                print("Failed to fetch dashboard data:", response.text)
        except Exception as e:
            print("Error fetching dashboard data:", e)


# Placeholder views for other tabs
class PlaceholderView(QWidget):
    def __init__(self, name):
        super().__init__()
        self.setStyleSheet(f"background-color: {THEME['bg']};")
        layout = QVBoxLayout(self)
        label = QLabel(f"{name} View Coming Soon")
        label.setFont(QFont(FONT_FAMILY, 16))
        label.setStyleSheet(f"color: {THEME['text']};")
        layout.addWidget(label, alignment=Qt.AlignCenter)


class MainWindow(QMainWindow):
    language_changed = Signal(str)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Optics Dashboard")
        self.resize(1200, 760)
        central = QWidget()
        self.setCentralWidget(central)
        
        self.translators = {
            'en': QTranslator(),
            'fr': QTranslator()
        }
        
        # Load .qm files
        self.translators['en'].load("i18n/en.qm")
        self.translators['fr'].load("i18n/fr.qm")

        # Default language
        self.current_lang = 'en'
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: qlineargradient(spread:pad, x1:0, y1:0.267, x2:1, y2:0.471, stop:0 rgba(2, 101, 195, 255), stop:1 rgba(44, 47, 132, 255));                
            }
        """)
        root = QVBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        self.header = Header()
        root.addWidget(self.header)

        body = QHBoxLayout()
        body.setContentsMargins(0, 0, 0, 0)
        body.setSpacing(0)
        
        self._create_toolbar()

        self.sidebar = Sidebar()
        body.addWidget(self.sidebar)

        self.stack = QStackedWidget()
        # self.stack.setStyleSheet(f"""
        #     QStackedWidget {{
        #         background-color: {THEME['card']};
        #         border: 1px solid {THEME['border']};
        #         border-radius: 12px;
        #     }}
        # """)        
        self.views = {
            0: DashboardView(),
            1: PatientForm(),
            2: PurchaseBoardManager(),
            3: MedicalReportSystem(),
            4: PlaceholderView("Appointments"),
            # 5: PlaceholderView("Settings"),
            #tool section
            5: InventoryReportViewer(),
            6: PaymentHistoryDialog(),
            7: InventorySystem(),
            8: InventoryManager(),
            9: ItemTypeForm(),
            10: InventoryManager(),
            #files InventoryManager
            11: BackupPanel(),
            12: BackupRestoreApp(),
            #13: whatsapp_automation_MainWindow(),
            13: whatsapp_automation_MainWindow(),
        }
# from modules.backup_module.backup_panel import BackupPanel #ok
# from modules.backup_module.BACKUPSYSTEM import BackupRestoreApp#ok 
        for view in self.views.values():
            self.stack.addWidget(view)

        body.addWidget(self.stack, 1)
        root.addLayout(body)

        self.sidebar.group.idClicked.connect(self.on_nav_clicked)
        self._create_actions()

    def _create_actions(self):
        self.act_quit = QAction("Quit", self)
        self.act_quit.triggered.connect(QApplication.instance().quit)
        self.addAction(self.act_quit)

    def on_nav_clicked(self, idx):
        titles = ["Home", "Patients", "Sales", "Appointments", "Settings", "Inventory"]
        self.stack.setCurrentIndex(idx)
        self.header.update_title(f"Optics Dashboard · {titles[idx]}")


    def _create_toolbar(self):
        toolbar = self.addToolBar("Main Toolbar")
        toolbar.setMovable(False)
        toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        toolbar.setStyleSheet(f"""
            QToolBar {{
                background: {THEME['bg_alt']};
                border-bottom: 1px solid {THEME['border']};
                spacing: 6px;
                padding: 6px;
            }}
        """)


        # 🔄 Refresh Action
        act_refresh = QAction("🔄 Refresh", self)
        act_refresh.setToolTip("Refresh dashboard data")
        # act_refresh.triggered.connect(self.refresh_dashboard)

        # ❌ Quit Action
        act_quit = QAction("❌ Quit", self)
        act_quit.setToolTip("Exit the application")
        act_quit.triggered.connect(QApplication.instance().quit)

        # 👁 View Menu (with dropdown)
        view_menu = QMenu(self)
        view_menu.setStyleSheet(f"""
            QMenu {{
                background-color: {THEME['bg_1']};
                color: {THEME['text']};
                border: 1px solid {THEME['border']};
                spacing: 6px;
                padding: 6px;                
            }}
            QMenu::item:selected {{
                background-color: {THEME['highlight']};
            }}
        """)
        # Add view switching options
        #view_menu.addAction("EN English", lambda: self.switch_view(0))
        #view_menu.addAction("FR French", lambda: self.switch_view(1))

        #view_menu.addAction("🛒 Sales", lambda: self.switch_view(2))
        #view_menu.addAction("📅 Appointments", lambda: self.switch_view(3))
        #view_menu.addAction("⚙️ Settings", lambda: self.switch_view(4))

        #tools
        tool_menu =  QMenu(self)
        tool_menu.setStyleSheet(f"""
            QMenu {{
                background-color: {THEME['bg_1']};
                color: {THEME['text']};
                border: 1px solid {THEME['border']};
                spacing: 6px;
                padding: 6px;                
            }}
            QMenu::item:selected {{
                background-color: {THEME['highlight']};
            }}
            QMenu::separator {{
                height: 1px;
                background: white;
                margin: 6px 0;}}
        """)        
        # tool_menu.addAction("🏠 Inverntory Report", lambda: self.switch_view(5))
        # tool_menu.addAction("🏠 Payment History", lambda: self.switch_view(6))
        # tool_menu.addAction("👤 Add Categorie/Items", lambda: self.switch_view(7))
        # tool_menu.addAction("🛒 Entery/Sales Report", lambda: self.switch_view(8))
        # tool_menu.addAction("📅 Payment History", lambda: self.switch_view(9))
        tool_menu.addAction(QAction(QIcon("images/report_file_64px.png"), "Inventory Report", self, triggered=lambda: self.switch_view(5)))        
        tool_menu.addAction(QAction(QIcon("images/add_property_40px.png"), "Add Categorie/Items", self, triggered=lambda: self.switch_view(9)))
        tool_menu.addAction(QAction(QIcon("images/add_property_40px.png"), "Inventory Managment", self, triggered=lambda: self.switch_view(10)))
        tool_menu.addSeparator()
        tool_menu.addAction(QAction(QIcon("images\payment_history_50px.png"), "Payment History", self, triggered=lambda: self.switch_view(6)))
        tool_menu.addSeparator()
        tool_menu.addAction(QAction(QIcon("images\phone_message_48px.png"), "Message Automation", self, triggered=lambda: self.switch_view(13)))
        tool_menu.addSeparator()
        # tool_menu.addAction(self.act_lang_en)
        # tool_menu.addAction(self.act_lang_fr)
        # # connect signal so other windows can update
        # self.language_changed.connect(self.on_language_changed)
    # ...existing code...        
        # tool_menu.addAction(QAction(QIcon("icons/business_report_64px.png"), "Entery/Sales Report", self, triggered=lambda: self.switch_view(8))) ItemTypeForm
        # tool_menu.addAction(QAction(QIcon("icons/payment_history.png"), "Payment History", self, triggered=lambda: self.switch_view(9)))        
                
                        
        tool_btn = QPushButton("⚙️ Tools")
        tool_btn.setCursor(Qt.PointingHandCursor)
        tool_btn.setStyleSheet(f"""
            QPushButton {{
                background: transparent;
                color: {THEME['text']};
                border: none;
                padding: 4px 12px;
            }}
            QPushButton:hover {{
                background-color: {THEME['highlight']};
            }}
        """)
        tool_btn.setMenu(tool_menu)
        
        #file section
        file_menu =  QMenu(self)
        file_menu.setStyleSheet(f"""
            QMenu {{
                background-color: {THEME['bg_1']};
                color: {THEME['text']};
                border: 1px solid {THEME['border']};
                spacing: 6px;
                padding: 6px;                
            }}
            QMenu::item:selected {{
                background-color: {THEME['highlight']};
            }}
        """)        
        # file_menu.addAction("🏠 Open session", lambda: self.switch_view(10))
        file_menu.addAction(QAction(QIcon("images\opened_folder_48px.png"), "Open Session", self, triggered=lambda: self.switch_view(11)))
        file_menu.addAction(QAction(QIcon("images\database_100px.png"), "Import/Export Data", self, triggered=lambda: self.switch_view(12)))
        # file_menu.addAction("🏠 Import/Export Data", lambda: self.switch_view(11))
      
                        
        file_btn = QPushButton("⚙️ files")
        file_btn.setCursor(Qt.PointingHandCursor)
        file_btn.setStyleSheet(f"""
            QPushButton {{
                background: transparent;
                color: {THEME['text']};
                border: none;
                padding: 4px 12px;
            }}
            QPushButton:hover {{
                background-color: {THEME['highlight']};
            }}
        """)
        file_btn.setMenu(file_menu)
        
        
        #Language section             
        language_menu =  QMenu(self)
        language_menu.setStyleSheet(f"""
            QMenu {{
                background-color: {THEME['bg_1']};
                color: {THEME['text']};
                border: 1px solid {THEME['border']};
                spacing: 6px;
                padding: 6px;                
            }}
            QMenu::item:selected {{
                background-color: {THEME['highlight']};
            }}
        """)        
        # language_menu.addAction("🏠 Open session", lambda: self.switch_view(10))
        language_menu.addAction(QAction(QIcon("images\opened_folder_48px.png"), "fr", self, triggered=lambda: self.change_language('fr')))
        language_menu.addAction(QAction(QIcon("images\database_100px.png"), "en", self, triggered=lambda: self.change_language('en')))
        # language_menu.addAction("🏠 Import/Export Data", lambda: self.switch_view(11))
      
                        
        language_btn = QPushButton("⚙️ languages")
        language_btn.setCursor(Qt.PointingHandCursor)
        language_btn.setStyleSheet(f"""
            QPushButton {{
                background: transparent;
                color: {THEME['text']};
                border: none;
                padding: 4px 12px;
            }}
            QPushButton:hover {{
                background-color: {THEME['highlight']};
            }}
        """)
        language_btn.setMenu(language_menu)        
        
        
        # Add actions and widget to toolbar
        toolbar.addWidget(file_btn)
        toolbar.addSeparator()
        toolbar.addAction(act_refresh)
        toolbar.addWidget(tool_btn)
        toolbar.addWidget(language_btn)        
        toolbar.addSeparator()
        toolbar.addAction(act_quit)


    # def switch_view(self, index):
    #     titles = ["Home", "Patients", "Sales", "Appointments", "Settings", "Inventory"]
    #     self.stack.setCurrentIndex(index)
    #     self.sidebar.group.button(index).setChecked(True)
    #     self.header.update_title(f"Optics Dashboard · {titles[index]}")
    
    # def switch_view(self, index):
    #     titles = ["Home", "Patients", "Sales", "Appointments", "Settings", "Inventory", "Payment History", "Add Categorie/Items", "Entery/Sales Report", "Payment History", "Open session","Import/Export Data", "Message Automation"]

    #     self.stack.setCurrentIndex(index)

    #     # Only set the sidebar button if it exists
    #     button = self.sidebar.group.button(index)
    #     if button:
    #         button.setChecked(True)
        
    #     self.header.update_title(f"Optics Dashboard · {titles[index]}")

    def switch_view(self, index):
        titles = [
            "Home", "Patients", "Sales", "Appointments", "Settings", "Inventory",
            "Payment History", "Add Categorie/Items", "Entery/Sales Report",
            "Payment History", "Open session", "Import/Export Data", "Message Automation"
        ]

        # prevent invalid stack index usage
        if index < 0 or index >= self.stack.count():
            return

        self.stack.setCurrentIndex(index)

        # Only set the sidebar button if it exists
        button = self.sidebar.group.button(index)
        if button:
            button.setChecked(True)

        # safe title lookup with fallback
        if 0 <= index < len(titles):
            title = titles[index]
        else:
            # fallback to widget class name if titles list is shorter than views
            widget = self.stack.widget(index)
            title = widget.__class__.__name__ if widget is not None else "Unknown"

        self.header.update_title(f"Optics Dashboard · {title}")

    def change_language(self, lang_code):
        if lang_code == self.current_lang:
            return

        app = QApplication.instance()

        # Remove the current translator
        app.removeTranslator(self.translators[self.current_lang])

        # Install the new translator
        app.installTranslator(self.translators[lang_code])

        self.current_lang = lang_code

        # Retranslate the UI
        # self.ui.retranslateUi(self)
        
def main():
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("Optics Dashboard")
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
