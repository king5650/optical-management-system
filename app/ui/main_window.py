import sys
import os

import sys
import os

# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


from settings_dialog import SettingsDialog
    
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFrame,
    QPushButton, QLabel, QLineEdit, QTableWidget, QTableWidgetItem,
    QHeaderView, QAbstractItemView, QMessageBox,QDialog
) 
from PySide6.QtWidgets import QMainWindow, QPushButton

# from app.ui.settings_dialog import SettingsDialog

class ServerIPWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Optical Management System")

        settings_btn = QPushButton("Settings")
        settings_btn.clicked.connect(self.open_settings)

        self.setCentralWidget(settings_btn)

    def open_settings(self):
        dialog = SettingsDialog()
        dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ServerIPWindows()
    win.show()
    sys.exit(app.exec())
