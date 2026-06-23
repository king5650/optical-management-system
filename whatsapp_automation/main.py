# main.py

import sys
from PySide6.QtWidgets import QApplication
from ui.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())






# page.goto("https://web.whatsapp.com", timeout=60000)

# try:
#     # Try to wait for the main chat screen (user already logged in)
#     page.wait_for_selector("div[role='textbox']", timeout=15000)
#     log_callback("✅ Already logged in to WhatsApp Web.")
# except:
#     # If not logged in, wait for the QR code
#     try:
#         log_callback("📷 Please scan the QR code to log in...")
#         page.wait_for_selector("canvas[aria-label='Scan me!']", timeout=60000)
#         log_callback("✅ QR Code scanned. Proceeding...")
#     except:
#         log_callback("❌ QR code not found, and not logged in. Aborting.")
#         return
