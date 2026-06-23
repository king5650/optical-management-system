import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QFrame, QMessageBox
)
from PySide6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QRect, QTimer
from PySide6.QtGui import QFont, QColor, QPalette, QLinearGradient, QBrush, QPainter


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modern Login")
        self.setFixedSize(420, 580)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.central_widget = QWidget()
        self.central_widget.setObjectName("central")
        self.central_widget.setStyleSheet("""
            border-radius: 20px;
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 #2c254f, stop:1 #1c1238);
        """)
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.create_ui()
        self.start_animations()

    def create_ui(self):
        # Main container with rounded corners & gradient
        self.container = QFrame()
        self.container.setObjectName("container")
        # self.container.setStyleSheet("""
        #     border-radius: 20px;
        #     background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
        #         stop:0 #2c254f, stop:1 #1c1238);
        # """)
        self.container.setFixedSize(380, 540)
        self.main_layout.addWidget(self.container, alignment=Qt.AlignCenter)

        layout = QVBoxLayout(self.container)
        layout.setContentsMargins(40, 50, 40, 40)
        layout.setSpacing(18)

        # Logo / App Name with animation
        self.logo_label = QLabel("OPTICS")
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setStyleSheet("""
            font-family: 'Segoe UI', sans-serif;
            font-size: 52px;
            font-weight: bold;
            color: white;
            background: transparent;
        """)
        layout.addWidget(self.logo_label)

        self.subtitle = QLabel("Server-Ip")
        self.subtitle.setAlignment(Qt.AlignCenter)
        self.subtitle.setStyleSheet("""
            color: #b0b0ff;
            font-size: 16px;
            margin-top: -10px;
            background: transparent;
        """)
        layout.addWidget(self.subtitle)

        layout.addSpacing(35)

        # ── Fields ───────────────────────────────
        self.create_input_field("Username or Email", self.container, is_password=False)
        layout.addSpacing(8)

        self.password_field = self.create_input_field("Password", self.container, is_password=True)
        layout.addSpacing(28)

        # Login Button
        self.btn_login = QPushButton("Connect")
        self.btn_login.setFixedHeight(52)
        self.btn_login.setCursor(Qt.PointingHandCursor)
        self.btn_login.clicked.connect(self.try_login)
        layout.addWidget(self.btn_login)

        layout.addSpacing(12)

   
    

    # def create_input_field(self, placeholder, parent, is_password=False):
    #     field = QLineEdit()
    #     field.setPlaceholderText(placeholder)
    #     field.setFixedHeight(52)
    #     field.setEchoMode(QLineEdit.Password if is_password else QLineEdit.Normal)

    #     field.setStyleSheet("""
    #         QLineEdit {
    #             background-color: rgba(255, 255, 255, 0.08);
    #             border: 2px solid rgba(255, 255, 255, 0.12);
    #             border-radius: 12px;
    #             padding: 0 18px;
    #             color: white;
    #             font-size: 15px;
    #         }
    #         QLineEdit:focus {
    #             border: 2px solid #7b5eff;
    #             background-color: rgba(255, 255, 255, 0.12);
    #         }
    #     """)
    #     parent.layout().addWidget(field)
    #     return field
    def create_input_field(self, placeholder, parent, is_password=False):
        # Create the input field
        field = QLineEdit()
        field.setPlaceholderText(placeholder)
        field.setFixedHeight(52)
        field.setEchoMode(QLineEdit.Password if is_password else QLineEdit.Normal)

        # Style the input field
        field.setStyleSheet("""
            QLineEdit {
                background-color: rgba(255, 255, 255, 0.08);
                border: 2px solid rgba(255, 255, 255, 0.12);
                border-radius: 12px;
                padding: 0 18px;
                color: white;
                font-size: 15px;
            }
            QLineEdit:focus {
                border: 2px solid #7b5eff;
                background-color: rgba(255, 255, 255, 0.12);
            }
        """)

        # Add a toggle button for password fields
        if is_password:
            toggle_btn = QPushButton("Show")
            toggle_btn.setCursor(Qt.PointingHandCursor)
            toggle_btn.setFixedSize(50, 30)
            toggle_btn.setStyleSheet("""
                QPushButton {
                    border: none;
                    background: transparent;
                    color: #7b5eff;
                    font-size: 12px;
                }
                QPushButton:hover {
                    color: #a78bfa;
                }
            """)

            # Toggle password visibility
            def toggle_password_visibility():
                if field.echoMode() == QLineEdit.Password:
                    field.setEchoMode(QLineEdit.Normal)
                    toggle_btn.setText("Hide")
                else:
                    field.setEchoMode(QLineEdit.Password)
                    toggle_btn.setText("Show")

            toggle_btn.clicked.connect(toggle_password_visibility)

            # Add the field and button to a layout
            container = QHBoxLayout()
            container.addWidget(field)
            container.addWidget(toggle_btn)
            container.setContentsMargins(0, 0, 0, 0)

            # Create a widget to hold the layout
            widget = QWidget()
            widget.setLayout(container)
            parent.layout().addWidget(widget)
        else:
            parent.layout().addWidget(field)

        return field
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor(28, 25, 60))
        gradient.setColorAt(0.5, QColor(40, 35, 85))
        gradient.setColorAt(1.0, QColor(20, 18, 45))

        painter.setBrush(QBrush(gradient))
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())

    def start_animations(self):
        # Fade in logo
        self.logo_label.setStyleSheet(self.logo_label.styleSheet() + "opacity: 0;")
        self.anim_logo = QPropertyAnimation(self.logo_label, b"geometry")
        self.anim_logo.setDuration(1200)
        self.anim_logo.setStartValue(QRect(0, 40, self.width(), 100))
        self.anim_logo.setEndValue(QRect(0, 60, self.width(), 100))
        self.anim_logo.setEasingCurve(QEasingCurve.OutCubic)

        # Slight bounce for logo
        QTimer.singleShot(300, lambda: self.animate_bounce(self.logo_label))

        # Fields slide from bottom
        QTimer.singleShot(600, self.animate_fields)

        self.anim_logo.start()

    def animate_bounce(self, widget):
        anim = QPropertyAnimation(widget, b"geometry")
        anim.setDuration(800)
        anim.setStartValue(widget.geometry())
        anim.setEndValue(widget.geometry())
        anim.setKeyValueAt(0.4, QRect(widget.x(), widget.y()-12, widget.width(), widget.height()))
        anim.setEasingCurve(QEasingCurve.OutBounce)
        anim.start()

    def animate_fields(self):
        for i, w in enumerate(self.container.findChildren(QLineEdit)):
            orig = w.geometry()
            start = QRect(orig.x(), orig.y()+80, orig.width(), orig.height())

            anim = QPropertyAnimation(w, b"geometry")
            anim.setDuration(900 + i*180)
            anim.setStartValue(start)
            anim.setEndValue(orig)
            anim.setEasingCurve(QEasingCurve.OutCubic)
            anim.start()

            # Fade in
            w.setStyleSheet(w.styleSheet() + "opacity: 0;")
            QTimer.singleShot(200 + i*150, lambda ww=w: setattr(ww, "styleSheet", ww.styleSheet().replace("opacity: 0;", "opacity: 1;")))

    def try_login(self):
        # Simple demo animation on click
        anim = QPropertyAnimation(self.btn_login, b"geometry")
        anim.setDuration(180)
        r = self.btn_login.geometry()
        anim.setStartValue(r)
        anim.setEndValue(QRect(r.x(), r.y()-4, r.width(), r.height()+8))
        anim.setEasingCurve(QEasingCurve.OutQuad)
        anim.start()

        QMessageBox.information(self, "Success", "Login animation demo!\n\n(In real app - check credentials here)")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Modern dark style
    app.setStyle("Fusion")

    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(18, 18, 38))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(28, 28, 48))
    palette.setColor(QPalette.AlternateBase, QColor(35, 35, 55))
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(50, 45, 90))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.Highlight, QColor(123, 94, 255))
    app.setPalette(palette)

    window = LoginWindow()
    window.show()

    # Center window
    qr = window.frameGeometry()
    cp = app.primaryScreen().availableGeometry().center()
    qr.moveCenter(cp)
    window.move(qr.topLeft())

    sys.exit(app.exec())