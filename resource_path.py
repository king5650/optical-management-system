"""
resource_path.py
-----------------
Resolves file paths correctly whether the app is running:
  - As a normal Python script (development)
  - As a PyInstaller-packaged .exe (production)

PROBLEM:
  When packaged, PyInstaller extracts files to a temp folder (sys._MEIPASS).
  Relative paths like "images/logo.png" work during development but break
  in the .exe because the working directory is not the project root.

SOLUTION:
  Always use resource_path() to build paths to any asset file.

USAGE — replace ALL hardcoded asset paths in your app like this:

  BEFORE:  QIcon("images/logo1.ico")
  AFTER:   QIcon(resource_path("images/logo1.ico"))

  BEFORE:  with open("style.qss") as f:
  AFTER:   with open(resource_path("style.qss")) as f:

  BEFORE:  translator.load("translation_fr.qm")
  AFTER:   translator.load(resource_path("translation_fr.qm"))

Place this file in your project root (same level as luncher.py).
"""

import os
import sys


def resource_path(relative_path: str) -> str:
    """
    Returns the absolute path to a resource file.

    In development:  returns path relative to project root
    In .exe:         returns path relative to PyInstaller's temp extract folder
    """
    if getattr(sys, 'frozen', False):
        # Running as packaged .exe — PyInstaller sets sys._MEIPASS
        base_path = sys._MEIPASS
    else:
        # Running as script — use the directory of this file (project root)
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)
