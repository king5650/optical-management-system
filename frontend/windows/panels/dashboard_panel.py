"""
windows/panels/dashboard_panel.py — Dashboard overview

CONNECTION FLOW:
  Panel shown → ApiWorker calls api.dashboard_counts()
  → Django returns { patient_count, sales_count, medical_report_count, inventory_count }
  → Stat cards updated with live numbers
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QFrame, QGridLayout, QScrollArea
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from api_client import api
from assets.styles import PRIMARY, TEXT_MUTED, CARD_BG, BORDER
from workers.api_worker import ApiWorker


class StatCard(QFrame):
    """Single metric card: big number + label + coloured left border."""

    def __init__(self, title: str, icon: str, colour: str):
        super().__init__()
        self.setObjectName("card")
        self.setFixedHeight(110)
        self.setStyleSheet(f"""
            QFrame#card {{
                background: {CARD_BG};
                border: 1px solid {BORDER};
                border-left: 4px solid {colour};
                border-radius: 8px;
                padding: 0;
            }}
        """)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 16, 20, 16)

        # Text side
        text_col = QVBoxLayout()
        text_col.setSpacing(4)

        self.number_lbl = QLabel("—")
        self.number_lbl.setObjectName("stat_number")
        self.number_lbl.setFont(QFont("Segoe UI", 26, QFont.Bold))
        self.number_lbl.setStyleSheet(f"color: {colour};")

        self.title_lbl = QLabel(title)
        self.title_lbl.setObjectName("stat_label")
        self.title_lbl.setStyleSheet(f"color: {TEXT_MUTED}; font-size: 12px;")

        text_col.addWidget(self.number_lbl)
        text_col.addWidget(self.title_lbl)
        layout.addLayout(text_col)
        layout.addStretch()

        # Icon
        icon_lbl = QLabel(icon)
        icon_lbl.setFont(QFont("Segoe UI", 28))
        icon_lbl.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(icon_lbl)

    def set_value(self, value):
        self.number_lbl.setText(str(value))


class DashboardPanel(QWidget):
    """
    Main dashboard screen.
    Shows live counts and a quick summary of the system state.
    """

    def __init__(self):
        super().__init__()
        self._worker = None
        self._build_ui()
        self.refresh()

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(28, 24, 28, 24)
        root.setSpacing(20)

        # ── Header ─────────────────────────────────────────────────────
        header = QHBoxLayout()
        title_col = QVBoxLayout()

        title = QLabel("Dashboard")
        title.setObjectName("section_title")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))

        sub = QLabel("Live overview of your optical cabinet")
        sub.setObjectName("section_sub")

        title_col.addWidget(title)
        title_col.addWidget(sub)
        header.addLayout(title_col)
        header.addStretch()
        root.addLayout(header)

        # ── Stat cards ──────────────────────────────────────────────────
        grid = QGridLayout()
        grid.setSpacing(16)

        self.card_patients   = StatCard("Total Patients",       "🧑‍⚕️",  "#1a73e8")
        self.card_sales      = StatCard("Sales Transactions",   "🛒",  "#1e8e3e")
        self.card_reports    = StatCard("Medical Reports",      "📋",  "#f9ab00")
        self.card_inventory  = StatCard("Inventory Items",      "📦",  "#e37400")

        grid.addWidget(self.card_patients,  0, 0)
        grid.addWidget(self.card_sales,     0, 1)
        grid.addWidget(self.card_reports,   1, 0)
        grid.addWidget(self.card_inventory, 1, 1)

        root.addLayout(grid)

        # ── Quick actions card ──────────────────────────────────────────
        quick = QFrame()
        quick.setObjectName("card")
        q_layout = QVBoxLayout(quick)
        q_layout.setContentsMargins(20, 16, 20, 16)

        q_title = QLabel("Quick actions")
        q_title.setFont(QFont("Segoe UI", 13, QFont.Bold))
        q_layout.addWidget(q_title)

        actions = [
            ("➕  New Order",          "Create a new customer order"),
            ("💰  Record Payment",     "Add a payment to an existing order"),
            ("🔄  Change Order Status","Advance an order through the workflow"),
            ("🔍  Search Patients",    "Find a patient by name, email or contact"),
        ]
        for action, desc in actions:
            row = QHBoxLayout()
            action_lbl = QLabel(action)
            action_lbl.setStyleSheet(f"color: {PRIMARY}; font-weight: bold;")
            desc_lbl = QLabel(desc)
            desc_lbl.setStyleSheet(f"color: {TEXT_MUTED}; font-size: 12px;")
            row.addWidget(action_lbl)
            row.addSpacing(12)
            row.addWidget(desc_lbl)
            row.addStretch()
            q_layout.addLayout(row)

        root.addWidget(quick)
        root.addStretch()

    def refresh(self):
        """Reload dashboard counts from the server."""
        self._worker = ApiWorker(api.dashboard_counts)
        self._worker.success.connect(self._on_data)
        self._worker.error.connect(lambda e: None)   # silently ignore on dashboard
        self._worker.start()

    def _on_data(self, data: dict):
        self.card_patients.set_value(data.get("patient_count", 0))
        self.card_sales.set_value(data.get("sales_count", 0))
        self.card_reports.set_value(data.get("medical_report_count", 0))
        self.card_inventory.set_value(data.get("inventory_count", 0))
