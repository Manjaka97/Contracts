import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "Contracts",
      version = "1.0",
      description = "Contract Management Software",
      executables = [Executable("contracts.py", base=base, icon="images\\icon_black.ico")],
      )