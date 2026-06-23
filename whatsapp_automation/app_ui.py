# app_ui.py
import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QMessageBox
)
from PySide6.QtCore import Qt, QThread, Signal
from sender import send_single_message

class SenderThread(QThread):
    finished = Signal(bool)

    def __init__(self, number, message):
        super().__init__()
        self.number = number
        self.message = message

    def run(self):
        result = send_single_message(self.number, self.message)
        self.finished.emit(result)

class WhatsAppSenderUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WhatsApp Message Sender")
        self.setFixedSize(400, 300)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Number Input
        self.number_label = QLabel("Phone Number (+countrycode...):")
        self.number_input = QLineEdit()
        layout.addWidget(self.number_label)
        layout.addWidget(self.number_input)

        # Message Input
        self.message_label = QLabel("Message:")
        self.message_input = QTextEdit()
        layout.addWidget(self.message_label)
        layout.addWidget(self.message_input)

        # Status
        self.status_label = QLabel("")
        self.status_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status_label)

        # Send Button
        self.send_button = QPushButton("Send Message")
        self.send_button.clicked.connect(self.send_message)
        layout.addWidget(self.send_button)

        self.setLayout(layout)

    def send_message(self):
        number = self.number_input.text().strip()
        message = self.message_input.toPlainText().strip()

        if not number or not message:
            QMessageBox.warning(self, "Input Error", "Please enter both number and message.")
            return

        self.send_button.setDisabled(True)
        self.status_label.setText("Sending...")
        self.status_label.setStyleSheet("color: blue")

        self.worker = SenderThread(number, message)
        self.worker.finished.connect(self.on_message_sent)
        self.worker.start()

    def on_message_sent(self, success):
        if success:
            self.status_label.setText("✅ Message sent successfully.")
            self.status_label.setStyleSheet("color: green")
        else:
            self.status_label.setText("❌ Failed to send message.")
            self.status_label.setStyleSheet("color: red")
        self.send_button.setDisabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WhatsAppSenderUI()
    window.show()
    sys.exit(app.exec())
