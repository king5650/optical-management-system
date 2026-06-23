import sys
import requests
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem,
    QHeaderView, QCheckBox, QWidget, QHBoxLayout, QTableWidget
)
from PySide6.QtCore import Qt, QRect, QSize
# from PySide6.QtGui import QMouseEvent, QPainter, QStyleOptionButton, QStyle
from ui_whatsapp_automate3 import Ui_MainWindow
from PySide6.QtGui import QMouseEvent, QPainter
from PySide6.QtWidgets import QStyleOptionButton, QStyle
from PySide6.QtGui import QColor
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

GROUPS_FILE = "whatsapp_groups.json"

class MessageAutomationsystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Add after self.setupUi(self)
        # self.group_dropdown = QComboBox(self)
        # self.group_dropdown.setGeometry(500, 100, 200, 30)

        # self.group_name_input = QLineEdit(self.actionbuttons)
        # self.group_name_input.setGeometry(8, 174, 200, 30)
        # self.group_name_input.setPlaceholderText("Enter Group Name")
        
        
        
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

    # def handle_send_message(self):
    #     message = self.message_box.toPlainText().strip()

    #     if not message:
    #         QMessageBox.warning(self, "Empty Message", "Please type a message to send.")
    #         return

    #     # Append to list
    #     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     entry = f"[{timestamp}] {message}"
    #     self.sent_messages.append(entry)
    #     self.message_model.setStringList(self.sent_messages)

    #     # Clear the message box (optional)
    #     self.message_box.clear()

    #     # At this point you would trigger WhatsApp send logic
    #     # For example:
    #     self.send_messages()
    
    # def save_group_name(self, group_name):
    #     if group_name and group_name not in self.group_names:
    #         self.group_names.append(group_name)
    #         self.group_dropdown.addItem(group_name)
    #         try:
    #             with open(GROUPS_FILE, "w") as f:
    #                 json.dump(self.group_names, f)
    #         except Exception as e:
    #             print("Failed to save group name:", e)


    # def load_group_names(self):
    #     if os.path.exists(GROUPS_FILE):
    #         try:
    #             with open(GROUPS_FILE, "r") as f:
    #                 self.group_names = json.load(f)
    #                 for name in self.group_names:
    #                     self.group_dropdown.addItem(name)
    #         except Exception as e:
                # print("Failed to load group names:", e)
    


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

        # Get scheduled datetime
        scheduled_datetime = self.dateTimeEdit.dateTime().toPython()

        if scheduled_datetime <= datetime.now():
            QMessageBox.warning(self, "Invalid Time", "Scheduled time must be in the future.")
            return

        # Schedule message
        self.schedule_message(message, numbers, msg_type, scheduled_datetime)
        self.add_message_to_list(message, "scheduled", scheduled_datetime)

        self.message_box.clear()

    # def schedule_message(self, message, numbers, msg_type, when):
    #     delay = datetime.now().msecs_to(QDateTime(when).toMSecsSinceEpoch())
    def schedule_message(self, message, numbers, msg_type, when):
        group_name = self.group_name_input.text().strip()
        now_qt = QDateTime.currentDateTime()
        when_qt = QDateTime(when)
        delay = now_qt.msecsTo(when_qt)
        def send_scheduled():
            try:
                driver = self.init_whatsapp_driver()
                if msg_type == "Personal":
                    self.send_personal_messages(driver, numbers, message)
                # else:
                #     self.send_group_message(driver, "Test version", message)
                    
                if not group_name:
                    QMessageBox.warning(self, "Group Name Missing", "Please enter or select a WhatsApp group name.")
                    return

                self.send_group_message(driver, group_name, message)
            
                # Save group name if not already saved
                self.add_message_to_list(message, "sent")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Scheduled send failed: {e}")

        timer = QTimer(self)
        timer.setSingleShot(True)
        timer.timeout.connect(send_scheduled)
        timer.start(delay)
        self.scheduled_tasks.append(timer)

    def add_message_to_list(self, message_text, status="sent", scheduled_time=None):
        from PySide6.QtGui import QStandardItem
        display_text = ""
        if status == "sent":
            display_text = f"Sent at {datetime.now().strftime('%Y-%m-%d %H:%M')} - ✅ {message_text}"
        elif status == "scheduled":
            display_text = f"Scheduled for {scheduled_time.strftime('%Y-%m-%d %H:%M')} - ⏳ {message_text}"

        item = QStandardItem(display_text)
        item.setEditable(False)
        item.setData({
            "status": status,
            "message": message_text,
            "scheduled_time": scheduled_time
        }, Qt.UserRole)
        self.message_model.appendRow(item)    
        
        


    def setCurrentDate(self):
        """Sets the dateTimeEdit widget to the current date and time."""
        current_datetime = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(current_datetime)        
        
    # def handle_send_message(self):
    #     message = self.message_box.toPlainText().strip()
    #     if not message:
    #         QMessageBox.warning(self, "Empty Message", "Please type a message to send.")
    #         return

    #     msg_type = self.get_message_type()
    #     if not msg_type:
    #         return  # User canceled

    #     selected_numbers = self.get_selected_numbers()
    #     if not selected_numbers and msg_type == "Personal":
    #         QMessageBox.warning(self, "No Selection", "Please select at least one patient.")
    #         return

    #     try:
    #         driver = self.init_whatsapp_driver()

    #         if msg_type == "Personal":
    #             self.send_personal_messages(driver, selected_numbers, message)
    #         else:
    #             group_name = "Test version"  # Could be dynamic
    #             self.send_group_message(driver, group_name, message)

    #         # Update listView
    #         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #         entry = f"[{timestamp}] ({msg_type}) {message}"
    #         self.sent_messages.append(entry)
    #         self.message_model.setStringList(self.sent_messages)
    #         self.message_box.clear()

    #         # ✅ Keep session alive
    #         print("✅ Messages sent. Browser session is still open.")
    #         input("📌 Press Enter to close the session manually...")

    #         # driver.quit()

    #     except Exception as e:
    #         QMessageBox.critical(self, "Error", f"Failed to send message.\n{str(e)}")


    # def add_message_to_list(self, message_text, status="sent", scheduled_time=None):
    #     display_text = ""
    #     if status == "sent":
    #         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    #         display_text = f"Sent at {timestamp} - ✅ {message_text}"
    #     elif status == "scheduled":
    #         display_text = f"Scheduled for {scheduled_time.strftime('%Y-%m-%d %H:%M')} - ⏳ {message_text}"

    #     item = QStandardItem(display_text)
    #     item.setEditable(False)
    #     item.setData({
    #         "status": status,
    #         "message": message_text,
    #         "scheduled_time": scheduled_time,
    #     }, Qt.UserRole)

    #     self.message_model.appendRow(item)


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
            checkbox.stateChanged.connect(lambda state, r=row: self.on_checkbox_changed(state, r))

            checkbox.setStyleSheet("margin-left:50%; margin-right:50%;")
            widget = QWidget()
            layout = QHBoxLayout(widget)
            layout.addWidget(checkbox)
            layout.setAlignment(Qt.AlignCenter)
            layout.setContentsMargins(0, 0, 0, 0)
            self.tableWidget.setCellWidget(row, 0, widget)

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

    def on_checkbox_changed(self, state, row):
        # Highlight or clear highlight
        color = QColor("red") if state == Qt.Checked else QColor("black")
        for col in range(self.tableWidget.columnCount()):
            item = self.tableWidget.item(row, col)
            if item:
                item.setBackground(color)

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
    #     options.add_argument("--user-data-dir=whatsapp_session")  # Persistent login session
    #     driver = webdriver.Chrome(options=options)
    #     driver.get("https://web.whatsapp.com")
    #     QMessageBox.information(self, "Scan QR", "Please scan the QR code in the opened browser window.")
    #     time.sleep(15)  # Wait to login
    #     return driver
    
    
    # def init_whatsapp_driver(self):
    #     options = Options()
    #     # options.add_argument("--user-data-dir=whatsapp_session")  # Persistent login session
    #     profile_dir = os.path.abspath("chrome_whatsapp_profile")  # Absolute path
    #     options.add_argument(f"--user-data-dir={profile_dir}")
    #     driver_path = r"c:\Users\falco\Desktop\system_optic\win32\chromedriver.exe"  # 🔁 Update with your actual path

    #     service = Service(driver_path)
    #     driver = webdriver.Chrome(service=service, options=options)

    #     driver.get("https://web.whatsapp.com")
    #     QMessageBox.information(self, "Scan QR", "Please scan the QR code in the opened browser window.")
    #     time.sleep(15)
    #     return driver

    def init_whatsapp_driver(self):
        options = Options()
        
        # Setup proper profile directory
        profile_dir = os.path.abspath("chrome_whatsapp_profile")
        options.add_argument(f"--user-data-dir={profile_dir}")

        # Optional stabilizing flags
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--remote-debugging-port=9222")

        # Optional: start maximized
        options.add_argument("--start-maximized")

        # Point to chromedriver
        driver_path = r"c:\Users\falco\Desktop\system_optic\win32\chromedriver.exe"  # chromedriver-win64\chromedriver-win64\chromedriver.exe Change this to your real path
        service = Service(driver_path)

        driver = webdriver.Chrome(service=service, options=options)
        driver.get("https://web.whatsapp.com")

        QMessageBox.information(self, "Scan QR", "Please scan the QR code in the opened browser window.")
        time.sleep(15)
        return driver            

    def send_personal_messages(self, driver, contacts, message):
        for number in contacts:
            url = f"https://web.whatsapp.com/send?phone={number}&text={message}"
            driver.get(url)
            time.sleep(10)

            try:
                send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
                send_button.click()
                time.sleep(2)
            except Exception as e:
                print(f"Failed to send to {number}: {e}")

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
# import requests
# from PySide6.QtWidgets import (
#     QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QHeaderView, QCheckBox, QLineEdit
# )
# from PySide6.QtCore import Qt
# from ui_p_MedicalList1 import Ui_MainWindow  # Import the UI file for the main system
# import requests
# from datetime import datetime
# #from ui_p_MedicalList import Ui_MainWindow
# # from medicalrepotForms import MedicalReportForm/
# from ui_whatsapp_automate2 import Ui_MainWindow
# from PySide6.QtCore import QTimer
# BASE_URL = "http://127.0.0.1:8000/auth"

# class MessageAutomationsystem(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)

#         self.tableWidget.setSelectionBehavior(self.tableWidget.SelectionBehavior.SelectRows)
#         self.tableWidget.setSortingEnabled(True)
#         self.search_bar.textChanged.connect(self.filter_table)

#         self.load_patients()
#         self.all_checkBox.stateChanged.connect(self.toggle_select_all)
#         self.customize_checkBox.stateChanged.connect(self.toggle_custom_select)

#     def filter_table(self, text):
#         for row in range(self.tableWidget.rowCount()):
#             match = False
#             for col in range(1, self.tableWidget.columnCount()):
#                 item = self.tableWidget.item(row, col)
#                 if item and text.lower() in item.text().lower():
#                     match = True
#                     break
#             self.tableWidget.setRowHidden(row, not match)

#     # def get_selected_patient_ids(self):
#     #     selected_ids = []
#     #     for row in range(self.tableWidget.rowCount()):
#     #         checkbox = self.tableWidget.cellWidget(row, 0)
#     #         if checkbox and checkbox.isChecked():
#     #             item = self.tableWidget.item(row, 1)  # Column 1 = patient ID
#     #             if item:
#     #                 selected_ids.append(item.text())
#     #     return selected_ids


#     def load_patients(self):
#         try:
#             response = requests.get(f"{BASE_URL}/patients/list/")
#             if response.status_code == 200:
#                 self.update_table(response.json()['patients'])
#             else:
#                 QMessageBox.warning(self, "Error", "Failed to load patients.")
#         except requests.RequestException as e:
#             QMessageBox.critical(self, "Error", f"Server error: {e}")

#     def get_value(self, val):
#         return str(val) if val not in (None, '', 'null') else 'N/A'

#     def toggle_select_all(self, state):
#         if state == Qt.Checked:
#             for cb in self.checkboxes:
#                 cb.setChecked(True)

#             self.customize_checkBox.setChecked(False)
#             self.customize_checkBox.setEnabled(False)
#             QMessageBox.information(self, "Selection", "All patients selected.")
#         else:
#             for cb in self.checkboxes:
#                 cb.setChecked(False)

#             self.customize_checkBox.setEnabled(True)


#     def toggle_custom_select(self, state):
#         if state == Qt.Checked:
#             self.all_checkBox.setChecked(False)
#             self.all_checkBox.setEnabled(False)
#             QMessageBox.information(self, "Selection", "Customized selection enabled.")
#         else:
#             self.all_checkBox.setEnabled(True)
#             for cb in self.checkboxes:
#                 cb.setChecked(False)

#     def update_table(self, patients):
#         self.tableWidget.setRowCount(0)
#         self.tableWidget.setSortingEnabled(False)
#         self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

#         self.checkboxes = []  # Track checkboxes directly

#         for patient in patients:
#             row = self.tableWidget.rowCount()
#             self.tableWidget.insertRow(row)

#             checkbox = QCheckBox()
#             self.checkboxes.append(checkbox)
#             self.tableWidget.setCellWidget(row, 0, checkbox)

#             self.tableWidget.setItem(row, 1, QTableWidgetItem(self.get_value(patient.get('id'))))
#             self.tableWidget.setItem(row, 2, QTableWidgetItem(self.get_value(patient.get('name'))))
#             self.tableWidget.setItem(row, 3, QTableWidgetItem(self.get_value(patient.get('email'))))
#             self.tableWidget.setItem(row, 4, QTableWidgetItem(self.get_value(patient.get('contact'))))
#             self.tableWidget.setItem(row, 5, QTableWidgetItem(self.get_value(patient.get('address'))))
#             self.tableWidget.setItem(row, 6, QTableWidgetItem(self.get_value(patient.get('profession'))))
#             self.tableWidget.setItem(row, 7, QTableWidgetItem(self.get_value(patient.get('age'))))
#             self.tableWidget.setItem(row, 8, QTableWidgetItem(self.get_value(patient.get('gender'))))

#         self.tableWidget.setSortingEnabled(True)
#         self.tableWidget.sortItems(2, Qt.SortOrder.AscendingOrder)


#     # def toggle_select_all(self, state):
#     #     if state == Qt.Checked:
#     #         QTimer.singleShot(100, self.check_all_checkboxes)
#     #         self.checkBox_2.setChecked(False)
#     #         self.checkBox_2.setEnabled(False)
#     #         QMessageBox.information(self, "Selection", "All patients selected.")
#     #     else:
#     #         for row in range(self.tableWidget.rowCount()):
#     #             checkbox = self.tableWidget.cellWidget(row, 0)
#     #             if checkbox:
#     #                 checkbox.setChecked(False)
            

#     # def check_all_checkboxes(self):
#     #     for row in range(self.tableWidget.rowCount()):
#     #         checkbox = self.tableWidget.cellWidget(row, 0)
#     #         if checkbox:
#     #             checkbox.setChecked(True)

#     #         self.checkBox_2.setEnabled(True)
#     # def toggle_custom_select(self, state):
#     #     if state == Qt.Checked:
#     #         self.checkBox.setChecked(False)
#     #         self.checkBox.setEnabled(False)
#     #         QMessageBox.information(self, "Selection", "Customized selection enabled.")
#     #     else:
#     #         self.checkBox.setEnabled(True)
#     #         # Optional: Clear all checkboxes when customized deselected
#     #         for row in range(self.tableWidget.rowCount()):
#     #             checkbox = self.tableWidget.cellWidget(row, 0)
#     #             if checkbox:
#     #                 checkbox.setChecked(False)
# if __name__ == "__main__":
#     QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
#     app = QApplication(sys.argv)
#     window = MessageAutomationsystem()
#     window.show()
#     sys.exit(app.exec())






