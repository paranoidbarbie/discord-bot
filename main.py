import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from os import getenv, name
import requests
import re

#load dotenv & assign variable to it
load_dotenv()
TOKEN = getenv('SERVER_TOKEN')

#bot starts here
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("We're ready master.")

@bot.command(aliases=["hi", "heyo", "hey", "hewo", "hiya", "hai"])
async def hello(self):
    await self.send(f"Hi cutie >_< {self.author.mention}.")


@bot.command()
async def embedvideo(self):
    channel = "https://youtube.com/@programmer_cutie"
    html = requests.get(channel+'/videos').text
    videoLink = "https://www.youtube.com/watch?v=" + re.search('(?<="videoId":").*?(?=")', html).group()
    youtubeimage = "https://img.youtube.com/vi/" + re.search('(?<="videoId":").*?(?=")', html).group()
    ytThumbnail = youtubeimage + '/maxresdefault.jpg'
    channel_id = 1254440863925407825
    channel = bot.get_channel(channel_id)
    embedMessage = discord.Embed(title="Hi cuties", description="Check out Hannah's new video on youtube", color=discord.Color.pink())
    embedMessage.add_field(name='', value=videoLink)
    embedMessage.set_thumbnail(url=self.author.avatar)
    embedMessage.set_image(url=ytThumbnail)
    await self.send(f"<@&1249459622205722686>")
    await self.send(embed=embedMessage)
    

bot.run(TOKEN)

