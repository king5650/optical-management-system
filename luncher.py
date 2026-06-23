import sys
from PySide6.QtWidgets import QApplication
from splash_screen import SplashScreen

def main():
    app = QApplication(sys.argv)

    # Show splash screen
    splash = SplashScreen()
    splash.show()

    # The SplashScreen class already handles opening the LoginApp window
    # No need to connect to a `finished` signal

    sys.exit(app.exec())

if __name__ == "__main__":
    main()