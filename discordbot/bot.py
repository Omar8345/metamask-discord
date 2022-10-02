import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv('TOKEN')


intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready")
    print("Username: {}".format(bot.user.name))
    print("ID: {}".format(bot.user.id))
    print("Discord.py Version: {}".format(discord.__version__))
    print("------")

@bot.command()
async def linkwallet(ctx):
    await ctx.author.send("Click on this link to connect your MetaMask Wallet")
    await ctx.author.send("Link your wallet here: http://127.0.0.1:5000/{}".format(ctx.author.id))

@bot.command()
async def readuser(ctx, userid: str):
    r = requests.post('http://127.0.0.1:5000/read', json={'discordId': userid})
    await ctx.send(r.text)




bot.run(token)