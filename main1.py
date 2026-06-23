# import sys
# import os

# # Add the project root directory to the Python path
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
# if project_root not in sys.path:
#     sys.path.insert(0, project_root)

# from PySide6.QtCore import Qt, QSize, QTimer, QTranslator, QLocale, QEvent, QLibraryInfo, Signal, QCoreApplication
# from PySide6.QtGui import QIcon, QFont, QAction, QColor
# from PySide6.QtWidgets import (
#     QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel,
#     QLineEdit, QPushButton, QFrame, QSizePolicy, QButtonGroup, QSpacerItem,
#     QGraphicsDropShadowEffect, QStackedWidget, QMenu, QGraphicsBlurEffect
# )

# import random
# # from pyautogui import size
# import requests

# # imports
# from modules.patient_module.patient_registratioin_system import PatientForm
# from modules.patient_module.patient_medicalLIst import MedicalReportSystem
# from modules.backup_module.backup_panel import BackupPanel
# from modules.backup_module.BACKUPSYSTEM import BackupRestoreApp
# from modules.inventory_module.inventory_system import InventorySystem
# from modules.inventory_module.inventory_report_viewer import InventoryReportViewer
# from modules.inventory_module.inventory_system_itemform_ui import ItemTypeForm
# from modules.inventory_module.InventoryManager_dashboard import InventoryManager
# from modules.sales_module.sales_puchase_board import PurchaseBoardManager
# from modules.sales_module.payment_history_report import PaymentHistoryDialog
# from modules.sales_module.month_sales_and_exits import MonthlyReportManager
# from modules.main_app.home_card import MainWindow as HomeCardMainWindow
# from ui_ux.main_app.ui_sidebar11 import Ui_MainWindow
# from whatsapp_auto.main import whatsapp_automation_MainWindow

# from app.ui.main_window import ServerIPWindows
# from app.ui.settings_dialog import SettingsDialog

# from resource_path import resource_path
# import runtime_hook_cwd


# from config_loader import BASE_URL


# # theming
# THEME = {
#     "bg": "none",
#     "bg_1": "#1E1E2F",
#     "bg_2": "white",
#     "bg_alt": "qlineargradient(spread:pad, x1:0, y1:0.267, x2:1, y2:0.471, stop:0 rgba(2, 101, 195, 255), stop:1 rgba(44, 47, 132, 255))",
#     "card": "rgb(44, 47, 134)",
#     "border": "#343454",
#     "text": "#E5E7EB",
#     "text_dim": "#C7CBD1",
#     "muted": "#9AA0A6",
#     "primary": "#3B82F6",
#     "success": "#10B981",
#     "warning": "#F59E0B",
#     "danger": "#EF4444",
#     "highlight": "#334155"
# }

# FONT_FAMILY = "Segoe UI, Inter, Roboto, Arial"

# def apply_shadow(widget, radius=18, opacity=0.25, y_offset=6):
#     shadow = QGraphicsDropShadowEffect()
#     shadow.setBlurRadius(radius)
#     col = QColor(0, 0, 0)
#     col.setAlphaF(max(0.0, min(1.0, opacity)))
#     shadow.setColor(col)
#     shadow.setOffset(0, y_offset)
#     widget.setGraphicsEffect(shadow)

# # class SidebarButton(QPushButton):
# #     def __init__(self, text, icon=None, parent=None):
# #         super().__init__(parent)
# #         self.setCheckable(True)
# #         self.setCursor(Qt.PointingHandCursor)
# #         self.setText(f"  {text}")
# #         self.setMinimumHeight(40)
# #         self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
# #         self.setObjectName("SidebarButton")
# #         if icon is not None:
# #             self.setIcon(icon)
# #             self.setIconSize(QSize(24, 24))
# class SidebarButton(QPushButton):
#     def __init__(self, text, icon=None, parent=None):
#         super().__init__(parent)
#         self.setCheckable(True)
#         self.setCursor(Qt.PointingHandCursor)
#         self.setText(f"  {text}")
#         self.setMinimumHeight(60)  # Increase the height of the button
#         self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
#         self.setObjectName("SidebarButton")
#         if icon is not None:
#             self.setIcon(icon)
#             self.setIconSize(QSize(32, 32))  # Increase the icon size
#         self.setStyleSheet(f"""
#             QPushButton#SidebarButton {{
#                 color: {THEME['text']};
#                 background-color: transparent;
#                 border: none;
#                 border-radius: 8px;
#                 padding: 12px 20px;  # Increase padding for larger buttons
#                 text-align: left;
#                 font-size: 20px;  # Increase font size for larger text
#             }}
#             QPushButton#SidebarButton:hover {{
#                 background-color: {THEME['highlight']};
#             }}
#             QPushButton#SidebarButton:checked {{
#                 background-color: {THEME['primary']}22;
#                 border: 1px solid {THEME['primary']}55;
#             }}
#         """)
# class StatCard(QFrame):
#     def __init__(self, title, value, subtitle="", accent=THEME["primary"], icon_char="•", parent=None):
#         super().__init__(parent)
#         self.accent = accent
#         self.icon_char = icon_char
#         self.setObjectName("StatCard")
#         self.setStyleSheet(f"""
#             QFrame#StatCard {{
#                 background-color: {THEME['card']};
#                 border: 1px solid white;
#                 border-radius: 12px;
#             }}
#         """)
#         apply_shadow(self, radius=28, opacity=0.2, y_offset=10)

#         self.value_lbl = QLabel(value)

#         lay = QVBoxLayout(self)
#         lay.setContentsMargins(16, 16, 16, 16)
#         lay.setSpacing(8)

#         # Top row
#         top = QHBoxLayout()
#         top.setSpacing(8)
#         icon = QLabel(self.icon_char)
#         icon.setObjectName("CardIcon")
#         icon.setFixedSize(28, 28)
#         icon.setAlignment(Qt.AlignCenter)
#         icon.setStyleSheet(f"""
#             QLabel#CardIcon {{
#                 color: {THEME['text']};
#                 /*background-color: {self.accent}22;*/
#                 background-color: {THEME['bg_2']};
#                 border: 1px solid {self.accent}55;
#                 border-radius: 6px;
#                 font-size: 16px;
#                 font-weight: 900px;
#             }}
#         """)

#         title_lbl = QLabel(title)
#         # title_lbl.setStyleSheet(f"color: {THEME['text_dim']};")
#         title_lbl.setStyleSheet(f"color: white; font-weight: 500;")
#         title_font = QFont(FONT_FAMILY, 12, QFont.Medium)
#         title_lbl.setFont(title_font)

#         top.addWidget(icon)
#         top.addWidget(title_lbl, 1)
#         top.addStretch(1)

#         # Value
#         value_font = QFont(FONT_FAMILY, 28, QFont.DemiBold)
#         self.value_lbl.setFont(value_font)
#         self.value_lbl.setStyleSheet(f"color: {THEME['text']};")

#         # Subtitle
#         subtitle_lbl = QLabel(subtitle)
#         subtitle_lbl.setStyleSheet(f"color: {THEME['bg_2']}; font-weight: 500;")
#         subtitle_font = QFont(FONT_FAMILY, 12)
#         subtitle_lbl.setFont(subtitle_font)

#         lay.addLayout(top)
#         lay.addSpacing(4)
#         lay.addWidget(self.value_lbl)
#         lay.addWidget(subtitle_lbl)
#         lay.addStretch(1)

#     def update_value(self, value: str):
#         self.value_lbl.setText(value)

# class Header(QFrame):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setObjectName("Header")
#         self.setStyleSheet(f"""
#             QFrame#Header {{
#                 background-color: {THEME['bg_alt']};
#                 border-bottom: 1px solid {THEME['border']};
#             }}
#         """)
#         lay = QHBoxLayout(self)
#         lay.setContentsMargins(16, 10, 16, 10)
#         lay.setSpacing(12)

#         self.title = QLabel("")
#         title_font = QFont(FONT_FAMILY, 18, QFont.DemiBold)
#         self.title.setFont(title_font)
#         self.title.setStyleSheet(f"color: {THEME['text']};")

#         spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
#         self.profile = QPushButton("User")
#         self.profile.setCursor(Qt.PointingHandCursor)
#         self.profile.setObjectName("Profile")
#         self.profile.setMinimumHeight(34)
#         self.profile.setStyleSheet(f"""
#             QPushButton#Profile {{
#                 color: {THEME['text']};
#                 background: {THEME['bg']};
#                 border: 1px solid {THEME['border']};
#                 border-radius: 8px;
#                 padding: 6px 12px;
#             }}
#         """)

#         lay.addWidget(self.title)
#         lay.addSpacing(8)
#         lay.addItem(spacer)
#         lay.addWidget(self.profile)      

#     def update_title(self, title: str):
#         self.title.setText(title)

# # class Sidebar(QFrame):
# #     def __init__(self, parent=None):
# #         super().__init__(parent)
# #         self.expanded = True
# #         self.full_width = 220
# #         self.collapsed_width = 60
# #         self.setFixedWidth(self.full_width)
# #         self.setObjectName("Sidebar")
# #         self.setFixedWidth(220)
# #         self.setStyleSheet(f"""
# #             QFrame#Sidebar {{
# #                 background-color: {THEME['bg_alt']};
# #                 border-right: 1px solid {THEME['border']};
# #             }}
# #             QPushButton#SidebarButton {{
# #                 color: {THEME['text']};
# #                 background-color: transparent;
# #                 border: none;
# #                 border-radius: 8px;
# #                 padding: 8px 10px;
# #                 text-align: left;
# #                 font-size: 18px;
# #                 font-weight: 900px;
# #             }}
# #             QPushButton#SidebarButton:hover {{
# #                 background-color: {THEME['highlight']};
# #             }}
# #             QPushButton#SidebarButton:checked {{
# #                 background-color: {THEME['primary']}22;
# #                 border: 1px solid {THEME['primary']}55;
# #             }}
# #         """)

# #         lay = QVBoxLayout(self)
# #         lay.setContentsMargins(12, 16, 12, 16)
# #         lay.setSpacing(6)

# #         self.brand = QLabel("")  # will be retranslated User
# #         self.brand.setFont(QFont(FONT_FAMILY, 16, QFont.DemiBold))
# #         self.brand.setStyleSheet(f"color: {THEME['text']};")

# #         self.muted = QLabel("")
# #         self.muted.setStyleSheet(f"color: {THEME['muted']}; font-size: 12px;")

# #         lay.addWidget(self.brand)
# #         lay.addWidget(self.muted)
# #         lay.addSpacing(12)

# #         self.group = QButtonGroup(self)
# #         self.group.setExclusive(True)

# #         from PySide6.QtGui import QIcon

# #         # create buttons but keep references so they can be retranslated
# #         # self.btn_home = SidebarButton("")
# #         # self.btn_patients = SidebarButton("")
# #         # self.btn_sales = SidebarButton("")
# #         # self.btn_medical_report = SidebarButton("")
# #         # self.btn_appts = SidebarButton("")
# #         # self.btn_settings = SidebarButton("")
# #         self.btn_home = SidebarButton("Home", QIcon("images/home_icon2.png"))
# #         self.btn_patients = SidebarButton("Patients", QIcon("images/patient_icon1.png"))
# #         self.btn_sales = SidebarButton("Sales", QIcon("images/sales_icon.png"))
# #         self.btn_medical_report = SidebarButton("Medical Rport", QIcon("images/med_rep.png"))
# #         #self.btn_appts = SidebarButton("Appointments", QIcon("images/appointments.png"))
# #         #self.btn_settings = SidebarButton("Settings", QIcon("images/settings.png"))
# #         for i, b in enumerate([
# #             self.btn_home, self.btn_patients, self.btn_sales, self.btn_medical_report,
# #             self.btn_appts, self.btn_settings
# #         ]):
# #             lay.addWidget(b)
# #             self.group.addButton(b, i)

# #         lay.addStretch(1)

# #         # self.cta = QPushButton("")
# #         # self.cta.setCursor(Qt.PointingHandCursor)
# #         # self.cta.setMinimumHeight(40)
# #         # self.cta.setObjectName("CTA")
# #         # self.cta.setStyleSheet(f"""
# #         #     QPushButton#CTA {{
# #         #         color: {THEME['bg']};
# #         #         background-color: {THEME['success']};
# #         #         border: none;
# #         #         border-radius: 8px;
# #         #         font-weight: 600;
# #         #     }}
# #         # """)
# #         # lay.addWidget(self.cta)
# #         # self.btn_home.setChecked(True)
# class Sidebar(QFrame):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.expanded = True  # Track whether the sidebar is expanded or collapsed
#         self.full_width = 250  # Expanded width
#         self.collapsed_width = 80  # Collapsed width
#         self.setFixedWidth(self.full_width)  # Start in expanded mode
#         self.setObjectName("Sidebar")
#         self.setStyleSheet(f"""
#             QFrame#Sidebar {{
#                 background-color: {THEME['bg_alt']};
#                 border-right: 1px solid {THEME['border']};
#             }}
#             QPushButton#SidebarButton {{
#                 color: {THEME['text']};
#                 background-color: transparent;
#                 border: none;
#                 border-radius: 8px;
#                 padding: 8px 10px;
#                 text-align: left;
#                 font-size: 18px;
#                 font-weight: 900px;
#             }}
#             QPushButton#SidebarButton:hover {{
#                 background-color: {THEME['highlight']};
#             }}
#             QPushButton#SidebarButton:checked {{
#                 background-color: {THEME['primary']}22;
#                 border: 1px solid {THEME['primary']}55;
#             }}

#         """)

#         lay = QVBoxLayout(self)
#         lay.setContentsMargins(12, 16, 12, 16)
#         lay.setSpacing(6)

#         # Add the toggle button at the top
#         self.toggle_btn = QPushButton("☰")  # Menu icon
#         self.toggle_btn.setCursor(Qt.PointingHandCursor)
#         self.toggle_btn.setObjectName("SidebarButton")  # Use the same style as other buttons
#         self.toggle_btn.setCheckable(False)  # Not a toggle button in the checked sense
#         self.toggle_btn.setStyleSheet(f"""
#             QPushButton#SidebarButton {{
#                 color: {THEME['text']};
#                 background-color: transparent;
#                 border: none;
#                 border-radius: 8px;
#                 padding: 8px 10px;
#                 text-align: left;
#                 font-size: 30px;
#             }}
#             QPushButton#SidebarButton:hover {{
#                 background-color: {THEME['highlight']};
#             }}
#         """)
#         self.toggle_btn.clicked.connect(self.toggle_sidebar)  # Connect to toggle function
#         lay.addWidget(self.toggle_btn)  # Add toggle button to the top

#         # Sidebar brand (title)
#         self.brand = QLabel("OptiCare")  # Sidebar title
#         self.brand.setFont(QFont(FONT_FAMILY, 16, QFont.DemiBold))
#         self.brand.setStyleSheet(f"color: {THEME['text']};")

#         self.muted = QLabel("v1.0")  # Sidebar subtitle
#         self.muted.setStyleSheet(f"color: {THEME['muted']}; font-size: 12px;")

#         lay.addWidget(self.brand)
#         lay.addWidget(self.muted)
#         lay.addSpacing(12)

#         # Sidebar buttons
#         self.group = QButtonGroup(self)
#         self.group.setExclusive(True)

#         # self.btn_home = SidebarButton("Home", QIcon("images/home_icon2.png"))
#         self.btn_home = SidebarButton("Home", QIcon(resource_path("images/home_icon2.png")))
#         self.btn_home.setMinimumHeight(70)  # Custom height for this button
#         self.btn_home.setIconSize(QSize(40, 40))  # Custom icon size for this button
#         self.btn_home.setStyleSheet("""
#             QPushButton#SidebarButton {
#                 padding: 16px 24px;  # Custom padding for this button
#                 font-size: 22px;  # Custom font size for this button
#             }
#         """)
        
#         self.btn_patients = SidebarButton("Patients", QIcon(resource_path("images/patient_icon1.png")))
#         self.btn_patients.setMinimumHeight(70)  # Custom height for this button
#         self.btn_patients.setIconSize(QSize(40, 40))  # Custom icon size for this button
#         self.btn_patients.setStyleSheet("""
#             QPushButton#SidebarButton {
#                 padding: 16px 24px;  # Custom padding for this button
#                 font-size: 22px;  # Custom font size for this button
#             }
#         """)        
#         self.btn_sales = SidebarButton("Sales", QIcon(resource_path("images/sales_icon.png")))
#         self.btn_sales.setMinimumHeight(70)  # Custom height for this button
#         self.btn_sales.setIconSize(QSize(40, 40))  # Custom icon size for this button  pyinstaller OpticalSystem.spec

#         self.btn_sales.setStyleSheet("""
#             QPushButton#SidebarButton {
#                 padding: 16px 24px;  # Custom padding for this button
#                 font-size: 22px;  # Custom font size for this button
#             }
#         """)        
#         self.btn_medical_report = SidebarButton("Medical Report", QIcon(resource_path("images/med_rep.png")))
#         self.btn_medical_report.setMinimumHeight(70)  # Custom height for this button
#         self.btn_medical_report.setIconSize(QSize(40, 40))  # Custom icon size for this button
#         self.btn_medical_report.setStyleSheet("""
#             QPushButton#SidebarButton {
#                 padding: 16px 24px;  # Custom padding for this button
#                 font-size: 22px;  # Custom font size for this button
#             }
#         """) 
#         for i, b in enumerate([self.btn_home, self.btn_patients, self.btn_sales, self.btn_medical_report]):
#             lay.addWidget(b)
#             self.group.addButton(b, i)

#         lay.addStretch(1)

#     def toggle_sidebar(self):
#         """Toggle the sidebar between expanded and collapsed states."""
#         if self.expanded:
#             # Collapse the sidebar
#             self.setFixedWidth(self.collapsed_width)
#             self.brand.hide()  # Hide the title
#             self.muted.hide()  # Hide the subtitle
#             for button in self.group.buttons():
#                 button.setText("")  # Hide button text
#         else:
#             # Expand the sidebar
#             self.setFixedWidth(self.full_width)
#             self.brand.show()  # Show the title
#             self.muted.show()  # Show the subtitle
#             self.btn_home.setText("  Home")
#             self.btn_patients.setText("  Patients")
#             self.btn_sales.setText("  Sales")
#             self.btn_medical_report.setText("  Medical Report")

#         self.expanded = not self.expanded  

# class DashboardView(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setStyleSheet(f"background-color: {THEME['bg']};")
#         outer = QVBoxLayout(self)
#         outer.setContentsMargins(16, 16, 16, 16)
#         outer.setSpacing(16)

#         row1 = QHBoxLayout()
#         row1.setSpacing(16)

#         # Add desc_label to each StatCard
#         self.card_patients = StatCard("Patients", "0", "Total registered", THEME["primary"], "👤")
#         self.card_patients.desc_label = QLabel("0 patients registered.")
#         self.card_patients.desc_label.setStyleSheet(f"color: {THEME['text']}; font-size: 20px; font-weight: 500;")
#         self.card_patients.layout().addWidget(self.card_patients.desc_label)

#         self.card_sales = StatCard("Sales", "0", "Sales count", THEME["success"], "🛒")
#         self.card_sales.desc_label = QLabel("0 Sales Count.")
#         self.card_sales.desc_label.setStyleSheet(f"color: {THEME['bg_2']}; font-size: 20px; font-weight: 500;")
#         self.card_sales.layout().addWidget(self.card_sales.desc_label)
        
#         #self.card_sales = StatCard("Sales", "0", "Sales count", THEME["success"], "🛒")
#         #self.card_sales.desc_label = QLabel("0 Sales Count.")
#         #self.card_sales.desc_label.setStyleSheet("color: red; font-size: 20px; font-weight: 500;")  # Custom color for desc_label
#         #self.card_sales.value_lbl.setStyleSheet("color: green; font-size: 28px; font-weight: bold;")  # Custom color for value label
#         # If you want to change the subtitle label color, you need to access it in StatCard and set its style there.
#         #self.card_sales.layout().addWidget(self.card_sales.desc_label)                

#         self.medical_rep = StatCard("Medical Report", "0", "Scheduled today", THEME["warning"], "📅")
#         self.medical_rep.desc_label = QLabel("0 Medical Report.")
#         self.medical_rep.desc_label.setStyleSheet(f"color: {THEME['bg_2']}; font-size: 20px; font-weight: 500;")
#         self.medical_rep.layout().addWidget(self.medical_rep.desc_label)

#         self.card_Inven_item = StatCard("Item Inventory", "0", "Scheduled today", THEME["warning"], "📅")
#         self.card_Inven_item.desc_label = QLabel("0 Item Inventory.")
#         self.card_Inven_item.desc_label.setStyleSheet(f"color: {THEME['bg_2']}; font-size: 20px; font-weight: 500;")
#         self.card_Inven_item.layout().addWidget(self.card_Inven_item.desc_label)


#         self.card_appts = StatCard("Appointments", "0", "Scheduled today", THEME["warning"], "📅")
#         self.card_appts.desc_label = QLabel("0 appointments.")
#         self.card_appts.desc_label.setStyleSheet(f"color: {THEME['bg_2']}; font-size: 20px; font-weight: 500;")
#         self.card_appts.layout().addWidget(self.card_appts.desc_label)

#         self.card_new = StatCard("New Patient", "Loading…", "Preparing form", THEME["primary"], "➕")

#         # for c in [self.card_patients, self.card_sales, self.card_appts, self.medical_rep, self.card_Inven_item, self.card_new]:
#         #     c.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
#         #     row1.addWidget(c)

#         # Arrange cards in rows of 3
#         cards = [
#             self.card_patients,
#             self.card_sales,
#             self.card_appts,
#             self.medical_rep,
#             self.card_Inven_item,
#             self.card_new
#         ]

#         for i in range(0, len(cards), 3):
#             row = QHBoxLayout()
#             row.setSpacing(16)
#             for card in cards[i:i+3]:
#                 card.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
#                 row.addWidget(card)
#             outer.addLayout(row)


#         outer.addLayout(row1)
#         outer.addStretch(1)

#         # Store cards in a list for easy access
#         self.cards = [self.card_patients, self.card_sales, self.card_appts]

#         # Timer to simulate real-time updates and fetch backend data
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_cards_from_backend)
#         self.timer.start(3000)  # every 3 seconds


#     def update_cards_from_backend(self):
#         try:
#             response = requests.get(f"{BASE_URL}/dashboard-counts/")
#             if response.status_code == 200:
#                 data = response.json()

#                 patient_count = data.get('patient_count', 0)
#                 sales_count = data.get('sales_count', 0)
#                 medical_report_count = data.get('medical_report_count', 0)
#                 inventory_county_count = data.get('inventory_count', 0)
#                 appointment_count = data.get('appointment_count', 0)

#                 # ✅ Update main values AND descriptions
#                 self.card_patients.update_value(str(patient_count))
#                 self.card_patients.desc_label.setText(f"{patient_count} patients registered.")

#                 self.card_sales.update_value(str(sales_count))
#                 self.card_sales.desc_label.setText(f"{sales_count} Sales Count.")
                
#                 self.medical_rep.update_value(str(medical_report_count))
#                 self.medical_rep.desc_label.setText(f"{medical_report_count} Medical report Count.")
                
#                 self.card_Inven_item.update_value(str(inventory_county_count))
#                 self.card_Inven_item.desc_label.setText(f"{inventory_county_count} Inventory Count.")
                

#                 self.card_appts.update_value(str(appointment_count))
#                 self.card_appts.desc_label.setText(f"{appointment_count} appointments.")

#             else:
#                 print("Failed to fetch dashboard data:", response.text)
#         except Exception as e:
#             print("Error fetching dashboard data:", e)


# class PlaceholderView(QWidget):
#     def __init__(self, name):
#         super().__init__()
#         self.setStyleSheet(f"background-color: {THEME['bg']};")
#         layout = QVBoxLayout(self)
#         label = QLabel(f"{name} View Coming Soon")
#         label.setFont(QFont(FONT_FAMILY, 16))
#         label.setStyleSheet(f"color: {THEME['text']};")
#         layout.addWidget(label, alignment=Qt.AlignCenter)

# class MainWindow(QMainWindow):
#     language_changed = Signal(str)
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Optics Dashboard")
#         self.resize(1200, 760)
#         central = QWidget()
#         self.setCentralWidget(central)

#         # translators
#         self.translators = {
#             'en': QTranslator(),
#             'fr': QTranslator()
#         }

#         # load .qm files (ensure the path is correct) 
#         # self.translators['en'].load("i18n/en.qm")
#         # self.translators['fr'].load("i18n/TS_fr.qm")
#         # self.translators['fr'].load("translation/patient_registration.qm")
#         # self.translators['fr'].load("translation/patient_medicalList_ok.qm")
#         # self.translators['fr'].load("translation/add_item_type_form.qm")
#         # inside MainWindow.__init__()
#         self.translators = {'en': [], 'fr': []}

#         # English (usually no translation needed, but for completeness)
#         en_trans = QTranslator()
#         en_trans.load(resource_path("i18n/en.qm"))
#         self.translators['en'].append(en_trans)

#         # French translations – one translator per .qm file
#         fr_base = QTranslator()
#         fr_base.load(resource_path("i18n/TS_fr.qm"))
#         self.translators['fr'].append(fr_base)

#         fr_patient = QTranslator()
#         fr_patient.load(resource_path("translation/patient_registration.qm"))
#         self.translators['fr'].append(fr_patient)

#         fr_medical = QTranslator()
#         fr_medical.load(resource_path("translation/patient_medicalList_ok.qm"))
#         self.translators['fr'].append(fr_medical)

#         fr_inventory = QTranslator()
#         fr_inventory.load(resource_path("translation/add_item_type_form.qm"))
#         self.translators['fr'].append(fr_inventory)

#         fr_item_inventory = QTranslator()
#         fr_item_inventory.load(resource_path("translation/item_inventory_ok.qm"))
#         self.translators['fr'].append(fr_item_inventory)
       
#         fr_monthly_sales= QTranslator()
#         fr_monthly_sales.load(resource_path("translation/monthly_entries1_ok.qm"))
#         self.translators['fr'].append(fr_monthly_sales) 
        
#         fr_sales_board= QTranslator()
#         fr_sales_board.load(resource_path("translation/puchase_board1_ok.qm"))
#         self.translators['fr'].append(fr_sales_board)           
        
#         fr_paiment_system= QTranslator()
#         fr_paiment_system.load(resource_path("translation/payment_history_report.qm"))
#         self.translators['fr'].append(fr_paiment_system)    
       
#         fr_backup_system= QTranslator()
#         fr_backup_system.load(resource_path("translation/backupsystemfr.qm"))
#         self.translators['fr'].append(fr_backup_system)
        
#         fr_whatsapp_aut= QTranslator()
#         fr_whatsapp_aut.load(resource_path("translation/whatsapp_aut.qm"))
#         self.translators['fr'].append(fr_whatsapp_aut)                 
       
#         # default 
#         self.current_lang = 'en'

#         self.setStyleSheet("""
#             QMainWindow {
#                 background-color: qlineargradient(spread:pad, x1:0, y1:0.267, x2:1, y2:0.471, stop:0 rgba(2, 101, 195, 255), stop:1 rgba(44, 47, 132, 255));
#             }
#         """)
#         root = QVBoxLayout(central)
#         root.setContentsMargins(0, 0, 0, 0)
#         root.setSpacing(0)

#         self.header = Header()
#         root.addWidget(self.header)

#         body = QHBoxLayout()
#         body.setContentsMargins(0, 0, 0, 0)
#         body.setSpacing(0)

#         self.sidebar = Sidebar()
#         body.addWidget(self.sidebar)

#         self.stack = QStackedWidget()
#         self.views = {
#             0: DashboardView(), 
#             1: PatientForm(),
#             2: PurchaseBoardManager(),
#             3: MedicalReportSystem(),
#             4: PlaceholderView("Appointments"),
#             5: InventoryReportViewer(),
#             6: PaymentHistoryDialog(),
#             7: InventorySystem(),
#             8: InventoryManager(),
#             9: ItemTypeForm(),
#             10: InventoryManager(),
#             11: BackupPanel(),
#             12: BackupRestoreApp(),
#             13: whatsapp_automation_MainWindow(),
#         }
#         for view in self.views.values():
#             self.stack.addWidget(view)
            
#         # Connect all module retranslate slots to main language signal
#         for view in self.views.values():
#             if hasattr(view, "retranslate_ui"):
#                 self.language_changed.connect(view.retranslate_ui)
            

#         body.addWidget(self.stack, 1)
#         root.addLayout(body)

#         # toolbar & actions (create before retranslate so attributes exist)
#         self._create_toolbar()

#         # connect navigation
#         self.sidebar.group.idClicked.connect(self.on_nav_clicked)

#         # initial retranslation (sets all labels from tr)
#         self._retranslate_ui()

#     def _create_toolbar(self):
#         toolbar = self.addToolBar("Main Toolbar")
#         toolbar.setMovable(False)
#         toolbar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
#         toolbar.setStyleSheet(f"""
#             QToolBar {{
#                 background: {THEME['bg_alt']};
#                 border-bottom: 1px solid {THEME['border']};
#                 spacing: 6px;
#                 padding: 6px;
#             }}
#         """)

#         # actions we keep references to
#         self.act_refresh = QAction("", self)
#         self.act_refresh.setToolTip("")  # will set via retranslate

#         self.act_quit = QAction("", self)
#         self.act_quit.triggered.connect(QApplication.instance().quit)

#         # tools menu
#         self.tool_menu = QMenu(self)
#         self.tool_menu.setStyleSheet(f"""
#             QMenu {{
#                 background-color: {THEME['bg_1']};
#                 color: {THEME['text']};
#                 border: 1px solid {THEME['border']};
#                 spacing: 6px;
#                 padding: 6px;
#             }}
#             QMenu::item:selected {{
#                 background-color: {THEME['highlight']};
#             }}
#         """)

#         # populate with actions referencing switch_view
#         self.tool_menu.addAction(QAction(QIcon(resource_path("images/report_file_64px.png")), "Inventory Report", self, triggered=lambda: self.switch_view(5)))
#         self.tool_menu.addAction(QAction(QIcon(resource_path("images/add_property_40px.png")), "Add Categorie/Items", self, triggered=lambda: self.switch_view(9)))
#         self.tool_menu.addAction(QAction(QIcon(resource_path("images/add_property_40px.png")), "Inventory Managment", self, triggered=lambda: self.switch_view(10)))
#         self.tool_menu.addSeparator()
#         self.tool_menu.addAction(QAction(QIcon(resource_path("images/payment_history_50px.png")), "Payment History", self, triggered=lambda: self.switch_view(6)))
#         self.tool_menu.addSeparator()
#         self.tool_menu.addAction(QAction(QIcon(resource_path("images/phone_message_48px.png")), "Message Automation", self, triggered=lambda: self.switch_view(13)))

#         # tool button
#         self.tool_btn = QPushButton("")
#         self.tool_btn.setCursor(Qt.PointingHandCursor)
#         self.tool_btn.setMenu(self.tool_menu)
#         self.tool_btn.setStyleSheet(f"""
#             QPushButton {{
#                 background: transparent;
#                 color: {THEME['text']};
#                 border: none;
#                 padding: 4px 12px;
#             }}
#             QPushButton:hover {{
#                 background-color: {THEME['highlight']};
#             }}
#         """)

#         # file menu
#         self.file_menu = QMenu(self)
#         self.file_menu.setStyleSheet(self.tool_menu.styleSheet())
#         self.file_menu.addAction(QAction(QIcon(resource_path("images/opened_folder_48px.png")), "Open Session", self, triggered=lambda: self.switch_view(11)))
#         self.file_menu.addAction(QAction(QIcon(resource_path("images/database_100px.png")), "Import/Export Data", self, triggered=lambda: self.switch_view(12)))
#         self.file_menu.addSeparator()
#         self.file_menu.addAction(QAction(QIcon(resource_path("images/database_100px.png")), "Server IP", self, triggered=lambda: self.open_settings()))        
#         self.file_btn = QPushButton("")
#         self.file_btn.setCursor(Qt.PointingHandCursor)
#         self.file_btn.setMenu(self.file_menu)
#         self.file_btn.setStyleSheet(self.tool_btn.styleSheet())

#         # language menu
#         self.language_menu = QMenu(self)
#         self.language_menu.setStyleSheet(self.tool_menu.styleSheet())
#         # language actions - store them so retranslate can update text if needed
#         self.act_lang_fr = QAction("fr", self, triggered=lambda: self.change_language('fr'))
#         self.act_lang_en = QAction("en", self, triggered=lambda: self.change_language('en'))
#         self.language_menu.addAction(self.act_lang_fr)
#         self.language_menu.addAction(self.act_lang_en)
#         self.language_btn = QPushButton("")
#         self.language_btn.setCursor(Qt.PointingHandCursor)
#         self.language_btn.setMenu(self.language_menu)
#         self.language_btn.setStyleSheet(self.tool_btn.styleSheet())

#         # add widgets to toolbar
#         toolbar.addWidget(self.file_btn)
#         toolbar.addSeparator()
#         toolbar.addAction(self.act_refresh)
#         toolbar.addWidget(self.tool_btn)
#         toolbar.addWidget(self.language_btn)
#         toolbar.addSeparator()
#         toolbar.addAction(self.act_quit)

#     def on_nav_clicked(self, idx):
#         titles = ["Home", "Patients", "Sales", "Appointments", "Settings", "Inventory"]
#         self.stack.setCurrentIndex(idx)
#         self.header.update_title(f"Optics Dashboard · {titles[idx]}")

#     def switch_view(self, index):
#         titles = [
#             "Home", "Patients", "Sales", "Appointments", "Settings", "Inventory",
#             "Payment History", "Add Categorie/Items", "Entery/Sales Report",
#             "Payment History", "Open session", "Import/Export Data", "Message Automation"
#         ]

#         if index < 0 or index >= self.stack.count():
#             return

#         self.stack.setCurrentIndex(index)
#         button = self.sidebar.group.button(index)
#         if button:
#             button.setChecked(True)

#         if 0 <= index < len(titles):
#             title = titles[index]
#         else:
#             widget = self.stack.widget(index)
#             title = widget.__class__.__name__ if widget is not None else "Unknown"

#         self.header.update_title(f"Optics Dashboard · {title}")

#     # def change_language(self, lang_code):
#     #     if lang_code == self.current_lang:
#     #         return

#     #     app = QApplication.instance()
#     #     # remove current translator
#     #     if self.current_lang in self.translators:
#     #         app.removeTranslator(self.translators[self.current_lang])

#     #     # install new translator
#     #     if lang_code in self.translators:
#     #         app.installTranslator(self.translators[lang_code])
#     #         self.current_lang = lang_code

#     #     # retranslate UI components
#     #     self._retranslate_ui()

#     #     # emit signal for other modules
#     #     self.language_changed.emit(lang_code)
    
    
#     def change_language(self, lang_code):
#         app = QApplication.instance()

#         # remove all translators for the old language
#         for tr in self.translators.get(self.current_lang, []):
#             app.removeTranslator(tr)

#         # install all translators for the new language
#         for tr in self.translators.get(lang_code, []):
#             app.installTranslator(tr)

#         self.current_lang = lang_code

#         # retranslate all active UIs
#         self._retranslate_ui()
#         self.language_changed.emit(lang_code)

#     def _retranslate_ui(self):
#         """Update all visible texts using tr(...) so translations from installed QTranslator apply."""
#         tr = self.tr

#         # Header
#         self.header.update_title(tr("Optics Dashboard"))

#         # Sidebar
#         self.sidebar.brand.setText(tr("OptiCare"))
#         self.sidebar.muted.setText(tr("v1.0"))
#         self.sidebar.btn_home.setText("  " + tr("Home"))
#         self.sidebar.btn_patients.setText("  " + tr("Patients"))
#         self.sidebar.btn_sales.setText("  " + tr("Sales"))
#         self.sidebar.btn_medical_report.setText("  " + tr("Medical Report"))
#         # self.sidebar.btn_appts.setText("  " + tr("Appointments"))
#         # self.sidebar.btn_settings.setText("  " + tr("Settings"))
#         # self.sidebar.cta.setText(tr("➕ New patient"))

#         # Toolbar and actions
#         self.act_refresh.setText(tr("🔄 Refresh"))
#         self.act_refresh.setToolTip(tr("Refresh dashboard data"))
#         self.act_quit.setText(tr("❌ Quit"))
#         self.act_quit.setToolTip(tr("Exit the application"))

#         self.tool_btn.setText(tr("⚙️ Tools"))
#         self.file_btn.setText(tr("⚙️ files"))
#         self.language_btn.setText(tr("⚙️ languages"))

#         # language menu actions (if you want them to show localized names)
#         self.act_lang_fr.setText(tr("French"))
#         self.act_lang_en.setText(tr("English"))
#         self.file_menu.actions()[0].setText(tr("Open Session"))
#         self.file_menu.actions()[1].setText(tr("Import/Export Data"))
        
#         self.tool_menu.actions()[0].setText(tr("Inventory Report"))
#         self.tool_menu.actions()[1].setText(tr("Add Categorie/Items"))
#         self.tool_menu.actions()[3].setText(tr("Payment History"))
#         self.tool_menu.actions()[5].setText(tr("Message Automation"))
#         self.tool_menu.actions()[2].setText(tr("inventory Managment"))
#         self.tool_menu.actions()[4].setText(tr("Payment History"))
#         self.tool_menu.actions()[6].setText(tr("Message Automation"))
        



#     def _create_actions(self):
#         # kept for compatibility if you used this method earlier
#         pass
 
#     def open_settings(self):
#         """Open the Monthly Entries/Sales window."""
#         self.server_window = SettingsDialog()
#         self.server_window.show()        
        

# def main():
#     app = QApplication(sys.argv)
#     app.setApplicationDisplayName("Optics Dashboard")
#     win = MainWindow()
#     win.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     main()
import sys
import os

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from PySide6.QtCore import Qt, QSize, QTimer, QTranslator, QLocale, QEvent, QLibraryInfo, Signal, QCoreApplication
from PySide6.QtGui import QIcon, QFont, QAction, QColor
from PySide6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QFrame, QSizePolicy, QButtonGroup, QSpacerItem,
    QGraphicsDropShadowEffect, QStackedWidget, QMenu, QGraphicsBlurEffect
)

import random
import requests

# imports
from modules.patient_module.patient_registratioin_system import PatientForm
from modules.patient_module.patient_medicalLIst import MedicalReportSystem
from modules.backup_module.backup_panel import BackupPanel
from modules.backup_module.BACKUPSYSTEM import BackupRestoreApp
from modules.inventory_module.inventory_system import InventorySystem
from modules.inventory_module.inventory_report_viewer import InventoryReportViewer
from modules.inventory_module.inventory_system_itemform_ui import ItemTypeForm
from modules.inventory_module.InventoryManager_dashboard import InventoryManager
from modules.sales_module.sales_puchase_board import PurchaseBoardManager
from modules.sales_module.payment_history_report import PaymentHistoryDialog
from modules.sales_module.month_sales_and_exits import MonthlyReportManager
from modules.main_app.home_card import MainWindow as HomeCardMainWindow
from ui_ux.main_app.ui_sidebar11 import Ui_MainWindow
from whatsapp_auto.main import whatsapp_automation_MainWindow

from app.ui.main_window import ServerIPWindows
from app.ui.settings_dialog import SettingsDialog

from resource_path import resource_path
from config_loader import BASE_URL

# theming
THEME = {
    "bg": "none",
    "bg_1": "#1E1E2F",
    "bg_2": "white",
    "bg_alt": "qlineargradient(spread:pad, x1:0, y1:0.267, x2:1, y2:0.471, stop:0 rgba(2, 101, 195, 255), stop:1 rgba(44, 47, 132, 255))",
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

class SidebarButton(QPushButton):
    def __init__(self, text, icon=None, parent=None):
        super().__init__(parent)
        self.setCheckable(True)
        self.setCursor(Qt.PointingHandCursor)
        self.setText(f"  {text}")
        self.setMinimumHeight(60)  # Increase the height of the button
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setObjectName("SidebarButton")
        if icon is not None:
            self.setIcon(icon)
            self.setIconSize(QSize(32, 32))  # Increase the icon size
        self.setStyleSheet(f"""
            QPushButton#SidebarButton {{
                color: {THEME['text']};
                background-color: transparent;
                border: none;
                border-radius: 8px;
                padding: 12px 20px;
                text-align: left;
                font-size: 20px;
            }}
            QPushButton#SidebarButton:hover {{
                background-color: {THEME['highlight']};
            }}
            QPushButton#SidebarButton:checked {{
                background-color: {THEME['primary']}22;
                border: 1px solid {THEME['primary']}55;
            }}
        """)
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

        self.title = QLabel("")
        title_font = QFont(FONT_FAMILY, 18, QFont.DemiBold)
        self.title.setFont(title_font)
        self.title.setStyleSheet(f"color: {THEME['text']};")

        spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.profile = QPushButton("User")
        self.profile.setCursor(Qt.PointingHandCursor)
        self.profile.setObjectName("Profile")
        self.profile.setMinimumHeight(34)
        self.profile.setStyleSheet(f"""
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
        lay.addItem(spacer)
        lay.addWidget(self.profile)      

    def update_title(self, title: str):
        self.title.setText(title)

class Sidebar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.expanded = True  # Track whether the sidebar is expanded or collapsed
        self.full_width = 250  # Expanded width
        self.collapsed_width = 80  # Collapsed width
        self.setFixedWidth(self.full_width)  # Start in expanded mode
        self.setObjectName("Sidebar")
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

        # Add the toggle button at the top
        self.toggle_btn = QPushButton("☰")  # Menu icon
        self.toggle_btn.setCursor(Qt.PointingHandCursor)
        self.toggle_btn.setObjectName("SidebarButton")  # Use the same style as other buttons
        self.toggle_btn.setCheckable(False)  # Not a toggle button in the checked sense
        self.toggle_btn.setStyleSheet(f"""
            QPushButton#SidebarButton {{
                color: {THEME['text']};
                background-color: transparent;
                border: none;
                border-radius: 8px;
                padding: 8px 10px;
                text-align: left;
                font-size: 30px;
            }}
            QPushButton#SidebarButton:hover {{
                background-color: {THEME['highlight']};
            }}
        """)
        self.toggle_btn.clicked.connect(self.toggle_sidebar)  # Connect to toggle function
        lay.addWidget(self.toggle_btn)  # Add toggle button to the top

        # Sidebar brand (title)
        self.brand = QLabel("OptiCare")  # Sidebar title
        self.brand.setFont(QFont(FONT_FAMILY, 16, QFont.DemiBold))
        self.brand.setStyleSheet(f"color: {THEME['text']};")

        self.muted = QLabel("v1.0")  # Sidebar subtitle
        self.muted.setStyleSheet(f"color: {THEME['muted']}; font-size: 12px;")

        lay.addWidget(self.brand)
        lay.addWidget(self.muted)
        lay.addSpacing(12)

        # Sidebar buttons
        self.group = QButtonGroup(self)
        self.group.setExclusive(True)

        # self.btn_home = SidebarButton("Home", QIcon("images/home_icon2.png"))
        self.btn_home = SidebarButton("Home", QIcon(resource_path("images/home_icon2.png")))
        self.btn_home.setMinimumHeight(70)  # Custom height for this button
        self.btn_home.setIconSize(QSize(40, 40))  # Custom icon size for this button
        self.btn_home.setStyleSheet("""
            QPushButton#SidebarButton {
                padding: 16px 24px;  # Custom padding for this button
                font-size: 22px;  # Custom font size for this button
            }
        """)
        
        self.btn_patients = SidebarButton("Patients", QIcon(resource_path("images/patient_icon1.png")))
        self.btn_patients.setMinimumHeight(70)  # Custom height for this button
        self.btn_patients.setIconSize(QSize(40, 40))  # Custom icon size for this button
        self.btn_patients.setStyleSheet("""
            QPushButton#SidebarButton {
                padding: 16px 24px;  # Custom padding for this button
                font-size: 22px;  # Custom font size for this button
            }
        """)        
        self.btn_sales = SidebarButton("Sales", QIcon(resource_path("images/sales_icon.png")))
        self.btn_sales.setMinimumHeight(70)  # Custom height for this button
        self.btn_sales.setIconSize(QSize(40, 40))  # Custom icon size for this button  pyinstaller OpticalSystem.spec

        self.btn_sales.setStyleSheet("""
            QPushButton#SidebarButton {
                padding: 16px 24px;  # Custom padding for this button
                font-size: 22px;  # Custom font size for this button
            }
        """)        
        self.btn_medical_report = SidebarButton("Medical Report", QIcon(resource_path("images/med_rep.png")))
        self.btn_medical_report.setMinimumHeight(70)  # Custom height for this button
        self.btn_medical_report.setIconSize(QSize(40, 40))  # Custom icon size for this button
        self.btn_medical_report.setStyleSheet("""
            QPushButton#SidebarButton {
                padding: 16px 24px;  # Custom padding for this button
                font-size: 22px;  # Custom font size for this button
            }
        """) 
        for i, b in enumerate([self.btn_home, self.btn_patients, self.btn_sales, self.btn_medical_report]):
            lay.addWidget(b)
            self.group.addButton(b, i)

        lay.addStretch(1)

    def toggle_sidebar(self):
        """Toggle the sidebar between expanded and collapsed states."""
        if self.expanded:
            # Collapse the sidebar
            self.setFixedWidth(self.collapsed_width)
            self.brand.hide()  # Hide the title
            self.muted.hide()  # Hide the subtitle
            for button in self.group.buttons():
                button.setText("")  # Hide button text
        else:
            # Expand the sidebar
            self.setFixedWidth(self.full_width)
            self.brand.show()  # Show the title
            self.muted.show()  # Show the subtitle
            self.btn_home.setText("  Home")
            self.btn_patients.setText("  Patients")
            self.btn_sales.setText("  Sales")
            self.btn_medical_report.setText("  Medical Report")

        self.expanded = not self.expanded  


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


        outer.addStretch(1)

        # Store cards in a list for easy access
        self.cards = [self.card_patients, self.card_sales, self.card_appts]

        # Timer to simulate real-time updates and fetch backend data
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_cards_from_backend)
        self.timer.start(3000)  # every 3 seconds


    def update_cards_from_backend(self):
        try:
            response = requests.get(f"{BASE_URL}/dashboard-counts/")
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

        # translators — one list per language, supports multiple .qm files
        self.translators = {'en': [], 'fr': []}

        # English (usually no translation needed, but for completeness)
        en_trans = QTranslator()
        en_trans.load(resource_path("i18n/en.qm"))
        self.translators['en'].append(en_trans)

        # French translations – one translator per .qm file
        fr_base = QTranslator()
        fr_base.load(resource_path("i18n/TS_fr.qm"))
        self.translators['fr'].append(fr_base)

        fr_patient = QTranslator()
        fr_patient.load(resource_path("translation/patient_registration.qm"))
        self.translators['fr'].append(fr_patient)

        fr_medical = QTranslator()
        fr_medical.load(resource_path("translation/patient_medicalList_ok.qm"))
        self.translators['fr'].append(fr_medical)

        fr_inventory = QTranslator()
        fr_inventory.load(resource_path("translation/add_item_type_form.qm"))
        self.translators['fr'].append(fr_inventory)

        fr_item_inventory = QTranslator()
        fr_item_inventory.load(resource_path("translation/item_inventory_ok.qm"))
        self.translators['fr'].append(fr_item_inventory)
       
        fr_monthly_sales= QTranslator()
        fr_monthly_sales.load(resource_path("translation/monthly_entries1_ok.qm"))
        self.translators['fr'].append(fr_monthly_sales) 
        
        fr_sales_board= QTranslator()
        fr_sales_board.load(resource_path("translation/puchase_board1_ok.qm"))
        self.translators['fr'].append(fr_sales_board)           
        
        fr_paiment_system= QTranslator()
        fr_paiment_system.load(resource_path("translation/payment_history_report.qm"))
        self.translators['fr'].append(fr_paiment_system)    
       
        fr_backup_system= QTranslator()
        fr_backup_system.load(resource_path("translation/backupsystemfr.qm"))
        self.translators['fr'].append(fr_backup_system)
        
        fr_whatsapp_aut= QTranslator()
        fr_whatsapp_aut.load(resource_path("translation/whatsapp_aut.qm"))
        self.translators['fr'].append(fr_whatsapp_aut)                 
       
        # default 
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

        self.sidebar = Sidebar()
        body.addWidget(self.sidebar)

        self.stack = QStackedWidget()
        self.views = {
            0: DashboardView(), 
            1: PatientForm(),
            2: PurchaseBoardManager(),
            3: MedicalReportSystem(),
            4: PlaceholderView("Appointments"),
            5: InventoryReportViewer(),
            6: PaymentHistoryDialog(),
            7: InventorySystem(),
            8: InventoryManager(),
            9: ItemTypeForm(),
            10: InventoryManager(),
            11: BackupPanel(),
            12: BackupRestoreApp(),
            13: whatsapp_automation_MainWindow(),
        }
        for view in self.views.values():
            self.stack.addWidget(view)
            
        # Connect all module retranslate slots to main language signal
        for view in self.views.values():
            if hasattr(view, "retranslate_ui"):
                self.language_changed.connect(view.retranslate_ui)
            

        body.addWidget(self.stack, 1)
        root.addLayout(body)

        # toolbar & actions (create before retranslate so attributes exist)
        self._create_toolbar()

        # connect navigation
        self.sidebar.group.idClicked.connect(self.on_nav_clicked)

        # initial retranslation (sets all labels from tr)
        self._retranslate_ui()

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

        # actions we keep references to
        self.act_refresh = QAction("", self)
        self.act_refresh.setToolTip("")  # will set via retranslate

        self.act_quit = QAction("", self)
        self.act_quit.triggered.connect(QApplication.instance().quit)

        # tools menu
        self.tool_menu = QMenu(self)
        self.tool_menu.setStyleSheet(f"""
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

        # populate with actions referencing switch_view
        self.tool_menu.addAction(QAction(QIcon(resource_path("images/report_file_64px.png")), "Inventory Report", self, triggered=lambda: self.switch_view(5)))
        self.tool_menu.addAction(QAction(QIcon(resource_path("images/add_property_40px.png")), "Add Categorie/Items", self, triggered=lambda: self.switch_view(9)))
        self.tool_menu.addAction(QAction(QIcon(resource_path("images/add_property_40px.png")), "Inventory Managment", self, triggered=lambda: self.switch_view(10)))
        self.tool_menu.addSeparator()
        self.tool_menu.addAction(QAction(QIcon(resource_path("images/payment_history_50px.png")), "Payment History", self, triggered=lambda: self.switch_view(6)))
        self.tool_menu.addSeparator()
        self.tool_menu.addAction(QAction(QIcon(resource_path("images/phone_message_48px.png")), "Message Automation", self, triggered=lambda: self.switch_view(13)))

        # tool button
        self.tool_btn = QPushButton("")
        self.tool_btn.setCursor(Qt.PointingHandCursor)
        self.tool_btn.setMenu(self.tool_menu)
        self.tool_btn.setStyleSheet(f"""
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

        # file menu
        self.file_menu = QMenu(self)
        self.file_menu.setStyleSheet(self.tool_menu.styleSheet())
        self.file_menu.addAction(QAction(QIcon(resource_path("images/opened_folder_48px.png")), "Open Session", self, triggered=lambda: self.open_monthly_backup()))
        self.file_menu.addAction(QAction(QIcon(resource_path("images/database_100px.png")), "Import/Export Data", self, triggered=lambda: self.open_monthly_backup()))
        self.file_menu.addSeparator()
        self.file_menu.addAction(QAction(QIcon(resource_path("images/database_100px.png")), "Server IP", self, triggered=lambda: self.open_settings()))        
        self.file_btn = QPushButton("")
        self.file_btn.setCursor(Qt.PointingHandCursor)
        self.file_btn.setMenu(self.file_menu)
        self.file_btn.setStyleSheet(self.tool_btn.styleSheet())

        # language menu
        self.language_menu = QMenu(self)
        self.language_menu.setStyleSheet(self.tool_menu.styleSheet())
        # language actions - store them so retranslate can update text if needed
        self.act_lang_fr = QAction("fr", self, triggered=lambda: self.change_language('fr'))
        self.act_lang_en = QAction("en", self, triggered=lambda: self.change_language('en'))
        self.language_menu.addAction(self.act_lang_fr)
        self.language_menu.addAction(self.act_lang_en)
        self.language_btn = QPushButton("")
        self.language_btn.setCursor(Qt.PointingHandCursor)
        self.language_btn.setMenu(self.language_menu)
        self.language_btn.setStyleSheet(self.tool_btn.styleSheet())

        # add widgets to toolbar
        toolbar.addWidget(self.file_btn)
        toolbar.addSeparator()
        toolbar.addAction(self.act_refresh)
        toolbar.addWidget(self.tool_btn)
        toolbar.addWidget(self.language_btn)
        toolbar.addSeparator()
        toolbar.addAction(self.act_quit)

    def on_nav_clicked(self, idx):
        titles = ["Home", "Patients", "Sales", "Appointments", "Settings", "Inventory"]
        self.stack.setCurrentIndex(idx)
        self.header.update_title(f"Optics Dashboard · {titles[idx]}")

    def switch_view(self, index):
        titles = [
            "Home", "Patients", "Sales", "Appointments", "Settings", "Inventory",
            "Payment History", "Add Categorie/Items", "Entery/Sales Report",
            "Payment History", "Open session", "Import/Export Data", "Message Automation"
        ]

        if index < 0 or index >= self.stack.count():
            return

        self.stack.setCurrentIndex(index)
        button = self.sidebar.group.button(index)
        if button:
            button.setChecked(True)

        if 0 <= index < len(titles):
            title = titles[index]
        else:
            widget = self.stack.widget(index)
            title = widget.__class__.__name__ if widget is not None else "Unknown"

        self.header.update_title(f"Optics Dashboard · {title}")
    
    def change_language(self, lang_code):
        app = QApplication.instance()

        # remove all translators for the old language
        for tr in self.translators.get(self.current_lang, []):
            app.removeTranslator(tr)

        # install all translators for the new language
        for tr in self.translators.get(lang_code, []):
            app.installTranslator(tr)

        self.current_lang = lang_code

        # retranslate all active UIs
        self._retranslate_ui()
        self.language_changed.emit(lang_code)

    def _retranslate_ui(self):
        """Update all visible texts using tr(...) so translations from installed QTranslator apply."""
        tr = self.tr

        # Header
        self.header.update_title(tr("Optics Dashboard"))

        # Sidebar
        self.sidebar.brand.setText(tr("OptiCare"))
        self.sidebar.muted.setText(tr("v1.0"))
        self.sidebar.btn_home.setText("  " + tr("Home"))
        self.sidebar.btn_patients.setText("  " + tr("Patients"))
        self.sidebar.btn_sales.setText("  " + tr("Sales"))
        self.sidebar.btn_medical_report.setText("  " + tr("Medical Report"))

        # Toolbar and actions
        self.act_refresh.setText(tr("🔄 Refresh"))
        self.act_refresh.setToolTip(tr("Refresh dashboard data"))
        self.act_quit.setText(tr("❌ Quit"))
        self.act_quit.setToolTip(tr("Exit the application"))

        self.tool_btn.setText(tr("⚙️ Tools"))
        self.file_btn.setText(tr("⚙️ files"))
        self.language_btn.setText(tr("⚙️ languages"))

        # language menu actions (if you want them to show localized names)
        self.act_lang_fr.setText(tr("French"))
        self.act_lang_en.setText(tr("English"))
        self.file_menu.actions()[0].setText(tr("Open Session"))
        self.file_menu.actions()[1].setText(tr("Import/Export Data"))
        
        self.tool_menu.actions()[0].setText(tr("Inventory Report"))
        self.tool_menu.actions()[1].setText(tr("Add Categorie/Items"))
        self.tool_menu.actions()[3].setText(tr("Payment History"))
        self.tool_menu.actions()[5].setText(tr("Message Automation"))
        self.tool_menu.actions()[2].setText(tr("inventory Managment"))
        self.tool_menu.actions()[4].setText(tr("Payment History"))
        self.tool_menu.actions()[6].setText(tr("Message Automation"))

    def _create_actions(self):
        # kept for compatibility if you used this method earlier
        pass
 
    def open_settings(self):
        """Open the settings window."""
        self.server_window = SettingsDialog()
        self.server_window.show()    
        
    def open_monthly_backup(self):
        """Open the Monthly backup."""
        self.server_window = BackupPanel()
        self.server_window.show()   
        
    def open_backup_panel(self):
        """Open the Backup windows."""
        self.server_window = BackupRestoreApp()
        self.server_window.show()                       
        

def main():
    app = QApplication(sys.argv)
    app.setApplicationDisplayName("Optics Dashboard")
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()