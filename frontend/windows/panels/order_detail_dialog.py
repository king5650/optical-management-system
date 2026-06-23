"""
windows/panels/order_detail_dialog.py — Order detail popup

Shows full order info, financial summary, payment history, status history,
and lets the user change status or record a payment.

CONNECTION FLOWS:
  On open    → GET /api/orders/<id>/summary/ + GET /api/payments/by-order/<id>/
  Add payment → POST /api/payments/            → refreshes summary
  Change status → POST /api/orders/<id>/change-status/ → refreshes order
  Cancel      → POST /api/orders/<id>/cancel/
"""

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QComboBox, QDoubleSpinBox,
    QFrame, QGroupBox, QScrollArea, QWidget, QMessageBox,
    QHeaderView, QLineEdit
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont, QColor

from api_client import api
from assets.styles import (
    PRIMARY, DANGER, SUCCESS, WARNING,
    STATUS_COLOURS, PAYMENT_COLOURS, TEXT_MUTED, CARD_BG, BORDER
)
from workers.api_worker import ApiWorker


def _badge(text: str, colour_map: dict, key: str) -> QLabel:
    """Creates a coloured badge label for status/payment display."""
    bg, fg = colour_map.get(key, ("#e8eaed", "#3c4043"))
    lbl = QLabel(text.replace("_", " ").title())
    lbl.setStyleSheet(f"""
        background-color: {bg};
        color: {fg};
        border-radius: 10px;
        padding: 2px 10px;
        font-size: 11px;
        font-weight: bold;
    """)
    lbl.setFixedHeight(22)
    return lbl


class OrderDetailDialog(QDialog):
    """
    Full-detail popup for a single order.
    'order_updated' is emitted when status or payments change so the
    parent order list can refresh its row.
    """
    order_updated = Signal()

    def __init__(self, order_data: dict, parent=None):
        super().__init__(parent)
        self.order_data = order_data
        self.order_id   = order_data["id"]
        self._workers   = []

        self.setWindowTitle(f"Order — {order_data.get('order_number', self.order_id)}")
        self.setMinimumSize(760, 640)
        self.setModal(True)

        self._build_ui()
        self._load_summary()
        self._load_payments()

    # ──────────────────────────────────────────────────────────────────────
    # UI construction
    # ──────────────────────────────────────────────────────────────────────

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ── Header bar ─────────────────────────────────────────────────
        header = QFrame()
        header.setStyleSheet(f"background: {PRIMARY}; border: none;")
        h_layout = QHBoxLayout(header)
        h_layout.setContentsMargins(24, 16, 24, 16)

        order_num = self.order_data.get("order_number", f"#{self.order_id}")
        h_title = QLabel(f"Order  {order_num}")
        h_title.setFont(QFont("Segoe UI", 15, QFont.Bold))
        h_title.setStyleSheet("color: white; background: transparent;")
        h_layout.addWidget(h_title)
        h_layout.addStretch()

        # Current status badge (white text on primary background)
        status = self.order_data.get("status", "draft")
        self.status_lbl = QLabel(status.replace("_", " ").title())
        self.status_lbl.setStyleSheet(
            "color: white; font-size: 12px; font-weight: bold; "
            "background: rgba(255,255,255,0.25); border-radius: 10px; padding: 2px 12px;"
        )
        h_layout.addWidget(self.status_lbl)
        root.addWidget(header)

        # ── Scrollable body ────────────────────────────────────────────
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)

        body_widget = QWidget()
        body = QVBoxLayout(body_widget)
        body.setContentsMargins(24, 20, 24, 20)
        body.setSpacing(16)

        # ── Financial summary row ──────────────────────────────────────
        self.summary_frame = self._build_summary_frame()
        body.addWidget(self.summary_frame)

        # ── Items table ────────────────────────────────────────────────
        items_group = QGroupBox("Order Items")
        items_group.setStyleSheet("QGroupBox { font-weight: bold; }")
        items_layout = QVBoxLayout(items_group)

        self.items_table = self._make_table(
            ["Product", "Type", "Qty", "Unit Price", "Total"]
        )
        items = self.order_data.get("items", [])
        self.items_table.setRowCount(len(items))
        for row, item in enumerate(items):
            self.items_table.setItem(row, 0, QTableWidgetItem(item.get("product_name", "")))
            self.items_table.setItem(row, 1, QTableWidgetItem(item.get("item_type", "")))
            self.items_table.setItem(row, 2, QTableWidgetItem(str(item.get("quantity", ""))))
            self.items_table.setItem(row, 3, QTableWidgetItem(f"{item.get('unit_price', 0)} XAF"))
            self.items_table.setItem(row, 4, QTableWidgetItem(f"{item.get('total_price', 0)} XAF"))
        self.items_table.setFixedHeight(min(40 + len(items) * 36, 200))
        items_layout.addWidget(self.items_table)
        body.addWidget(items_group)

        # ── Payments table ─────────────────────────────────────────────
        pay_group = QGroupBox("Payment History")
        pay_group.setStyleSheet("QGroupBox { font-weight: bold; }")
        pay_layout = QVBoxLayout(pay_group)

        self.payments_table = self._make_table(
            ["Date", "Method", "Reference", "Amount"]
        )
        self.payments_table.setFixedHeight(160)
        pay_layout.addWidget(self.payments_table)
        body.addWidget(pay_group)

        # ── Add payment form ───────────────────────────────────────────
        pay_form_group = QGroupBox("Record New Payment")
        pay_form_group.setStyleSheet("QGroupBox { font-weight: bold; }")
        pay_form_layout = QHBoxLayout(pay_form_group)

        self.amount_spin = QDoubleSpinBox()
        self.amount_spin.setRange(0.01, 9_999_999)
        self.amount_spin.setDecimals(0)
        self.amount_spin.setSuffix(" XAF")
        self.amount_spin.setFixedHeight(36)
        self.amount_spin.setFixedWidth(160)

        self.method_combo = QComboBox()
        self.method_combo.addItems(["cash", "mobile_money", "card"])
        self.method_combo.setFixedHeight(36)

        self.ref_input = QLineEdit()
        self.ref_input.setPlaceholderText("Transaction reference (optional)")
        self.ref_input.setFixedHeight(36)

        self.pay_btn = QPushButton("Add Payment")
        self.pay_btn.setObjectName("primary_btn")
        self.pay_btn.setFixedHeight(36)
        self.pay_btn.clicked.connect(self._add_payment)

        pay_form_layout.addWidget(QLabel("Amount:"))
        pay_form_layout.addWidget(self.amount_spin)
        pay_form_layout.addWidget(QLabel("Method:"))
        pay_form_layout.addWidget(self.method_combo)
        pay_form_layout.addWidget(self.ref_input)
        pay_form_layout.addWidget(self.pay_btn)
        body.addWidget(pay_form_group)

        # ── Change status ──────────────────────────────────────────────
        status_group = QGroupBox("Change Order Status")
        status_group.setStyleSheet("QGroupBox { font-weight: bold; }")
        status_layout = QHBoxLayout(status_group)

        self.new_status_combo = QComboBox()
        self.new_status_combo.setFixedHeight(36)
        self._populate_status_combo()

        self.change_status_btn = QPushButton("Apply Status")
        self.change_status_btn.setObjectName("secondary_btn")
        self.change_status_btn.setFixedHeight(36)
        self.change_status_btn.clicked.connect(self._change_status)

        self.cancel_btn = QPushButton("Cancel Order")
        self.cancel_btn.setObjectName("danger_btn")
        self.cancel_btn.setFixedHeight(36)
        self.cancel_btn.clicked.connect(self._cancel_order)

        status_layout.addWidget(QLabel("Move to:"))
        status_layout.addWidget(self.new_status_combo)
        status_layout.addWidget(self.change_status_btn)
        status_layout.addStretch()
        status_layout.addWidget(self.cancel_btn)
        body.addWidget(status_group)

        body.addStretch()
        scroll.setWidget(body_widget)
        root.addWidget(scroll)

        # ── Bottom close button ────────────────────────────────────────
        footer = QFrame()
        footer.setStyleSheet(f"background: #f8f9fa; border-top: 1px solid {BORDER};")
        f_layout = QHBoxLayout(footer)
        f_layout.setContentsMargins(24, 12, 24, 12)
        f_layout.addStretch()
        close_btn = QPushButton("Close")
        close_btn.setObjectName("secondary_btn")
        close_btn.clicked.connect(self.accept)
        f_layout.addWidget(close_btn)
        root.addWidget(footer)

    def _build_summary_frame(self) -> QFrame:
        frame = QFrame()
        frame.setObjectName("card")
        layout = QHBoxLayout(frame)
        layout.setContentsMargins(20, 16, 20, 16)
        layout.setSpacing(32)

        def _metric(label, attr_name):
            col = QVBoxLayout()
            lbl = QLabel(label)
            lbl.setStyleSheet(f"color: {TEXT_MUTED}; font-size: 11px;")
            val = QLabel("—")
            val.setFont(QFont("Segoe UI", 14, QFont.Bold))
            setattr(self, attr_name, val)
            col.addWidget(lbl)
            col.addWidget(val)
            return col

        layout.addLayout(_metric("Total Amount",    "lbl_total"))
        layout.addLayout(_metric("Amount Paid",     "lbl_paid"))
        layout.addLayout(_metric("Balance Owed",    "lbl_balance"))
        layout.addLayout(_metric("Payment Status",  "lbl_pay_status"))
        layout.addStretch()
        return frame

    def _make_table(self, headers: list) -> QTableWidget:
        t = QTableWidget(0, len(headers))
        t.setHorizontalHeaderLabels(headers)
        t.setEditTriggers(QTableWidget.NoEditTriggers)
        t.setSelectionBehavior(QTableWidget.SelectRows)
        t.setAlternatingRowColors(True)
        t.horizontalHeader().setStretchLastSection(True)
        t.verticalHeader().setVisible(False)
        return t

    def _populate_status_combo(self):
        """Only show allowed transitions for the current status."""
        VALID_TRANSITIONS = {
            "draft":       ["confirmed", "cancelled"],
            "confirmed":   ["in_progress", "cancelled"],
            "in_progress": ["ready"],
            "ready":       ["delivered"],
            "delivered":   ["completed"],
            "completed":   [],
            "cancelled":   [],
        }
        current = self.order_data.get("status", "draft")
        allowed = VALID_TRANSITIONS.get(current, [])
        self.new_status_combo.clear()
        for s in allowed:
            self.new_status_combo.addItem(s.replace("_", " ").title(), s)
        if not allowed:
            self.new_status_combo.addItem("No transitions available", "")
            self.change_status_btn.setEnabled(False)

    # ──────────────────────────────────────────────────────────────────────
    # Data loading
    # ──────────────────────────────────────────────────────────────────────

    def _load_summary(self):
        w = ApiWorker(api.order_summary, self.order_id)
        w.success.connect(self._on_summary)
        w.error.connect(lambda e: None)
        w.start()
        self._workers.append(w)

    def _on_summary(self, data: dict):
        s = data.get("summary", data)
        self.lbl_total.setText(f"{s.get('total_amount', '—')} XAF")
        self.lbl_paid.setText(f"{s.get('paid', '—')} XAF")

        balance = s.get('balance', 0)
        self.lbl_balance.setText(f"{balance} XAF")
        self.lbl_balance.setStyleSheet(
            f"color: {'#d93025' if float(balance) > 0 else '#1e8e3e'}; font-weight: bold;"
        )

        pay_status = s.get("payment_status", "unpaid")
        bg, fg = PAYMENT_COLOURS.get(pay_status, ("#e8eaed", "#3c4043"))
        self.lbl_pay_status.setText(pay_status.title())
        self.lbl_pay_status.setStyleSheet(
            f"color: {fg}; font-weight: bold; font-size: 14px;"
        )

    def _load_payments(self):
        w = ApiWorker(api.payments_by_order, self.order_id)
        w.success.connect(self._on_payments)
        w.error.connect(lambda e: None)
        w.start()
        self._workers.append(w)

    def _on_payments(self, data: dict):
        payments = data.get("payments", [])
        self.payments_table.setRowCount(len(payments))
        for row, p in enumerate(payments):
            date = p.get("payment_date", "")[:10]
            method = p.get("payment_method", "").replace("_", " ").title()
            ref = p.get("transaction_reference", "") or "—"
            amount = float(p.get("amount", 0))
            amount_str = f"-{abs(amount):.0f} XAF" if amount < 0 else f"{amount:.0f} XAF"

            self.payments_table.setItem(row, 0, QTableWidgetItem(date))
            self.payments_table.setItem(row, 1, QTableWidgetItem(method))
            self.payments_table.setItem(row, 2, QTableWidgetItem(ref))
            amount_item = QTableWidgetItem(amount_str)
            amount_item.setForeground(QColor("#d93025") if amount < 0 else QColor("#1e8e3e"))
            self.payments_table.setItem(row, 3, amount_item)

    # ──────────────────────────────────────────────────────────────────────
    # Actions
    # ──────────────────────────────────────────────────────────────────────

    def _add_payment(self):
        amount = self.amount_spin.value()
        method = self.method_combo.currentData() or self.method_combo.currentText()
        ref    = self.ref_input.text().strip()

        if amount <= 0:
            QMessageBox.warning(self, "Invalid", "Enter an amount greater than zero.")
            return

        self.pay_btn.setEnabled(False)
        self.pay_btn.setText("Recording…")

        w = ApiWorker(api.add_payment, self.order_id, amount, method, ref)
        w.success.connect(self._on_payment_added)
        w.error.connect(self._on_error)
        w.start()
        self._workers.append(w)

    def _on_payment_added(self, data: dict):
        self.pay_btn.setEnabled(True)
        self.pay_btn.setText("Add Payment")
        self.amount_spin.setValue(0)
        self.ref_input.clear()
        self._load_summary()
        self._load_payments()
        self.order_updated.emit()

    def _change_status(self):
        new_status = self.new_status_combo.currentData()
        if not new_status:
            return

        confirm = QMessageBox.question(
            self, "Confirm",
            f"Change status to  '{new_status.replace('_',' ').title()}'?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm != QMessageBox.Yes:
            return

        self.change_status_btn.setEnabled(False)
        w = ApiWorker(api.change_order_status, self.order_id, new_status)
        w.success.connect(self._on_status_changed)
        w.error.connect(self._on_error)
        w.start()
        self._workers.append(w)

    def _on_status_changed(self, data: dict):
        self.change_status_btn.setEnabled(True)
        updated = data.get("order", {})
        new_status = updated.get("status", "")
        self.status_lbl.setText(new_status.replace("_", " ").title())
        self.order_data["status"] = new_status
        self._populate_status_combo()
        self.order_updated.emit()

    def _cancel_order(self):
        confirm = QMessageBox.question(
            self, "Cancel Order",
            "Are you sure you want to cancel this order? This cannot be undone.",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm != QMessageBox.Yes:
            return

        w = ApiWorker(api.cancel_order, self.order_id)
        w.success.connect(self._on_cancelled)
        w.error.connect(self._on_error)
        w.start()
        self._workers.append(w)

    def _on_cancelled(self, data: dict):
        self.status_lbl.setText("Cancelled")
        self.order_data["status"] = "cancelled"
        self._populate_status_combo()
        self.cancel_btn.setEnabled(False)
        self.order_updated.emit()

    def _on_error(self, message: str):
        self.pay_btn.setEnabled(True)
        self.pay_btn.setText("Add Payment")
        self.change_status_btn.setEnabled(True)
        QMessageBox.critical(self, "Error", message)
