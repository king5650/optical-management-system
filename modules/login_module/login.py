import sys
import os
# Go two levels up to reach the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import sys
import os
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QIcon
# from ui_login import Ui_MainWindow  # Import the login UI
# from ui_login import Ui_MainWindow
from ui_ux.login.ui_LOGINFORM2 import Ui_MainWindow  
from PySide6.QtCore import Qt
#from home_page import MainLauncher  
from main1 import MainWindow  


# After (config-driven - correct):

from config_loader import BASE_URL
response = requests.get(f'{BASE_URL}')



# BASE_URL = "http://127.0.0.1:8000/auth/"
#BASE_URL = "http://192.168.10.50:8000/auth/login/"   

class LoginApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Login")
        self.setWindowFlags(Qt.FramelessWindowHint)
        icon_path = "images/login.png"
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Warning: Icon file not found at {icon_path}")        
        self.pushButton.clicked.connect(self.handle_login)  # Login button click

    def handle_login(self):
        # username = self.textEdit.toPlainText()
        # password = self.textEdit_2.toPlainText()
        username = self.lineEdit_3.text()
        password = self.lineEdit_2.text()
        try:
            response = requests.post(
                f'{BASE_URL}/login/',  # Update with your backend login URL
                json={'username': username, 'password': password}
            )
            if response.status_code == 200:
                data = response.json()
                role_redirect = data.get('redirect')
                QMessageBox.information(self, "Login Successful", f"Redirecting to: {role_redirect}")

                # Redirect to the appropriate window based on the role
                if role_redirect == 'Home_page':
                    self.open_patient_form()
                elif role_redirect == 'admin_dashboard':
                    # You can implement admin functionality here
                    QMessageBox.information(self, "Redirect", "Admin Dashboard is under construction!")
                elif role_redirect == 'inventory_management':
                    # Implement inventory management window
                    QMessageBox.information(self, "Redirect", "Inventory Management is under construction!")
                else:
                    QMessageBox.information(self, "Redirect", "error in role redirection!")
            else:
                QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")

    def open_patient_form(self):
        self.patient_form = MainWindow()  
        self.patient_form.show()
        self.close() 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec())


