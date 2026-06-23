import os
import sys
import json
import shutil

APP_NAME = "OpticalSystem"

# Writable system location
USER_CONFIG_DIR = os.path.join(
    os.environ.get("PUBLIC", "C:\\Users\\Public"),
    APP_NAME
)

USER_CONFIG_PATH = os.path.join(USER_CONFIG_DIR, "default_config.json")

#DEFAULT_CONFIG_PATH = "app\config\default_config.json"
DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "default_config.json")

def resource_path(relative_path: str) -> str:
    """
    Resolve path for dev and PyInstaller
    """
    base_path = getattr(sys, "_MEIPASS", os.getcwd())
    return os.path.join(base_path, relative_path)


def ensure_user_config_exists():
    """
    Copy default config if user config is missing
    """
    if not os.path.exists(USER_CONFIG_PATH):
        os.makedirs(USER_CONFIG_DIR, exist_ok=True)
        shutil.copy(
            resource_path(DEFAULT_CONFIG_PATH),
            USER_CONFIG_PATH
        )


def load_config() -> dict:
    """
    Load config with auto-recovery
    """
    ensure_user_config_exists()
    try:
        with open(USER_CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        # Restore default if corrupted
        shutil.copy(
            resource_path(DEFAULT_CONFIG_PATH),
            USER_CONFIG_PATH
        )
        with open(USER_CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)


CONFIG = load_config()

# FALLBACK DEFAULTS (CRITICAL)
SERVER_URL = CONFIG.get("SERVER_URL", "http://127.0.0.1:8000")
TIMEOUT = CONFIG.get("TIMEOUT", 10)
