import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox
from discord.ext import commands
import discord

TOKEN = 'TWÓJ_TOKEN_BOTA'
CHANNEL_ID = 'ID_TWEGO_KANAŁU'

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user.name}')

@bot.command(name='get_channel_messages')
async def get_channel_messages(ctx):
    channel = bot.get_channel(int(CHANNEL_ID))
    messages = await channel.history(limit=10).flatten()

    display_text = ""
    for message in reversed(messages):
        display_text += f"{message.author.name}: {message.content}\n"

    text_widget.config(state=tk.NORMAL)
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, display_text)
    text_widget.config(state=tk.DISABLED)

def start_bot():
    bot.run(TOKEN)

def get_messages():
    bot.invoke(get_channel_messages)

# Stworzenie głównego okna
root = tk.Tk()
root.title("Discord Channel Viewer")

# Pole tekstowe do wyświetlania wiadomości
text_widget = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD, state=tk.DISABLED)
text_widget.grid(row=0, column=0, padx=10, pady=10)

# Przycisk do pobierania wiadomości z kanału Discord
get_messages_button = tk.Button(root, text="Pobierz wiadomości", command=get_messages)
get_messages_button.grid(row=1, column=0, padx=10, pady=10)

# Uruchomienie pętli głównej
root.after(0, start_bot)  # Uruchomienie bota w tle
root.mainloop()
