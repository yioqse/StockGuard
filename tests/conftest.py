import os
import sys

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PACKAGE_DIR = os.path.join(ROOT_DIR, "stockguard")

if PACKAGE_DIR not in sys.path:
    sys.path.insert(0, PACKAGE_DIR)
