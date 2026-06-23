

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout,
    QHBoxLayout, QStackedWidget, QListWidget, QListWidgetItem, QLabel, QToolBar
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction



from modules.patient_module.patient_registratioin_system import PatientForm
from testform import MedicalReportForm
from modules.patient_module.patient_medicalLIst import MedicalReportSystem

from medicalrepotForms import MedicalReportForm
#from messgae_test import MessageAutomationsystem


#imported modules
#backup module
from modules.backup_module.backup_panel import BackupPanel #ok
from modules.backup_module.BACKUPSYSTEM import BackupRestoreApp#ok

#inventory system
from modules.inventory_module.inventory_system import InventorySystem #ok
from modules.inventory_module.inventory_report_viewer import InventoryReportViewer #ok
from modules.inventory_module.inventory_system_itemform_ui import ItemTypeForm #ok
from modules.inventory_module.InventoryManager_dashboard import InventoryManager #ok



#patient registration system
from modules.patient_module.patient_registratioin_system import PatientForm #ok
from modules.patient_module.patient_medicalLIst import MedicalReportSystem #ok

#sales modules
from modules.sales_module.sales_puchase_board import PurchaseBoardManager #ok
from modules.sales_module.PaymentHistoryDialog import PaymentHistoryDialog #ok
from modules.sales_module.month_sales_and_exits import MonthlyReportManager #ok

from modules.main_app.home_card import MainWindow #ok

from ui_ux.main_app.ui_sidebar11  import Ui_MainWindow


#task schedular
# from whatsapp_auth_system_final.job_scheduler import JobScheduler
from whatsapp_auto.main import whatsapp_automation_MainWindow 


import os
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QColorDialog, QMessageBox
from theme_dialog import ThemeDialog
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout
import sys
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class MainLauncher(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("NGASSAM OPTIC CLINIC")

        icon_path = "logo1.png"
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Warning: Icon file not found at {icon_path}")        

        self.ui.verticalLayout_5.setSpacing(0)
        self.ui.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.ui.stackedWidget.setCurrentIndex(0)  # 0 is the index for ui.page
        # Placeholder to track current index for refreshes
        self.ui.actionToggle_Theme.triggered.connect(self.open_theme_dialog)

        self.current_page_index = 0

        self.setup_connections()
        self.init_pages()

        # ✅ Show icon_only_widget by default and hide full_menu_widget
        self.ui.icon_only_widget.setVisible(True)
        self.ui.full_menu_widget.setVisible(False)

        # Sidebar toggle functionality
        self.ui.change_btn.setChecked(True)  # 🟢 Ensure toggle state is synced
        

  

        # # Add this after setting up your QStackedWidget
        # self.bg_label = QLabel(self.ui.stackedWidget)
        # pixmap = QPixmap(":/icon_home/logo1.png")
        # scaled = pixmap.scaled(self.ui.stackedWidget.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        # self.bg_label.setPixmap(scaled)
        # self.bg_label.setGeometry(self.ui.stackedWidget.rect())
        # self.bg_label.setScaledContents(True)
        # self.bg_label.lower()  # Put it behind all other widgets
# Inside your setup or init method
        self.bg_label = QLabel(self.ui.stackedWidget)
        self.bg_label.setScaledContents(True)  # 🔹 Make the image stretch to the QLabel size
        self.bg_label.lower()  # 🔹 Send the label behind other widgets

        # Load and set the image
        pixmap = QPixmap(":/icon_home/logo1.png")
        self.bg_label.setPixmap(pixmap)
        self.bg_label.setGeometry(self.ui.stackedWidget.rect())  # 🔹 Match stacked widget size
        self.bg_label.setStyleSheet("background-color: rgb(49, 58, 70);")

        
            
    def resizeEvent(self, event):
        if hasattr(self, 'bg_label'):
            self.bg_label.setGeometry(self.ui.stackedWidget.rect())  # Resize label
        return super().resizeEvent(event)
    
    def showEvent(self, event):
        if hasattr(self, 'bg_label'):
            self.bg_label.setGeometry(self.ui.stackedWidget.rect())
            pixmap = QPixmap(":/icon_home/logo1.png")
            scaled = pixmap.scaled(self.ui.stackedWidget.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self.bg_label.setPixmap(scaled)
        super().showEvent(event)

                
            
    def setup_connections(self):
        # Sidebar connections
        self.ui.home_btn_1.clicked.connect(lambda: self.change_page(0))
        self.ui.home_btn_2.clicked.connect(lambda: self.change_page(0))

        self.ui.patient_form_btn_1.clicked.connect(lambda: self.change_page(1))
        self.ui.patient_form_btn_2.clicked.connect(lambda: self.change_page(1))

        self.ui.medical_prescription_btn_1.clicked.connect(lambda: self.change_page(2))
        self.ui.medical_prescription_btn_2.clicked.connect(lambda: self.change_page(2))

        self.ui.invemtory_btn_1.clicked.connect(lambda: self.change_page(3))
        self.ui.invemtory_btn_2.clicked.connect(lambda: self.change_page(3))

        self.ui.whatsapp_btn_1.clicked.connect(lambda: self.change_page(4))
        self.ui.whatsapp_btn_2.clicked.connect(lambda: self.change_page(4))
        
        self.ui.sales_btn_1.clicked.connect(lambda: self.change_page(5))
        self.ui.sales_btn_2.clicked.connect(lambda: self.change_page(5))        

        self.ui.exit_btn_1.clicked.connect(self.close)
        self.ui.exit_btn_2.clicked.connect(self.close)

        # Top menu actions
        self.ui.actionRefresh_Data.triggered.connect(self.refresh_data)
        self.ui.actionImport_Restore_Backup.triggered.connect(self.show_backup_panel)
        self.ui.actionWhatsApp_Automation.triggered.connect(lambda: self.change_page(4))
        self.ui.actionLogout.triggered.connect(self.logout_user)
        self.ui.actionInventory_Report.triggered.connect(self.show_inventory_report)
        self.ui.actionPayment_History_2.triggered.connect(self.show_payament_history_dialog)
        self.ui.actionCategory_Items.triggered.connect(self.show_inventory_category_item_add_system)
        self.ui.actionEntry_Sales_Report.triggered.connect(self.show_Entry_sales_report)
                

    def init_pages(self):
        def apply_layout(page, layout, widget):
            if page.layout() is None:
                vbox = QVBoxLayout(page)
            else:
                vbox = page.layout()
            vbox.addWidget(widget)

        # Store module widgets in instance attributes for access
        self.card_display = MainWindow()
        # self.inventory_widget = InventorySystem()
        self.inventory_widget = InventoryManager()
        self.patient_form = PatientForm()
        self.medical_report = MedicalReportSystem()
        self.whatsapp_widget = whatsapp_automation_MainWindow()  # important
        self.purchase_board = PurchaseBoardManager()
        self.backup_panel = BackupPanel()
        

        apply_layout(self.ui.page, self.ui.gridLayout_2, self.card_display)            # Page 0
        apply_layout(self.ui.page_2, self.ui.gridLayout_3, self.patient_form)          # Page 1
        apply_layout(self.ui.page_3, self.ui.gridLayout_4, self.medical_report)        # Page 2
        apply_layout(self.ui.page_4, self.ui.gridLayout_5, self.inventory_widget)      # Page 3 inventory_widget
        apply_layout(self.ui.page_5, self.ui.gridLayout_6, self.whatsapp_widget)       # Page 4
        apply_layout(self.ui.page_7, self.ui.gridLayout_7, self.backup_panel)          # Page 5 (Backup)
        apply_layout(self.ui.page_6, self.ui.gridLayout_8, self.purchase_board)        # Page 6 
        

    def change_page(self, index):
        """Switch page and trigger any special behavior."""
        self.ui.stackedWidget.setCurrentIndex(index)
        self.current_page_index = index
        print(f"[INFO] Switched to page index {index}")

        # Special logic for WhatsApp Automation page
        if index == 3 and hasattr(self.whatsapp_widget, "load_patients"):
            print("[DEBUG] Loading patients in WhatsApp Automation...")
            self.whatsapp_widget.load_patients()

    def show_backup_panel(self):
        index = self.ui.stackedWidget.indexOf(self.ui.page_7)
        if index != -1:
            self.change_page(index)

    def refresh_data(self):
        print(f"[INFO] Refreshing page {self.current_page_index}")
        # Optional: You can reload the current page logic here

    def logout_user(self):
        print("[INFO] User logged out.")

    def show_inventory_report(self):
        self.inventory_report_window = InventoryReportViewer()
        self.inventory_report_window.show()
    def show_payament_history_dialog(self):
        self.payment_hiatory = PaymentHistoryDialog()
        self.payment_hiatory.show()
    def show_inventory_category_item_add_system(self):
        self.payment_hiatory = ItemTypeForm()
        self.payment_hiatory.show()

    def show_Entry_sales_report(self):
        self.payment_hiatory = MonthlyReportManager()
        self.payment_hiatory.show()
        
    def open_theme_dialog(self):
        dialog = ThemeDialog(self)
        dialog.exec()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainLauncher()
    window.show()
    sys.exit(app.exec())
