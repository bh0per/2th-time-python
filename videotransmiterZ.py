import io
import cv2
import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.video = True

bot = commands.Bot(command_prefix='!', intents=intents)
vc = None

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user.name}')

@tasks.loop(seconds=1)
async def send_camera_stream():
    global vc

    channel_id = 1 #Zastąp swoim ID kanału
    channel = bot.get_channel(channel_id)

    if channel:
        if vc is None or not vc.is_connected():
            vc = await channel.connect()

        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()

        if ret:
            _, buffer = cv2.imencode('.jpg', frame)
            image_bytes = buffer.tobytes()
            await channel.send(file=discord.File(io.BytesIO(image_bytes), filename='image.jpg'))
        else:
            print("Błąd podczas przechwytywania obrazu z kamery")

        cap.release()

@bot.command(name='start_stream')
async def start_stream(ctx):
    send_camera_stream.start()
    await ctx.send("Stream z kamerą rozpoczęty!")

@bot.command(name='stop_stream')
async def stop_stream(ctx):
    global vc
    send_camera_stream.stop()

    if vc and vc.is_connected():
        await vc.disconnect()

    vc = None
    await ctx.send("Stream z kamerą zatrzymany!")

bot.run('token bocika')
