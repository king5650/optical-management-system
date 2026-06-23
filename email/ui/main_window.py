# # import sys
# # import os

# # # Add the project root directory to the Python path
# # sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# # from PySide6.QtWidgets import (
# #     QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFrame,
# #     QPushButton, QLabel, QLineEdit, QTableWidget, QTableWidgetItem,
# #     QHeaderView, QAbstractItemView, QTableWidgetSelectionRange, QScrollArea,
# #     QListWidget, QListWidgetItem, QSizePolicy, QStyle, QSpacerItem,
# # )
# # from PySide6.QtCore import Qt, QSize
# # from PySide6.QtGui import QIcon
# # from add_person import AddPersonDialog
# # from send_mail import SendMailDialog


# # from backend.person_service import PersonService
# # from backend.history_service import HistoryService

# # class MainWindow(QMainWindow):
# #     def __init__(self):
# #         super().__init__()

# #         self.setWindowTitle("Mail Broadcast System")
# #         self.setMinimumSize(1100, 650)
# #         self.setStyleSheet(self.load_styles())   # Load custom QSS

# #         main_container = QWidget()
# #         main_layout = QHBoxLayout(main_container)
# #         main_layout.setContentsMargins(0, 0, 0, 0)

# #         # ---------------------
# #         # SIDEBAR
# #         # ---------------------
# #         self.sidebar = QFrame()
# #         self.sidebar.setObjectName("sidebar")
# #         self.sidebar.setFixedWidth(220)

# #         sidebar_layout = QVBoxLayout(self.sidebar)
# #         sidebar_layout.setContentsMargins(20, 20, 20, 20)
# #         sidebar_layout.setSpacing(20)

# #         # App name / logo
# #         app_title = QLabel("Mail System")
# #         app_title.setObjectName("appTitle")

# #         # Sidebar buttons
# #         btn_people = QPushButton(" People")
# #         btn_people.setObjectName("sidebarBtn")
# #         btn_people.setIcon(QIcon.fromTheme("user"))

# #         btn_send = QPushButton(" Send Mail")
# #         btn_send.setObjectName("sidebarBtn")
# #         btn_send.setIcon(QIcon.fromTheme("mail-send"))

# #         btn_settings = QPushButton(" Settings")
# #         btn_settings.setObjectName("sidebarBtn")
# #         btn_settings.setIcon(QIcon.fromTheme("settings"))

# #         sidebar_layout.addWidget(app_title)
# #         sidebar_layout.addSpacing(10)
# #         sidebar_layout.addWidget(btn_people)
# #         sidebar_layout.addWidget(btn_send)
# #         sidebar_layout.addWidget(btn_settings)
# #         sidebar_layout.addStretch()

# #         # ---------------------
# #         # MAIN AREA
# #         # ---------------------
# #         self.main_area = QFrame()
# #         self.main_area.setObjectName("mainArea")

# #         main_area_layout = QVBoxLayout(self.main_area)
# #         main_area_layout.setContentsMargins(20, 20, 20, 20)
# #         main_area_layout.setSpacing(15)


# #         # ---------------------
# #         # TOPBAR
# #         # ---------------------
# #         topbar = QFrame()
# #         topbar.setObjectName("topbar")
# #         topbar_layout = QHBoxLayout(topbar)
# #         topbar_layout.setContentsMargins(10, 10, 10, 10)

# #         self.search = QLineEdit()
# #         self.search.setPlaceholderText("Search people…")
# #         self.search.setObjectName("searchBox")
# #         self.search.textChanged.connect(self.filter_table)

# #         import_btn = QPushButton("Import CSV")
# #         import_btn.setObjectName("secondaryBtn")

# #         add_btn = QPushButton("Add Person")
# #         add_btn.setObjectName("primaryBtn")
# #         add_btn.clicked.connect(self.open_add_person_dialog)

# #         edit_btn = QPushButton("Edit")
# #         edit_btn.setObjectName("secondaryBtn")
# #         # edit_btn.clicked.connect(self.edit_person)

# #         delete_btn = QPushButton("Delete")
# #         delete_btn.setObjectName("secondaryBtn")
# #         # delete_btn.clicked.connect(self.delete_person)

# #         refresh_btn = QPushButton("Refresh")
# #         refresh_btn.setObjectName("secondaryBtn")
# #         refresh_btn.clicked.connect(self.load_people)


# #         topbar_layout.addWidget(self.search)
# #         topbar_layout.addStretch()
# #         topbar_layout.addWidget(import_btn)
# #         topbar_layout.addWidget(add_btn)
# #         topbar_layout.addWidget(edit_btn)
# #         topbar_layout.addWidget(delete_btn)
# #         topbar_layout.addWidget(refresh_btn)
# #         # ---------------------
# #         # TABLE OF PEOPLE filter_table
# #         # ---------------------
# #         self.table = QTableWidget()
# #         self.table.setColumnCount(4)
# #         self.table.setHorizontalHeaderLabels(["Name", "Email", "Group", "Status"])
# #         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
# #         self.table.setSelectionMode(QAbstractItemView.SingleSelection)
# #         self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
# #         self.table.setObjectName("peopleTable")

# #         # Sample data
# #         self.add_table_row("John Doe", "john@example.com", "General", "Active")
# #         self.add_table_row("Sarah Kiven", "sarah@example.com", "Staff", "Active")

# #         main_area_layout.addWidget(topbar)
# #         main_area_layout.addWidget(self.table)

# #         # ADD TO LAYOUT
# #         main_layout.addWidget(self.sidebar)
# #         main_layout.addWidget(self.main_area)

# #         self.setCentralWidget(main_container)
# #         add_btn.clicked.connect(self.open_add_person_dialog)
# #         btn_send.clicked.connect(self.open_send_mail_dialog)
# #         self.load_people()

# #     # Add sample row function
# #     def add_table_row(self, name, email, group, status):
# #         row = self.table.rowCount()
# #         self.table.insertRow(row)

# #         self.table.setItem(row, 0, QTableWidgetItem(name))
# #         self.table.setItem(row, 1, QTableWidgetItem(email))
# #         self.table.setItem(row, 2, QTableWidgetItem(group))
# #         self.table.setItem(row, 3, QTableWidgetItem(status))

# #     def open_add_person_dialog(self):
# #         dialog = AddPersonDialog(self)
# #         # dialog.person_added.connect(self.add_person_to_table)
# #         dialog.exec()
        
# #     def open_send_mail_dialog(self):
# #         # Example list of people
# #         self.people_list = ["John Doe", "Jane Smith", "Alice Johnson"]

# #         # Pass the list of people to the SendMailDialog
# #         dialog = SendMailDialog(self.people_list, self)
# #         # dialog.mailSent.connect(self.handle_mail_sent)  # Optional: connect to a signal
# #         dialog.exec()
        
# #     def load_people(self):
# #         """Load ALL people from database into the table."""
# #         self.table.setRowCount(0)

# #         try:
# #             # Fetch all people from the database
# #             people = PersonService.get_all_people()    # returns list[dict]

# #             for p in people:
# #                 full_name = p["first_name"] + " " + p["last_name"]

# #                 self.add_table_row(
# #                     full_name,
# #                     p["email"],
# #                     p["group_name"],
# #                     p["status"]
# #                 )

# #         except Exception as e:
# #             print("Error loading people:", e)

# #     def filter_table(self, text):
# #         text = text.lower()
# #         for row in range(self.table.rowCount()):
# #             name = self.table.item(row, 1).text().lower()
# #             email = self.table.item(row, 2).text().lower()

# #             self.table.setRowHidden(row, text not in name and text not in email)
# #     # ---------------------
# #     # QSS THEME
# #     # ---------------------
# #     def load_styles(self):
# #         return """
# #         /* MAIN COLORS */
# #         * {
# #             font-family: 'Segoe UI', sans-serif;
# #             font-size: 14px;
# #         }

# #         #sidebar {
# #             background: qlineargradient(spread:pad, x1:0, y1:0.267, x2:1, y2:0.471, stop:0 rgba(2, 101, 195, 255), stop:1 rgba(44, 47, 132, 255));
# #             border-right: 1px solid #E5E7EB;
# #         }

# #         #appTitle {
# #             font-size: 22px;
# #             font-weight: 600;
# #             color: white;
# #         }

# #         #sidebarBtn {
# #             background: transparent;
# #             color: white;
# #             font-weight: 900;
# #             padding: 12px;
# #             text-align: left;
# #             border-radius: 6px;
# #         }
# #         #sidebarBtn:hover {
# #             background: rgba(19,99,223,0.12);
# #         }

# #         /* MAIN AREA */
# #         #mainArea {
# #             background: rgba(2, 101, 195, 255);
# #         }

# #         /* TOPBAR */
# #         #topbar {
# #             background: #FFFFFF;
# #             border: 1px solid #E5E7EB;
# #             border-radius: 8px;
# #         }

# #         #searchBox {
# #             background: rgb(218, 216, 216);
# #             border-radius: 6px;
# #             padding: 8px;
# #             border: 1px solid #CBD5E1;
# #             color: black;
# #         }

# #         /* BUTTONS */
# #         #primaryBtn {
# #             background: #1363DF;
# #             color: #FFFFFF;
# #             padding: 8px 14px;
# #             border-radius: 6px;
# #         }
# #         #primaryBtn:hover {
# #             background: #0F52B3;
# #         }

# #         #secondaryBtn {
# #             background: #EEF4FF;
# #             color: #1363DF;
# #             padding: 8px 14px;
# #             border-radius: 6px;
# #             border: 1px solid rgba(19,99,223,0.12);
# #         }

# #         /* TABLE */
# #         #peopleTable {
# #             background: #FFFFFF;
# #             border-radius: 8px;
# #             color: black;
# #         }
# #         QHeaderView::section {
# #             background: #F8FAFC;
# #             padding: 10px;
# #             border: none;
# #             font-weight: 600;
# #             color: black;
# #         }
# #         QTableWidget::item {
# #             padding: 2px;
# #         }
# #         QTableWidget::item:selected {
# #             background: rgba(19,99,223,0.15);
# #             color: #0F172A;
    
# #         }
# #         """


# # if __name__ == "__main__":
# #     app = QApplication([])
# #     win = MainWindow()
# #     win.show()
# #     app.exec()


# import sys
# import os

# # Add the project root directory to the Python path
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from PySide6.QtWidgets import (
#     QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFrame,
#     QPushButton, QLabel, QLineEdit, QTableWidget, QTableWidgetItem,
#     QHeaderView, QAbstractItemView
# )
# from PySide6.QtCore import Qt
# from PySide6.QtGui import QIcon

# from add_person import AddPersonDialog
# from send_mail import SendMailDialog

# from backend.person_service import PersonService
# from backend.history_service import HistoryService


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Mail Broadcast System")
#         self.setMinimumSize(1100, 650)
#         self.setStyleSheet(self.load_styles())

#         main_container = QWidget()
#         main_layout = QHBoxLayout(main_container)
#         main_layout.setContentsMargins(0, 0, 0, 0)

#         # ---------------------
#         # SIDEBAR
#         # ---------------------
#         self.sidebar = QFrame()
#         self.sidebar.setObjectName("sidebar")
#         self.sidebar.setFixedWidth(220)

#         sidebar_layout = QVBoxLayout(self.sidebar)
#         sidebar_layout.setContentsMargins(20, 20, 20, 20)
#         sidebar_layout.setSpacing(20)

#         # App Title
#         app_title = QLabel("Mail System")
#         app_title.setObjectName("appTitle")

#         # Sidebar buttons
#         btn_people = QPushButton(" People")
#         btn_people.setObjectName("sidebarBtn")
#         btn_people.setIcon(QIcon.fromTheme("user"))

#         btn_send = QPushButton(" Send Mail")
#         btn_send.setObjectName("sidebarBtn")
#         btn_send.setIcon(QIcon.fromTheme("mail-send"))

#         btn_settings = QPushButton(" Settings")
#         btn_settings.setObjectName("sidebarBtn")
#         btn_settings.setIcon(QIcon.fromTheme("settings"))

#         sidebar_layout.addWidget(app_title)
#         sidebar_layout.addSpacing(10)
#         sidebar_layout.addWidget(btn_people)
#         sidebar_layout.addWidget(btn_send)
#         sidebar_layout.addWidget(btn_settings)
#         sidebar_layout.addStretch()

#         # ---------------------
#         # MAIN AREA
#         # ---------------------
#         self.main_area = QFrame()
#         self.main_area.setObjectName("mainArea")

#         main_area_layout = QVBoxLayout(self.main_area)
#         main_area_layout.setContentsMargins(20, 20, 20, 20)
#         main_area_layout.setSpacing(15)

#         # ---------------------
#         # TOPBAR
#         # ---------------------
#         topbar = QFrame()
#         topbar.setObjectName("topbar")
#         topbar_layout = QHBoxLayout(topbar)
#         topbar_layout.setContentsMargins(10, 10, 10, 10)

#         self.search = QLineEdit()
#         self.search.setPlaceholderText("Search people…")
#         self.search.setObjectName("searchBox")
#         self.search.textChanged.connect(self.filter_table)

#         import_btn = QPushButton("Import CSV")
#         import_btn.setObjectName("secondaryBtn")

#         add_btn = QPushButton("Add Person")
#         add_btn.setObjectName("primaryBtn")
#         add_btn.clicked.connect(self.open_add_person_dialog)

#         edit_btn = QPushButton("Edit")
#         edit_btn.setObjectName("secondaryBtn")

#         delete_btn = QPushButton("Delete")
#         delete_btn.setObjectName("secondaryBtn")

#         refresh_btn = QPushButton("Refresh")
#         refresh_btn.setObjectName("secondaryBtn")
#         refresh_btn.clicked.connect(self.load_people)

#         topbar_layout.addWidget(self.search)
#         topbar_layout.addStretch()
#         topbar_layout.addWidget(import_btn)
#         topbar_layout.addWidget(add_btn)
#         topbar_layout.addWidget(edit_btn)
#         topbar_layout.addWidget(delete_btn)
#         topbar_layout.addWidget(refresh_btn)

#         # ---------------------
#         # PEOPLE TABLE
#         # ---------------------
#         self.table = QTableWidget()
#         self.table.setColumnCount(4)
#         self.table.setHorizontalHeaderLabels(["Name", "Email", "Group", "Status"])
#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
#         self.table.setSelectionMode(QAbstractItemView.SingleSelection)
#         self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
#         self.table.setObjectName("peopleTable")

#         # LOAD DATA FROM DATABASE
#         self.load_people()

#         main_area_layout.addWidget(topbar)
#         main_area_layout.addWidget(self.table)

#         main_layout.addWidget(self.sidebar)
#         main_layout.addWidget(self.main_area)

#         self.setCentralWidget(main_container)

#         btn_send.clicked.connect(self.open_send_mail_dialog)

#     # ---------------------------------------------
#     # LOAD PEOPLE FROM DATABASE
#     # ---------------------------------------------
#     # def load_people(self):
#     #     """Load all people from the SQLite database into the table."""
#     #     self.table.setRowCount(0)  # Clear current rows

#     #     try:
#     #         people = PersonService.get_all_people()

#     #         for person in people:
#     #             full_name = person["first_name"] + " " + person["last_name"]

#     #             self.add_table_row(
#     #                 full_name,
#     #                 person["email"],
#     #                 person["group_name"],
#     #                 person["status"]
#     #             )

#     #     except Exception as e:
#     #         print("Error loading people:", e)
#     def load_people(self):
#         """Load all people from the database into the table."""
#         self.table.setRowCount(0)  # Clear current rows

#         try:
#             # Fetch all people from the database
#             people = PersonService.get_all_people()  # Ensure this returns a list of dictionaries

#             if not people:
#                 print("No people found in the database.")
#                 return

#             for person in people:
#                 full_name = person.get("name", "") 
#                 email = person.get("email", "")
#                 group_name = person.get("group_name", "")
#                 status = person.get("created_at", "")

#                 self.add_table_row(full_name, email, group_name, status)

#             print(f"Loaded {len(people)} people into the table.")

#         except Exception as e:
#             print("Error loading people:", e)
#     # ---------------------------------------------
#     # ADD ROW TO TABLE
#     # ---------------------------------------------
#     def add_table_row(self, name, email, group, status):
#         row = self.table.rowCount()
#         self.table.insertRow(row)

#         self.table.setItem(row, 0, QTableWidgetItem(name))
#         self.table.setItem(row, 1, QTableWidgetItem(email))
#         self.table.setItem(row, 2, QTableWidgetItem(group))
#         self.table.setItem(row, 3, QTableWidgetItem(status))

#     # ---------------------------------------------
#     # OPEN ADD PERSON DIALOG
#     # ---------------------------------------------
#     def open_add_person_dialog(self):
#         dialog = AddPersonDialog(self)
#         dialog.person_added.connect(self.add_person_from_dialog)
#         dialog.exec()

#     def add_person_from_dialog(self, data):
#         """Refresh table after a person is added."""
#         self.load_people()

#     # ---------------------------------------------
#     # SEND MAIL
#     # ---------------------------------------------
#     def open_send_mail_dialog(self):
#         # Retrieve updated people list from DB
#         people = PersonService.get_all_people()
#         people_names = [f"{p['first_name']} {p['last_name']}" for p in people]

#         dialog = SendMailDialog(people_names, self)
#         dialog.exec()

#     # ---------------------------------------------
#     # FILTER TABLE
#     # ---------------------------------------------
#     def filter_table(self, text):
#         text = text.lower().strip()

#         for row in range(self.table.rowCount()):
#             name = self.table.item(row, 0).text().lower()
#             email = self.table.item(row, 1).text().lower()

#             is_match = text in name or text in email
#             self.table.setRowHidden(row, not is_match)

#     # ---------------------------------------------
#     # QSS THEME
#     # ---------------------------------------------
#     def load_styles(self):
#         return """
#         /* MAIN COLORS */
#         * {
#             font-family: 'Segoe UI', sans-serif;
#             font-size: 14px;
#         }

#         #sidebar {
#             background: qlineargradient(spread:pad, x1:0, y1:0.267, x2:1, y2:0.471, stop:0 rgba(2, 101, 195, 255), stop:1 rgba(44, 47, 132, 255));
#             border-right: 1px solid #E5E7EB;
#         }

#         #appTitle {
#             font-size: 22px;
#             font-weight: 600;
#             color: white;
#         }

#         #sidebarBtn {
#             background: transparent;
#             color: white;
#             font-weight: 900;
#             padding: 12px;
#             text-align: left;
#             border-radius: 6px;
#         }
#         #sidebarBtn:hover {
#             background: rgba(19,99,223,0.12);
#         }

#         /* MAIN AREA */
#         #mainArea {
#             background: rgba(2, 101, 195, 255);
#         }

#         /* TOPBAR */
#         #topbar {
#             background: #FFFFFF;
#             border: 1px solid #E5E7EB;
#             border-radius: 8px;
#         }

#         #searchBox {
#             background: rgb(218, 216, 216);
#             border-radius: 6px;
#             padding: 8px;
#             border: 1px solid #CBD5E1;
#             color: black;
#         }

#         /* BUTTONS */
#         #primaryBtn {
#             background: #1363DF;
#             color: #FFFFFF;
#             padding: 8px 14px;
#             border-radius: 6px;
#         }
#         #primaryBtn:hover {
#             background: #0F52B3;
#         }

#         #secondaryBtn {
#             background: #EEF4FF;
#             color: #1363DF;
#             padding: 8px 14px;
#             border-radius: 6px;
#             border: 1px solid rgba(19,99,223,0.12);
#         }

#         /* TABLE */
#         #peopleTable {
#             background: #FFFFFF;
#             border-radius: 8px;
#             color: black;
#         }
#         QHeaderView::section {
#             background: #F8FAFC;
#             padding: 10px;
#             border: none;
#             font-weight: 600;
#             color: black;
#         }
#         QTableWidget::item {
#             padding: 2px;
#         }
#         QTableWidget::item:selected {
#             background: rgba(19,99,223,0.15);
#             color: #0F172A;
    
#         }
#         """

# if __name__ == "__main__":
#     app = QApplication([])
#     win = MainWindow()
#     win.show()
#     app.exec()

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFrame,
    QPushButton, QLabel, QLineEdit, QTableWidget, QTableWidgetItem,
    QHeaderView, QAbstractItemView, QMessageBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

# Correct imports (adjust if they are in folders)


from backend.person_service import PersonService
from add_person import AddPersonDialog
from send_mail import SendMailDialog

from backend.person_service import PersonService
from backend.history_service import HistoryService

from smtp_settings import SMTPSettingsDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mail Broadcast System")
        self.setMinimumSize(1100, 650)
        # 
        self.setStyleSheet(self.load_styles())

        main_container = QWidget()
        main_layout = QHBoxLayout(main_container)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # ----------------------------------
        # SIDEBAR
        # ----------------------------------
        self.sidebar = QFrame()
        self.sidebar.setObjectName("sidebar")
        self.sidebar.setFixedWidth(220)

        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(20, 20, 20, 20)
        sidebar_layout.setSpacing(20)

        app_title = QLabel("Mail System")
        app_title.setObjectName("appTitle")
        
        btn_people = QPushButton(" People")
        btn_people.setObjectName("sidebarBtn")
        btn_people.setIcon(QIcon.fromTheme("user"))  
              
        btn_send = QPushButton(" Send Mail")
        btn_send.setObjectName("sidebarBtn")
        btn_send.setIcon(QIcon.fromTheme("mail-send"))
        
        btn_settings = QPushButton(" Settings")
        btn_settings.setObjectName("sidebarBtn")
        btn_settings.setIcon(QIcon.fromTheme("settings"))

        sidebar_layout.addWidget(app_title)
        sidebar_layout.addSpacing(10)
        sidebar_layout.addWidget(btn_people)
        sidebar_layout.addWidget(btn_send)
        sidebar_layout.addWidget(btn_settings)
        sidebar_layout.addStretch()

        # ----------------------------------
        # MAIN AREA
        # ----------------------------------
        self.main_area = QFrame()
        self.main_area.setObjectName("mainArea")
        
        main_area_layout = QVBoxLayout(self.main_area)
        main_area_layout.setContentsMargins(20, 20, 20, 20)
        main_area_layout.setSpacing(15)

        # ----------------------------------
        # TOPBAR
        # ----------------------------------
        # topbar = QFrame()
        # topbar_layout = QHBoxLayout(topbar)

        # self.search = QLineEdit()
        # self.search.setPlaceholderText("Search people…")
        # self.search.textChanged.connect(self.filter_table)

        # add_btn = QPushButton("Add Person")
        # add_btn.clicked.connect(self.open_add_person_dialog)

        # refresh_btn = QPushButton("Refresh")
        # refresh_btn.clicked.connect(self.load_people)

        # topbar_layout.addWidget(self.search)
        # topbar_layout.addStretch()
        # topbar_layout.addWidget(add_btn)
        # topbar_layout.addWidget(refresh_btn)
        
        topbar = QFrame()
        topbar.setObjectName("topbar")
        topbar_layout = QHBoxLayout(topbar)
        topbar_layout.setContentsMargins(10, 10, 10, 10)

        self.search = QLineEdit()
        self.search.setPlaceholderText("Search people…")
        self.search.setObjectName("searchBox")
        self.search.textChanged.connect(self.filter_table)

        import_btn = QPushButton("Import CSV")
        import_btn.setObjectName("secondaryBtn")

        add_btn = QPushButton("Add Person")
        add_btn.setObjectName("primaryBtn")
        add_btn.clicked.connect(self.open_add_person_dialog)

        edit_btn = QPushButton("Edit")
        edit_btn.setObjectName("secondaryBtn")

        delete_btn = QPushButton("Delete")
        delete_btn.setObjectName("secondaryBtn")

        refresh_btn = QPushButton("Refresh")
        refresh_btn.setObjectName("secondaryBtn")
        refresh_btn.clicked.connect(self.load_people)

        topbar_layout.addWidget(self.search)
        topbar_layout.addStretch()
        topbar_layout.addWidget(import_btn)
        topbar_layout.addWidget(add_btn)
        topbar_layout.addWidget(edit_btn)
        topbar_layout.addWidget(delete_btn)
        topbar_layout.addWidget(refresh_btn)


        # ----------------------------------
        # TABLE
        # ----------------------------------
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Name", "Email", "Group", "Added"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setObjectName("peopleTable")
        
        # Load data initially
        self.load_people()

        main_area_layout.addWidget(topbar)
        main_area_layout.addWidget(self.table)

        main_layout.addWidget(self.sidebar)
        main_layout.addWidget(self.main_area)

        self.setCentralWidget(main_container)

        # Connect sidebar send mail button
        btn_send.clicked.connect(self.open_send_mail_dialog)
        edit_btn.clicked.connect(self.edit_selected_person)
        delete_btn.clicked.connect(self.delete_selected_person)
        btn_settings.clicked.connect(self.open_smtp_settings)

        

    # ---------------------------------------------------
    # ADD TABLE ROW
    # ---------------------------------------------------
    def add_table_row(self, name, email, group_name, created_at):
        row = self.table.rowCount()
        self.table.insertRow(row)

        self.table.setItem(row, 0, QTableWidgetItem(name))
        self.table.setItem(row, 1, QTableWidgetItem(email))
        self.table.setItem(row, 2, QTableWidgetItem(group_name))
        self.table.setItem(row, 3, QTableWidgetItem(created_at))

    # ---------------------------------------------------
    # LOAD PEOPLE FROM DB
    # ---------------------------------------------------
    def load_people(self):
        self.table.setRowCount(0)

        try:
            people = PersonService.get_all_people()
            for p in people:
                self.add_table_row(
                    p["name"], p["email"], p["group_name"], p["created_at"]
                )
        except Exception as e:
            print("Error loading people:", e)

    # ---------------------------------------------------
    # FILTERING   insert into people (name, email, group_name, created_at) VALUES("loop", "lopwew@gmail.com", "all", "loop")
    # ---------------------------------------------------
    def filter_table(self, text):
        text = text.lower().strip()

        for row in range(self.table.rowCount()):
            name = self.table.item(row, 0).text().lower()
            email = self.table.item(row, 1).text().lower()
            visible = text in name or text in email
            self.table.setRowHidden(row, not visible)

    # ---------------------------------------------------
    # OPEN DIALOGS
    # --------------------------------------------------- get_all_people
    def open_add_person_dialog(self):
        if AddPersonDialog is None:
            print("AddPersonDialog not found")
            return
        dialog = AddPersonDialog(self)
        if dialog.exec():
            self.load_people()

    def open_send_mail_dialog(self):
        if SendMailDialog is None:
            print("SendMailDialog not found")
            return
        dialog = SendMailDialog(self)
        dialog.exec()
        
    def open_add_person_dialog(self):
        dialog = AddPersonDialog(self)
        # dialog.person_added.connect(self.add_person_from_dialog)
        dialog.exec()

    def get_selected_person_id(self):
        row = self.table.currentRow()
        if row < 0:
            return None

        email = self.table.item(row, 1).text()
        # Lookup ID using email
        people = PersonService.get_all_people()
        for p in people:
            if p["email"] == email:
                return p["id"]

        return None


    def edit_selected_person(self):
        person_id = self.get_selected_person_id()

        if not person_id:
            QMessageBox.warning(self, "Select Person", "Please select a person to edit.")
            return

        from edit_person import EditPersonDialog
        dialog = EditPersonDialog(person_id, self)

        if dialog.exec():
            self.load_people()


    def delete_selected_person(self):
        person_id = self.get_selected_person_id()

        if not person_id:
            QMessageBox.warning(self, "Select Person", "Please select a person to delete.")
            return

        # Confirm deletion
        confirm = QMessageBox.question(
            self,
            "Delete Person",
            "Are you sure you want to delete this person?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.No:
            return

        try:
            PersonService.delete_person(person_id)
            QMessageBox.information(self, "Deleted", "Person deleted successfully.")
            self.load_people()

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            
    def open_smtp_settings(self):
        dlg = SMTPSettingsDialog(self)
        dlg.exec()
            

    # ---------------------------------------------
    # QSS THEME
    # ---------------------------------------------
    def load_styles(self):
        return """
        /* MAIN COLORS */
        * {
            font-family: 'Segoe UI', sans-serif;
            font-size: 14px;
        }

        #sidebar {
            background: qlineargradient(spread:pad, x1:0, y1:0.267, x2:1, y2:0.471, stop:0 rgba(2, 101, 195, 255), stop:1 rgba(44, 47, 132, 255));
            border-right: 1px solid #E5E7EB;
        }

        #appTitle {
            font-size: 22px;
            font-weight: 600;
            color: white;
        }

        #sidebarBtn {
            background: transparent;
            color: white;
            font-weight: 900;
            padding: 12px;
            text-align: left;
            border-radius: 6px;
        }
        #sidebarBtn:hover {
            background: rgba(19,99,223,0.12);
        }

        /* MAIN AREA */
        #mainArea {
            background: rgba(2, 101, 195, 255);
        }

        /* TOPBAR */
        #topbar {
            background: #FFFFFF;
            border: 1px solid #E5E7EB;
            border-radius: 8px;
        }

        #searchBox {
            background: rgb(218, 216, 216);
            border-radius: 6px;
            padding: 8px;
            border: 1px solid #CBD5E1;
            color: black;
        }

        /* BUTTONS */
        #primaryBtn {
            background: #1363DF;
            color: #FFFFFF;
            padding: 8px 14px;
            border-radius: 6px;
        }
        #primaryBtn:hover {
            background: #0F52B3;
        }

        #secondaryBtn {
            background: #EEF4FF;
            color: #1363DF;
            padding: 8px 14px;
            border-radius: 6px;
            border: 1px solid rgba(19,99,223,0.12);
        }

        /* TABLE */
        #peopleTable {
            background: #FFFFFF;
            border-radius: 8px;
            color: black;
        }
        QHeaderView::section {
            background: #F8FAFC;
            padding: 10px;
            border: none;
            font-weight: 600;
            color: black;
        }
        QTableWidget::item {
            padding: 2px;
        }
        QTableWidget::item:selected {
            background: rgba(19,99,223,0.15);
            color: #0F172A;
    
        }
        """
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
