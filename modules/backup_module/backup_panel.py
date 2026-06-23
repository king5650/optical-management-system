import sys
import os
# Go two levels up to reach the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame, QSizePolicy
from PySide6.QtCore import Qt, QPoint
# Adjust path accordingly
from modules.backup_module.BACKUPSYSTEM import BackupRestoreApp
import sys
import os
import requests
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit, QLabel,
    QVBoxLayout, QHBoxLayout, QFileDialog, QProgressBar, QDateTimeEdit
)
from PySide6.QtCore import Qt, QTimer, QDateTime


class BackupPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFixedSize(500, 500)
        self.original_size = self.size()
        self.is_maximized = False

        self.setStyleSheet("""
            QFrame#ContainerFrame {
                background-color: #58a29d;
            }
            QVBoxLayout {
                margin: 0px;
                padding: 10px;
                
            }
            QFrame#TitleBar {
                background-color: #2c3e50;
                color: white;
                padding: 5px;
            }
            QLabel#TitleLabel {
                font-weight: bold;
                background-color: none;
            }
            QPushButton {
                background-color: #34495e;
                border: none;
                color: white;
                width: 20px;
                height: 20px;
            }
            QPushButton:hover {
                background-color: #e74c3c;
            }
        """)

        # Main layout of the widget
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # New outer container
        self.container_frame = QFrame()
        self.container_frame.setObjectName("ContainerFrame")
        self.container_layout = QVBoxLayout(self.container_frame)
        self.container_layout.setContentsMargins(0, 0, 0, 0)
        
        # --- Title Bar ---
        self.title_bar = QFrame()
        self.title_bar.setObjectName("TitleBar")
        self.title_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.title_layout = QHBoxLayout(self.title_bar)
        self.title_layout.setContentsMargins(10, 2, 10, 2)

  
        
        self.title_label = QLabel("🔧 Backup & Restore")
        self.title_label.setObjectName("TitleLabel")

        self.btn_minimize = QPushButton("–")
        self.btn_minimize.clicked.connect(self.toggle_minimize)

        self.btn_maximize = QPushButton("⬜")
        self.btn_maximize.clicked.connect(self.toggle_maximize)

        self.btn_close = QPushButton("×")
        self.btn_close.clicked.connect(self.hide)

        self.title_layout.addWidget(self.title_label)
        self.title_layout.addStretch()
        self.title_layout.addWidget(self.btn_minimize)
        self.title_layout.addWidget(self.btn_maximize)
        self.title_layout.addWidget(self.btn_close)

        # --- Backup UI ---
        self.backup_app = BackupRestoreApp()

        # Add title bar and backup UI to container
        self.container_layout.addWidget(self.title_bar)
        self.container_layout.addWidget(self.backup_app)

        # Add container to main layout
        self.layout.addWidget(self.container_frame)

        # Dragging variables
        self._is_dragging = False
        self._drag_pos = QPoint()

        # Frameless window
        self.setWindowFlags(Qt.FramelessWindowHint)

    def toggle_minimize(self):
        if self.backup_app.isVisible():
            self.backup_app.hide()
            self.setFixedHeight(self.title_bar.height())
        else:
            self.backup_app.show()
            self.setFixedSize(self.original_size)

    def toggle_maximize(self):
        if not self.is_maximized:
            parent = self.parent()
            if parent:
                self.setFixedSize(parent.size())
            self.is_maximized = True
            self.btn_maximize.setText("❐")
        else:
            self.setFixedSize(self.original_size)
            self.is_maximized = False
            self.btn_maximize.setText("⬜")

    # --- Dragging logic ---
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.title_bar.underMouse():
            self._is_dragging = True
            self._drag_pos = event.globalPosition().toPoint() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._is_dragging:
            new_pos = event.globalPosition().toPoint() - self._drag_pos
            self.move(new_pos)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_dragging = False






if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BackupPanel()
    window.show()
    sys.exit(app.exec())


