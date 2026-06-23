
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLineEdit, QLabel, QFrame, QGraphicsDropShadowEffect
)
from PySide6.QtGui import QFont, QColor, QPainter, QBrush
from PySide6.QtCore import Qt, QPropertyAnimation, QRect, QTimer
import sys
from PySide6.QtWidgets import QGraphicsOpacityEffect

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

class NeumorphicApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setFixedSize(400, 500)
        self.setWindowTitle("Neumorphic Style Login")
        self.opacity_anim = None
        self.cards = []  # Store card references
        self.init_ui()
        self.setStyleSheet(open("style.qss").read())
        self.fade_in_window()

    def fade_in_window(self):
        opacity_effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(opacity_effect)
        self.opacity_anim = QPropertyAnimation(opacity_effect, b"opacity")
        self.opacity_anim.setDuration(1000)
        self.opacity_anim.setStartValue(0)
        self.opacity_anim.setEndValue(1)
        self.opacity_anim.start()

    def add_shadow(self, widget, blur=20, x_offset=4, y_offset=4, color=QColor(180, 180, 180, 120)):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(blur)
        shadow.setOffset(x_offset, y_offset)
        shadow.setColor(color)
        widget.setGraphicsEffect(shadow)

    def animate_widget(self, widget):
        anim = QPropertyAnimation(widget, b"geometry")
        anim.setDuration(500)
        anim.setStartValue(widget.geometry())
        end_rect = QRect(widget.x(), widget.y()-5, widget.width(), widget.height())
        anim.setEndValue(end_rect)
        anim.setLoopCount(2)
        anim.setEasingCurve(Qt.EaseInOutQuad)
        anim.start()
        self._anim = anim

    def switch_tab_animation(self, active, inactive):
        active.setObjectName("activeTab")
        inactive.setObjectName("")
        self.setStyleSheet(open("style.qss").read())

        anim = QPropertyAnimation(active, b"geometry")
        anim.setDuration(300)
        rect = active.geometry()
        anim.setStartValue(QRect(rect.x(), rect.y(), rect.width(), rect.height()))
        anim.setEndValue(QRect(rect.x(), rect.y()-5, rect.width(), rect.height()))
        anim.start()
        self._anim2 = anim

    def init_ui(self):
        main_layout = QVBoxLayout(self)
        main_layout.setAlignment(Qt.AlignCenter)

        container = QFrame()
        container.setObjectName("container")
        container.setFixedWidth(300)
        container_layout = QVBoxLayout(container)
        container_layout.setSpacing(15)
        self.add_shadow(container)

        # Tabs (Login/Register)
        tabs_layout = QHBoxLayout()
        self.login_tab = QPushButton("Login")
        self.login_tab.setObjectName("activeTab")
        self.login_tab.setProperty("class", "tab")
        self.register_tab = QPushButton("Register")
        self.register_tab.setProperty("class", "tab")
        tabs_layout.addWidget(self.login_tab)
        tabs_layout.addWidget(self.register_tab)
        container_layout.addLayout(tabs_layout)

        self.login_tab.clicked.connect(lambda: self.switch_tab_animation(self.login_tab, self.register_tab))
        self.register_tab.clicked.connect(lambda: self.switch_tab_animation(self.register_tab, self.login_tab))

        # Inputs
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        container_layout.addWidget(self.username_input)
        container_layout.addWidget(self.password_input)

        # Button
        self.login_button = QPushButton("Login")
        self.login_button.setObjectName("mainBtn")
        self.login_button.clicked.connect(lambda: self.animate_widget(self.login_button))
        container_layout.addWidget(self.login_button)
        self.add_shadow(self.login_button)
        


        # OR text
        or_label = QLabel("OR")
        or_label.setObjectName("orLabel")
        or_label.setAlignment(Qt.AlignCenter)
        container_layout.addWidget(or_label)

        # Social Buttons
        social_layout = QHBoxLayout()
        for name in ["F", "G", "T"]:
            btn = QPushButton(name)
            btn.setProperty("class", "social")
            btn.setFixedSize(40, 40)
            self.add_shadow(btn)
            social_layout.addWidget(btn)
        container_layout.addLayout(social_layout)

        main_layout.addWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NeumorphicApp()
    window.show()
    sys.exit(app.exec())
