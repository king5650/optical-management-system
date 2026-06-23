import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QProgressBar, QGraphicsDropShadowEffect
)
from PySide6.QtGui import QColor, QFont
from PySide6.QtCore import Qt, QTimer
from ui_ux.splash_screen.ui_splash_screen2 import Ui_MainWindow  
from modules.login_module.login import LoginApp


class MainAppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Application Window")
        self.setGeometry(100, 100, 600, 400)
        label = QLabel("Welcome to the Main Application", self)
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("Arial", 14))
        self.setCentralWidget(label)



class SplashScreen(QMainWindow):
    def __init__(self):
        super(SplashScreen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(2, 127, 196, 150))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        # Progress Bar
        # === ProgressBar ===
        self.progress = QProgressBar(self.ui.centralwidget)
        self.progress.setGeometry(10, 350, 380, 20)  # Adjust x, y, width, height
        self.progress.setValue(0)
        self.progress.setStyleSheet("""
            QProgressBar {
                border: 2px solid #007ACC;
                border-radius: 10px;
                text-align: center;
                background-color: #EEE;
            }
            QProgressBar::chunk {
                background-color: #027fc4;
                border-radius: 10px;
            }
        """)

        
        self.loading_label = QLabel("Please wait", self.ui.centralwidget)
        self.loading_label.setGeometry(180, 260, 200, 30)
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_label.setFont(QFont("Arial", 12, QFont.Bold))
        self.dot_count = 0

        self.progress_value = 0
        self.progress_timer = QTimer()
        self.progress_timer.timeout.connect(self.update_progress)
        self.progress_timer.start(50)

        self.dot_timer = QTimer()
        self.dot_timer.timeout.connect(self.animate_dots)
        self.dot_timer.start(500)

        self.main_app_window = None  # Placeholder for main app window

        self.show()

    def update_progress(self):
        if self.progress_value >= 100:
            self.progress_timer.stop()
            self.dot_timer.stop()
            self.loading_label.setText("Loading Complete!")

            # Open main app window after short delay
            QTimer.singleShot(500, self.open_main_window)
        else:
            self.progress_value += 1
            self.progress.setValue(self.progress_value)

    def animate_dots(self):
        self.dot_count = (self.dot_count + 1) % 4
        self.loading_label.setText("Please wait" + "." * self.dot_count)

    def open_main_window(self):
        self.main_app_window = LoginApp()
        self.main_app_window.show()
        self.close()


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    splash = SplashScreen()
    sys.exit(app.exec())




#hello chat 
#i want you to woron my ui-ux design made with pyside6 to provide a more professional ui-ux. i have attached the screenshot of my ui-ux. check it and code a new one or adjust and suggest improvements 