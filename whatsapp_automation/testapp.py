import sys
import asyncio
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QMessageBox
)
from PySide6.QtCore import QThread, Signal, QObject
from playwright.async_api import async_playwright
from datetime import datetime

WHATSAPP_WEB = "https://web.whatsapp.com/"
CHECK_STRING = "STRING TO SEARCH"

def name_formatter(name_and_surname):
    try:
        # name = name_and_surname.split()[0]
        # return name.replace("_", " ").lower().title()
        name = name_and_surname
        return name   
    except IndexError:
        return name_and_surname

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

### Thread worker for Playwright ###
class Worker(QObject):
    finished = Signal()
    log_signal = Signal(str)

    def __init__(self, name, number, message):
        super().__init__()
        self.name = name
        self.number = number
        self.message = message

    async def run_playwright(self):
        async with async_playwright() as p:
            browser = await p.chromium.launch_persistent_context(
                user_data_dir="/home/dario/.config/google-chrome",  # Change for your OS
                headless=False
            )
            page = await browser.new_page()
            await page.goto(WHATSAPP_WEB)

            self.log_signal.emit("Waiting for QR code scan...")
            await page.wait_for_selector('//div[@contenteditable="true"][@data-tab="3"]', timeout=60000)
            self.log_signal.emit("QR code scanned. Ready to send message.")

            await self.send_message(page, self.number, self.message, self.name, self.name)

            await browser.close()
            self.finished.emit()

    # async def send_message(self, page, number, message, name, full_name):
    #     try:
    #         search_box = page.locator('//div[@contenteditable="true"][@data-tab="3"]')
    #         await search_box.click()
    #         await search_box.fill("")
    #         await search_box.fill(number)
    #         await asyncio.sleep(2)
 
    #         no_results = page.locator('text=No results found')
    #         if await no_results.count() > 0:
    #             self.log_signal.emit(f"No WhatsApp account found for {full_name} ({number})")
    #             return

    #         await search_box.fill(name)
    #         contact = page.locator(f'//span[@title="{name}"]')
    #         # contact = page.locator(f'//span[@title="{number }"]')
    #         await contact.wait_for(timeout=10000)
    #         await contact.click()

    #         await page.wait_for_selector('//div[@contenteditable="true"][@data-tab="10"]', timeout=15000)
    #         await asyncio.sleep(2)

    #         if await page.get_by_text(CHECK_STRING).count() > 0:
    #             self.log_signal.emit(f"{name} already received the message.")
    #             return

    #         message_box = page.locator('//div[@contenteditable="true"][@data-tab="10"]')
    #         await message_box.click()
    #         await message_box.fill(message)
    #         await message_box.press("Enter")
    #         await asyncio.sleep(1)

    #         last_msg = page.locator('.message-out').last
    #         if await last_msg.count() > 0:
    #             last_msg_text = await last_msg.inner_text()
    #             if message in last_msg_text:
    #                 self.log_signal.emit(f"Successfully sent message to {full_name}.")
    #                 return

    #         self.log_signal.emit(f"Message may not have sent to {full_name}")

    #     except Exception as e:
    #         self.log_signal.emit(f"Error sending to {full_name}: {str(e)}")

    async def send_message(self, page, number, message, name, full_name):
        try:
            search_box = page.locator('//div[@contenteditable="true"][@data-tab="3"]')
            await search_box.click()
            await search_box.fill("")
            await search_box.fill(number if number else name)
            await asyncio.sleep(3)

            # Check if there are no results
            no_results = page.locator('text="No results found"')
            if await no_results.count() > 0:
                self.log_signal.emit(f"No WhatsApp contact found for {full_name} ({number})")
                return

            # Try finding the contact by number first
            contact_locator = page.locator(f'//span[@title="{number}"]')
            if await contact_locator.count() == 0:
                # If not found, fall back to name
                contact_locator = page.locator(f'//span[@title="{name}"]')

            if await contact_locator.count() == 0:
                self.log_signal.emit(f"Could not find contact '{full_name}' in search results.")
                return

            await contact_locator.first.click()
            await page.wait_for_selector('//div[@contenteditable="true"][@data-tab="10"]', timeout=15000)
            await asyncio.sleep(5)

            # Optional: Check if the message has already been sent
            if await page.get_by_text(CHECK_STRING).count() > 0:
                self.log_signal.emit(f"{full_name} already received the message.")
                return

            message_box = page.locator('//div[@contenteditable="true"][@data-tab="10"]')
            await message_box.click()
            await message_box.fill(message)
            await message_box.press("Enter")
            await asyncio.sleep(1)

            last_msg = page.locator('.message-out').last
            if await last_msg.count() > 0:
                last_msg_text = await last_msg.inner_text()
                if message in last_msg_text:
                    self.log_signal.emit(f"Successfully sent message to {full_name}.")
                    return

            self.log_signal.emit(f"Message may not have sent to {full_name}.")

        except Exception as e:
            self.log_signal.emit(f"Error sending to {full_name}: {str(e)}")



    def run(self):
        asyncio.run(self.run_playwright())

### PySide6 UI ###
class WhatsAppUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WhatsApp Automation")
        self.setFixedSize(400, 300)

        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter Name")
        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.name_input)

        self.number_input = QLineEdit()
        self.number_input.setPlaceholderText("Enter Number")
        layout.addWidget(QLabel("Number:"))
        layout.addWidget(self.number_input)

        self.message_box = QTextEdit()
        self.message_box.setPlaceholderText("Enter your message here")
        layout.addWidget(QLabel("Message:"))
        layout.addWidget(self.message_box)

        self.send_button = QPushButton("Send WhatsApp Message")
        self.send_button.clicked.connect(self.send_message)
        layout.addWidget(self.send_button)

        self.log_box = QTextEdit()
        self.log_box.setReadOnly(True)
        layout.addWidget(QLabel("Log:"))
        layout.addWidget(self.log_box)

        self.setLayout(layout)

    def send_message(self):
        name = name_formatter(self.name_input.text())
        number = self.number_input.text().strip()
        custom_message = self.message_box.toPlainText().strip()

        # if not number:
        #     QMessageBox.warning(self, "Input Error", "Please enter a phone number.")
        #     return

        # if not custom_message:
        #     QMessageBox.warning(self, "Input Error", "Please enter a message to send.")
        #     return

        self.thread = QThread()
        self.worker = Worker(name, number, custom_message)
        self.worker.moveToThread(self.thread)

        self.worker.log_signal.connect(self.append_log)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.started.connect(self.worker.run)
        self.thread.start()

        self.send_button.setEnabled(False)
        self.thread.finished.connect(lambda: self.send_button.setEnabled(True))

    def append_log(self, text):
        self.log_box.append(f"{text}")

### App Launch ###
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WhatsAppUI()
    window.show()
    sys.exit(app.exec())


# import sys
# import asyncio
# from PySide6.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QMessageBox, QDateTimeEdit
# )
# from PySide6.QtCore import QThread, Signal, QObject, QDateTime
# from playwright.async_api import async_playwright
# from datetime import datetime

# WHATSAPP_WEB = "https://web.whatsapp.com/"
# CHECK_STRING = "STRING TO SEARCH"

# def name_formatter(name_and_surname):
#     try:
#         name = name_and_surname
#         return name   
#     except IndexError:
#         return name_and_surname

# def log(message):
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     print(f"[{timestamp}] {message}")

# ### Thread worker for Playwright ###
# class Worker(QObject):
#     finished = Signal()
#     log_signal = Signal(str)

#     def __init__(self, name, number, message, send_time):  # ⬅️ Added `send_time`
#         super().__init__()
#         self.name = name
#         self.number = number
#         self.message = message
#         self.send_time = send_time

#     async def wait_until(self, scheduled_time):
#         """Wait until the scheduled time (non-blocking)."""
#         now = datetime.now()
#         delay = (scheduled_time - now).total_seconds()
#         if delay > 0:
#             self.log_signal.emit(f"Waiting until {scheduled_time.strftime('%Y-%m-%d %H:%M:%S')} to send message...")
#             await asyncio.sleep(delay)
#         else:
#             self.log_signal.emit("Scheduled time is in the past. Sending immediately.")

#     async def run_playwright(self):
#         async with async_playwright() as p:
#             browser = await p.chromium.launch_persistent_context(
#                 user_data_dir="/home/dario/.config/google-chrome",  # Change for your OS
#                 headless=False
#             )
#             page = await browser.new_page()
#             await page.goto(WHATSAPP_WEB)

#             self.log_signal.emit("Waiting for QR code scan...")
#             await page.wait_for_selector('//div[@contenteditable="true"][@data-tab="3"]', timeout=60000)
#             self.log_signal.emit("QR code scanned. Ready to send message.")

#             await self.wait_until(self.send_time)  # ⬅️ Wait for scheduled time

#             await self.send_message(page, self.number, self.message, self.name, self.name)

#             await browser.close()
#             self.finished.emit()

#     async def send_message(self, page, number, message, name, full_name):
#         try:
#             search_box = page.locator('//div[@contenteditable="true"][@data-tab="3"]')
#             await search_box.click()
#             await search_box.fill("")
#             await search_box.fill(number if number else name)
#             await asyncio.sleep(3)

#             no_results = page.locator('text="No results found"')
#             if await no_results.count() > 0:
#                 self.log_signal.emit(f"No WhatsApp contact found for {full_name} ({number})")
#                 return

#             contact_locator = page.locator(f'//span[@title="{number}"]')
#             if await contact_locator.count() == 0:
#                 contact_locator = page.locator(f'//span[@title="{name}"]')

#             if await contact_locator.count() == 0:
#                 self.log_signal.emit(f"Could not find contact '{full_name}' in search results.")
#                 return

#             await contact_locator.first.click()
#             await page.wait_for_selector('//div[@contenteditable="true"][@data-tab="10"]', timeout=15000)
#             await asyncio.sleep(2)

#             if await page.get_by_text(CHECK_STRING).count() > 0:
#                 self.log_signal.emit(f"{full_name} already received the message.")
#                 return

#             message_box = page.locator('//div[@contenteditable="true"][@data-tab="10"]')
#             await message_box.click()
#             await message_box.fill(message)
#             await message_box.press("Enter")
#             await asyncio.sleep(1)

#             last_msg = page.locator('.message-out').last
#             if await last_msg.count() > 0:
#                 last_msg_text = await last_msg.inner_text()
#                 if message in last_msg_text:
#                     self.log_signal.emit(f"Successfully sent message to {full_name}.")
#                     return

#             self.log_signal.emit(f"Message may not have sent to {full_name}.")

#         except Exception as e:
#             self.log_signal.emit(f"Error sending to {full_name}: {str(e)}")

#     def run(self):
#         asyncio.run(self.run_playwright())

# ### PySide6 UI ###
# class WhatsAppUI(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("WhatsApp Automation")
#         self.setFixedSize(400, 400)  # ⬅️ Increased height

#         layout = QVBoxLayout()

#         self.name_input = QLineEdit()
#         self.name_input.setPlaceholderText("Enter Name")
#         layout.addWidget(QLabel("Name:"))
#         layout.addWidget(self.name_input)

#         self.number_input = QLineEdit()
#         self.number_input.setPlaceholderText("Enter Number")
#         layout.addWidget(QLabel("Number:"))
#         layout.addWidget(self.number_input)

#         self.message_box = QTextEdit()
#         self.message_box.setPlaceholderText("Enter your message here")
#         layout.addWidget(QLabel("Message:"))
#         layout.addWidget(self.message_box)

#         # ⬇️ QDateTimeEdit for scheduling
#         self.datetime_picker = QDateTimeEdit()
#         self.datetime_picker.setCalendarPopup(True)
#         self.datetime_picker.setDateTime(QDateTime.currentDateTime())
#         self.datetime_picker.setMinimumDateTime(QDateTime.currentDateTime())
#         layout.addWidget(QLabel("Schedule Time:"))
#         layout.addWidget(self.datetime_picker)

#         self.send_button = QPushButton("Send WhatsApp Message")
#         self.send_button.clicked.connect(self.send_message)
#         layout.addWidget(self.send_button)

#         self.log_box = QTextEdit()
#         self.log_box.setReadOnly(True)
#         layout.addWidget(QLabel("Log:"))
#         layout.addWidget(self.log_box)

#         self.setLayout(layout)

#     def send_message(self):
#         name = name_formatter(self.name_input.text())
#         number = self.number_input.text().strip()
#         custom_message = self.message_box.toPlainText().strip()
#         send_time = self.datetime_picker.dateTime().toPython()  # ⬅️ Get as Python datetime

#         if not number and not name:
#             QMessageBox.warning(self, "Input Error", "Please enter a name or number.")
#             return

#         if not custom_message:
#             QMessageBox.warning(self, "Input Error", "Please enter a message.")
#             return

#         self.thread = QThread()
#         self.worker = Worker(name, number, custom_message, send_time)  # ⬅️ Pass send_time
#         self.worker.moveToThread(self.thread)

#         self.worker.log_signal.connect(self.append_log)
#         self.worker.finished.connect(self.thread.quit)
#         self.worker.finished.connect(self.worker.deleteLater)
#         self.thread.finished.connect(self.thread.deleteLater)

#         self.thread.started.connect(self.worker.run)
#         self.thread.start()

#         self.send_button.setEnabled(False)
#         self.thread.finished.connect(lambda: self.send_button.setEnabled(True))

#     def append_log(self, text):
#         self.log_box.append(f"{text}")

# ### App Launch ###
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = WhatsAppUI()
#     window.show()
#     sys.exit(app.exec())









# hello chat
# i am working on a whatsapp web automation system with python and playwrite. now this code i made automate the message well. but there is this thing the user enter the name of the contact and type in the message and click on send to automate. now i had this worry when the enter the just the number and automate with the message is lunch whatsapp web search for the contact finds the contact but doesn't click on the search result to send the message. whereas when the enter the name instead of the number it search and automate the message well. so wanted to know why this happens and how can it be resolved for it ti take both name and number.