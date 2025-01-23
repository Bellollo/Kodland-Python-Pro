#le immagini sono disposte così:
#images --->normal>meme1, meme2, meme3
#        |->homemade>my_meme


import discord
from discord.ext import commands
import os, random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command()
async def meme_homemade(ctx):
    with open('images/homemade/my_meme.jpg', 'rb') as meme:
        picture = discord.File(meme)
   
    await ctx.send(file=picture)

@bot.command()
async def normal_meme(ctx):
    image = random.choice(os.listdir('images/normal'))
    with open(f'images/{image}', 'rb') as meme:
        picture = discord.File(meme)
   
    await ctx.send(file=picture)

bot.run('token')
