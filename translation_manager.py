# translation_manager.py
import os
from PySide6.QtCore import QTranslator, QLocale, QLibraryInfo, QCoreApplication, QEvent
from PySide6.QtWidgets import QApplication

class TranslationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            cls._instance.translators = []
            cls._instance.current_lang = "en"
        return cls._instance

    def switch_language(self, lang: str):
        app = QCoreApplication.instance()
        if not app:
            return

        # Remove old translators
        for t in self.translators:
            app.removeTranslator(t)
        self.translators.clear()

        self.current_lang = lang

        # Load .qm files
        i18n_dir = os.path.join(os.path.dirname(__file__), "translation")
        qm_files = ["patient_medicalList_ok" ,"add_item_type_form" , "item_inventory_ok" , "monthly_entries1_ok" , "patient_registration" , "puchase_board1_ok"]  # Add more as needed

        for base in qm_files:
            path = os.path.join(i18n_dir, f"{base}_{lang}.qm")
            if os.path.exists(path):
                t = QTranslator()
                if t.load(path):
                    app.installTranslator(t)
                    self.translators.append(t)

        # Load Qt base translation (for dialogs)
        qt_t = QTranslator()
        qt_path = QLibraryInfo.path(QLibraryInfo.TranslationsPath)
        if qt_t.load(f"qt_{QLocale(lang).name()}", qt_path):
            app.installTranslator(qt_t)
            self.translators.append(qt_t)

        # RTL support
        QApplication.setLayoutDirection(QLocale(lang).textDirection())

        # Retranslate all widgets
        self.retranslate_all()

    def retranslate_all(self):
        app = QApplication.instance()
        if not app:
            return

        # Send LanguageChange event to all widgets
        event = QEvent(QEvent.LanguageChange)
        for widget in app.allWidgets():
            # For .ui-based widgets
            if hasattr(widget, "retranslateUi"):
                try:
                    widget.retranslateUi(widget)
                except Exception as e:
                    print(f"retranslateUi failed for {widget}: {e}")
            # Trigger changeEvent for Python widgets using self.tr()
            QApplication.sendEvent(widget, event)