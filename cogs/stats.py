import discord, os, urllib, requests, json, random, aiohttp
import datetime
from discord.ext import commands
from discord.ext.commands import AutoShardedBot, cooldown, BucketType
from discord.ui import Button, View

from aiohttp import request
from aiohttp import ClientSession

colors = [0x00C09A, 0x00D166, 0x0099E1, 0xA652BB, 0xFD0061, 0xF8C300, 0xF93A2F]

class Stats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def stats(self, ctx):
        r = requests.get("https://tscache.com/donation_total.json")
        data = r.json()
        e = requests.get("https://tscache.com/lb_recent.json")
        data2 = e.json()
        headers = {}
        ts = datetime.datetime.fromtimestamp(data2["recent"][0]["created_at"])
        em = discord.Embed(
            title = "TeamSeas", url = "https://teamseas.org/",
            description = "Team Seas is an international collaborative fundraiser project run by YouTubers MrBeast and Mark Rober as a follow up to Team Trees. They have succeeded in raising 30 million U.S. dollars, pledging to remove 30,000,000 pounds of marine debris from the ocean by the end of 2021.",
            color = random.choice(colors)
        )
        em.set_author(name="#TeamSeas", icon_url = "https://cdn.discordapp.com/attachments/840374613169930310/927544831927025664/TeamSeas.png")
        em.add_field(name="Total lbs removed", value = f'{data["count"]}', inline = False)
        em.add_field(name="Most Recent Donator", value = f'{data2["recent"][0]["name"]}', inline = False)
        em.add_field(name="Donated", value = f'${data2["recent"][0]["pounds"]}')
        em.add_field(name="Message", value = f'{data2["recent"][0]["message_public"]}', inline = False)
        em.set_footer(text = f'Donated At: {ts.strftime("%Y-%m-%d %H:%M")}')
        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Stats(bot))