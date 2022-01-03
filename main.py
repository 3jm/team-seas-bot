import discord, os, urllib, requests, json, random, aiohttp
from discord.ext import commands
from discord.ext.commands import AutoShardedBot, cooldown, BucketType
from discord.ui import Button, View

from aiohttp import request
from aiohttp import ClientSession

colors = [0x00C09A, 0x00D166, 0x0099E1, 0xA652BB, 0xFD0061, 0xF8C300, 0xF93A2F]


bot = commands.Bot(command_prefix=(">"))
bot.remove_command('help')

@bot.event
async def on_ready():
    print("SoCal is online.")

@bot.event 
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
        em = discord.Embed(
            description=f"Command not found.",
            color = random.choice(colors)
        ) 
        await ctx.send(embed=em)

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'`cogs.{extension}` was loaded.')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'`cogs.{extension}` was unloaded. You can no longer use it until it is reloaded.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

token = open('token.json', 'r')
jsondata = token.read()
obj = json.loads(jsondata)

bot.run(str(obj['Token']))