import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


"""
assets/styles.py — Application-wide stylesheet and colour tokens

WHY CENTRALISE STYLES?
───────────────────────
Defining colours and fonts in one place means you change a colour once
and it updates everywhere. No hunting through 10 files.
"""

# ── Colour tokens ────────────────────────────────────────────────────────────
PRIMARY      = "#1a73e8"     # blue — buttons, active sidebar item
PRIMARY_DARK = "#1557b0"     # blue darker — button hover
DANGER       = "#d93025"     # red — delete, cancel actions
SUCCESS      = "#1e8e3e"     # green — paid status badge
WARNING      = "#f9ab00"     # amber — partial payment badge
SIDEBAR_BG   = "#1e1e2e"     # near-black — sidebar background
SIDEBAR_TEXT = "#cdd6f4"     # light lavender — sidebar text
CARD_BG      = "#ffffff"     # white — card surfaces
PAGE_BG      = "#f0f2f5"     # light grey — page background
BORDER       = "#dadce0"     # light grey — card borders
TEXT_PRIMARY = "#202124"     # near-black — main text
TEXT_MUTED   = "#5f6368"     # grey — secondary text

# ── Status badge colours ──────────────────────────────────────────────────────
STATUS_COLOURS = {
    "draft":       ("#e8eaed", "#3c4043"),
    "confirmed":   ("#e8f0fe", "#1a73e8"),
    "in_progress": ("#fce8b2", "#b06000"),
    "ready":       ("#e6f4ea", "#137333"),
    "delivered":   ("#d2e3fc", "#185abc"),
    "completed":   ("#e6f4ea", "#137333"),
    "cancelled":   ("#fce8e6", "#c5221f"),
}

PAYMENT_COLOURS = {
    "unpaid":  ("#fce8e6", "#c5221f"),
    "partial": ("#fce8b2", "#b06000"),
    "paid":    ("#e6f4ea", "#137333"),
}

# ── Main stylesheet ───────────────────────────────────────────────────────────
APP_STYLE = f"""
QMainWindow, QWidget {{
    background-color: {PAGE_BG};
    font-family: "Segoe UI", "Arial", sans-serif;
    font-size: 13px;
    color: {TEXT_PRIMARY};
}}

/* ── Sidebar ── */
#sidebar {{
    background-color: {SIDEBAR_BG};
    min-width: 220px;
    max-width: 220px;
}}
#sidebar QPushButton {{
    background: transparent;
    color: {SIDEBAR_TEXT};
    border: none;
    text-align: left;
    padding: 12px 20px;
    font-size: 13px;
    border-radius: 0;
}}
#sidebar QPushButton:hover {{
    background-color: rgba(255,255,255,0.08);
}}
#sidebar QPushButton[active="true"] {{
    background-color: {PRIMARY};
    color: white;
    font-weight: bold;
}}
#app_title {{
    color: white;
    font-size: 15px;
    font-weight: bold;
    padding: 20px;
    background-color: {SIDEBAR_BG};
}}

/* ── Cards ── */
#card {{
    background-color: {CARD_BG};
    border: 1px solid {BORDER};
    border-radius: 8px;
    padding: 16px;
}}

/* ── Primary button ── */
QPushButton#primary_btn {{
    background-color: {PRIMARY};
    color: white;
    border: none;
    border-radius: 6px;
    padding: 8px 18px;
    font-size: 13px;
    font-weight: bold;
}}
QPushButton#primary_btn:hover {{
    background-color: {PRIMARY_DARK};
}}
QPushButton#primary_btn:disabled {{
    background-color: #bdc1c6;
}}

/* ── Danger button ── */
QPushButton#danger_btn {{
    background-color: {DANGER};
    color: white;
    border: none;
    border-radius: 6px;
    padding: 8px 18px;
    font-size: 13px;
}}
QPushButton#danger_btn:hover {{
    background-color: #b3261e;
}}

/* ── Secondary button ── */
QPushButton#secondary_btn {{
    background-color: white;
    color: {PRIMARY};
    border: 1px solid {PRIMARY};
    border-radius: 6px;
    padding: 8px 18px;
    font-size: 13px;
}}
QPushButton#secondary_btn:hover {{
    background-color: #e8f0fe;
}}

/* ── Input fields ── */
QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox, QTextEdit {{
    border: 1px solid {BORDER};
    border-radius: 6px;
    padding: 7px 10px;
    background: white;
    font-size: 13px;
    color: {TEXT_PRIMARY};
}}
QLineEdit:focus, QComboBox:focus {{
    border: 2px solid {PRIMARY};
}}
QComboBox::drop-down {{
    border: none;
    padding-right: 8px;
}}

/* ── Table ── */
QTableWidget {{
    background: white;
    border: 1px solid {BORDER};
    border-radius: 6px;
    gridline-color: #f1f3f4;
    selection-background-color: #e8f0fe;
    selection-color: {TEXT_PRIMARY};
    alternate-background-color: #fafafa;
}}
QTableWidget::item {{
    padding: 8px;
}}
QHeaderView::section {{
    background-color: #f8f9fa;
    border: none;
    border-bottom: 1px solid {BORDER};
    padding: 8px;
    font-weight: bold;
    color: {TEXT_MUTED};
    font-size: 12px;
}}

/* ── Status labels ── */
QLabel#status_badge {{
    border-radius: 10px;
    padding: 3px 10px;
    font-size: 11px;
    font-weight: bold;
}}

/* ── Section headers ── */
QLabel#section_title {{
    font-size: 18px;
    font-weight: bold;
    color: {TEXT_PRIMARY};
}}
QLabel#section_sub {{
    font-size: 12px;
    color: {TEXT_MUTED};
}}

/* ── Stat card number ── */
QLabel#stat_number {{
    font-size: 28px;
    font-weight: bold;
    color: {PRIMARY};
}}
QLabel#stat_label {{
    font-size: 12px;
    color: {TEXT_MUTED};
}}

/* ── Scrollbars ── */
QScrollBar:vertical {{
    width: 8px;
    background: transparent;
}}
QScrollBar::handle:vertical {{
    background: {BORDER};
    border-radius: 4px;
}}

/* ── Dialog ── */
QDialog {{
    background-color: {CARD_BG};
}}
"""
