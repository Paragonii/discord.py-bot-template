#Imports and stuff
import discord
from discord.ext import commands

#This is essential to making the bot
bot = commands.Bot(command_prefix="prefix")
#let me explain: This basically tells the code that the "bot" variable will be used for commands.

@bot.event
async def on_ready():
  print(f"You are connected to {bot.user.name}")
  #this tells us when the bot is online

#text command
@bot.command()
async def hello(ctx):
  await ctx.send("Hey there!")
  
#This is NOT recommended, your token should be in a .json file or any file that can keep it safe.
token = "Token"
bot.run(token)
