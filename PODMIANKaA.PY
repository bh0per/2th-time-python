import tkinter as tk
import pyautogui
import keyboard
import time

class MouseClickerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Mouse Clicker App")

        self.start_button = tk.Button(master, text="Start", command=self.start_clicker)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_clicker, state="disabled")
        self.stop_button.pack(pady=10)

        self.key_label = tk.Label(master, text="Press 't' to trigger actions")  # Zmiana na 't'
        self.key_label.pack()

        self.performing_actions = False

    def start_clicker(self):
        self.performing_actions = True
        self.start_button["state"] = "disabled"
        self.stop_button["state"] = "normal"
        self.key_label.config(text="Performing actions... Press 't' to stop.")  # Zmiana na 't'

        keyboard.on_press_key('t', self.perform_actions)  # Zmiana na 't'

    def stop_clicker(self):
        self.performing_actions = False
        self.start_button["state"] = "normal"
        self.stop_button["state"] = "disabled"

    def perform_actions(self, e):
        while self.performing_actions:
            for _ in range(5):
                pyautogui.click()  # Kliknij lewy przycisk myszy
                time.sleep(0.05)
                keyboard.press('z')  # Wciśnij klawisz "z"
                time.sleep(0.05)
                keyboard.release('z')  # Zwolnij klawisz "z"
                time.sleep(0.05)

    def reset_ui(self):
        pass

def main():
    root = tk.Tk()
    app = MouseClickerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
