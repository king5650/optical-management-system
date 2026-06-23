import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QDateEdit, QMessageBox, QListWidget, QHBoxLayout
from PyQt6.QtCore import QDate
import json
import sys
import os  # Add this import at the top of the file

class RemainderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Remainder - Event Reminder System")
        self.setGeometry(100, 100, 600, 400)

        main_layout = QHBoxLayout()

        # Left Side: Event Management
        event_layout = QVBoxLayout()

        event_layout.addWidget(QLabel("Event Name:"))
        self.event_name = QLineEdit(self)
        event_layout.addWidget(self.event_name)

        event_layout.addWidget(QLabel("Event Date:"))
        self.event_date = QDateEdit(self)
        self.event_date.setDate(QDate.currentDate())
        event_layout.addWidget(self.event_date)

        event_layout.addWidget(QLabel("Reminder Message:"))
        self.reminder_message = QTextEdit(self)
        event_layout.addWidget(self.reminder_message)

        self.save_button = QPushButton("Save Event", self)
        self.save_button.clicked.connect(self.save_event)
        event_layout.addWidget(self.save_button)

        # Right Side: Contact Management
        contact_layout = QVBoxLayout()

        contact_layout.addWidget(QLabel("Contacts:"))
        self.contact_list = QListWidget(self)
        contact_layout.addWidget(self.contact_list)

        self.load_contacts()

        contact_layout.addWidget(QLabel("Add New Contact:"))
        self.contact_name = QLineEdit(self)
        contact_layout.addWidget(self.contact_name)

        self.contact_phone = QLineEdit(self)
        contact_layout.addWidget(QLabel("Phone Number:"))
        contact_layout.addWidget(self.contact_phone)

        self.add_contact_button = QPushButton("Add Contact", self)
        self.add_contact_button.clicked.connect(self.add_contact)
        contact_layout.addWidget(self.add_contact_button)

        main_layout.addLayout(event_layout)
        main_layout.addLayout(contact_layout)
        self.setLayout(main_layout)



    def load_contacts(self):
        try:
            # Ensure the 'data' directory exists
            os.makedirs("data", exist_ok=True)

            # Check if the file exists, and create it if it doesn't
            if not os.path.exists("data/contacts.json"):
                with open("data/contacts.json", "w") as file:
                    json.dump({"contacts": []}, file)

            # Load contacts from the file
            with open("data/contacts.json", "r") as file:
                data = json.load(file)
                self.contact_list.clear()
                for contact in data["contacts"]:
                    self.contact_list.addItem(f"{contact['name']} - {contact['phone']}")
        except Exception as e:
            print(f"Error loading contacts: {e}")

    def add_contact(self):
        name = self.contact_name.text()
        phone = self.contact_phone.text()

        if not name or not phone:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return

        try:
            # Ensure the 'data' directory exists
            os.makedirs("data", exist_ok=True)

            # Load existing contacts or initialize an empty list
            if os.path.exists("data/contacts.json"):
                with open("data/contacts.json", "r") as file:
                    data = json.load(file)
            else:
                data = {"contacts": []}

            # Add the new contact
            data["contacts"].append({"name": name, "phone": phone})

            # Save the updated contacts
            with open("data/contacts.json", "w") as file:
                json.dump(data, file, indent=4)

            # Refresh the contact list
            self.load_contacts()
            QMessageBox.information(self, "Success", "Contact added successfully!")
        except Exception as e:
            print(f"Error adding contact: {e}")
            QMessageBox.critical(self, "Error", f"Failed to add contact: {e}")







    def save_event(self):
        event_name = self.event_name.text()
        event_date = self.event_date.date().toString("yyyy-MM-dd")
        reminder_message = self.reminder_message.toPlainText()

        if not event_name or not reminder_message:
            QMessageBox.warning(self, "Error", "Please fill in all fields.")
            return

        # Save event to JSON or database (backend logic)
        print(f"Event Saved: {event_name} on {event_date} with message: {reminder_message}")
        QMessageBox.information(self, "Success", "Event saved successfully!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RemainderApp()
    window.show()
    sys.exit(app.exec())