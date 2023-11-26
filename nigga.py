import tkinter as tk
from tkinter import ttk
import keyboard
import pyautogui
import time

class MouseMoverApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Mouse Mover App")

        self.key_label = tk.Label(master, text="Press 'u' to move the mouse for 365 degrees to the right with right-click held down")
        self.key_label.pack()

        # Dodane pola do wprowadzania danych
        self.dpi_label = tk.Label(master, text="DPI:")
        self.dpi_label.pack()

        self.dpi_entry = ttk.Entry(master)
        self.dpi_entry.insert(0, "800")  # Domyślna wartość DPI
        self.dpi_entry.pack()

        self.sensitivity_label = tk.Label(master, text="Sensitivity X (%):")
        self.sensitivity_label.pack()

        self.sensitivity_entry = ttk.Entry(master)
        self.sensitivity_entry.insert(0, "12.6")  # Domyślna wartość sensitivity X
        self.sensitivity_entry.pack()

        # Dodane przycisku do aktywacji ruchu myszki
        self.activate_button = ttk.Button(master, text="Activate", command=self.activate_mouse_move)
        self.activate_button.pack()

        # Dodane nasłuchiwanie na klawisz 'u'
        keyboard.on_press_key('u', self.move_mouse)

    def activate_mouse_move(self):
        dpi = float(self.dpi_entry.get())
        sensitivity_x = float(self.sensitivity_entry.get())
        degrees_to_rotate = 365

        # Obliczenia liczby pikseli na osi X
        pixels_to_move_x = (degrees_to_rotate * dpi) / (360 * sensitivity_x)

        # Trzymanie prawego przycisku myszy i przeciąganie myszy
        pyautogui.mouseDown(button='right')
        pyautogui.drag(pixels_to_move_x, 0, duration=0.5)
        pyautogui.mouseUp(button='right')

    def move_mouse(self, e):
        self.key_label.config(text="Moving mouse to the right with right-click held down...")
        self.activate_mouse_move()
        self.key_label.config(text="Press 'u' to move the mouse for 365 degrees to the right with right-click held down")

def main():
    root = tk.Tk()
    app = MouseMoverApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
