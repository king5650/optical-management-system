# from PyQt6.QtWidgets import (
#     QApplication,
#     QLabel,
#     QWidget,
#     QVBoxLayout,
#     QTableWidget,
#     QTableWidgetItem,
# )
# from PyQt6.QtGui import QFont


# class InvoiceWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Invoice")

#         # Create widgets
#         self.title_label = QLabel("NGASSAM OPTIQUE")
#         self.title_label.setFont(QFont("Arial", 24))

#         self.sub_title_label = QLabel(
#             "CABINET OPTIQUE\nVente de materiel - Ophtanique médical-Verre ophtarnique - Montures de marque\nN.I.U: P039116571319P-RC/YAO/2023/A/351\nSitué content is not safe and I can't generate an answer for your request




from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import QTimer, Qt, QPropertyAnimation
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import QGraphicsOpacityEffect

class SlideShow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Header Slideshow Example")
        self.resize(800, 400)

        # Layout
        self.layout = QVBoxLayout(self)
        
        # Image Label
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label)

        # Overlay Text
        self.text_label = QLabel("Welcome to My App", self)
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setFont(QFont("Arial", 28, QFont.Bold))
        self.text_label.setStyleSheet("color: white; background: transparent;")
        self.layout.addWidget(self.text_label, alignment=Qt.AlignCenter)

        # Image List
        self.images = ["add_shopping_cart_16px.png", "logo1.png","logo1.png", "logo1.png"]
        self.index = 0

        # Fade effect
        self.opacity_effect = QGraphicsOpacityEffect(self.image_label)
        self.image_label.setGraphicsEffect(self.opacity_effect)
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(1500)

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.next_slide)
        self.timer.start(4000)  # change every 4s

        self.next_slide()

    def next_slide(self):
        pixmap = QPixmap(self.images[self.index]).scaled(
            self.image_label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation
        )
        self.image_label.setPixmap(pixmap)

        # Fade animation
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

        self.index = (self.index + 1) % len(self.images)

if __name__ == "__main__":
    app = QApplication([])
    w = SlideShow()
    w.show()
    app.exec()
