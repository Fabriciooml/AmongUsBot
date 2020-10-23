import os
from discord.ext import commands, tasks
from dotenv import load_dotenv
import pyscreenshot as ImageGrab
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

global X1
global X2
global Y1
global Y2
X1 = 529
Y1 = 86
X2 = 1288
Y2 = 193

member_list = []
dead_list = []

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='am!')
    
@tasks.loop(seconds=1.0)
async def start_game(ctx):
  img = ImageGrab.grab(bbox=(X1, Y1, X2, Y2))
  img.save("test.jpg")
  img = cv2.imread("test.jpg")
  text = pytesseract.image_to_string(img)

  if("The Impostor" in text):
    await desmute_all(ctx)
  else:
    await mute_all(ctx)

@bot.command(name="mute_all", help="Mute all members.")
async def mute_all(ctx):
  for member in member_list:
    await member.edit(mute = True)

@bot.command(name="add_player", help="add new player.")
async def add_player(ctx):
  member_list.append(ctx.author)

@bot.command(name="desmute_all", help="Desmute all members.")
async def desmute_all(ctx):
  for member in member_list:
    await member.edit(mute = False)

@bot.command(name="death", help="player is dead.")
async def death(ctx):
  member_list.remove(ctx.author)
  dead_list.append(ctx.author)
  ctx.author.edit(mute = True)

@bot.command(name="desmute_self", help="self desmute.")
async def desmute_self(ctx):
  ctx.author.edit(mute = False)

@bot.command(name="set_resolution", help="set resolution.")
async def set_resolution(ctx, width:int, height:int):
  global X1
  global X2
  global Y1
  global Y2
  X1 = int(X1*width/1920)
  X2 = int(X2*width/1920)
  Y1 = int(Y1*height/1080)
  Y2 = int(Y2*height/1080)

@bot.command(name="start", help="start recognition.")
async def start_rec(ctx):
  start_game.start(ctx)

@bot.command(name="lobby", help="stop recognition.")
async def stop_rec(ctx):
  start_game.cancel()
  await desmute_all(ctx)
  member_list.append(dead_list)

bot.run(TOKEN)