import tkinter as tk
import keyboard
import pyautogui
import time

class KeyReplacerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Key Replacer App")

        self.key_label = tk.Label(master, text="Press 'u' to trigger key replacement")  
        self.key_label.pack()

        self.replacing_keys = False

        # Dodane nasłuchiwanie na klawisz 'u'
        keyboard.on_press_key('u', self.replace_keys)

        # Rozpoczęcie pętli
        self.master.after(100, self.check_for_key)

    def replace_keys(self, e):
        if not self.replacing_keys:
            self.replacing_keys = True
            self.key_label.config(text="Replacing keys...")

            # Symulacja kliknięcia "g" i naciśnięcia lewego przycisku myszy
            pyautogui.press('g')
            pyautogui.mouseDown(button='left')
            time.sleep(0.00)
            pyautogui.mouseUp(button='left')
            self.replacing_keys = False
            self.key_label.config(text="Press 'u' to trigger key replacement")

    def check_for_key(self):
        # Kontynuacja pętli, sprawdzanie co 100 ms
        self.master.after(100, self.check_for_key)
        self.master.update()

def main():
    root = tk.Tk()
    app = KeyReplacerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
