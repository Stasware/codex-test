import os
import discord
from discord.ext import commands

# Read the bot token from an environment variable for security
TOKEN = os.getenv("DISCORD_TOKEN")

# Configure intents to allow message content access
intents = discord.Intents.default()
intents.message_content = True

# Configure the bot with a simple prefix
bot = commands.Bot(command_prefix="!", intents=intents)

if __name__ == "__main__":
    if not TOKEN:
        raise ValueError("DISCORD_TOKEN environment variable not set.")
    # Load cogs containing commands and listeners
    bot.load_extension("cogs.FunCog")
    bot.load_extension("cogs.RelayCog")
    bot.run(TOKEN)
