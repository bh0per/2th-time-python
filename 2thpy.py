import tkinter as tk
import pyautogui
import keyboard
import time
from threading import Thread

class ColorClickerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Color Clicker App")

        self.start_button = tk.Button(master, text="Start", command=self.start_color_clicker)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_color_clicker)
        self.stop_button.pack(pady=10)
        self.stop_button["state"] = "disabled"

        self.color_label = tk.Label(master, text="Target Color (R G B):")
        self.color_label.pack()

        self.color_entry = tk.Entry(master)
        self.color_entry.insert(0, "135 206 250")  # Domyślny kolor: jasnoniebieski
        self.color_entry.pack()

        self.key_label = tk.Label(master, text="Activation Key:")
        self.key_label.pack()

        self.key_entry = tk.Entry(master)
        self.key_entry.insert(0, "q")  # Domyślny klawisz aktywacyjny: 'q'
        self.key_entry.pack()

        self.status_label = tk.Label(master, text="")
        self.status_label.pack(pady=10)

        self.color_check_thread = None
        self.stop_event = None

    def start_color_clicker(self):
        self.start_button["state"] = "disabled"
        self.stop_button["state"] = "normal"
        self.status_label.config(text="Running...")

        target_color = tuple(map(int, self.color_entry.get().split()))
        activation_key = self.key_entry.get()

        self.stop_event = False

        def color_clicker_loop():
            screen_width, screen_height = pyautogui.size()
            center_x, center_y = screen_width // 2, screen_height // 2

            while not self.stop_event:
                if keyboard.is_pressed(activation_key):
                    if self.is_color_at_center(center_x, center_y, target_color):
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

    def is_color_at_center(self, x, y, target_color, tolerance=10):
        screen = pyautogui.screenshot()
        pixel_color = screen.getpixel((x, y))

        for i in range(3):
            if not target_color[i] - tolerance <= pixel_color[i] <= target_color[i] + tolerance:
                return False
        return True

def main():
    root = tk.Tk()
    app = ColorClickerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
