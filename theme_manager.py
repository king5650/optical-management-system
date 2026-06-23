# theme_manager.py

from PySide6.QtWidgets import QWidget

# 🎨 Define available themes
THEMES = {
    
    "Default": None,
    
    "Light": {
        "background": "#FFFFFF",
        "text": "#000000",
        "sidebar": "#F0F0F0",
        "button": "#E0E0E0"
    },
    "Dark": {
        "background": "#2E3440",
        "text": "#ECEFF4",
        "sidebar": "#3B4252",
        "button": "#4C566A"
    },
    "Ocean Blue": {
        "background": "#DDEFFF",
        "text": "#002244",
        "sidebar": "#99CCFF",
        "button": "#66B2FF"
    },
    "Forest Green": {
        "background": "#E6F2E6",
        "text": "#003300",
        "sidebar": "#99CC99",
        "button": "#66B266"
    },

    
}

def apply_theme(main_window: QWidget, theme_name: str):
    """
    Apply the selected theme to the main window and its key widgets.
    :param main_window: The QMainWindow instance
    :param theme_name: Name of the theme to apply
    """
    if theme_name not in THEMES:
        print(f"Theme '{theme_name}' not found.")
        return

    theme = THEMES[theme_name]
    

    
    # Apply background and text color to the entire main window
    main_window.setStyleSheet(f"""
        QMainWindow {{
            background-color: {theme['background']};
            color: {theme['text']};
        }}

        QLabel {{
            color: {theme['text']};
        }}

        QPushButton {{
            background-color: {theme['button']};
            color: {theme['text']};
            border-radius: 4px;
            padding: 6px 10px;
        }}
        QPushButton:hover {{
            background-color: #cccccc;
        }}
    """)

    # Apply sidebar color manually (since it's separate widgets)
    if hasattr(main_window.ui, 'icon_only_widget'):
        main_window.ui.icon_only_widget.setStyleSheet(
            f"background-color: {theme['sidebar']};"
        )
    if hasattr(main_window.ui, 'full_menu_widget'):
        main_window.ui.full_menu_widget.setStyleSheet(
            f"background-color: {theme['sidebar']};"
        )

    # You can expand to style toolbars, search bars, etc.
    print(f"Theme '{theme_name}' applied.")
