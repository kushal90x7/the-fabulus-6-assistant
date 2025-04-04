# bot.py

import discord
from discord.ext import commands
import config

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{config.BOT_NAME} is online and fabulous! Logged in as {bot.user}")

# Load all cogs
bot.load_extension("cogs.greeter")

bot.run(config.BOT_TOKEN)
