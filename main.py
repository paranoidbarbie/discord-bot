import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
from requests import get
from re import search
from pytube import YouTube
#import json 

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
    discordChannel = bot.get_channel(1249457341854781520)
    channel = "https://youtube.com/@programmer_cutie"
    html = get(channel+'/videos').text
    videoLink = "https://www.youtube.com/watch?v=" + search('(?<="videoId":").*?(?=")', html).group()
    youtubeimage = "https://img.youtube.com/vi/" + search('(?<="videoId":").*?(?=")', html).group()
    ytTitle = YouTube(videoLink).title
    ytThumbnail = youtubeimage + '/maxresdefault.jpg'
    channel_id = 1254440863925407825
    discordChannel = bot.get_channel(channel_id)
    embedMessage = discord.Embed(title="Hi cuties", description=f"Check out Hannah's new video on youtube\n## [{ytTitle}]({videoLink})", color=discord.Color.pink())
    embedMessage.add_field(name='', value=f"Hope you'll love it.", inline=False)
    embedMessage.set_thumbnail(url=self.author.avatar)
    embedMessage.set_image(url=ytThumbnail)
    await discordChannel.send(f"<@&1249459622205722686>", embed=embedMessage) 

bot.run(TOKEN)

