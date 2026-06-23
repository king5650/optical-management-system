# ui/main_window.py

from PySide6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QTextEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QGroupBox, QApplication, QPlainTextEdit
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
# from automation.whatsapp_selenium import send_whatsapp_message
from concurrent.futures import ThreadPoolExecutor
from PySide6.QtCore import QMetaObject, Qt, Q_ARG
from automation.whatsapp_playwright import send_whatsapp_message




class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WhatsApp Message Automation")
        self.setMinimumSize(500, 500)
        self.setup_ui()
        self.send_button.clicked.connect(self.handle_send_message)
        self.executor = ThreadPoolExecutor(max_workers=1)
        # self.append_log("🔧 Ready to send WhatsApp messages!")


    def setup_ui(self):
        # Fonts
        header_font = QFont("Arial", 16, QFont.Bold)

        # Header
        header_label = QLabel("📨 WhatsApp Message Automation")
        header_label.setFont(header_font)
        header_label.setAlignment(Qt.AlignCenter)

        # Phone Number Input
        phone_label = QLabel("Enter WhatsApp Number:")
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("+237XXXXXXXXX")

        # Message Input
        message_label = QLabel("Enter Message:")
        self.message_input = QTextEdit()
        self.message_input.setPlaceholderText("Type your message here...")

        # Send Button
        self.send_button = QPushButton("Send Message")
        self.send_button.setStyleSheet("padding: 8px 16px; font-weight: bold;")

        # Status Log
        log_label = QLabel("Status / Log:")
        self.log_output = QPlainTextEdit()
        self.log_output.setReadOnly(True)

        # Layouts
        main_layout = QVBoxLayout()

        form_group = QGroupBox("Message Sender")
        form_layout = QVBoxLayout()
        form_layout.addWidget(phone_label)
        form_layout.addWidget(self.phone_input)
        form_layout.addWidget(message_label)
        form_layout.addWidget(self.message_input)
        form_layout.addWidget(self.send_button)
        form_group.setLayout(form_layout)

        main_layout.addWidget(header_label)
        main_layout.addSpacing(10)
        main_layout.addWidget(form_group)
        main_layout.addSpacing(10)
        main_layout.addWidget(log_label)
        main_layout.addWidget(self.log_output)

        self.setLayout(main_layout)

    def append_log(self, message: str):
        self.log_output.appendPlainText(message)

    def handle_send_message(self):
        phone = self.phone_input.text().strip()
        message = self.message_input.toPlainText().strip()

        if not phone.startswith("+") or not phone[1:].isdigit():
            self.append_log("❌ Invalid phone number. Must start with '+' and contain only digits.")
            return

        if not message:
            self.append_log("❌ Message cannot be empty.")
            return
        self.append_log(f"✅ Sending message to {phone}...{message}")
        
        self.run_in_background(phone, message)
    # def handle_send_message(self):
        # phone = self.phone_input.text().strip()
        # message = self.message_input.toPlainText().strip()

        # if not phone.startswith("+") or not phone[1:].isdigit():
        #     self.append_log("❌ Invalid phone number. Must start with '+' and contain only digits.")
        #     return

        # if not message:
        #     self.append_log("❌ Message cannot be empty.")
        #     return

        # self.append_log(f"✅ Sending message to {phone}...")
        
        # # TODO: Replace with actual automation call (in next step)
        # self.simulate_send(phone, message)


    # def simulate_send(self, phone, message):
    #     from datetime import datetime
    #     self.append_log(f"📤 [SIMULATION] Message to {phone} sent at {datetime.now().strftime('%H:%M:%S')}")
    #     self.append_log(f"📝 Message: {message}")
    #     self.append_log("------")

    # def simulate_send(self, phone, message):
    #     self.append_log("⚙️ Starting Selenium automation...")
    #     send_whatsapp_message(phone, message, log_callback=self.append_log)

    def run_in_background(self, phone, message):
        self.append_log("⚙️ Starting automation in background...")

        # Submit to thread pool
        self.executor.submit(self._send_task, phone, message)

    def _send_task(self, phone, message):
        # from automation.whatsapp_playwright import send_whatsapp_message
        send_whatsapp_message(phone, message, log_callback=self.thread_safe_log)


    def thread_safe_log(self, message):
        QMetaObject.invokeMethod(
            self.log_output,
            "appendPlainText",
            Qt.QueuedConnection,
            Q_ARG(str, message)
        )
# from PySide6.QtWidgets import (
#     QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout,
#     QHBoxLayout, QGroupBox, QApplication, QPlainTextEdit, QTableWidget,
#     QTableWidgetItem, QHeaderView
# )
# from PySide6.QtGui import QFont, QColor, QPalette
# from PySide6.QtCore import Qt, QMetaObject, Q_ARG
# from concurrent.futures import ThreadPoolExecutor

# from automation.whatsapp_playwright import send_whatsapp_message


# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("📨 WhatsApp Message Automation")
#         self.setMinimumSize(700, 600)
#         self.setup_ui()
#         self.send_button.clicked.connect(self.handle_send_message)
#         self.executor = ThreadPoolExecutor(max_workers=1)

#     def setup_ui(self):
#         self.setStyleSheet("""
#             QWidget {
                
#                 font-family: 'Segoe UI', sans-serif;
#                 font-size: 14px;
#             }
#             QGroupBox {
#                 border: none;
#                 border-radius: 15px;
                
#                 padding: 15px;
#                 margin-top: 10px;
                
#             }
#             QLineEdit, QTextEdit, QPlainTextEdit {
#                 border: none;
#                 border-radius: 10px;
#                 padding: 10px;
                
#                 box-shadow: inset 4px 4px 6px #bec4cf, inset -4px -4px 6px #ffffff;
#             }
#             QPushButton {
#                 background-color: #00a884;
#                 color: white;
#                 border: none;
#                 border-radius: 10px;
#                 padding: 10px 20px;
#                 font-weight: bold;
#             }
#             QPushButton:hover {
#                 background-color: #029b76;
#             }
#             QLabel {
#                 font-weight: bold;
#             }
#         """)

#         header_font = QFont("Segoe UI", 18, QFont.Bold)
#         header_label = QLabel("📨 WhatsApp Message Automation")
#         header_label.setFont(header_font)
#         header_label.setAlignment(Qt.AlignCenter)

#         # Phone number
#         phone_label = QLabel("Recipient WhatsApp Number:")
#         self.phone_input = QLineEdit()
#         self.phone_input.setPlaceholderText("+237XXXXXXXXX")

#         # Message
#         message_label = QLabel("Enter Message:")
#         self.message_input = QTextEdit()
#         self.message_input.setPlaceholderText("Type your message here...")

#         # Send button
#         self.send_button = QPushButton("📤 Send Message")

#         # Status log
#         log_label = QLabel("System Log:")
#         self.log_output = QPlainTextEdit()
#         self.log_output.setReadOnly(True)

#         # Message history table
#         self.table = QTableWidget(0, 3)
#         self.table.setHorizontalHeaderLabels(["Phone", "Message", "Status"])
#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
#         self.table.setStyleSheet("""
#             QTableWidget {
                
#                 border-radius: 10px;
#             }
#             QHeaderView::section {
#                 background-color: #00a884;
#                 color: white;
#                 font-weight: bold;
#                 border: none;
#                 padding: 5px;
#             }
#         """)

#         # Group: Message Form
#         form_group = QGroupBox("Message Sender")
#         form_layout = QVBoxLayout()
#         form_layout.addWidget(phone_label)
#         form_layout.addWidget(self.phone_input)
#         form_layout.addWidget(message_label)
#         form_layout.addWidget(self.message_input)
#         form_layout.addWidget(self.send_button)
#         form_group.setLayout(form_layout)

#         # Layout
#         main_layout = QVBoxLayout()
#         main_layout.addWidget(header_label)
#         main_layout.addWidget(form_group)
#         main_layout.addWidget(log_label)
#         main_layout.addWidget(self.log_output)
#         main_layout.addWidget(QLabel("📋 Message History"))
#         main_layout.addWidget(self.table)

#         self.setLayout(main_layout)

#     def append_log(self, message: str):
#         self.log_output.appendPlainText(message)

#     def add_message_to_table(self, phone, message, status):
#         row = self.table.rowCount()
#         self.table.insertRow(row)
#         self.table.setItem(row, 0, QTableWidgetItem(phone))
#         self.table.setItem(row, 1, QTableWidgetItem(message))
#         self.table.setItem(row, 2, QTableWidgetItem(status))

#     def handle_send_message(self):
#         phone = self.phone_input.text().strip()
#         message = self.message_input.toPlainText().strip()

#         if not phone.startswith("+") or not phone[1:].isdigit():
#             self.append_log("❌ Invalid phone number. Must start with '+' and contain only digits.")
#             self.add_message_to_table(phone, message, "❌ Invalid number")
#             return

#         if not message:
#             self.append_log("❌ Message cannot be empty.")
#             self.add_message_to_table(phone, "(empty)", "❌ Empty message")
#             return

#         self.append_log(f"✅ Sending message to {phone}...\n📨 {message}")
#         self.add_message_to_table(phone, message, "⏳ Sending...")

#         self.run_in_background(phone, message)

#     def run_in_background(self, phone, message):
#         self.append_log("⚙️ Starting automation in background...")
#         self.executor.submit(self._send_task, phone, message)

#     def _send_task(self, phone, message):
#         send_whatsapp_message(phone, message, log_callback=self.thread_safe_log)
#         self.thread_safe_add_row_status(phone, "✅ Sent")

#     def thread_safe_log(self, message):
#         QMetaObject.invokeMethod(
#             self.log_output,
#             "appendPlainText",
#             Qt.QueuedConnection,
#             Q_ARG(str, message)
#         )

#     def thread_safe_add_row_status(self, phone, status):
#         for row in range(self.table.rowCount()):
#             if self.table.item(row, 0).text() == phone:
#                 self.table.setItem(row, 2, QTableWidgetItem(status))
