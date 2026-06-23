
from PySide6.QtWidgets import QMenu, QMainWindow
from PySide6.QtGui import QAction
from ui_MainDashbrad import Ui_MainWindow  # Import the UI file for the main system


class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("My SideBar")
        
        
        self.icon_widget.setHidden(True)

        
        self.dashboard1.clicked.connect(self.switch_to_dashboardpage)
        self.dashboard2.clicked.connect(self.switch_to_dashboardpage)
        self.dashboard1.clicked.connect(self.switch_to_patientpage)
        self.dashboard1.clicked.connect(self.switch_to_patientpage)
        self.dashboard1.clicked.connect(self.switch_to_medicalreportpage)
        self.dashboard1.clicked.connect(self.switch_to_medicalreportpage)
        self.dashboard1.clicked.connect(self.switch_to_receipage)
        self.dashboard1.clicked.connect(self.switch_to_receipage)        
        
        

        
    def switch_to_dashboardpage(self):
        self.stackedWidget.setCurrentIndex(0)
    def switch_to_patientpage(self):
        self.stackedWidget.setCurrentIndex(0)
    def switch_to_medicalreportpage(self):
        self.stackedWidget.setCurrentIndex(0)
    def switch_to_receipage(self):
        self.stackedWidget.setCurrentIndex(0)
    def switch_to_dashboardpage(self):
        self.stackedWidget.setCurrentIndex(0)
    def switch_to_dashboardpage(self):
        self.stackedWidget.setCurrentIndex(0)                        


