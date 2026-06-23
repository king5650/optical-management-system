import sys
import requests
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem,
    QHeaderView, QCheckBox, QWidget, QHBoxLayout, QTableWidget, QProgressBar
)
from PySide6.QtCore import Qt, QRect, QSize
# from PySide6.QtGui import QMouseEvent, QPainter, QStyleOptionButton, QStyle
# from ui_whatsapp_automate3 import Ui_MainWindowz
from ui_whatsapp_automate7 import Ui_MainWindow
from PySide6.QtGui import QMouseEvent, QPainter
from PySide6.QtWidgets import QStyleOptionButton, QStyle
from PySide6.QtGui import QColor, QBrush
from enum import Enum
from PySide6.QtWidgets import QMessageBox
# from PySide6.QtGui import QStringListModel
from PySide6.QtCore import QStringListModel
from datetime import datetime
from PySide6.QtWidgets import QInputDialog
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QInputDialog, QMessageBox
from PySide6.QtCore import QTimer, QDateTime
from datetime import datetime
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import QThread, Signal, QObject
from PySide6.QtWidgets import QComboBox, QLabel, QLineEdit
from concurrent.futures import ThreadPoolExecutor
import json
from PySide6.QtCore import QObject, Signal, QThread
from PySide6.QtWidgets import QProgressBar, QLabel
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options


class MessageMode(Enum):
    PERSONAL = 1
    GROUP = 2

BASE_URL = "http://127.0.0.1:8000/auth"

class CheckBoxHeader(QHeaderView):
    def __init__(self, orientation, controller, parent=None):
        super().__init__(orientation, parent)
        self.controller = controller
        self.check_box_state = Qt.Unchecked
        self.setSectionsClickable(True)



    def paintSection(self, painter, rect, logicalIndex):
        super().paintSection(painter, rect, logicalIndex)
        if logicalIndex == 0:
            option = QStyleOptionButton()
            option.rect = QRect(rect.left() + 4, rect.top() + 4, 20, 20)
            option.state = QStyle.State_Enabled | (
                QStyle.State_On if self.check_box_state == Qt.Checked else QStyle.State_Off
            )
            self.style().drawControl(QStyle.CE_CheckBox, option, painter)

    def mousePressEvent(self, event: QMouseEvent):
        index = self.logicalIndexAt(event.pos())
        if index == 0:
            self.check_box_state = Qt.Unchecked if self.check_box_state == Qt.Checked else Qt.Checked
            self.controller.toggle_all_checkboxes(self.check_box_state)
            self.viewport().update()
        else:
            super().mousePressEvent(event)            
            
class MessageSenderWorker(QObject):
    progress = Signal(int)  # emits progress percentage
    status = Signal(str)    # emits status text
    finished = Signal(bool) # emits when done (success/fail)
    show_qr_prompt = Signal(str, str)  # title, message

    def __init__(self, message, numbers, msg_type, group_name):
        super().__init__()
        self.message = message
        self.numbers = numbers
        self.msg_type = msg_type
        self.group_name = group_name
        

    def run(self):
        try:
            self.status.emit("Initializing WhatsApp Web...")
            self.progress.emit(10)

            driver = self.init_whatsapp_driver()
            self.progress.emit(40)

            if self.msg_type == "Personal":
                self.status.emit("Sending personal messages...")
                self.send_personal_messages(driver, self.numbers, self.message)
            else:
                self.status.emit("Sending to group...")
                self.send_group_message(driver, self.group_name, self.message)

            self.status.emit("Message sent successfully ✅")
            self.progress.emit(100)
            self.finished.emit(True)

        except Exception as e:
            self.status.emit(f"Failed: {e}")
            self.finished.emit(False)

    # def init_whatsapp_driver(self):
    #     options = Options()
        
    #     # Setup proper profile directory
    #     profile_dir = os.path.abspath("chrome_whatsapp_profile")
    #     options.add_argument(f"--user-data-dir={profile_dir}")

    #     # Optional stabilizing flags
    #     options.add_argument("--disable-dev-shm-usage")
    #     options.add_argument("--no-sandbox")
    #     options.add_argument("--remote-debugging-port=9222")

    #     # Optional: start maximized
    #     options.add_argument("--start-maximized")

    #     # Point to chromedriver
    #     driver_path = r"C:\Users\falco\Desktop\system_optic\chromedriver-win64\chromedriver-win64\chromedriver.exe"  # Change this to your real path r"C:\Users\falco\Desktop\system_optic\chromedriver-win64\chromedriver-win64\chromedriver.exe" 
    #     service = Service(driver_path)

    #     driver = webdriver.Chrome(service=service, options=options)
    #     driver.get("https://web.whatsapp.com")

    #     # QMessageBox.information(self, "Scan QR", "Please scan the QR code in the opened browser window.")
    #     self.show_qr_prompt.emit("Scan QR", "Please scan the QR code in the opened browser window.")
    #     time.sleep(15)
    #     return driver            

# def init_whatsapp_driver(self):
#     options = Options()

#     # ✅ Setup persistent Chrome user profile
#     profile_dir = os.path.abspath("chrome_whatsapp_profile")
#     options.add_argument(f"--user-data-dir={profile_dir}")

#     # ✅ Stability and debugging flags
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--start-maximized")
#     options.add_argument("--remote-debugging-port=9222")

#     try:
#         # ⚡ Prefer automatic driver setup
#         from webdriver_manager.chrome import ChromeDriverManager
#         from selenium.webdriver.chrome.service import Service as ChromeService
#         service = ChromeService(ChromeDriverManager().install())
#     except Exception as e:
#         # 🔧 Fallback to manual path if auto fails
#         driver_path = r"C:\Users\falco\Desktop\system_optic\chromedriver-win64\chromedriver-win64\chromedriver.exe"
#         from selenium.webdriver.chrome.service import Service
#         service = Service(driver_path)

#     # 🚀 Launch Chrome with configured options
#     driver = webdriver.Chrome(service=service, options=options)
#     driver.get("https://web.whatsapp.com")

#     # 🛂 Prompt user to scan the QR code
#     self.show_qr_prompt.emit("Scan QR", "Please scan the QR code in the opened browser window.")
#     time.sleep(15)

#     return driver

    def init_whatsapp_driver(self):
        options = Options()

        # Custom Chrome user profile to keep sessions
        profile_dir = os.path.abspath("chrome_whatsapp_profiles")
        options.add_argument(f"--user-data-dir={profile_dir}")

        # Optional flags to stabilize headless automation
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--start-maximized")

        # 🧠 Automatically download and manage correct driver
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        # Open WhatsApp Web
        driver.get("https://web.whatsapp.com")

        # Prompt user to scan QR code if needed
        self.show_qr_prompt.emit("Scan QR", "Please scan the QR code in the opened browser window.")
        time.sleep(15)

        return driver



            
    # def send_personal_messages(self, driver, contacts, message):
    #     for number in contacts:
    #         url = f"https://web.whatsapp.com/send?phone={number}&text={message}"
    #         driver.get(url)
    #         time.sleep(10)

    #         try:
    #             send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
    #             send_button.click()
    #             time.sleep(2)
    #         except Exception as e:
    #             print(f"Failed to send to {number}: {e}")




    def send_personal_messages(self, driver, contacts, message):
        for number in contacts:
            url = f"https://web.whatsapp.com/send?phone={number}&text={message}"
            driver.get(url)
            time.sleep(10)  # wait for the chat to load

            try:
                # Ensure the input box is focused, then press ENTER to send
                input_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
                time.sleep(2)
                input_box.send_keys(Keys.ENTER)
                time.sleep(2)

            except Exception as e:
                print(f"❌ Failed to send to {number}: {e}")


    def send_group_message(self, driver, group_name, message):
        search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
        driver.find_element(By.XPATH, search_xpath).send_keys(group_name)
        time.sleep(2)
        driver.find_element(By.XPATH, f'//span[@title="{group_name}"]').click()
        time.sleep(2)

        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        time.sleep(2)
                    

GROUPS_FILE = "whatsapp_groups.json"

class MessageAutomationsystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        
        
        # layout = QVBoxLayout()list_message_sent
        # layout.addWidget(self.progressBar)
        # layout.addWidget(self.statusLabel)
        # self.centralwidget.setLayout(layout)

        # self.progressBar = QProgressBar(self.centralwidget)
        # self.progressBar.setGeometry(QRect(50, 600, 400, 25))
        # self.progressBar.setValue(0)
        # self.statusLabel = QLabel("Status: Waiting", self.centralwidget)
        # self.statusLabel.setGeometry(QRect(40, 170, 780, 130))
                
                        
     # Replace header with custom checkbox header
        header = CheckBoxHeader(Qt.Horizontal, controller=self)
        self.tableWidget.setHorizontalHeader(header)
        self.tableWidget.setSelectionBehavior(self.tableWidget.SelectionBehavior.SelectRows)
        self.tableWidget.setSortingEnabled(True)
        self.search_bar.textChanged.connect(self.filter_table)
        
        self.message_model = QStringListModel()
        self.sent_messages = []  # Keep track of all sent messages
        self.scheduled_tasks = []
        self.list_message_sent.setModel(self.message_model)

        self.send_message.clicked.connect(self.handle_send_message)
                
        # --- Initialize message model and connect to QListView ---
        self.message_model = QStandardItemModel(self)
        self.list_message_sent.setModel(self.message_model)

        # Optional: handle double-clicks (will be used later for Edit/Cancel)
        self.list_message_sent.doubleClicked.connect(self.handle_message_double_click)

        self.add_message_to_list("Hello John!", "sent")
        self.add_message_to_list("Follow-up message", "scheduled", datetime(2025, 5, 20, 10, 0))

        self.setCurrentDate()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.setCurrentDate)
        self.timer.start(60000)
                
        # Add in your setupUi(self) or __init__ section:
        self.group_name_input.setPlaceholderText("Enter WhatsApp Group Name")
        self.group_dropdown.addItem("-- Select Previous Group --")

        self.group_dropdown.currentTextChanged.connect(self.group_name_input.setText)
        self.executor = ThreadPoolExecutor(max_workers=2)


        # self.send_message.clicked.connect(self.print_selected_rows)
        # self.send_message.clicked.connect(self.send_messages) 
        
        # Track previously used group names
        self.group_names = []

        # Load saved group names into the dropdown
        self.load_group_names()

        # When user selects from dropdown, autofill input
        self.group_dropdown.currentTextChanged.connect(self.on_group_selected)

      
    def on_group_selected(self, text):
        if text != "-- Select Previous Group --":
            self.group_name_input.setText(text)

    def save_group_name(self, group_name_input):
        if group_name_input and group_name_input not in self.group_names:
            self.group_names.append(group_name_input)
            self.group_dropdown.addItem(group_name_input)
            try:
                with open(GROUPS_FILE, "w") as f:
                    json.dump(self.group_names, f)
            except Exception as e:
                print("Failed to save group name:", e)


    def display_info_box(self, title, message):
        QMessageBox.information(self, title, message)

    def load_group_names(self):
        if os.path.exists(GROUPS_FILE):
            try:
                with open(GROUPS_FILE, "r") as f:
                    self.group_names = json.load(f)
                    for name in self.group_names:
                        self.group_dropdown.addItem(name)
            except Exception as e:
                print("Failed to load group names:", e)                     

    def print_selected_rows(self):
        rows = self.get_selected_rows()
        print("Selected patients:")
        for row in rows:
            print(row)

    def handle_send_message(self):
        message = self.message_box.toPlainText().strip()
        if not message:
            QMessageBox.warning(self, "Empty Message", "Please type a message to send.")
            return

        msg_type = self.get_message_type()
        if not msg_type:
            return

        numbers = self.get_selected_numbers()
        if not numbers and msg_type == "Personal":
            QMessageBox.warning(self, "No Selection", "Select at least one contact.")
            return

        group_name = self.group_name_input.text().strip()
        scheduled_datetime = self.dateTimeEdit.dateTime().toPython()

        if scheduled_datetime > datetime.now():
            self.schedule_message(message, numbers, msg_type, scheduled_datetime, group_name)
            self.add_message_to_list(message, "scheduled", scheduled_datetime,)
        else:
            self.run_sending_thread(message, numbers, msg_type, group_name)
            self.add_message_to_list(message, "sent")

        self.message_box.clear()

    # def run_sending_thread(self, message, numbers, msg_type, group_name):
    #     self.progressBar.setValue(0)
    #     self.statusLabel.setText("Status: Starting...")

    #     if msg_type == "Group" and group_name and group_name not in self.group_names:
    #         self.save_group_name(group_name)

    #     self.thread = QThread()
    #     self.worker = MessageSenderWorker(message, numbers, msg_type, group_name)
    #     self.worker.moveToThread(self.thread)

    #     self.worker.progress.connect(self.progressBar.setValue)
    #     self.worker.status.connect(self.statusLabel.setText)
    #     self.worker.finished.connect(self.on_sending_finished)

    #     self.thread.started.connect(self.worker.run)
    #     self.worker.finished.connect(self.thread.quit)
    #     self.worker.finished.connect(self.worker.deleteLater)
    #     self.thread.finished.connect(self.thread.deleteLater)

    #     self.thread.start()
    
    def run_sending_thread(self, message, numbers, msg_type, group_name):
        self.progressBar.setValue(0)
        self.statusLabel.setText("Status: Starting...")

        if msg_type == "Group" and group_name and group_name not in self.group_names:
            self.save_group_name(group_name)

        self.thread = QThread()
        self.worker = MessageSenderWorker(message, numbers, msg_type, group_name)
        self.worker.moveToThread(self.thread)

        self.worker.progress.connect(self.progressBar.setValue)
        self.worker.status.connect(self.statusLabel.setText)
        self.worker.finished.connect(self.on_sending_finished)

        # 📌 Connect the signal to show QR scan info in the main thread
        self.worker.show_qr_prompt.connect(self.display_info_box)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()


    def on_sending_finished(self, success):
        if success:
            QMessageBox.information(self, "Success", "Message sent successfully.")
        else:
            QMessageBox.critical(self, "Error", "Message sending failed.")
        self.statusLabel.setText("Status: Done")

    def schedule_message(self, message, numbers, msg_type, when, group_name):
        now_qt = QDateTime.currentDateTime()
        when_qt = QDateTime(when)
        delay = now_qt.msecsTo(when_qt)

        def send_scheduled():
            self.run_sending_thread(message, numbers, msg_type, group_name)
            self.add_message_to_list(message, "sent")

        timer = QTimer(self)
        timer.setSingleShot(True)
        timer.timeout.connect(send_scheduled)
        timer.start(delay)
        self.scheduled_tasks.append(timer)

    # def add_message_to_list(self, message_text, status="sent", scheduled_time=None):
    #     from PySide6.QtGui import QStandardItem
    #     display_text = ""
    #     if status == "sent":
    #         display_text = f"Sent at {datetime.now().strftime('%Y-%m-%d %H:%M')} - ✅ {message_text} "
    #     elif status == "scheduled":
    #         display_text = f"Scheduled for {scheduled_time.strftime('%Y-%m-%d %H:%M')} - ⏳ {message_text}"

    #     item = QStandardItem(display_text)
    #     item.setEditable(False)
    #     item.setData({
    #         "status": status,
    #         "message": message_text,
    #         "scheduled_time": scheduled_time
    #     }, Qt.UserRole)
    #     self.message_model.appendRow(item)                    
    def add_message_to_list(self, message_text, status="sent", scheduled_time=None, sender=None, receiver=None):
        from PySide6.QtGui import QStandardItem
        display_text = ""
        if status == "sent":
            display_text = (
                f"Sent at {datetime.now().strftime('%Y-%m-%d %H:%M')} - ✅ {message_text}\n"
                f"From: {sender or 'Me'} To: {receiver or ''}"
            )
        elif status == "scheduled":
            display_text = (
                f"Scheduled for {scheduled_time.strftime('%Y-%m-%d %H:%M')} - ⏳ {message_text}\n"
                f"From: {sender or 'Me'} To: {receiver or ''}"
            )

        item = QStandardItem(display_text)
        item.setEditable(False)
        item.setData({
            "status": status,
            "message": message_text,
            "scheduled_time": scheduled_time,
            "sender": sender,
            "receiver": receiver
        }, Qt.UserRole)
        self.message_model.appendRow(item)


    def setCurrentDate(self):
        """Sets the dateTimeEdit widget to the current date and time."""
        current_datetime = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(current_datetime)                

    def handle_message_double_click(self, index):
        item = self.message_model.itemFromIndex(index)
        data = item.data(Qt.UserRole)

        if data and data.get("status") == "scheduled":
            choice = QMessageBox.question(
                self,
                "Scheduled Message",
                "This message is scheduled.\n\nWhat do you want to do?.\n Yes - Edit\nNo - Cancel",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel,
                QMessageBox.StandardButton.Cancel
            )

            # Interpret choices: Yes = Edit, No = Cancel
            if choice == QMessageBox.StandardButton.Yes:
                # EDIT message content
                new_text, ok = QInputDialog.getText(self, "Edit Message", "Modify the message:", text=data["message"])
                if ok and new_text:
                    data["message"] = new_text
                    # Update display text
                    display_text = f"Scheduled for {data['scheduled_time'].strftime('%Y-%m-%d %H:%M')} - ⏳ {new_text}"
                    item.setText(display_text)
                    item.setData(data, Qt.UserRole)

            elif choice == QMessageBox.StandardButton.No:
                confirm = QMessageBox.question(
                    self, "Cancel Message", "Are you sure you want to cancel this scheduled message?",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                )
                if confirm == QMessageBox.StandardButton.Yes:
                    self.message_model.removeRow(item.row())


    def send_messages(self):
        rows = self.get_selected_rows()
        print("Selected patients:")
        for row in rows:
            print(row)
        mode = self.ask_message_mode()
        if mode == MessageMode.PERSONAL:
            self.send_personal_messages()
        elif mode == MessageMode.GROUP:
            self.send_group_message()



    def ask_message_mode(self):
        reply = QMessageBox.question(
            self,
            "Choose Message Type",
            "Send message to:\n\nYes - Personal (each recipient individually)\nNo - Group (WhatsApp group)",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            return MessageMode.PERSONAL
        else:
            return MessageMode.GROUP

    def filter_table(self, text):
        for row in range(self.tableWidget.rowCount()):
            match = False
            for col in range(1, self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item and text.lower() in item.text().lower():
                    match = True
                    break
            self.tableWidget.setRowHidden(row, not match)

    def load_patients(self):
        try:
            response = requests.get(f"{BASE_URL}/patients/list/")
            if response.status_code == 200:
                self.update_table(response.json()['patients'])
            else:
                QMessageBox.warning(self, "Error", "Failed to load patients.")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")

    def get_value(self, val):
        return str(val) if val not in (None, '', 'null') else 'N/A'

    def update_table(self, patients):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for patient in patients:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)

            # Add checkbox in column 0
            checkbox = QCheckBox()
            checkbox.setCheckState(Qt.Unchecked)
            # checkbox.stateChanged.connect(lambda state, r=row: self.on_checkbox_changed(state, r))
            checkbox.stateChanged.connect(lambda state, chk=checkbox: self.on_checkbox_changed(state, chk))


            # checkbox.setStyleSheet("margin-left:50%; margin-right:50%;")
            checkbox.setStyleSheet("""
                QCheckBox::indicator {
                    width: 20px;
                    height: 20px;
                    border: 2px solid black; /* Blue border */
                    border-radius: 10px; /* Half of width/height for perfect circle */
                    background-color: white;
                }
                QCheckBox::indicator:checked {
                    background-color: #007BFF; /* Blue when checked */
                }
                QCheckBox::indicator:unchecked:hover {
                    border: 2px solid #55aaff;
                }
                QCheckBox::indicator:checked:hover {
                    background-color: #0056b3;
                }
                QCheckBox::indicator:checked {
                    image: url(tick.png); /* You'd provide a tick.png image */
                    /* If using a custom image, you might need to adjust padding or other properties */
                }
            """)            
            
            widget = QWidget()
            layout = QHBoxLayout(widget)
            layout.addWidget(checkbox)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            self.tableWidget.setCellWidget(row, 0, widget)
            # self.tableWidget.setCellWidget(row, 0, checkbox)
            self.tableWidget.setItem(row, 1, QTableWidgetItem(self.get_value(patient.get('id'))))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(self.get_value(patient.get('name'))))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(self.get_value(patient.get('email'))))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(self.get_value(patient.get('contact'))))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(self.get_value(patient.get('address'))))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(self.get_value(patient.get('profession'))))
            self.tableWidget.setItem(row, 7, QTableWidgetItem(self.get_value(patient.get('age'))))
            self.tableWidget.setItem(row, 8, QTableWidgetItem(self.get_value(patient.get('gender'))))

        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.sortItems(2, Qt.AscendingOrder)

    def toggle_all_checkboxes(self, state):
        for row in range(self.tableWidget.rowCount()):
            widget = self.tableWidget.cellWidget(row, 0)
            if widget:
                checkbox = widget.findChild(QCheckBox)
                if checkbox:
                    checkbox.setCheckState(state)

    # def on_checkbox_changed(self, state, row):
    #     # Highlight or clear highlight
    #     color = QColor("red") if state == Qt.Checked else QColor("black")
    
    #     for col in range(self.tableWidget.columnCount()):
    #         item = self.tableWidget.item(row, col)
    #         if item:
    #             item.setBackground(color)

                    
    # def on_checkbox_changed(self, state, checkbox: QCheckBox):
    #     parent_widget = checkbox.parentWidget()
    #     if parent_widget:
    #         found_row = -1
    #         for r in range(self.tableWidget.rowCount()):
    #             cell_widget = self.tableWidget.cellWidget(r, 0)
    #             if cell_widget is parent_widget:
    #                 found_row = r
    #                 break

    #         if found_row != -1:
    #             if state == Qt.Checked:
    #                 highlight_color = QColor(255, 0, 0)  # Red
    #             else:
    #                 highlight_color = QColor(255, 0, 255)  # White
                
    #             # Apply the color change using setBackground
    #             for col in range(self.tableWidget.columnCount()):
    #                 item = self.tableWidget.item(found_row, col)
    #                 if item:
    #                     item.setBackground(QBrush(highlight_color))  # Use QBrush to properly apply color
                    
    #             # Apply the same color to the checkbox's container (column 0)
    #             cell_widget = self.tableWidget.cellWidget(found_row, 0)
    #             if cell_widget:
    #                 cell_widget.setStyleSheet(f"background-color: {highlight_color.name()};")
    def on_checkbox_changed(self, state, checkbox: QCheckBox):
        parent_widget = checkbox.parentWidget()
        if not parent_widget:
            return

        found_row = -1
        for r in range(self.tableWidget.rowCount()):
            if self.tableWidget.cellWidget(r, 0) is parent_widget:
                found_row = r
                break

        if found_row == -1:
            return

        if state == Qt.Checked:
            highlight_brush = QBrush(QColor(255, 0, 0))  # Red
            checkbox_cell_style = "background-color: rgb(255, 0, 0);"
        else:
            highlight_brush = QBrush()  # No color = default
            checkbox_cell_style = ""   # Clear stylesheet to reset

        # Apply to each item in the row
        for col in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(found_row, col)
            if item:
                item.setBackground(highlight_brush)

        # Apply style to checkbox container (column 0 cell widget)
        checkbox_cell_widget = self.tableWidget.cellWidget(found_row, 0)
        if checkbox_cell_widget:
            checkbox_cell_widget.setStyleSheet(checkbox_cell_style)




    def get_selected_rows(self):
        selected = []
        for row in range(self.tableWidget.rowCount()):
            widget = self.tableWidget.cellWidget(row, 0)
            if widget:
                checkbox = widget.findChild(QCheckBox)
                if checkbox and checkbox.checkState() == Qt.Checked:
                    row_data = {
                        'id': self.tableWidget.item(row, 1).text(),
                        'name': self.tableWidget.item(row, 2).text(),
                        'email': self.tableWidget.item(row, 3).text(),
                        'contact': self.tableWidget.item(row, 4).text()
                        # Add more fields as needed
                    }
                    selected.append(row_data)
        return selected

    def get_message_type(self):
        options = ["Personal", "Group"]
        msg_type, ok = QInputDialog.getItem(self, "Send Message", "Choose message type:", options, 0, False)
        return msg_type if ok else None

    # def init_whatsapp_driver(self):
    #     options = Options()
        
    #     # Setup proper profile directory
    #     profile_dir = os.path.abspath("chrome_whatsapp_profile")
    #     options.add_argument(f"--user-data-dir={profile_dir}")

    #     # Optional stabilizing flags
    #     options.add_argument("--disable-dev-shm-usage")
    #     options.add_argument("--no-sandbox")
    #     options.add_argument("--remote-debugging-port=9222")

    #     # Optional: start maximized
    #     options.add_argument("--start-maximized")

    #     # Point to chromedriver
    #     driver_path = r"c:\Users\falco\Desktop\system_optic\win32\chromedriver.exe"  # Change this to your real path
    #     service = Service(driver_path)

    #     driver = webdriver.Chrome(service=service, options=options)
    #     driver.get("https://web.whatsapp.com")

    #     QMessageBox.information(self, "Scan QR", "Please scan the QR code in the opened browser window.")
    #     time.sleep(15)
    #     return driver            


    def get_selected_numbers(self):
        numbers = []
        for row in range(self.tableWidget.rowCount()):
            widget = self.tableWidget.cellWidget(row, 0)
            if widget:
                checkbox = widget.findChild(QCheckBox)
                if checkbox and checkbox.checkState() == Qt.Checked:
                    number_item = self.tableWidget.item(row, 4)  # Assuming column 4 is 'contact'
                    if number_item:
                        number = number_item.text()
                        if number and number != "N/A":
                            numbers.append(number)
        return numbers



if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    window = MessageAutomationsystem()
    window.load_patients()  # Load data at startup
    window.show()
    sys.exit(app.exec())











































# import sys
# import os
# import time
# import requests
# from datetime import datetime
# from PySide6.QtWidgets import (
#     QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QHeaderView,
#     QCheckBox, QHBoxLayout, QStyleOptionButton, QStyle, QLineEdit, QComboBox, QTextEdit
# )
# from PySide6.QtCore import Qt, QRect, QStringListModel, QTimer
# from PySide6.QtGui import QColor, QStandardItemModel, QStandardItem
# from PySide6.QtCore import QThreadPool, QRunnable, Slot
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

# # --------------------
# # Constants
# # --------------------
# BASE_URL = "http://127.0.0.1:8000/auth"
# CHROMEDRIVER_PATH = r"c:\Users\falco\Desktop\system_optic\win32\chromedriver.exe"


# class CheckBoxHeader(QHeaderView):
#     def __init__(self, orientation, controller, parent=None):
#         super().__init__(orientation, parent)
#         self.controller = controller
#         self.check_box_state = Qt.Unchecked
#         self.setSectionsClickable(True)

#     def paintSection(self, painter, rect, logicalIndex):
#         super().paintSection(painter, rect, logicalIndex)
#         if logicalIndex == 0:
#             option = QStyleOptionButton()
#             option.rect = QRect(rect.left() + 4, rect.top() + 4, 20, 20)
#             option.state = QStyle.State_Enabled | (
#                 QStyle.State_On if self.check_box_state == Qt.Checked else QStyle.State_Off
#             )
#             self.style().drawControl(QStyle.CE_CheckBox, option, painter)

#     def mousePressEvent(self, event):
#         index = self.logicalIndexAt(event.pos())
#         if index == 0:
#             self.check_box_state = Qt.Unchecked if self.check_box_state == Qt.Checked else Qt.Checked
#             self.controller.toggle_all_checkboxes(self.check_box_state)
#             self.viewport().update()
#         else:
#             super().mousePressEvent(event)


# class SendMessageWorker(QRunnable):
#     def __init__(self, mode, numbers, message, group_name=None, callback=None):
#         super().__init__()
#         self.mode = mode
#         self.numbers = numbers
#         self.message = message
#         self.group_name = group_name
#         self.callback = callback

#     @Slot()
#     def run(self):
#         try:
#             options = Options()
#             profile_dir = os.path.abspath("chrome_whatsapp_profile")
#             options.add_argument(f"--user-data-dir={profile_dir}")
#             options.add_argument("--start-maximized")

#             driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)
#             driver.get("https://web.whatsapp.com")
#             time.sleep(15)

#             if self.mode == "Personal":
#                 for number in self.numbers:
#                     url = f"https://web.whatsapp.com/send?phone={number}&text={self.message}"
#                     driver.get(url)
#                     time.sleep(10)
#                     send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
#                     send_button.click()
#                     time.sleep(2)
#             else:
#                 search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
#                 driver.find_element(By.XPATH, search_xpath).send_keys(self.group_name)
#                 time.sleep(2)
#                 driver.find_element(By.XPATH, f'//span[@title="{self.group_name}"]').click()
#                 time.sleep(2)

#                 msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
#                 msg_box.send_keys(self.message)
#                 msg_box.send_keys(Keys.ENTER)
#                 time.sleep(2)

#             if self.callback:
#                 self.callback(success=True)
#         except Exception as e:
#             print(f"Send error: {e}")
#             if self.callback:
#                 self.callback(success=False)


# class WhatsAppAutomationSystem(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("WhatsApp Automation System")
#         self.setGeometry(100, 100, 1200, 700)

#         self.thread_pool = QThreadPool()

#         # Widgets
#         self.message_box = QTextEdit(self)
#         self.message_box.setGeometry(30, 20, 800, 80)

#         self.group_name_input = QLineEdit(self)
#         self.group_name_input.setGeometry(850, 20, 200, 30)
#         self.group_name_input.setPlaceholderText("Enter group name")

#         self.group_dropdown = QComboBox(self)
#         self.group_dropdown.setGeometry(850, 60, 200, 30)
#         self.group_dropdown.setEditable(False)
#         self.saved_groups = set()

#         from PySide6.QtWidgets import QPushButton, QListView, QTableWidget
#         self.send_button = QPushButton("Send", self)
#         self.send_button.setGeometry(1070, 20, 80, 70)
#         self.send_button.clicked.connect(self.handle_send)

#         self.list_message_sent = QListView(self)
#         self.list_message_sent.setGeometry(30, 110, 1120, 150)
#         self.message_model = QStringListModel()
#         self.list_message_sent.setModel(self.message_model)
#         self.sent_messages = []

#         from PySide6.QtWidgets import QTableWidget
#         self.tableWidget = QTableWidget(self)
#         self.tableWidget.setGeometry(30, 280, 1120, 400)
#         self.tableWidget.setColumnCount(6)
#         self.tableWidget.setHorizontalHeaderLabels(["", "ID", "Name", "Email", "Contact", "Gender"])

#         self.tableWidget.setHorizontalHeader(CheckBoxHeader(Qt.Horizontal, controller=self))
#         self.load_patients()

#     def load_patients(self):
#         try:
#             response = requests.get(f"{BASE_URL}/patients/list/")
#             if response.status_code == 200:
#                 self.update_table(response.json()['patients'])
#         except Exception as e:
#             print("Error loading patients:", e)

#     def update_table(self, patients):
#         self.tableWidget.setRowCount(0)
#         for patient in patients:
#             row = self.tableWidget.rowCount()
#             self.tableWidget.insertRow(row)

#             # Checkbox
#             checkbox = QCheckBox()
#             widget = QWidget()
#             layout = QHBoxLayout(widget)
#             layout.addWidget(checkbox)
#             layout.setAlignment(Qt.AlignCenter)
#             layout.setContentsMargins(0, 0, 0, 0)
#             self.tableWidget.setCellWidget(row, 0, widget)

#             self.tableWidget.setItem(row, 1, QTableWidgetItem(str(patient.get("id"))))
#             self.tableWidget.setItem(row, 2, QTableWidgetItem(str(patient.get("name"))))
#             self.tableWidget.setItem(row, 3, QTableWidgetItem(str(patient.get("email"))))
#             self.tableWidget.setItem(row, 4, QTableWidgetItem(str(patient.get("contact"))))
#             self.tableWidget.setItem(row, 5, QTableWidgetItem(str(patient.get("gender"))))

#     def toggle_all_checkboxes(self, state):
#         for row in range(self.tableWidget.rowCount()):
#             widget = self.tableWidget.cellWidget(row, 0)
#             if widget:
#                 checkbox = widget.findChild(QCheckBox)
#                 if checkbox:
#                     checkbox.setCheckState(state)

#     def get_selected_numbers(self):
#         numbers = []
#         for row in range(self.tableWidget.rowCount()):
#             widget = self.tableWidget.cellWidget(row, 0)
#             if widget:
#                 checkbox = widget.findChild(QCheckBox)
#                 if checkbox and checkbox.checkState() == Qt.Checked:
#                     number = self.tableWidget.item(row, 4).text()
#                     if number and number != "N/A":
#                         numbers.append(number)
#         return numbers

#     def handle_send(self):
#         message = self.message_box.toPlainText().strip()
#         if not message:
#             QMessageBox.warning(self, "Message Missing", "Please type a message.")
#             return

#         mode = QMessageBox.question(
#             self, "Send Mode",
#             "Send as personal or group message?\n\nYes - Personal\nNo - Group",
#             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
#         )
#         msg_type = "Personal" if mode == QMessageBox.StandardButton.Yes else "Group"

#         numbers = self.get_selected_numbers()

#         group_name = self.group_name_input.text().strip()
#         if msg_type == "Group":
#             if not group_name:
#                 QMessageBox.warning(self, "Group Name Missing", "Please enter the group name.")
#                 return
#             if group_name not in self.saved_groups:
#                 self.saved_groups.add(group_name)
#                 self.group_dropdown.addItem(group_name)

#         worker = SendMessageWorker(
#             msg_type,
#             numbers,
#             message,
#             group_name=group_name if msg_type == "Group" else None,
#             callback=self.message_sent_callback
#         )
#         self.thread_pool.start(worker)

#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         entry = f"[{timestamp}] ({msg_type}) {message}"
#         self.sent_messages.append(entry)
#         self.message_model.setStringList(self.sent_messages)
#         self.message_box.clear()

#     def message_sent_callback(self, success):
#         print("Message sent" if success else "Failed to send message.")


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = WhatsAppAutomationSystem()
#     window.show()
#     sys.exit(app.exec())
