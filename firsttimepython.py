import tkinter as tk
from threading import Thread
import pyautogui
import keyboard
import time

class ColorClickerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Color Clicker App")

        self.start_button = tk.Button(master, text="Start", command=self.start_color_clicker)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_color_clicker)
        self.stop_button.pack(pady=10)
        self.stop_button["state"] = "disabled"

        self.status_label = tk.Label(master, text="")
        self.status_label.pack(pady=10)

        self.color_check_thread = None
        self.stop_event = None

    def start_color_clicker(self):
        self.start_button["state"] = "disabled"
        self.stop_button["state"] = "normal"
        self.status_label.config(text="Running...")

        self.stop_event = False

        def color_clicker_loop():
            screen_width, screen_height = pyautogui.size()
            center_x, center_y = screen_width // 2, screen_height // 2

            while not self.stop_event:
                if keyboard.is_pressed('q'):
                    if self.is_color_at_center(center_x, center_y):
                        self.status_label.config(text="Color found! Clicking.")
                        pyautogui.click()
                        time.sleep(1)

            self.status_label.config(text="Stopped.")
            self.start_button["state"] = "normal"
            self.stop_button["state"] = "disabled"

        self.color_check_thread = Thread(target=color_clicker_loop)
        self.color_check_thread.start()

    def stop_color_clicker(self):
        self.stop_event = True

    def is_color_at_center(self, x, y, color=(135, 206, 250), tolerance=10):
        screen = pyautogui.screenshot()
        pixel_color = screen.getpixel((x, y))
        for i in range(3):
            if not color[i] - tolerance <= pixel_color[i] <= color[i] + tolerance:
                return False
        return True

def main():
    root = tk.Tk()
    app = ColorClickerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
