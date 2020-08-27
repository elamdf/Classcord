import discord

import tracemalloc
from discord.ext import commands
from scraper import classBot
token = open('token.txt', 'r')
token = token.read()
scraper = classBot()
scraper.login()
scraper.gotophysics()
tracemalloc.start()
async def printlist(ctx,arg):
    stuff = scraper.grabstream(int(arg))
    for i in stuff:
        await ctx.send(i[1])
        await ctx.send(i[0])
    return True
bot = commands.Bot(command_prefix='$')
@bot.command()
async def grabstream(ctx, arg):
    await printlist(ctx,arg)
bot.run(token)