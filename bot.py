import os
import discord
import time
from discord.ext import commands
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

start_game = False

member_list = []

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='am!')

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
    print("desmutado")
    await member.edit(mute = False)
    print("desmutado")

@bot.command(name="death", help="player is dead.")
async def death(ctx):
  member_list.remove(ctx.author)

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

@bot.command(name="start", help="start game.")
async def start(ctx):
  start_game = True

  while(start_game):
    img = ImageGrab.grab(bbox=(X1, Y1, X2, Y2))
    img.save("test.jpg")
    img = cv2.imread("test.jpg")
    text = pytesseract.image_to_string(img)
    
    if("The Impostor" in text):
      await desmute_all(ctx)
    else:
      await mute_all(ctx)
    time.sleep(10)

bot.run(TOKEN)
