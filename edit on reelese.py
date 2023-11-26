import tkinter as tk
import keyboard
import pyautogui
import time

class MouseClickerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Mouse Clicker App")

        self.key_label = tk.Label(master, text="Press 't' to trigger actions")  # Zmiana na 't'
        self.key_label.pack()

        self.performing_actions = False

        # Dodane nasłuchiwanie na klawisz 't'
        keyboard.on_press_key('t', self.perform_actions)

    def perform_actions(self, e):
        if not self.performing_actions:
            self.performing_actions = True
            self.key_label.config(text="Performing actions...")  # Zmiana na 't'

            # Kliknij klawisz "G"
            pyautogui.press('g')

            # Zakończ tryb wykonywania akcji
            self.performing_actions = False
            self.key_label.config(text="Press 't' to trigger actions")  # Zmiana na 't'

def main():
    root = tk.Tk()
    app = MouseClickerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
