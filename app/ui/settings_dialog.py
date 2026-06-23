# import sys
# import os
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# if project_root not in sys.path:
#     sys.path.insert(0, project_root)
    
# import json
# from PySide6.QtWidgets import (
#     QDialog, QVBoxLayout, QLabel,
#     QLineEdit, QPushButton, QMessageBox
# )

# from config.app_config import USER_CONFIG_PATH, load_config


# # class SettingsDialog(QDialog):
# #     def __init__(self):
# #         super().__init__()
# #         self.setWindowTitle("System Settings")
# #         self.setMinimumWidth(350)

# #         layout = QVBoxLayout(self)

# #         layout.addWidget(QLabel("Server URL"))
# #         self.server_input = QLineEdit()
# #         layout.addWidget(self.server_input)

# #         save_btn = QPushButton("Save")
# #         save_btn.clicked.connect(self.save_config)
# #         layout.addWidget(save_btn)

# #         self.load_config()

# #     def load_config(self):
# #         config = load_config()
# #         self.server_input.setText(
# #             config.get("SERVER_URL", "")
# #         )

# #     def save_config(self):
# #         try:
# #             config = load_config()
# #             config["SERVER_URL"] = self.server_input.text().strip()

# #             with open(USER_CONFIG_PATH, "w", encoding="utf-8") as f:
# #                 json.dump(config, f, indent=4)

# #             QMessageBox.information(
# #                 self,
# #                 "Success",
# #                 "Settings saved.\nRestart application to apply changes."
# #             )
# #             self.accept()
# #         except Exception as e:
# #             QMessageBox.critical(self, "Error", str(e))



# import sys
# import os
# import json
# from pathlib import Path

# from PySide6.QtWidgets import (
#     QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
#     QPushButton, QFrame, QMessageBox, QDialogButtonBox, QApplication
# )
# from PySide6.QtCore import Qt
# from PySide6.QtGui import QFont, QIcon

# # Assuming these are defined in your project
# # from config.app_config import USER_CONFIG_PATH, load_config


# class SettingsDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("Settings")
#         self.setFixedWidth(460)
#         self.setMinimumHeight(240)
#         self.setWindowFlags(
#             self.windowFlags() & ~Qt.WindowContextHelpButtonHint
#         )

#         self.setup_ui()
#         # self.load_settings()

#     def setup_ui(self):
#         self.setStyleSheet("""
#             QDialog {
#                 background-color: #1e1e2e;
#                 color: #cdd6f4;
#             }
#             QLineEdit {
#                 background-color: #2a2a3e;
#                 border: 1px solid #45475a;
#                 border-radius: 6px;
#                 padding: 10px 12px;
#                 color: #cdd6f4;
#                 font-size: 14px;
#             }
#             QLineEdit:focus {
#                 border: 1px solid #89b4fa;
#                 background-color: #2f2f44;
#             }
#             QLabel {
#                 color: #94e2d5;
#                 font-size: 13px;
#                 font-weight: 500;
#                 margin-bottom: 4px;
#             }
#             QPushButton {
#                 background-color: #45475a;
#                 color: white;
#                 border: none;
#                 border-radius: 6px;
#                 padding: 10px 18px;
#                 font-size: 14px;
#                 font-weight: 500;
#             }
#             QPushButton:hover {
#                 background-color: #585b70;
#             }
#             QPushButton:pressed {
#                 background-color: #3e404e;
#             }
#             QPushButton#primary {
#                 background-color: #89b4fa;
#                 color: #1e1e2e;
#             }
#             QPushButton#primary:hover {
#                 background-color: #a0c0ff;
#             }
#             QFrame.separator {
#                 background: #45475a;
#                 height: 1px;
#                 margin: 12px 0;
#             }
#         """)

#         main_layout = QVBoxLayout(self)
#         main_layout.setContentsMargins(24, 28, 24, 20)
#         main_layout.setSpacing(16)

#         # Header
#         title = QLabel("System Settings")
#         title.setStyleSheet("""
#             font-size: 20px;
#             font-weight: 600;
#             color: #cdd6f4;
#             margin-bottom: 8px;
#         """)
#         main_layout.addWidget(title)

#         subtitle = QLabel("Configure application connection")
#         subtitle.setStyleSheet("color: #7f849c; font-size: 13px; margin-bottom: 12px;")
#         main_layout.addWidget(subtitle)

#         # Separator
#         sep = QFrame()
#         sep.setFrameShape(QFrame.HLine)
#         sep.setObjectName("separator")
#         main_layout.addWidget(sep)

#         main_layout.addSpacing(12)

#         # Server URL field
#         server_label = QLabel("Server URL")
#         main_layout.addWidget(server_label)

#         self.server_input = QLineEdit()
#         self.server_input.setPlaceholderText("https://api.example.com")
#         self.server_input.setClearButtonEnabled(True)
#         main_layout.addWidget(self.server_input)

#         main_layout.addSpacing(28)

#         # Buttons
#         btn_layout = QHBoxLayout()
#         btn_layout.setContentsMargins(0, 0, 0, 0)
#         btn_layout.addStretch()

#         cancel_btn = QPushButton("Cancel")
#         cancel_btn.setFixedWidth(100)
#         cancel_btn.clicked.connect(self.reject)

#         save_btn = QPushButton("Save Changes")
#         save_btn.setObjectName("primary")
#         save_btn.setFixedWidth(140)
#         save_btn.setDefault(True)
#         # save_btn.clicked.connect(self.save_and_close)

#         btn_layout.addWidget(cancel_btn)
#         btn_layout.addSpacing(12)
#         btn_layout.addWidget(save_btn)

#         main_layout.addLayout(btn_layout)
        
#         self.load_config()

       
        
#     def load_config(self):
#         config = load_config()
#         self.server_input.setText(
#             config.get("SERVER_URL", "")
#         )

#     def save_config(self):
#         try:
#             config = load_config()
#             config["SERVER_URL"] = self.server_input.text().strip()

#             with open(USER_CONFIG_PATH, "w", encoding="utf-8") as f:
#                 json.dump(config, f, indent=4)

#             QMessageBox.information(
#                 self,
#                 "Success",
#                 "Settings saved.\nRestart application to apply changes."
#             )
#             self.accept()
#         except Exception as e:
#             QMessageBox.critical(self, "Error", str(e))        
        
# # Demo / Test
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     app.setStyle("Fusion")

#     # Optional dark theme palette
#     from PySide6.QtGui import QPalette, QColor
#     palette = QPalette()
#     palette.setColor(QPalette.Window, QColor(30, 30, 46))
#     palette.setColor(QPalette.WindowText, QColor(205, 214, 244))
#     palette.setColor(QPalette.Base, QColor(42, 42, 62))
#     palette.setColor(QPalette.AlternateBase, QColor(50, 50, 74))
#     palette.setColor(QPalette.Text, QColor(205, 214, 244))
#     palette.setColor(QPalette.Button, QColor(69, 71, 90))
#     palette.setColor(QPalette.ButtonText, Qt.white)
#     palette.setColor(QPalette.Highlight, QColor(137, 180, 250))
#     app.setPalette(palette)

#     dialog = SettingsDialog()
#     dialog.exec()        


import sys
import os
import json

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QFrame, QMessageBox, QApplication
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon

# Uses config_loader to find config.json whether running as script or .exe
from config_loader import _get_config_path


def _read_config() -> dict:
    """Read current config.json and return it as a dict."""
    try:
        with open(_get_config_path(), 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {"BASE_URL": ""}


def _write_config(data: dict):
    """Write updated config back to config.json."""
    with open(_get_config_path(), 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setFixedWidth(460)
        self.setMinimumHeight(240)
        self.setWindowFlags(
            self.windowFlags() & ~Qt.WindowContextHelpButtonHint
        )
        self.setup_ui()

    def setup_ui(self):
        self.setStyleSheet("""
            QDialog {
                background-color: #1e1e2e;
                color: #cdd6f4;
            }
            QLineEdit {
                background-color: #2a2a3e;
                border: 1px solid #45475a;
                border-radius: 6px;
                padding: 10px 12px;
                color: #cdd6f4;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #89b4fa;
                background-color: #2f2f44;
            }
            QLabel {
                color: #94e2d5;
                font-size: 13px;
                font-weight: 500;
                margin-bottom: 4px;
            }
            QPushButton {
                background-color: #45475a;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 18px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: #585b70;
            }
            QPushButton:pressed {
                background-color: #3e404e;
            }
            QPushButton#primary {
                background-color: #89b4fa;
                color: #1e1e2e;
            }
            QPushButton#primary:hover {
                background-color: #a0c0ff;
            }
        """)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(24, 28, 24, 20)
        main_layout.setSpacing(16)

        # Header
        title = QLabel("System Settings")
        title.setStyleSheet("font-size: 20px; font-weight: 600; color: #cdd6f4; margin-bottom: 8px;")
        main_layout.addWidget(title)

        subtitle = QLabel("Configure server connection URL")
        subtitle.setStyleSheet("color: #7f849c; font-size: 13px; margin-bottom: 12px;")
        main_layout.addWidget(subtitle)

        # Separator
        sep = QFrame()
        sep.setFrameShape(QFrame.HLine)
        sep.setStyleSheet("background: #45475a;")
        main_layout.addWidget(sep)
        main_layout.addSpacing(12)

        # Server URL field
        server_label = QLabel("Server URL")
        main_layout.addWidget(server_label)

        self.server_input = QLineEdit()
        self.server_input.setPlaceholderText("http://192.168.1.146:8000")
        self.server_input.setClearButtonEnabled(True)
        main_layout.addWidget(self.server_input)

        main_layout.addSpacing(28)

        # Buttons
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()

        cancel_btn = QPushButton("Cancel")
        cancel_btn.setFixedWidth(100)
        cancel_btn.clicked.connect(self.reject)

        save_btn = QPushButton("Save Changes")
        save_btn.setObjectName("primary")
        save_btn.setFixedWidth(140)
        save_btn.setDefault(True)
        save_btn.clicked.connect(self.save_config)

        btn_layout.addWidget(cancel_btn)
        btn_layout.addSpacing(12)
        btn_layout.addWidget(save_btn)
        main_layout.addLayout(btn_layout)

        # Load current value from config.json into the input field
        self.load_config()

    def load_config(self):
        """Read BASE_URL from config.json and display it in the input field."""
        config = _read_config()
        self.server_input.setText(config.get("BASE_URL", ""))

    def save_config(self):
        """Save the new BASE_URL back to config.json."""
        new_url = self.server_input.text().strip().rstrip('/')
        if not new_url:
            QMessageBox.warning(self, "Validation", "Server URL cannot be empty.")
            return
        try:
            config = _read_config()
            config["BASE_URL"] = new_url
            _write_config(config)
            QMessageBox.information(
                self,
                "Saved",
                f"Server URL updated to:\n{new_url}\n\nRestart the application to apply changes."
            )
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save settings:\n{str(e)}")


#
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = SettingsDialog()
    dialog.exec()

