import subprocess
import sys

def install_module(module_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])

modules_to_install = ["pyautogui", "keyboard", "time"]

for module in modules_to_install:
    install_module(module)

print("Instalacja zakończona.")
