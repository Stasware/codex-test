import os
import random
from discord.ext import commands

# Read the bot token from an environment variable for security
TOKEN = os.getenv("DISCORD_TOKEN")

# Configure the bot with a simple prefix
bot = commands.Bot(command_prefix="!")

@bot.command(help="Responds with pong")
async def ping(ctx):
    """Simple ping command to check responsiveness."""
    await ctx.send("Pong!")

@bot.command(help="Greet the user")
async def greet(ctx):
    """Greets the user who invoked the command."""
    await ctx.send(f"Hello {ctx.author.display_name}!")

@bot.command(help="Roll a die with an optional number of sides")
async def roll(ctx, sides: int = 6):
    """Roll a dice. Defaults to six sides if not specified."""
    result = random.randint(1, sides)
    await ctx.send(f"🎲 You rolled a {result}")

@bot.command(help="Flip a coin")
async def flip(ctx):
    """Flip a coin and return heads or tails."""
    outcome = random.choice(["Heads", "Tails"])
    await ctx.send(outcome)

@bot.command(help="Echo the provided message")
async def echo(ctx, *, message: str):
    """Echo back the user's message."""
    await ctx.send(message)

if __name__ == "__main__":
    if not TOKEN:
        raise ValueError("DISCORD_TOKEN environment variable not set.")
    bot.run(TOKEN)
