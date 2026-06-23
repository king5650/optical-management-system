# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMenuBar
# from PySide6.QtGui import QAction
# # ...existing code...
# import sys
# from PySide6.QtCore import QTranslator, QLocale, QEvent, QLibraryInfo

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle(self.tr("My App"))  # Translatable window title
#         self.label = QLabel(self.tr("Hello, World!"), self)
#         self.label.move(50, 50)

#         # Language selection menu
#         menu = self.menuBar().addMenu(self.tr("Language"))
#         eng_action = QAction(self.tr("English"), self)
#         eng_action.triggered.connect(lambda: self.change_language("en"))
#         fr_action = QAction(self.tr("French"), self)
#         fr_action.triggered.connect(lambda: self.change_language("fr"))
#         menu.addAction(eng_action)
#         menu.addAction(fr_action)

#     def change_language(self, lang):
#         # Store the translator as an instance variable to keep it alive
#         self.translator = QTranslator()
#         if lang == "fr":
#             if self.translator.load("app_fr", "i18n/"):
#                 QApplication.instance().installTranslator(self.translator)
#         elif lang == "en":
#             QApplication.instance().removeTranslator(self.translator)  # Revert to default (English)
        
#         # Optional: Load Qt's translations for standard dialogs
#         self.qt_translator = QTranslator()
#         qt_locale = QLocale(lang).name()
#         self.qt_translator.load(f"qt_{qt_locale}", QLibraryInfo.path(QLibraryInfo.TranslationsPath))
#         QApplication.instance().installTranslator(self.qt_translator)

#         self.retranslate_ui()

#     def retranslate_ui(self):
#         # Update all translatable UI elements
#         self.setWindowTitle(self.tr("My App"))
#         self.label.setText(self.tr("Hello, World!"))
#         # Menu items are automatically updated by Qt for QAction

#     def changeEvent(self, event):
#         # Handle language change events to update UI
#         if event.type() == QEvent.LanguageChange:
#             self.retranslate_ui()
#         super().changeEvent(event)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())
    
#venv\Scripts\pyside6-lrelease.exe "translation/patient_registration.ts" -qm translation\patient_medicalList_ok.qm    
#venv\Scripts\pyside6-lrelease.exe "translation/add_item_type_form.ts" -qm translation\add_item_type_form.qm    
#venv\Scripts\pyside6-lrelease.exe "translation/item_inventory_ok.ts" -qm translation\item_inventory_ok.qm
#venv\Scripts\pyside6-lrelease.exe "translation/monthly_entries1_ok.ts" -qm translation\monthly_entries1_ok.qm
#venv\Scripts\pyside6-lrelease.exe "translation/patient_registration.ts" -qm translation\patient_registration.qm
#venv\Scripts\pyside6-lrelease.exe "translation/puchase_board1_ok.ts" -qm translation\puchase_board1_ok.qm
#venv\Scripts\pyside6-lrelease.exe "main_ui_en.ts" -qm main_ui_en.qm  

#venv\Scripts\pyside6-lupdate.exe "front_end\final ui\prescription_form_ok.ui" -ts prescription_form_en.ts   modules\backup_module\BACKUPSYSTEM.py

#venv\Scripts\pyside6-lupdate.exe "modules\backup_module\BACKUPSYSTEM.py" -ts translation\BACKUPSYSTEM.ts



#venv\Scripts\pyside6-lrelease.exe i18n/main_ui_fr.ts -qm i18n/TS_fr.qm    payment_history_report


#venv\Scripts\pyside6-lrelease.exe translation/payment_history_report.ts -qm translation/payment_history_report.qm       

#venv\Scripts\pyside6-lrelease.exe "translation/backupsystemfr.ts" -qm translation/backupsystemfr.qm  

#venv\Scripts\pyside6-lrelease.exe "translation\whatsapp_aut.ts" -qm translation\whatsapp_aut.qm

# venv\Scripts\pyside6-lupdate.exe modules\sales_module\payment_history_report.py -ts translation/payment_history_report.ts  

# venv\Scripts\pyside6-lupdate.exe whatsapp_auto\main.py -ts translation/whatsapp_aut.ts 

#"patient_medicalList_ok" ,"add_item_type_form" , "item_inventory_ok" , "monthly_entries1_ok" , "patient_registration" , "puchase_board1_ok"
#pyinstaller --noconsole --name OPticalsystem --onefile luncher.py
import sys
import os
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QMenuBar, QWidget, QVBoxLayout
)
from PySide6.QtGui import QAction
from PySide6.QtCore import (
    QTranslator, QLocale, QEvent, QLibraryInfo, QSettings
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ------------------------------------------------------------------
        # Keep every translator alive – otherwise Python GC removes them
        # ------------------------------------------------------------------
        self.translators: list[QTranslator] = []

        # Load the last used language (fallback to English)
        self.current_lang = self.load_language()

        self.init_ui()
        self.apply_language(self.current_lang)

    # ----------------------------------------------------------------------
    # UI construction (unchanged visual layout)
    # ----------------------------------------------------------------------
    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        self.label = QLabel(self.tr("Hello, World!"))
        layout.addWidget(self.label)

        # ---- Language menu -------------------------------------------------
        menu = self.menuBar().addMenu(self.tr("Language"))

        en_act = QAction(self.tr("English"), self)
        fr_act = QAction(self.tr("French"), self)

        en_act.triggered.connect(lambda: self.switch_language("en"))
        fr_act.triggered.connect(lambda: self.switch_language("fr"))

        menu.addAction(en_act)
        menu.addAction(fr_act)

        self.resize(300, 150)

    # ----------------------------------------------------------------------
    # Core language switching logic
    # ----------------------------------------------------------------------
    def switch_language(self, lang: str):
        if lang == self.current_lang:
            return

        # 1. Remove every previously installed translator
        app = QApplication.instance()
        for t in self.translators:
            app.removeTranslator(t)
        self.translators.clear()

        self.current_lang = lang

        # 2. Load *our* translation file (i18n/app_xx.qm)
        tr = QTranslator()
        qm_path = os.path.join("i18n", f"app_{lang}.qm")
        if tr.load(qm_path):
            app.installTranslator(tr)
            self.translators.append(tr)

        # 3. Load Qt’s own translation (for QMessageBox, etc.)
        qt_tr = QTranslator()
        locale_name = QLocale(lang).name()          # e.g. "fr_FR"
        qt_path = QLibraryInfo.path(QLibraryInfo.TranslationsPath)
        if qt_tr.load(f"qt_{locale_name}", qt_path):
            app.installTranslator(qt_tr)
            self.translators.append(qt_tr)

        # 4. Layout direction (LTR vs RTL)
        QApplication.setLayoutDirection(QLocale(lang).textDirection())

        # 5. Persist choice
        self.save_language(lang)

        # 6. Retranslate UI
        self.retranslate_ui()
        app.processEvents()   # force immediate repaint

    # ----------------------------------------------------------------------
    # Apply language on start-up (called from __init__)
    # ----------------------------------------------------------------------
    def apply_language(self, lang: str):
        # Same code as switch_language but without the "if same" guard
        app = QApplication.instance()
        for t in self.translators:
            app.removeTranslator(t)
        self.translators.clear()

        self.current_lang = lang

        tr = QTranslator()
        if tr.load(os.path.join("i18n", f"app_{lang}.qm")):
            app.installTranslator(tr)
            self.translators.append(tr)

        qt_tr = QTranslator()
        locale_name = QLocale(lang).name()
        qt_path = QLibraryInfo.path(QLibraryInfo.TranslationsPath)
        if qt_tr.load(f"qt_{locale_name}", qt_path):
            app.installTranslator(qt_tr)
            self.translators.append(qt_tr)

        QApplication.setLayoutDirection(QLocale(lang).textDirection())
        self.retranslate_ui()

    # ----------------------------------------------------------------------
    # Retranslate every widget that uses self.tr()
    # ----------------------------------------------------------------------
    def retranslate_ui(self):
        self.setWindowTitle(self.tr("My App"))
        self.label.setText(self.tr("Hello, World!"))
        # QAction texts are automatically retranslated by Qt

    # ----------------------------------------------------------------------
    # QEvent.LanguageChange → Qt’s own retranslation mechanism
    # ----------------------------------------------------------------------
    def changeEvent(self, event: QEvent):
        if event.type() == QEvent.LanguageChange:
            self.retranslate_ui()
        super().changeEvent(event)

    # ----------------------------------------------------------------------
    # Persistence helpers
    # ----------------------------------------------------------------------
    def save_language(self, lang: str):
        settings = QSettings("MyCompany", "MyApp")
        settings.setValue("language", lang)

    def load_language(self) -> str:
        settings = QSettings("MyCompany", "MyApp")
        return settings.value("language", "en")

# --------------------------------------------------------------------------
# Application entry point
# --------------------------------------------------------------------------
if __name__ == "__main__":
    # Make QSettings work on all platforms
    QApplication.setOrganizationName("MyCompany")
    QApplication.setApplicationName("MyApp")

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())