import tkinter as tk
import pyautogui

class MouseClickerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Mouse Clicker App")

        self.key_label = tk.Label(master, text="Move the mouse up to trigger actions")
        self.key_label.pack()

        # Zainicjalizuj zmienne
        self.idle_duration = 3  # Czas (w sekundach), po którym uznajemy myszkę za bezczynną
        self.last_mouse_position = pyautogui.position()

        # Ustawienie czasu, po którym sprawdzamy aktywność myszy
        self.master.after(1000, self.check_mouse_activity)

    def check_mouse_activity(self):
        current_mouse_position = pyautogui.position()

        # Sprawdź, czy myszka porusza się do góry
        if current_mouse_position != self.last_mouse_position:
            self.last_mouse_position = current_mouse_position
            self.idle_duration_counter = 0
        else:
            self.idle_duration_counter += 1

        if self.idle_duration_counter > self.idle_duration:
            # Kliknij klawisz "G"
            pyautogui.press('g')
            self.idle_duration_counter = 0

        # Ustaw ponownie sprawdzanie po upływie 1000 ms (1 sekunda)
        self.master.after(1000, self.check_mouse_activity)

def main():
    root = tk.Tk()
    app = MouseClickerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
