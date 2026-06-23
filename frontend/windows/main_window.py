import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

"""
windows/main_window.py — Main application window

STRUCTURE:
  ┌──────────────┬─────────────────────────────────┐
  │   Sidebar    │         Content Area             │
  │  (nav menu)  │   (panel swapped on nav click)   │
  └──────────────┴─────────────────────────────────┘

CONNECTION FLOW:
  User clicks sidebar item
    → setCurrentWidget() swaps the visible panel
    → Each panel loads its own data on first show via its refresh() method
"""

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QLabel, QPushButton, QStackedWidget, QFrame, QSizePolicy
)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont

from assets.styles import SIDEBAR_BG, SIDEBAR_TEXT, PRIMARY, TEXT_MUTED

from windows.panels.dashboard_panel import DashboardPanel
from windows.panels.orders_panel    import OrdersPanel
from windows.panels.patients_panel  import PatientsPanel


class MainWindow(QMainWindow):
    """
    Root window. Owns the sidebar and the stacked content area.
    role — string passed from LoginWindow: 'admin', 'secretary', etc.
    """

    def __init__(self, role: str = "admin"):
        super().__init__()
        self.role = role
        self.setWindowTitle("Optical Cabinet — Management System")
        self.setMinimumSize(1100, 680)
        self._nav_buttons = {}
        self._build_ui()

    # ──────────────────────────────────────────────────────────────────────
    # Build layout
    # ──────────────────────────────────────────────────────────────────────

    def _build_ui(self):
        root = QWidget()
        self.setCentralWidget(root)

        layout = QHBoxLayout(root)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addWidget(self._build_sidebar())
        layout.addWidget(self._build_content())

    # ── Sidebar ────────────────────────────────────────────────────────────

    def _build_sidebar(self) -> QFrame:
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(220)

        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # App title
        title = QLabel("👁  Optical Cabinet")
        title.setObjectName("app_title")
        title.setFont(QFont("Segoe UI", 13, QFont.Bold))
        title.setStyleSheet(f"color: white; background: {SIDEBAR_BG}; padding: 22px 20px 16px 20px;")
        layout.addWidget(title)

        # Divider
        div = QFrame()
        div.setFixedHeight(1)
        div.setStyleSheet("background: rgba(255,255,255,0.12);")
        layout.addWidget(div)

        # Nav items: (label, icon, panel_key)
        # Add or remove items here to control what the sidebar shows
        nav_items = [
            ("Dashboard",   "🏠", "dashboard"),
            ("Orders",      "📋", "orders"),
            ("Patients",    "🧑‍⚕️", "patients"),
        ]

        # Role-based: only admin sees all panels
        if self.role in ("admin",):
            nav_items += [
                ("Inventory",   "📦", "inventory"),
                ("Reports",     "📊", "reports"),
            ]

        for label, icon, key in nav_items:
            btn = QPushButton(f"  {icon}  {label}")
            btn.setObjectName("nav_btn")
            btn.setCheckable(False)
            btn.setStyleSheet(f"""
                QPushButton {{
                    background: transparent;
                    color: {SIDEBAR_TEXT};
                    border: none;
                    text-align: left;
                    padding: 12px 20px;
                    font-size: 13px;
                    border-radius: 0;
                }}
                QPushButton:hover {{
                    background: rgba(255,255,255,0.08);
                }}
            """)
            btn.clicked.connect(lambda checked, k=key: self._navigate(k))
            layout.addWidget(btn)
            self._nav_buttons[key] = btn

        layout.addStretch()

        # Bottom: logged-in user label + logout
        div2 = QFrame()
        div2.setFixedHeight(1)
        div2.setStyleSheet("background: rgba(255,255,255,0.12);")
        layout.addWidget(div2)

        role_lbl = QLabel(f"Role: {self.role.title()}")
        role_lbl.setStyleSheet(f"color: rgba(255,255,255,0.5); font-size: 11px; padding: 10px 20px 4px 20px; background: transparent;")
        layout.addWidget(role_lbl)

        logout_btn = QPushButton("  🚪  Log Out")
        logout_btn.setStyleSheet(f"""
            QPushButton {{
                background: transparent;
                color: rgba(255,255,255,0.7);
                border: none;
                text-align: left;
                padding: 10px 20px;
                font-size: 13px;
            }}
            QPushButton:hover {{
                background: rgba(255,0,0,0.15);
                color: #f28b82;
            }}
        """)
        logout_btn.clicked.connect(self._logout)
        layout.addWidget(logout_btn)

        return sidebar

    # ── Content stack ──────────────────────────────────────────────────────

    def _build_content(self) -> QStackedWidget:
        self.stack = QStackedWidget()

        # Instantiate panels
        self._panels = {
            "dashboard": DashboardPanel(),
            "orders":    OrdersPanel(),
            "patients":  PatientsPanel(),
        }

        # Placeholder panels for inventory / reports (extend as needed)
        for key in ("inventory", "reports"):
            placeholder = self._placeholder_panel(key)
            self._panels[key] = placeholder

        for panel in self._panels.values():
            self.stack.addWidget(panel)

        # Start on dashboard
        self._navigate("dashboard")
        return self.stack

    def _placeholder_panel(self, name: str) -> QWidget:
        """Temporary panel shown for sections not yet implemented."""
        w = QWidget()
        v = QVBoxLayout(w)
        v.setAlignment(Qt.AlignCenter)
        icon = QLabel("🚧")
        icon.setFont(QFont("Segoe UI", 36))
        icon.setAlignment(Qt.AlignCenter)
        lbl = QLabel(f"{name.title()} panel coming soon")
        lbl.setFont(QFont("Segoe UI", 14))
        lbl.setStyleSheet(f"color: {TEXT_MUTED};")
        lbl.setAlignment(Qt.AlignCenter)
        v.addWidget(icon)
        v.addWidget(lbl)
        return w

    # ──────────────────────────────────────────────────────────────────────
    # Navigation
    # ──────────────────────────────────────────────────────────────────────

    def _navigate(self, key: str):
        """Switch the visible panel and highlight the active nav button."""
        panel = self._panels.get(key)
        if panel:
            self.stack.setCurrentWidget(panel)

        # Update nav button styles
        ACTIVE_STYLE = f"""
            QPushButton {{
                background: {PRIMARY};
                color: white;
                border: none;
                text-align: left;
                padding: 12px 20px;
                font-size: 13px;
                font-weight: bold;
                border-radius: 0;
            }}
        """
        INACTIVE_STYLE = f"""
            QPushButton {{
                background: transparent;
                color: {SIDEBAR_TEXT};
                border: none;
                text-align: left;
                padding: 12px 20px;
                font-size: 13px;
                border-radius: 0;
            }}
            QPushButton:hover {{
                background: rgba(255,255,255,0.08);
            }}
        """
        for k, btn in self._nav_buttons.items():
            btn.setStyleSheet(ACTIVE_STYLE if k == key else INACTIVE_STYLE)

    # ──────────────────────────────────────────────────────────────────────
    # Logout
    # ──────────────────────────────────────────────────────────────────────

    def _logout(self):
        """Close main window — main.py will show the login screen again."""
        self.close()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()