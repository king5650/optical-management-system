# runtime_hook_cwd.py
# ---------------------
# PyInstaller runtime hook — runs before your app code on every startup.
#
# PURPOSE:
#   Sets the working directory to sys._MEIPASS (where PyInstaller unpacks
#   all bundled files). This ensures that any code using bare relative paths
#   like open("style.qss") or QIcon("images/x.png") still works even
#   without resource_path(), giving you an extra safety net.
#
# LOCATION: Place in your project root alongside luncher.py
# SPEC:     Already referenced in OPticalsystem.spec as runtime_hooks=[...]

import os
import sys

if getattr(sys, 'frozen', False):
    # Running as .exe — change working dir to the unpacked temp folder
    os.chdir(sys._MEIPASS)
