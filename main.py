import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
from requests import get
from re import search
from pytube import YouTube

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
    await self.send(f"Hi cutie >_< {self.author.mention}.") #genetic basic hello


@bot.command()
async def embedvideo(self):
    roleid = "<@&role_id>" #put the role id you want to mention
    ytChannelID = "channeid" #put the channel id of the channel you wanna show video of
    channel = "https://youtube.com/@" + ytChannelID #put the channel id you wanna fetch data from 
    discordChannel = bot.get_channel("channelid") # replace channelid with actual channel id wiout the parenthesis
    html = get(channel+'/videos').text
    videoLink = "https://www.youtube.com/watch?v=" + search('(?<="videoId":").*?(?=")', html).group()
    youtubeimage = "https://img.youtube.com/vi/" + search('(?<="videoId":").*?(?=")', html).group()
    ytTitle = YouTube(videoLink).title
    ytThumbnail = youtubeimage + '/maxresdefault.jpg'
    embedMessage = discord.Embed(title="Hi cuties", description=f"Check out {ytChannelID}'s new video on youtube\n## [{ytTitle}]({videoLink})", color=discord.Color.pink())
    embedMessage.add_field(name='', value=f"Hope you'll love it.", inline=False)
    embedMessage.set_thumbnail(url=self.author.avatar)
    embedMessage.set_image(url=ytThumbnail)
    await discordChannel.send(f"{roleid}", embed=embedMessage) 

bot.run(TOKEN)

