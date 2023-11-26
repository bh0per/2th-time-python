import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
import requests
import json

WEBHOOK_URL = "https://discord.com/api/webhooks/1178426995701461012/7grgokYxmUBWxxGP9H18CA1REL-Y8vs0RwwvPoY6tJN8618NjvQeRhbpWNYkwYJZNyHQ"

def send_discord_message(message, file_path=None):
    data = {
        "content": message
    }

    files = None
    if file_path:
        files = {"file": ("uploaded_file", open(file_path, "rb"))}

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(WEBHOOK_URL, data=json.dumps(data), headers=headers, files=files)

    if response.status_code == 204:
        messagebox.showinfo("Sukces", "Wiadomość została wysłana pomyślnie.")
    else:
        messagebox.showerror("Błąd", f"Wystąpił błąd przy wysyłaniu wiadomości. Kod odpowiedzi: {response.status_code}")

def send_message(event=None):
    user_message = message_entry.get("1.0", tk.END).strip()
    if user_message:
        send_discord_message(user_message, file_path_entry.get())
        message_entry.delete("1.0", tk.END)
        file_path_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Uwaga", "Wprowadź wiadomość przed wysłaniem!")

def browse_file():
    file_path = filedialog.askopenfilename()
    file_path_entry.delete(0, tk.END)
    file_path_entry.insert(0, file_path)

# Stworzenie głównego okna
root = tk.Tk()
root.title("Discord Message Sender")

# Pole na wprowadzenie wiadomości
message_label = tk.Label(root, text="Wiadomość:")
message_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
message_entry = scrolledtext.ScrolledText(root, width=50, height=5, wrap=tk.WORD)
message_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

# Pole na ścieżkę do pliku
file_path_label = tk.Label(root, text="Ścieżka do pliku:")
file_path_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
file_path_entry = tk.Entry(root, width=40)
file_path_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
file_browse_button = tk.Button(root, text="Przeglądaj", command=browse_file)
file_browse_button.grid(row=1, column=2, pady=5)

# Przycisk do wysłania wiadomości
send_button = tk.Button(root, text="Wyślij Wiadomość", command=send_message)
send_button.grid(row=2, column=1, padx=10, pady=10)

# Dodanie zdarzenia Enter do pola wprowadzania wiadomości
message_entry.bind("<Return>", send_message)

# Dodanie zdarzenia FocusIn do pola wprowadzania wiadomości
message_entry.bind("<FocusIn>", lambda event: root.bind("<Return>", send_message))

# Dodanie zdarzenia FocusOut do pola wprowadzania wiadomości
message_entry.bind("<FocusOut>", lambda event: root.unbind("<Return>"))

# Uruchomienie pętli głównej
root.mainloop()
