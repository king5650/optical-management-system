# theme_dialog.py

from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QButtonGroup, QWidget, QGridLayout
)
from PySide6.QtCore import Qt
from theme_manager import THEMES, apply_theme


class ThemeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Choose Theme")
        self.setMinimumWidth(400)

        self.main_window = parent  # Store reference to MainWindow

        # Layouts
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.grid_layout = QGridLayout()
        self.layout.addLayout(self.grid_layout)

        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)

        # Build radio buttons with color previews
        self.build_theme_grid()

        # Apply + Cancel buttons
        button_layout = QHBoxLayout()
        apply_btn = QPushButton("Apply")
        cancel_btn = QPushButton("Cancel")
        apply_btn.clicked.connect(self.apply_theme)
        cancel_btn.clicked.connect(self.reject)
        button_layout.addWidget(apply_btn)
        button_layout.addWidget(cancel_btn)

        self.layout.addLayout(button_layout)

    def build_theme_grid(self):
        row, col = 0, 0
        for i, (theme_name, theme_data) in enumerate(THEMES.items()):
            # Theme card layout
            card = QWidget()
            card_layout = QVBoxLayout()
            card.setLayout(card_layout)

            # Color preview bar
            preview = QWidget()
            preview.setFixedHeight(25)
            preview.setStyleSheet(
                f"background-color: {theme_data['background']};"
            )
            text_preview = QLabel("Aa")
            text_preview.setStyleSheet(f"color: {theme_data['text']}; font-weight: bold;")
            text_preview.setAlignment(Qt.AlignCenter)
            preview_layout = QHBoxLayout(preview)
            preview_layout.addWidget(text_preview)

            # Radio button
            radio = QRadioButton(theme_name)
            self.button_group.addButton(radio)
            if i == 0:
                radio.setChecked(True)

            card_layout.addWidget(preview)
            card_layout.addWidget(radio)

            self.grid_layout.addWidget(card, row, col)
            col += 1
            if col >= 2:
                col = 0
                row += 1

    def apply_theme(self):
        selected_btn = self.button_group.checkedButton()
        if selected_btn:
            selected_theme = selected_btn.text()
            apply_theme(self.main_window, selected_theme)
        self.accept()
