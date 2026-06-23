import sys
import os
import requests
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QLineEdit, QLabel,
    QVBoxLayout, QHBoxLayout, QFileDialog, QProgressBar, QDateTimeEdit
)
from PySide6.QtCore import Qt, QTimer, QDateTime, QCoreApplication

BACKUP_URL = "http://127.0.0.1:8000/auth/backup/"
RESTORE_URL = "http://127.0.0.1:8000/auth/restore/"

class BackupRestoreApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🔧 Backup & Restore Utility")
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        self.setup_ui()
        self.setStyleSheet("""
                           
            QWidget{
                background-color: qlineargradient(spread:pad, x1:0, y1:0.267, x2:1, y2:0.471, stop:0 rgba(2, 101, 195, 255), stop:1 rgba(44, 47, 132, 255));
                font-weight: 700;

            }
            QLineEdit {
                background-color: white;
                color: black;
                font-weight: bold;
                font-size: 14px;
            }
            QLabel{
                background-color: none;
            }
            QPushButton {
                /*background-color: #34495e;*/
                background-color: white/*rgb(236, 130, 43)*/;
                border: none;
                border-radius: 10px;
                color: black;
                width: 80px;
                height: 50px;
                spacing: 10px;
                font-family: "Segoe UI, Inter, Roboto, Arial"
            }
            QPushButton:hover {
                background-color: #e74c3c;
            }
            QDateTime{
                background-color: #ecf0f1;
                border: 1px solid #bdc3c7;
                padding: 5px;
                height: 900px;
            }
            /* QDateTimeEdit */
            QDateTimeEdit {
                background-color: #ffffff;
                border: 1px solid #dcdfe6;
                border-radius: 4px;
                padding: 8px 10px;
                color: #333333;
                selection-background-color: #a8d9ff;
            }
            QDateTimeEdit::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left: 1px solid #dcdfe6;
                image: url(images/plus_48px.png); /* Optional: path to an icon */
            }
            QDateTimeEdit::drop-down:hover {
                background-color: #f0f2f5;
            }
            QDateTimeEdit:on { /* When the calendar popup is open */
                border: 1px solid #4a90e2;
            }
            QCalendarWidget {
                border: 1px solid #dcdfe6;
                border-radius: 4px;
                background-color: #ffffff;
                color: black;
                font-weight: bold;
            }
            QCalendarWidget QAbstractItemView:enabled { /* Days in the calendar */
                color: white;
            }
            QCalendarWidget QAbstractItemView:selected {
                background-color: #4a90e2;
                color: black;
            }
            QCalendarWidget QToolButton { /* Month/Year navigation buttons */
                background-color: #e9ecef;
                border: none;
                border-radius: 3px;
                margin: 5px;
            }
            QCalendarWidget QToolButton:hover {
                background-color: #dcdfe6;
            }
            QCalendarWidget QToolButton::menu-indicator {
                image: none; /* Hide default menu indicator */
            }            
        """)
    def setup_ui(self):
        layout = QVBoxLayout()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        # --- BACKUP SECTION ---
        #layout.addWidget(QLabel("🗂 Backup System Data"))

        self.backup_title_label = QLabel("🗂 Backup System Data")
        layout.addWidget(self.backup_title_label)
        
        
        self.backup_path_input = QLineEdit()
        self.backup_path_input.setPlaceholderText("Backup Folder Path...")
        
        self.btn_browse_backup = QPushButton("Browse…")
        self.btn_browse_backup.clicked.connect(self.browse_backup_path)
        # btn_browse_backup.setStyleSheet("background-color: #34495e; padding: 5px; color: black; width: 50px; height: 30px;")
        
        self.btn_create_backup = QPushButton("Create Backup")
        self.btn_create_backup.clicked.connect(self.create_backup)
       
        
        
        self.lbl_backup_status = QLabel()
        self.lbl_backup_status.setStyleSheet("color: green;")

        # Layout for backup path
        backup_path_layout = QHBoxLayout()
        backup_path_layout.addWidget(self.backup_path_input)
        backup_path_layout.addWidget(self.btn_browse_backup)

        layout.addLayout(backup_path_layout)
        layout.addWidget(self.btn_create_backup)
        layout.addWidget(self.lbl_backup_status)

        layout.addSpacing(20)

        # --- RESTORE SECTION ---
        #layout.addWidget(QLabel("🔄 Restore System Data"))
        self.restore_title_label = QLabel("🔄 Restore System Data")
        layout.addWidget(self.restore_title_label)        

        self.restore_file_input = QLineEdit()
        self.restore_file_input.setPlaceholderText("Select Backup File (.zip)")
        
        self.btn_browse_restore = QPushButton("Browse…")
        self.btn_browse_restore.clicked.connect(self.browse_restore_file)
        # btn_browse_restore.setStyleSheet("background-color: #34495e; margin: 15px; color: white; width: 50px; height: 20px;")

        
        self.btn_restore_data = QPushButton("Restore from Backup")
        self.btn_restore_data.clicked.connect(self.restore_backup)

        self.lbl_restore_status = QLabel()
        self.lbl_restore_status.setStyleSheet("color: green;")

        # Layout for restore path
        restore_path_layout = QHBoxLayout()
        restore_path_layout.addWidget(self.restore_file_input)
        restore_path_layout.addWidget(self.btn_browse_restore)

        layout.addLayout(restore_path_layout)
        layout.addWidget(self.btn_restore_data)
        layout.addWidget(self.lbl_restore_status)

        layout.addSpacing(20)

        # --- OPTIONAL: Progress & Schedule ---
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        # layout.addWidget(QLabel("🕓 Schedule Future Backup (optional)"))
        self.schedule_label = QLabel("🕓 Schedule Future Backup (optional)")
        layout.addWidget(self.schedule_label)
            
        self.scheduled_backup_time = QDateTimeEdit(QDateTime.currentDateTime())
        self.scheduled_backup_time.setCalendarPopup(True)

        self.btn_schedule_backup = QPushButton("Schedule Backup")
        self.btn_schedule_backup.clicked.connect(self.schedule_backup)

        layout.addWidget(self.scheduled_backup_time)
        layout.addWidget(self.btn_schedule_backup)

        self.setLayout(layout)
        self.retranslate_ui() 
    def browse_backup_path(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Backup Folder")
        if folder:
            self.backup_path_input.setText(folder)

    def browse_restore_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Backup File", "", "ZIP Files (*.zip)")
        if file_path:
            self.restore_file_input.setText(file_path)

    def create_backup(self):
        path = self.backup_path_input.text()
        if not path:
            self.lbl_backup_status.setText("❌ Please select a backup folder path.")
            return

        self.lbl_backup_status.setText("⏳ Creating backup...")
        self.progress_bar.setValue(10)

        try:
            res = requests.post(BACKUP_URL, data={"path": path})
            if res.status_code == 200:
                file = res.json().get("file")
                self.lbl_backup_status.setText(f"✅ Backup created at: {file}")
                self.progress_bar.setValue(100)
            else:
                self.lbl_backup_status.setText(f"❌ Error: {res.json().get('error')}")
                self.progress_bar.setValue(0)
        except Exception as e:
            self.lbl_backup_status.setText(f"❌ Exception: {str(e)}")
            self.progress_bar.setValue(0)

    def restore_backup(self):
        file_path = self.restore_file_input.text()
        if not file_path:
            self.lbl_restore_status.setText("❌ Please select a backup file.")
            return

        self.lbl_restore_status.setText("⏳ Restoring backup...")
        self.progress_bar.setValue(10)

        try:
            res = requests.post(RESTORE_URL, data={"file": file_path})
            if res.status_code == 200:
                self.lbl_restore_status.setText("✅ Restore completed successfully.")
                self.progress_bar.setValue(100)
            else:
                self.lbl_restore_status.setText(f"❌ Error: {res.json().get('error')}")
                self.progress_bar.setValue(0)
        except Exception as e:
            self.lbl_restore_status.setText(f"❌ Exception: {str(e)}")
            self.progress_bar.setValue(0)

    # def schedule_backup(self):
    #     dt = self.scheduled_backup_time.dateTime().toString(Qt.ISODate)
    #     self.lbl_backup_status.setText(f"🕓 Scheduled backup time set to: {dt}")
    #     # Future: Implement QTimer or external cron job

    def schedule_backup(self):
        scheduled_qdatetime = self.scheduled_backup_time.dateTime()
        now_qdatetime = QDateTime.currentDateTime()

        # Calculate milliseconds until scheduled time
        msecs_to_backup = now_qdatetime.msecsTo(scheduled_qdatetime)

        if msecs_to_backup <= 0:
            self.lbl_backup_status.setText("❌ Scheduled time is in the past. Please choose a future time.")
            return

        # Format and show scheduled time
        dt_string = scheduled_qdatetime.toString(Qt.ISODate)
        self.lbl_backup_status.setText(f"🕓 Scheduled backup time set to: {dt_string}")

        # Schedule the backup using QTimer
        QTimer.singleShot(msecs_to_backup, self.trigger_scheduled_backup)
    def trigger_scheduled_backup(self):
        self.lbl_backup_status.setText("⏳ Performing scheduled backup...")
        try:
            self.create_backup()  # Call your backup method here
            self.lbl_backup_status.setText("✅ Scheduled backup completed successfully.")
        except Exception as e:
            self.lbl_backup_status.setText(f"❌ Backup failed: {str(e)}")


    def retranslate_ui(self):
        _translate = QCoreApplication.translate

        self.setWindowTitle(_translate("BackupRestoreApp", "🔧 Backup & Restore Utility"))

        # Backup section
        self.backup_title_label.setText(_translate("BackupRestoreApp", "🗂 Backup System Data"))
        self.backup_path_input.setPlaceholderText(_translate("BackupRestoreApp", "Backup Folder Path..."))
        self.btn_browse_backup.setText(_translate("BackupRestoreApp", "Browse…"))
        self.btn_create_backup.setText(_translate("BackupRestoreApp", "Create Backup"))

        # Restore section
        self.restore_title_label.setText(_translate("BackupRestoreApp", "🔄 Restore System Data"))
        self.restore_file_input.setPlaceholderText(_translate("BackupRestoreApp", "Select Backup File (.zip)"))
        self.btn_browse_restore.setText(_translate("BackupRestoreApp", "Browse…"))
        self.btn_restore_data.setText(_translate("BackupRestoreApp", "Restore from Backup"))

        # Schedule section
        self.schedule_label.setText(_translate("BackupRestoreApp", "🕓 Schedule Future Backup (optional)"))
        self.btn_schedule_backup.setText(_translate("BackupRestoreApp", "Schedule Backup"))


    # def setup_ui(self):
    #     layout = QVBoxLayout(self)

    #     # --- BACKUP SECTION ---
    #     self.backup_title_label = QLabel("🗂 Backup System Data")
    #     layout.addWidget(self.backup_title_label)

    #     self.backup_path_input = QLineEdit()
    #     self.backup_path_input.setPlaceholderText("Backup Folder Path...")

    #     self.btn_browse_backup = QPushButton("Browse…")
    #     self.btn_browse_backup.clicked.connect(self.browse_backup_path)

    #     self.btn_create_backup = QPushButton("Create Backup")
    #     self.btn_create_backup.clicked.connect(self.create_backup)

    #     # RESTORE
    #     self.restore_title_label = QLabel("🔄 Restore System Data")
    #     layout.addWidget(self.restore_title_label)

    #     self.restore_file_input = QLineEdit()
    #     self.restore_file_input.setPlaceholderText("Select Backup File (.zip)")

    #     self.btn_browse_restore = QPushButton("Browse…")
    #     self.btn_browse_restore.clicked.connect(self.browse_restore_file)

    #     self.btn_restore_data = QPushButton("Restore from Backup")
    #     self.btn_restore_data.clicked.connect(self.restore_backup)

    #     # SCHEDULE
    #     self.schedule_label = QLabel("🕓 Schedule Future Backup (optional)")
    #     layout.addWidget(self.schedule_label)

    #     self.btn_schedule_backup = QPushButton("Schedule Backup")
    #     self.btn_schedule_backup.clicked.connect(self.schedule_backup)

    #     # Call translation here
    #     self.retranslate_ui()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BackupRestoreApp()
    window.show()
    sys.exit(app.exec())
