
import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

class WhatsAppBot:
    def __init__(self):
        self.driver = self.init_whatsapp_driver()

    def init_whatsapp_driver(self):
        options = Options()

        # Set up Firefox profile directory (you may want to rename it appropriately)
        profile_dir = os.path.abspath("firefox_whatsapp_profile")
        options.profile = profile_dir

        # Optional: Launch maximized
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")

        # Path to geckodriver executable
        driver_path = r"C:\Users\falco\Desktop\system_optic\geckodriver-v0.36.0-win-aarch64_2\geckodriver.exe"
        service = Service(driver_path)

        # Launch Firefox with defined options
        driver = webdriver.Firefox(service=service, options=options)
        driver.get("https://web.whatsapp.com")

        # Show QR scan prompt (emit signal if using Qt framework)
        self.show_qr_prompt("Scan QR", "Please scan the QR code in the opened browser window.")
        time.sleep(15)
        return driver

    def show_qr_prompt(self, title, message):
        print(f"[{title}] {message}")  # Replace with QMessageBox if using PyQt or PySide

# Example usage
if __name__ == "__main__":
    bot = WhatsAppBot()