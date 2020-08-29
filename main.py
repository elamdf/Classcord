import discord
from csahelp import get_stackoverflow
import tracemalloc
from discord.ext import commands
from scraper import classBot
token = open('token.txt', 'r')
token = token.read()
# scraper = classBot()
# scraper.login()
# scraper.gotophysics()
tracemalloc.start()
async def printlist(ctx,arg):
    print(arg)
    stuff = get_stackoverflow(arg)
    print(stuff)
    for i in stuff:
       # await ctx.send(i[0])
        await ctx.send(i[1])
    return True
bot = commands.Bot(command_prefix='$')
@bot.command()
async def helpme(ctx, *args):
    await printlist(ctx," ".join(args))
bot.run(token)