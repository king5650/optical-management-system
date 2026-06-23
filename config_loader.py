import json
import os
import sys

# def resource_path(relative_path):
#     """For PyInstaller compatibility"""
#     if hasattr(sys, '_MEIPASS'):
#         return os.path.join(sys._MEIPASS, relative_path)
#     return os.path.join(os.path.dirname(__file__), relative_path)

# def load_config():
#     path = resource_path("config.json")
#     with open(path, "r") as f:
#         return json.load(f)

# CONFIG = load_config()
# BASE_URL = CONFIG["API_URL"]  # <---- IMPORTANT

# config_loader.py
import json, os, sys

def _get_config_path():
    if getattr(sys, 'frozen', False):
        base_path = os.path.dirname(sys.executable)  # .exe location
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, 'config.json')

def _load_config():
    with open(_get_config_path()) as f:
        config = json.load(f)
    config['BASE_URL'] = config['BASE_URL'].rstrip('/')
    return config

_config = _load_config()
BASE_URL = _config['BASE_URL']
