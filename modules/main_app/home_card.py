from PySide6.QtWidgets import QFrame, QLabel, QVBoxLayout, QGraphicsDropShadowEffect
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
import sys
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout
# from NeumorphicCard import NeumorphicCard

class NeumorphicCard(QFrame):
    def __init__(self, title, description):
        super().__init__()
        self.setFixedSize(290, 150)
        self.setStyleSheet("""
            QFrame {
                background-color: #F5F6FA;
                border-radius: 16px;
            }
        """)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(3)
        self.shadow.setYOffset(3)
        self.shadow.setColor(QColor(30, 61, 89, 100))  # soft blue shadow
        self.setGraphicsEffect(self.shadow)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignTop)

        self.title_label = QLabel(title)
        self.title_label.setObjectName("cardTitle")

        self.desc_label = QLabel(description)
        self.desc_label.setObjectName("cardDescription")
        self.desc_label.setWordWrap(True)

        layout.addWidget(self.title_label)
        layout.addWidget(self.desc_label)

    def enterEvent(self, event):
        self.shadow.setBlurRadius(30)
        self.shadow.setXOffset(5)
        self.shadow.setYOffset(5)
        self.shadow.setColor(QColor(0, 118, 168, 160))  # accent blue glow
        return super().enterEvent(event)

    def leaveEvent(self, event):
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(3)
        self.shadow.setYOffset(3)
        self.shadow.setColor(QColor(30, 61, 89, 100))
        return super().leaveEvent(event)

import requests

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Optical System UI - Smooth Design")
        self.setStyleSheet(self.load_styles())
        self.cards = []  # Store card references
        self.init_ui()
        self.update_cards_from_backend()  # Fetch and display data

    def init_ui(self):
        from PySide6.QtWidgets import QGridLayout

        grid = QGridLayout(self)
        grid.setSpacing(30)
        grid.setContentsMargins(30, 50, 30, 200)

        # Create cards with placeholder text
        self.cards = [
            NeumorphicCard("👥Patients", "Loading..."),
            NeumorphicCard("📦 Sales", "Loading..."),
            NeumorphicCard("👁️ Appointments", "Loading..."),
            NeumorphicCard("➕ New Patient", "Loading..."),
        ]

        cards_per_row = 4
        for i, card in enumerate(self.cards):
            row = i // cards_per_row
            col = i % cards_per_row
            grid.addWidget(card, row, col)

    def update_cards_from_backend(self):
        try:
            response = requests.get("http://127.0.0.1:8000/auth/dashboard-counts/")
            if response.status_code == 200:
                data = response.json()
                # Update card descriptions with real data
                self.cards[0].desc_label.setText(f"{data['patient_count']} patients registered.")
                self.cards[1].desc_label.setText(f"{data['sales_count']} Sales Count.")
                self.cards[2].desc_label.setText(f"{data['patient_count']} patients registered.")
            else:
                print("Failed to fetch dashboard data:", response.text)
        except Exception as e:
            print("Error fetching dashboard data:", e)

    def load_styles(self):
        return """
        QWidget {
            background-color: #1E3D59;
        }

        QLabel#cardTitle {
            font-family: 'Nunito';
            font-size: 17pt;
            color: #0076A8;
            font-weight: bold;
            padding-bottom: 6px;
        }

        QLabel#cardDescription {
            font-family: 'Inter';
            font-size: 11pt;
            color: #444;
        }
        """


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
