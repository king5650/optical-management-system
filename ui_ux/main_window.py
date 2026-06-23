from PySide6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit, QMessageBox, QDialog
from PySide6.QtCore import QThreadPool
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from api.order_api import OrderAPI

from api.order_api import OrderAPI
from api.payment_api import PaymentAPI
from workers import Worker


class MainWindow(QMainWindow):  
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Optical Management System")
        self.resize(900, 600)

        self.threadpool = QThreadPool()

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.order_list = OrderListWidget(self)
        self.create_order = CreateOrderWidget(self)

        self.tabs.addTab(self.order_list, "Orders")
        self.tabs.addTab(self.create_order, "Create Order")
        
class OrderListWidget(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Patient", "Status", "Total"])

        layout.addWidget(self.table)

        refresh_btn = QPushButton("Refresh")
        refresh_btn.clicked.connect(self.load_orders)

        layout.addWidget(refresh_btn)
        self.setLayout(layout)

        self.load_orders()        
        
    def load_orders(self):
        worker = Worker(OrderAPI.get_orders)
        worker.signals.finished.connect(self.populate_table)
        worker.signals.error.connect(self.show_error)

        self.parent.threadpool.start(worker)        
        
    def populate_table(self, data):
        self.table.setRowCount(len(data))

        for row, order in enumerate(data):
            self.table.setItem(row, 0, QTableWidgetItem(str(order["id"])))
            self.table.setItem(row, 1, QTableWidgetItem(str(order["patient"])))
            self.table.setItem(row, 2, QTableWidgetItem(order["status"]))
            self.table.setItem(row, 3, QTableWidgetItem(str(order["total_amount"])))        
            
class CreateOrderWidget(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent

        layout = QVBoxLayout()

        self.patient_id = QLineEdit()
        self.patient_id.setPlaceholderText("Patient ID")

        self.product_id = QLineEdit()
        self.product_id.setPlaceholderText("Product ID")

        self.quantity = QLineEdit()
        self.quantity.setPlaceholderText("Quantity")

        self.price = QLineEdit()
        self.price.setPlaceholderText("Unit Price")

        btn = QPushButton("Create Order")
        btn.clicked.connect(self.create_order)

        layout.addWidget(self.patient_id)
        layout.addWidget(self.product_id)
        layout.addWidget(self.quantity)
        layout.addWidget(self.price)
        layout.addWidget(btn)

        self.setLayout(layout)            
        
        
    def create_order(self):
        data = {
            "patient": int(self.patient_id.text()),
            "prescription": 1,
            "items": [
                {
                    "product": int(self.product_id.text()),
                    "quantity": int(self.quantity.text()),
                    "unit_price": float(self.price.text())
                }
            ]
        }

        worker = Worker(OrderAPI.create_order, data)
        worker.signals.finished.connect(self.success)
        worker.signals.error.connect(self.error)

        self.parent.threadpool.start(worker)
        
    def success(self, data):
        QMessageBox.information(self, "Success", "Order created")

    def error(self, err):
        QMessageBox.critical(self, "Error", err)
        
class PaymentDialog(QDialog):
    def __init__(self, order_id, parent):
        super().__init__()

        self.order_id = order_id
        self.parent = parent

        layout = QVBoxLayout()

        self.amount = QLineEdit()
        self.amount.setPlaceholderText("Amount")

        btn = QPushButton("Pay")
        btn.clicked.connect(self.pay)

        layout.addWidget(self.amount)
        layout.addWidget(btn)

        self.setLayout(layout)

    def pay(self):
        data = {
            "order": self.order_id,
            "amount": float(self.amount.text()),
            "payment_method": "cash"
        }

        worker = Worker(PaymentAPI.add_payment, data)
        worker.signals.finished.connect(lambda _: self.accept())
        worker.signals.error.connect(lambda e: QMessageBox.critical(self, "Error", e))

        self.parent.threadpool.start(worker)
        
if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())                                        