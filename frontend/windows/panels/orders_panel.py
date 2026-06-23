"""
windows/panels/orders_panel.py — Order list and creation

CONNECTION FLOWS:
  Load         → GET /api/orders/?status=<filter>
  Row double-click → opens OrderDetailDialog
  Create       → POST /api/orders/
  Status filter → GET /api/orders/?status=draft  etc.
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QComboBox, QLineEdit,
    QHeaderView, QFrame, QMessageBox, QDialog, QFormLayout,
    QSpinBox, QDoubleSpinBox, QTextEdit, QScrollArea, QDateEdit
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor

from api_client import api
from assets.styles import PRIMARY, TEXT_MUTED, STATUS_COLOURS, PAYMENT_COLOURS
from workers.api_worker import ApiWorker
from windows.panels.order_detail_dialog import OrderDetailDialog


STATUS_OPTIONS = ["all", "draft", "confirmed", "in_progress", "ready", "delivered", "completed", "cancelled"]


# class OrdersPanel(QWidget):
#     """
#     Displays the order list with filtering by status and a search bar.
#     Double-clicking a row opens OrderDetailDialog for full management.
#     """

#     def __init__(self):
#         super().__init__()
#         self._workers = []
#         self._all_orders = []
#         self._build_ui()
#         self.refresh()

#     # ──────────────────────────────────────────────────────────────────────
#     # UI construction
#     # ──────────────────────────────────────────────────────────────────────

#     def _build_ui(self):
#         root = QVBoxLayout(self)
#         root.setContentsMargins(28, 24, 28, 24)
#         root.setSpacing(16)

#         # ── Header ─────────────────────────────────────────────────────
#         header = QHBoxLayout()
#         col = QVBoxLayout()
#         col.addWidget(self._h1("Orders"))
#         col.addWidget(self._sub("Create, track, and manage optical orders"))
#         header.addLayout(col)
#         header.addStretch()

#         new_btn = QPushButton("＋  New Order")
#         new_btn.setObjectName("primary_btn")
#         new_btn.setFixedHeight(38)
#         new_btn.clicked.connect(self._open_create_dialog)
#         header.addWidget(new_btn)
#         root.addLayout(header)

#         # ── Toolbar (filter + search) ───────────────────────────────────
#         toolbar = QHBoxLayout()

#         self.status_filter = QComboBox()
#         self.status_filter.addItems([s.replace("_", " ").title() for s in STATUS_OPTIONS])
#         self.status_filter.setFixedHeight(34)
#         self.status_filter.setFixedWidth(160)
#         self.status_filter.currentIndexChanged.connect(self.refresh)
#         toolbar.addWidget(QLabel("Filter:"))
#         toolbar.addWidget(self.status_filter)

#         self.search_input = QLineEdit()
#         self.search_input.setPlaceholderText("Search by order number or patient…")
#         self.search_input.setFixedHeight(34)
#         self.search_input.textChanged.connect(self._filter_table)
#         toolbar.addWidget(self.search_input)

#         refresh_btn = QPushButton("⟳ Refresh")
#         refresh_btn.setObjectName("secondary_btn")
#         refresh_btn.setFixedHeight(34)
#         refresh_btn.clicked.connect(self.refresh)
#         toolbar.addWidget(refresh_btn)
#         root.addLayout(toolbar)

#         # ── Table ───────────────────────────────────────────────────────
#         self.table = QTableWidget(0, 7)
#         self.table.setHorizontalHeaderLabels([
#             "Order #", "Patient", "Status", "Total (XAF)",
#             "Paid (XAF)", "Balance (XAF)", "Payment"
#         ])
#         self.table.setEditTriggers(QTableWidget.NoEditTriggers)
#         self.table.setSelectionBehavior(QTableWidget.SelectRows)
#         self.table.setAlternatingRowColors(True)
#         self.table.horizontalHeader().setStretchLastSection(True)
#         self.table.verticalHeader().setVisible(False)
#         self.table.setShowGrid(False)
#         self.table.doubleClicked.connect(self._open_detail)
#         root.addWidget(self.table)

#         # ── Status bar ──────────────────────────────────────────────────
#         self.status_bar = QLabel("Loading…")
#         self.status_bar.setStyleSheet(f"color: {TEXT_MUTED}; font-size: 12px;")
#         root.addWidget(self.status_bar)

#     # ──────────────────────────────────────────────────────────────────────
#     # Data loading
#     # ──────────────────────────────────────────────────────────────────────

#     def refresh(self):
#         self.status_bar.setText("Loading orders…")
#         idx = self.status_filter.currentIndex()
#         status_key = STATUS_OPTIONS[idx]
#         status_param = None if status_key == "all" else status_key

#         w = ApiWorker(api.list_orders, status_param)
#         w.success.connect(self._on_orders)
#         w.error.connect(self._on_error)
#         w.start()
#         self._workers.append(w)

#     def _on_orders(self, data: dict):
#         self._all_orders = data.get("orders", [])
#         self._populate_table(self._all_orders)
#         self.status_bar.setText(f"{len(self._all_orders)} orders  •  double-click a row to open")

#     def _populate_table(self, orders: list):
#         self.table.setRowCount(0)
#         for order in orders:
#             row = self.table.rowCount()
#             self.table.insertRow(row)

#             order_num = order.get("order_number", str(order.get("id", "")))
#             # Patient may be an ID or a nested dict depending on serializer
#             patient = order.get("patient_name") or str(order.get("patient", ""))
#             status  = order.get("status", "")
#             total   = order.get("total_amount", "0")
#             paid    = order.get("amount_paid", "0")
#             balance = order.get("balance", "0")
#             pay_status = order.get("payment_status", "unpaid")

#             self.table.setItem(row, 0, QTableWidgetItem(order_num))
#             self.table.setItem(row, 1, QTableWidgetItem(patient))

#             # Status badge cell
#             status_item = QTableWidgetItem(status.replace("_", " ").title())
#             bg, fg = STATUS_COLOURS.get(status, ("#e8eaed", "#3c4043"))
#             status_item.setBackground(QColor(bg))
#             status_item.setForeground(QColor(fg))
#             self.table.setItem(row, 2, status_item)

#             self.table.setItem(row, 3, QTableWidgetItem(f"{total}"))
#             self.table.setItem(row, 4, QTableWidgetItem(f"{paid}"))

#             balance_item = QTableWidgetItem(f"{balance}")
#             if float(balance) > 0:
#                 balance_item.setForeground(QColor("#d93025"))
#             self.table.setItem(row, 5, balance_item)

#             # Payment status badge
#             pay_item = QTableWidgetItem(pay_status.title())
#             pbg, pfg = PAYMENT_COLOURS.get(pay_status, ("#e8eaed", "#3c4043"))
#             pay_item.setBackground(QColor(pbg))
#             pay_item.setForeground(QColor(pfg))
#             self.table.setItem(row, 6, pay_item)

#             # Store full order data for the detail dialog
#             self.table.item(row, 0).setData(Qt.UserRole, order)

#         self.table.resizeColumnsToContents()

#     def _filter_table(self, query: str):
#         query = query.lower()
#         filtered = [
#             o for o in self._all_orders
#             if query in str(o.get("order_number", "")).lower()
#             or query in str(o.get("patient", "")).lower()
#         ]
#         self._populate_table(filtered)

#     # ──────────────────────────────────────────────────────────────────────
#     # Row double-click → detail dialog
#     # ──────────────────────────────────────────────────────────────────────

#     def _open_detail(self, index):
#         row = index.row()
#         item = self.table.item(row, 0)
#         if not item:
#             return
#         order_data = item.data(Qt.UserRole)
#         if not order_data:
#             return

#         dialog = OrderDetailDialog(order_data, self)
#         dialog.order_updated.connect(self.refresh)
#         dialog.exec()

#     # ──────────────────────────────────────────────────────────────────────
#     # Create order dialog
#     # ──────────────────────────────────────────────────────────────────────

#     def _open_create_dialog(self):
#         dialog = CreateOrderDialog(self)
#         if dialog.exec() == QDialog.Accepted:
#             self.refresh()

#     # ──────────────────────────────────────────────────────────────────────
#     # Helpers
#     # ──────────────────────────────────────────────────────────────────────

#     def _on_error(self, message: str):
#         self.status_bar.setText(f"Error: {message}")

#     def _h1(self, text):
#         l = QLabel(text)
#         l.setObjectName("section_title")
#         l.setFont(QFont("Segoe UI", 18, QFont.Bold))
#         return l

#     def _sub(self, text):
#         l = QLabel(text)
#         l.setObjectName("section_sub")
#         l.setStyleSheet(f"color: {TEXT_MUTED}; font-size: 12px;")
#         return l


# # ──────────────────────────────────────────────────────────────────────────────
# # Create Order dialog
# # ──────────────────────────────────────────────────────────────────────────────

# class CreateOrderDialog(QDialog):
#     """
#     Simple form to create a new order.

#     CONNECTION FLOW:
#     User fills form → clicks Create
#     → ApiWorker calls api.create_order(payload)
#     → POST /api/orders/
#     → OrderCreateSerializer.create() → OrderService.create_order()
#     → Order + OrderItems saved, totals calculated
#     → dialog closes, OrdersPanel refreshes
#     """

#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("Create New Order")
#         self.setFixedSize(540, 520)
#         self._workers = []
#         self._patients = []
#         self._inventory = []
#         self._build_ui()
#         self._load_patients()
#         self._load_inventory()

#     def _build_ui(self):
#         root = QVBoxLayout(self)
#         root.setContentsMargins(24, 24, 24, 24)
#         root.setSpacing(16)

#         title = QLabel("New Order")
#         title.setFont(QFont("Segoe UI", 14, QFont.Bold))
#         root.addWidget(title)

#         form = QFormLayout()
#         form.setSpacing(10)

#         self.order_num_input = QLineEdit()
#         self.order_num_input.setPlaceholderText("e.g. ORD-2025-001")
#         form.addRow("Order Number *", self.order_num_input)

#         self.patient_combo = QComboBox()
#         self.patient_combo.setPlaceholderText("Select patient…")
#         form.addRow("Patient *", self.patient_combo)

#         self.prescription_input = QLineEdit()
#         self.prescription_input.setPlaceholderText("Medical report ID")
#         form.addRow("Prescription ID *", self.prescription_input)

#         self.product_combo = QComboBox()
#         self.product_combo.setPlaceholderText("Select product…")
#         form.addRow("Product *", self.product_combo)

#         self.qty_spin = QSpinBox()
#         self.qty_spin.setRange(1, 999)
#         self.qty_spin.setValue(1)
#         form.addRow("Quantity *", self.qty_spin)

#         self.price_spin = QDoubleSpinBox()
#         self.price_spin.setRange(0.01, 9_999_999)
#         self.price_spin.setDecimals(0)
#         self.price_spin.setSuffix(" XAF")
#         form.addRow("Unit Price *", self.price_spin)

#         self.item_type_combo = QComboBox()
#         self.item_type_combo.addItems(["frame", "lens", "accessory", "service"])
#         form.addRow("Item Type", self.item_type_combo)

#         self.discount_spin = QDoubleSpinBox()
#         self.discount_spin.setRange(0, 999_999)
#         self.discount_spin.setDecimals(0)
#         self.discount_spin.setSuffix(" XAF")
#         form.addRow("Discount", self.discount_spin)

#         self.notes_input = QTextEdit()
#         self.notes_input.setFixedHeight(60)
#         self.notes_input.setPlaceholderText("Additional notes…")
#         form.addRow("Notes", self.notes_input)

#         root.addLayout(form)

#         self.error_lbl = QLabel("")
#         self.error_lbl.setStyleSheet("color: #d93025; font-size: 12px;")
#         self.error_lbl.setVisible(False)
#         root.addWidget(self.error_lbl)

#         # Buttons
#         btn_row = QHBoxLayout()
#         btn_row.addStretch()

#         cancel_btn = QPushButton("Cancel")
#         cancel_btn.setObjectName("secondary_btn")
#         cancel_btn.clicked.connect(self.reject)
#         btn_row.addWidget(cancel_btn)

#         self.create_btn = QPushButton("Create Order")
#         self.create_btn.setObjectName("primary_btn")
#         self.create_btn.clicked.connect(self._submit)
#         btn_row.addWidget(self.create_btn)
#         root.addLayout(btn_row)

#     def _load_patients(self):
#         w = ApiWorker(api.list_patients)
#         w.success.connect(self._on_patients)
#         w.error.connect(lambda e: None)
#         w.start()
#         self._workers.append(w)

#     def _on_patients(self, data: dict):
#         self._patients = data.get("patients", [])
#         self.patient_combo.clear()
#         for p in self._patients:
#             self.patient_combo.addItem(p.get("name", ""), p.get("id"))

#     def _load_inventory(self):
#         w = ApiWorker(api.fetch_inventory)
#         w.success.connect(self._on_inventory)
#         w.error.connect(lambda e: None)
#         w.start()
#         self._workers.append(w)

#     def _on_inventory(self, data: dict):
#         self._inventory = data.get("items", [])
#         self.product_combo.clear()
#         for item in self._inventory:
#             label = f"{item.get('type_name', item.get('type', ''))} — {item.get('unit_price', 0)} XAF"
#             self.product_combo.addItem(label, item.get("id"))
#             # Pre-fill price when product is selected
#         self.product_combo.currentIndexChanged.connect(self._on_product_selected)

#     def _on_product_selected(self, idx):
#         if idx < 0 or idx >= len(self._inventory):
#             return
#         price = self._inventory[idx].get("unit_price", 0)
#         try:
#             self.price_spin.setValue(float(price))
#         except (ValueError, TypeError):
#             pass

#     def _submit(self):
#         order_num    = self.order_num_input.text().strip()
#         patient_id   = self.patient_combo.currentData()
#         prescription = self.prescription_input.text().strip()
#         product_id   = self.product_combo.currentData()
#         qty          = self.qty_spin.value()
#         price        = self.price_spin.value()
#         item_type    = self.item_type_combo.currentText()
#         discount     = self.discount_spin.value()
#         notes        = self.notes_input.toPlainText().strip()

#         if not order_num:
#             self._show_error("Order number is required")
#             return
#         if not patient_id:
#             self._show_error("Please select a patient")
#             return
#         if not prescription:
#             self._show_error("Prescription ID is required")
#             return
#         if not product_id:
#             self._show_error("Please select a product")
#             return

#         payload = {
#             "order_number": order_num,
#             "patient": patient_id,
#             "prescription": int(prescription),
#             "discount": str(discount),
#             "notes": notes,
#             "items": [{
#                 "product":    product_id,
#                 "quantity":   qty,
#                 "unit_price": str(price),
#                 "item_type":  item_type,
#             }]
#         }

#         self.create_btn.setEnabled(False)
#         self.create_btn.setText("Creating…")

#         w = ApiWorker(api.create_order, payload)
#         w.success.connect(self._on_created)
#         w.error.connect(self._on_create_error)
#         w.start()
#         self._workers.append(w)

#     def _on_created(self, data: dict):
#         QMessageBox.information(self, "Success", "Order created successfully.")
#         self.accept()

#     def _on_create_error(self, message: str):
#         self.create_btn.setEnabled(True)
#         self.create_btn.setText("Create Order")
#         self._show_error(message)

#     def _show_error(self, msg: str):
#         self.error_lbl.setText(msg)
#         self.error_lbl.setVisible(True)



"""
windows/panels/orders_panel.py — updated version

CHANGES FROM PREVIOUS VERSION
──────────────────────────────
CreateOrderDialog is completely rewritten with:

  1. AUTO ORDER NUMBER
       No manual input. Field removed entirely from the form.
       Backend generates ORD-YYYY-NNNN automatically.

  2. PATIENT → PRESCRIPTION CASCADE
       Selecting a patient immediately fires:
         GET /api/prescriptions/by-patient/<id>/
       The prescription dropdown fills with that patient's reports,
       showing "REF-2025-007  (2025-11-03)" style labels.
       Shows "No prescriptions found" warning if the patient has none.

  3. CATEGORY → ITEM TYPE CASCADE
       Step 1: Category dropdown loads all ItemCategory rows on form open.
       Step 2: Selecting a category fires:
                 GET /api/item-types/by-category/<id>/
               Item type dropdown fills with types in that category.
       Step 3: Selecting an item type fires:
                 GET /api/inventory/by-type/<id>/
               Form auto-selects a matching InventoryItem and fills its price.
               Shows stock level in label: "VIP  (8 in stock)"
               Shows ⚠ warning if stock is low.

COMPLETE FORM FIELD ORDER:
  1. Patient *          ← combo, loads on open
  2. Prescription *     ← combo, loads after patient selected
  3. Category *         ← combo, loads on open (ItemCategory)
  4. Item Type *        ← combo, loads after category selected (ItemType)
    5. Quantity *         ← spinbox, min 1
    6. Unit Price *       ← spinbox, auto-filled from the selected item type
  8. Discount           ← spinbox, optional
  9. Expected Delivery  ← date input, optional
  10. Notes             ← text area, optional

  [Cancel]  [Create Order]

WORKERS:
  Every API call uses ApiWorker so the form stays responsive
  while data is loading. Dropdowns show "Loading..." while waiting.
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QComboBox, QLineEdit,
    QHeaderView, QFrame, QMessageBox, QDialog, QFormLayout,
    QSpinBox, QDoubleSpinBox, QTextEdit, QDateEdit, QSizePolicy, QScrollArea
)
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QFont, QColor

from api_client import api
from assets.styles import PRIMARY, TEXT_MUTED, STATUS_COLOURS, PAYMENT_COLOURS
from workers.api_worker import ApiWorker
from windows.panels.order_detail_dialog import OrderDetailDialog

STATUS_OPTIONS = [
    "all", "draft", "confirmed", "in_progress",
    "ready", "delivered", "completed", "cancelled"
]


# ─────────────────────────────────────────────────────────────────────────────
# Orders panel (list view — unchanged)
# ─────────────────────────────────────────────────────────────────────────────

class OrdersPanel(QWidget):
    """
    Displays the full order list with status filter and search.
    Double-clicking a row opens OrderDetailDialog for full management.
    """

    def __init__(self):
        super().__init__()
        self._workers = []
        self._all_orders = []
        self._build_ui()
        self.refresh()

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(28, 24, 28, 24)
        root.setSpacing(16)

        # Header
        header = QHBoxLayout()
        col = QVBoxLayout()
        col.addWidget(self._h1("Orders"))
        col.addWidget(self._sub("Create, track, and manage optical orders"))
        header.addLayout(col)
        header.addStretch()

        new_btn = QPushButton("＋  New Order")
        new_btn.setObjectName("primary_btn")
        new_btn.setFixedHeight(38)
        new_btn.clicked.connect(self._open_create_dialog)
        header.addWidget(new_btn)
        root.addLayout(header)

        # Toolbar
        toolbar = QHBoxLayout()
        self.status_filter = QComboBox()
        self.status_filter.addItems(
            [s.replace("_", " ").title() for s in STATUS_OPTIONS]
        )
        self.status_filter.setFixedHeight(34)
        self.status_filter.setFixedWidth(160)
        self.status_filter.currentIndexChanged.connect(self.refresh)
        toolbar.addWidget(QLabel("Filter:"))
        toolbar.addWidget(self.status_filter)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText(
            "Search by order number or patient…"
        )
        self.search_input.setFixedHeight(34)
        self.search_input.textChanged.connect(self._filter_table)
        toolbar.addWidget(self.search_input)

        refresh_btn = QPushButton("⟳  Refresh")
        refresh_btn.setObjectName("secondary_btn")
        refresh_btn.setFixedHeight(34)
        refresh_btn.clicked.connect(self.refresh)
        toolbar.addWidget(refresh_btn)
        root.addLayout(toolbar)

        # Table
        self.table = QTableWidget(0, 7)
        self.table.setHorizontalHeaderLabels([
            "Order #", "Patient", "Status",
            "Total (XAF)", "Paid (XAF)", "Balance (XAF)", "Payment"
        ])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setShowGrid(False)
        self.table.doubleClicked.connect(self._open_detail)
        root.addWidget(self.table)

        self.status_bar = QLabel("Loading…")
        self.status_bar.setStyleSheet(
            f"color: {TEXT_MUTED}; font-size: 12px;"
        )
        root.addWidget(self.status_bar)

    def refresh(self):
        self.status_bar.setText("Loading orders…")
        idx = self.status_filter.currentIndex()
        status_key = STATUS_OPTIONS[idx]
        status_param = None if status_key == "all" else status_key

        w = ApiWorker(api.list_orders, status_param)
        w.success.connect(self._on_orders)
        w.error.connect(self._on_error)
        w.start()
        self._workers.append(w)

    def _on_orders(self, data: dict):
        self._all_orders = data.get("orders", [])
        self._populate_table(self._all_orders)
        count = len(self._all_orders)
        self.status_bar.setText(
            f"{count} order{'s' if count != 1 else ''}  •  "
            "double-click a row to open"
        )

    def _populate_table(self, orders: list):
        self.table.setRowCount(0)
        for order in orders:
            row = self.table.rowCount()
            self.table.insertRow(row)

            order_num  = order.get("order_number", str(order.get("id", "")))
            patient    = order.get("patient_name") or str(order.get("patient", ""))
            status     = order.get("status", "")
            total      = order.get("total_amount", "0")
            paid       = order.get("amount_paid", "0")
            balance    = order.get("balance", "0")
            pay_status = order.get("payment_status") or "unpaid"

            self.table.setItem(row, 0, QTableWidgetItem(order_num))
            self.table.setItem(row, 1, QTableWidgetItem(patient))

            status_item = QTableWidgetItem(status.replace("_", " ").title())
            bg, fg = STATUS_COLOURS.get(status, ("#e8eaed", "#3c4043"))
            status_item.setBackground(QColor(bg))
            status_item.setForeground(QColor(fg))
            self.table.setItem(row, 2, status_item)

            self.table.setItem(row, 3, QTableWidgetItem(str(total)))
            self.table.setItem(row, 4, QTableWidgetItem(str(paid)))

            balance_item = QTableWidgetItem(str(balance))
            try:
                if float(balance) > 0:
                    balance_item.setForeground(QColor("#d93025"))
            except (ValueError, TypeError):
                pass
            self.table.setItem(row, 5, balance_item)

            pay_item = QTableWidgetItem(pay_status.title())
            pbg, pfg = PAYMENT_COLOURS.get(pay_status, ("#e8eaed", "#3c4043"))
            pay_item.setBackground(QColor(pbg))
            pay_item.setForeground(QColor(pfg))
            self.table.setItem(row, 6, pay_item)

            self.table.item(row, 0).setData(Qt.UserRole, order)

        self.table.resizeColumnsToContents()

    def _filter_table(self, query: str):
        query = query.lower()
        filtered = [
            o for o in self._all_orders
            if query in str(o.get("order_number", "")).lower()
            or query in str(o.get("patient_name", "")).lower()
            or query in str(o.get("patient", "")).lower()
        ]
        self._populate_table(filtered)

    def _open_detail(self, index):
        row = index.row()
        item = self.table.item(row, 0)
        if not item:
            return
        order_data = item.data(Qt.UserRole)
        if not order_data:
            return
        dialog = OrderDetailDialog(order_data, self)
        dialog.order_updated.connect(self.refresh)
        dialog.exec()

    def _open_create_dialog(self):
        dialog = CreateOrderDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.refresh()

    def _on_error(self, message: str):
        self.status_bar.setText(f"Error: {message}")

    def _h1(self, text):
        l = QLabel(text)
        l.setObjectName("section_title")
        l.setFont(QFont("Segoe UI", 18, QFont.Bold))
        return l

    def _sub(self, text):
        l = QLabel(text)
        l.setObjectName("section_sub")
        l.setStyleSheet(f"color: {TEXT_MUTED}; font-size: 12px;")
        return l


# ─────────────────────────────────────────────────────────────────────────────
# Create Order dialog — fully rewritten
# ─────────────────────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────────────────────
# Create Order dialog — fully rewritten
# ─────────────────────────────────────────────────────────────────────────────

class CreateOrderDialog(QDialog):
    """
    Form to create a new order with three cascaded dropdowns.

    CASCADE CHAIN:
      Patient selected
          └→ loads prescriptions for that patient

      Category selected
          └→ loads item types in that category
              └→ item type selected
                  └→ loads inventory items of that type
                      └→ selects an available inventory item
                          └→ auto-fills unit price

    ORDER NUMBER:
      Not shown in the form. Generated by the backend.
      Displayed in the success message after creation.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create New Order")
        self.setMinimumWidth(520)
        self.setModal(True)

        # Internal data caches (populated by API calls)
        self._patients      = []
        self._prescriptions = []
        self._categories    = []
        self._item_types    = []
        self._inv_items     = []

        self._workers = []

        self._build_ui()
        self._load_initial_data()
        # Ensure dialog height stays within the available screen area.
        # Some style combinations or widget sizeHints can return an
        # unexpectedly large minimum height; constrain it to avoid
        # QWindowsWindow::setGeometry warnings on small displays.
        try:
            self.adjustSize()
            screen = self.screen()
            avail_h = screen.availableGeometry().height() if screen else 900
            # Minimum reasonable dialog height, and max slightly below screen
            min_h = 420
            max_h = max(min_h, avail_h - 100)
            self.setMinimumHeight(min_h)
            self.setMaximumHeight(max_h)
        except Exception:
            pass

    # ── UI construction ────────────────────────────────────────────────────

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(24, 24, 24, 20)
        root.setSpacing(14)

        # Title
        title = QLabel("New Order")
        title.setFont(QFont("Segoe UI", 14, QFont.Bold))
        root.addWidget(title)

        subtitle = QLabel(
            "Order number is auto-generated  •  "
            "Select patient to load prescriptions  •  "
            "Select category to load item types"
        )
        subtitle.setStyleSheet(f"color: {TEXT_MUTED}; font-size: 11px;")
        subtitle.setWordWrap(True)
        root.addWidget(subtitle)

        form = QFormLayout()
        form.setSpacing(10)
        form.setLabelAlignment(Qt.AlignRight)

        # ── 1. Patient ─────────────────────────────────────────────────────
        self.patient_combo = QComboBox()
        self.patient_combo.setFixedHeight(34)
        self.patient_combo.setPlaceholderText("Loading patients…")
        self.patient_combo.currentIndexChanged.connect(self._on_patient_selected)
        form.addRow("Patient *", self.patient_combo)

        # ── 2. Prescription (loads after patient selected) ─────────────────
        self.prescription_combo = QComboBox()
        self.prescription_combo.setFixedHeight(34)
        self.prescription_combo.setEnabled(False)
        self.prescription_combo.setPlaceholderText("Select a patient first")
        form.addRow("MedicalReports *", self.prescription_combo)

        self.prescription_warning = QLabel("")
        self.prescription_warning.setStyleSheet("color: #f9ab00; font-size: 11px;")
        self.prescription_warning.setVisible(False)
        form.addRow("", self.prescription_warning)

        # ── 3. Category (loads on open) ────────────────────────────────────
        self.category_combo = QComboBox()
        self.category_combo.setFixedHeight(34)
        self.category_combo.setPlaceholderText("Loading categories…")
        self.category_combo.currentIndexChanged.connect(self._on_category_selected)
        form.addRow("Category *", self.category_combo)

        # ── 4. Item Type (loads after category selected) ───────────────────
        self.item_type_combo = QComboBox()
        self.item_type_combo.setFixedHeight(34)
        self.item_type_combo.setEnabled(False)
        self.item_type_combo.setPlaceholderText("Select a category first")
        self.item_type_combo.currentIndexChanged.connect(self._on_item_type_selected)
        form.addRow("Item Type *", self.item_type_combo)

        self.stock_label = QLabel("")
        self.stock_label.setStyleSheet("color: #5f6368; font-size: 11px;")
        self.stock_label.setVisible(False)
        form.addRow("", self.stock_label)

        # ── 6. Quantity ────────────────────────────────────────────────────
        self.qty_spin = QSpinBox()
        self.qty_spin.setRange(1, 9999)
        self.qty_spin.setValue(1)
        self.qty_spin.setFixedHeight(34)
        form.addRow("Quantity *", self.qty_spin)

        # ── 7. Unit Price (auto-filled from product, editable) ─────────────
        price_row = QHBoxLayout()
        self.price_spin = QDoubleSpinBox()
        self.price_spin.setRange(0.01, 9_999_999)
        self.price_spin.setDecimals(0)
        self.price_spin.setSuffix("  XAF")
        self.price_spin.setFixedHeight(34)
        self.price_spin.setValue(0)

        self.price_auto_lbl = QLabel("  ✓ Auto-filled")
        self.price_auto_lbl.setStyleSheet("color: #1e8e3e; font-size: 11px;")
        self.price_auto_lbl.setVisible(False)

        price_row.addWidget(self.price_spin)
        price_row.addWidget(self.price_auto_lbl)
        price_row.addStretch()

        price_widget = QWidget()
        price_widget.setLayout(price_row)
        form.addRow("Unit Price *", price_widget)

        # ── 8. Discount ────────────────────────────────────────────────────
        self.discount_spin = QDoubleSpinBox()
        self.discount_spin.setRange(0, 9_999_999)
        self.discount_spin.setDecimals(0)
        self.discount_spin.setSuffix("  XAF")
        self.discount_spin.setFixedHeight(34)
        self.discount_spin.setValue(0)
        form.addRow("Discount", self.discount_spin)

        # ── 9. Expected Delivery ───────────────────────────────────────────
        self.delivery_date = QDateEdit()
        self.delivery_date.setCalendarPopup(True)
        self.delivery_date.setDate(QDate.currentDate().addDays(7))
        self.delivery_date.setFixedHeight(34)
        self.delivery_date.setSpecialValueText("Not set")
        form.addRow("Expected Delivery", self.delivery_date)

        # ── 10. Notes ──────────────────────────────────────────────────────
        self.notes_input = QTextEdit()
        self.notes_input.setFixedHeight(60)
        self.notes_input.setPlaceholderText("Lens prescription details, special instructions…")
        form.addRow("Notes", self.notes_input)

        scroll = QScrollArea()
        scroll.setFrameShape(QFrame.NoFrame)
        scroll.setWidgetResizable(True)

        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(10)
        content_layout.addLayout(form)

        # API error label (cascade/load errors separate from submit errors)
        self.api_error_lbl = QLabel("")
        self.api_error_lbl.setStyleSheet("color: #d93025; font-size: 12px;")
        self.api_error_lbl.setWordWrap(True)
        self.api_error_lbl.setVisible(False)
        content_layout.addWidget(self.api_error_lbl)

        # Submit/error label
        self.error_lbl = QLabel("")
        self.error_lbl.setStyleSheet("color: #d93025; font-size: 12px;")
        self.error_lbl.setWordWrap(True)
        self.error_lbl.setVisible(False)
        content_layout.addWidget(self.error_lbl)

        # Preview line
        self.preview_lbl = QLabel("")
        self.preview_lbl.setStyleSheet(
            f"color: {PRIMARY}; font-size: 12px; font-weight: bold;"
        )
        self.preview_lbl.setVisible(False)
        content_layout.addWidget(self.preview_lbl)

        scroll.setWidget(content_widget)
        root.addWidget(scroll)

        # Buttons
        btn_row = QHBoxLayout()
        btn_row.addStretch()

        cancel_btn = QPushButton("Cancel")
        cancel_btn.setObjectName("secondary_btn")
        cancel_btn.setFixedHeight(36)
        cancel_btn.clicked.connect(self.reject)
        btn_row.addWidget(cancel_btn)

        self.create_btn = QPushButton("Create Order")
        self.create_btn.setObjectName("primary_btn")
        self.create_btn.setFixedHeight(36)
        self.create_btn.clicked.connect(self._submit)
        btn_row.addWidget(self.create_btn)
        root.addLayout(btn_row)

    # ── Initial data load (runs immediately on open) ───────────────────────

    def _load_initial_data(self):
        """Load patients and categories in parallel when dialog opens."""
        self._load_patients()
        self._load_categories()

    def _load_patients(self):
        w = ApiWorker(api.list_patients)
        w.success.connect(self._on_patients_loaded)
        w.error.connect(lambda e: self._show_api_error(f"Could not load patients: {e}"))
        w.start()
        self._workers.append(w)

    def _on_patients_loaded(self, data: dict):
        self._clear_api_error()
        self._patients = data.get("patients", [])
        self.patient_combo.blockSignals(True)
        self.patient_combo.clear()
        self.patient_combo.addItem("— Select patient —", None)
        for p in self._patients:
            self.patient_combo.addItem(p.get("name", ""), p.get("id"))
        self.patient_combo.blockSignals(False)

    def _load_categories(self):
        w = ApiWorker(api.categories)
        w.success.connect(self._on_categories_loaded)
        w.error.connect(lambda e: self._show_api_error(f"Could not load categories: {e}"))
        w.start()
        self._workers.append(w)

    def _on_categories_loaded(self, data):
        self._clear_api_error()
        # Backend may return a dict with key "categories" or a list directly.
        # Accept both shapes without calling .get() on a list (which raised).
        if isinstance(data, dict):
            self._categories = data.get("categories", data.get("data", []))
        elif isinstance(data, list):
            self._categories = data
        else:
            # Unexpected shape: be defensive and treat as empty
            self._categories = []

        self.category_combo.blockSignals(True)
        self.category_combo.clear()
        self.category_combo.addItem("— Select category —", None)
        for c in self._categories:
            # Each category is expected to be a dict; fall back safely if not.
            if isinstance(c, dict):
                name = c.get("name", c.get("label", ""))
                cid = c.get("id")
            else:
                name = str(c)
                cid = None
            self.category_combo.addItem(name, cid)
        self.category_combo.blockSignals(False)

    # ── Cascade: patient → prescriptions ──────────────────────────────────

    def _on_patient_selected(self, index):
        """Fires every time the patient combo selection changes."""
        patient_id = self.patient_combo.currentData()

        # Reset prescription dropdown
        self.prescription_combo.clear()
        self.prescription_combo.setEnabled(False)
        self.prescription_combo.setPlaceholderText("Loading prescriptions…")
        self.prescription_warning.setVisible(False)

        if not patient_id:
            self.prescription_combo.setPlaceholderText("Select a patient first")
            return

        w = ApiWorker(api.prescriptions_by_patient, patient_id)
        w.success.connect(self._on_prescriptions_loaded)
        w.error.connect(
            lambda e: self._show_api_error(f"Could not load prescriptions: {e}")
        )
        w.start()
        self._workers.append(w)

    def _on_prescriptions_loaded(self, data):
        if isinstance(data, dict):
            self._prescriptions = data.get("prescriptions", data.get("reports", data.get("MedicalReports", [])))
        elif isinstance(data, list):
            self._prescriptions = data
        else:
            self._prescriptions = []

        self.prescription_combo.clear()

        if not self._prescriptions:
            # Patient exists but has no medical reports yet
            self.prescription_combo.setEnabled(False)
            self.prescription_combo.setPlaceholderText(
                "No prescriptions found for this patient"
            )
            self.prescription_warning.setText(
                "⚠  This patient has no medical reports. "
                "Create one first in the Medical Reports section."
            )
            self.prescription_warning.setVisible(True)
            return

        self.prescription_combo.setEnabled(True)
        self.prescription_combo.addItem("— Select prescription —", None)

        for r in self._prescriptions:
            # Display:  "REF-2025-007  (2025-11-03)"
            ref  = r.get("reference_id") or f"Report #{r['id']}"
            date = r.get("date", "")
            label = f"{ref}  ({date})"
            self.prescription_combo.addItem(label, r.get("id"))

    # ── Cascade: category → item types ────────────────────────────────────

    def _on_category_selected(self, index):
        """Fires every time the category combo selection changes."""
        category_id = self.category_combo.currentData()

        # Reset downstream state
        self._reset_item_type_combo("Select a category first")
        self._selected_inventory_item = None
        self.stock_label.setVisible(False)
        self.price_auto_lbl.setVisible(False)

        if not category_id:
            return

        self.item_type_combo.setEnabled(False)
        self.item_type_combo.clear()
        self.item_type_combo.addItem("Loading…", None)

        w = ApiWorker(api.item_types_by_category, category_id)
        w.success.connect(self._on_item_types_loaded)
        w.error.connect(
            lambda e: self._show_api_error(f"Could not load item types: {e}")
        )
        w.start()
        self._workers.append(w)

    def _on_item_types_loaded(self, data):
        if isinstance(data, dict):
            self._item_types = data.get("item_types", data.get("types", []))
        elif isinstance(data, list):
            self._item_types = data
        else:
            self._item_types = []

        self.item_type_combo.clear()

        if not self._item_types:
            self.item_type_combo.setEnabled(False)
            self.item_type_combo.addItem("No item types in this category", None)
            return

        self.item_type_combo.setEnabled(True)
        self.item_type_combo.addItem("— Select item type —", None)
        for t in self._item_types:
            self.item_type_combo.addItem(t.get("name", ""), t.get("id"))

    # ── Cascade: item type → products ─────────────────────────────────────

    def _on_item_type_selected(self, index):
        """Fires every time the item type combo selection changes."""
        type_id = self.item_type_combo.currentData()

        self._selected_inventory_item = None
        self.stock_label.setVisible(False)
        self.price_auto_lbl.setVisible(False)
        self.price_spin.setValue(0)

        if not type_id:
            return

        w = ApiWorker(api.inventory_items_by_type, type_id)
        w.success.connect(self._on_inventory_loaded)
        w.error.connect(
            lambda e: self._show_api_error(f"Could not load item prices: {e}")
        )
        w.start()
        self._workers.append(w)

    def _on_inventory_loaded(self, data):
        if isinstance(data, dict):
            self._inv_items = data.get("items", data.get("inventory_items", []))
        elif isinstance(data, list):
            self._inv_items = data
        else:
            self._inv_items = []

        if not self._inv_items:
            self._show_api_error("No stock available for the selected item type.")
            self._selected_inventory_item = None
            self.price_spin.setValue(0)
            self.stock_label.setVisible(False)
            return

        self._selected_inventory_item = self._inv_items[0]
        item = self._selected_inventory_item
        try:
            price = float(item.get("unit_price", 0))
            self.price_spin.setValue(price)
            self.price_auto_lbl.setVisible(True)
        except (ValueError, TypeError):
            self.price_spin.setValue(0)
            self.price_auto_lbl.setVisible(False)

        stock = item.get("stock_level", 0)
        low   = item.get("is_low_stock", False)
        cat   = item.get("category_name", "")
        type_nm = item.get("type_name", "")

        if low:
            self.stock_label.setText(
                f"⚠  Only {stock} left in stock — consider ordering more"
            )
            self.stock_label.setStyleSheet("color: #f9ab00; font-size: 11px;")
        else:
            self.stock_label.setText(
                f"✓  {stock} {type_nm} ({cat}) in stock"
            )
            self.stock_label.setStyleSheet("color: #1e8e3e; font-size: 11px;")
        self.stock_label.setVisible(True)
        self._update_preview()

    # ── Live order preview ─────────────────────────────────────────────────

    def _update_preview(self):
        """Shows a running total estimate as the user fills the form."""
        qty      = self.qty_spin.value()
        price    = self.price_spin.value()
        discount = self.discount_spin.value()
        total    = (qty * price) - discount

        if price > 0:
            self.preview_lbl.setText(
                f"Estimated total:  {total:,.0f} XAF  "
                f"({qty} × {price:,.0f} − {discount:,.0f} discount)"
            )
            self.preview_lbl.setVisible(True)
        else:
            self.preview_lbl.setVisible(False)

    # ── Helper resets ──────────────────────────────────────────────────────

    def _reset_item_type_combo(self, placeholder: str):
        self.item_type_combo.clear()
        self.item_type_combo.setEnabled(False)
        self.item_type_combo.addItem(placeholder, None)
        self._item_types = []
        self._selected_inventory_item = None
        self._inv_items = []

    # ── Form submission ────────────────────────────────────────────────────

    def _submit(self):
        """Validates all fields then posts to POST /api/orders/."""
        # Prevent unauthenticated POSTs which redirect to the login page
        if not api.has_session():
            self._show_error(
                "You must sign in before creating orders. Please log in first."
            )
            return
        patient_id      = self.patient_combo.currentData()
        prescription_id = self.prescription_combo.currentData()
        selected_item   = self._selected_inventory_item
        category_id     = self.category_combo.currentData()
        qty             = self.qty_spin.value()
        price           = self.price_spin.value()
        discount        = self.discount_spin.value()
        notes           = self.notes_input.toPlainText().strip()

        # Validation
        if not patient_id:
            self._show_error("Please select a patient")
            return
        if not prescription_id:
            self._show_error(
                "Please select a prescription. "
                "If none appear, create a medical report for this patient first."
            )
            return
        if not category_id:
            self._show_error("Please select a product category")
            return
        if not self.item_type_combo.currentData():
            self._show_error("Please select an item type")
            return
        if not selected_item:
            self._show_error("Please select a valid item type with available stock")
            return
        if price <= 0:
            self._show_error("Unit price must be greater than zero")
            return

        # Get the category name to store as item_type label on the OrderItem
        category_name = self.category_combo.currentText()

        # Build the payload.
        # NOTE: 'order_number' is intentionally absent — backend generates it.
        payload = {
            "patient":      patient_id,
            "prescription": prescription_id,
            "discount":     str(discount),
            "notes":        notes,
            "expected_delivery_date": (
                self.delivery_date.date().toString("yyyy-MM-dd")
            ),
            "items": [
                {
                    "product":    selected_item.get("id"),
                    "quantity":   qty,
                    "unit_price": str(price),
                    # item_type on OrderItem stores the category name
                    # so you can later group line items by type
                    "item_type":  category_name,
                }
            ],
        }

        self.create_btn.setEnabled(False)
        self.create_btn.setText("Creating…")
        self.error_lbl.setVisible(False)

        w = ApiWorker(api.create_order, payload)
        w.success.connect(self._on_created)
        w.error.connect(self._on_create_error)
        w.start()
        self._workers.append(w)

    def _on_created(self, data: dict):
        self.create_btn.setEnabled(True)
        self.create_btn.setText("Create Order")

        order = data.get("order", {})
        order_number = order.get("order_number", "")

        QMessageBox.information(
            self,
            "Order Created",
            f"Order {order_number} has been created successfully.\n\n"
            f"Status: Draft\n"
            f"You can now add payments or change the status in the order list."
        )
        self.accept()

    def _on_create_error(self, message: str):
        self.create_btn.setEnabled(True)
        self.create_btn.setText("Create Order")
        self._show_error(f"Failed to create order: {message}")

    def _show_error(self, msg: str):
        self.error_lbl.setText(msg)
        self.error_lbl.setVisible(True)

    def _show_api_error(self, msg: str):
        self.api_error_lbl.setText(msg)
        self.api_error_lbl.setVisible(True)

    def _clear_api_error(self):
        self.api_error_lbl.setText("")
        self.api_error_lbl.setVisible(False)