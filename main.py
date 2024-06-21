import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from os import getenv

#load dotenv & assign variable to it
load_dotenv()
TOKEN = getenv('SERVER_TOKEN')

#bot starts here
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
@bot.event
async def on_ready():
    print("We're ready master.")

@bot.command()
async def hello(self):
    await self.send(f"Hi cutie >_< {self.author.mention}.")

bot.run(TOKEN)
