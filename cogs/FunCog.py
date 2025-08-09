import random
from discord.ext import commands


class FunCog(commands.Cog):
    """Fun commands for the bot."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Responds with pong")
    async def ping(self, ctx):
        """Simple ping command to check responsiveness."""
        await ctx.send("Pong!")

    @commands.command(help="Greet the user")
    async def greet(self, ctx):
        """Greets the user who invoked the command."""
        await ctx.send(f"Hello {ctx.author.display_name}!")

    @commands.command(help="Roll a die with an optional number of sides")
    async def roll(self, ctx, sides: int = 6):
        """Roll a dice. Defaults to six sides if not specified."""
        result = random.randint(1, sides)
        await ctx.send(f"🎲 You rolled a {result}")

    @commands.command(help="Flip a coin")
    async def flip(self, ctx):
        """Flip a coin and return heads or tails."""
        outcome = random.choice(["Heads", "Tails"])
        await ctx.send(outcome)

    @commands.command(help="Echo the provided message")
    async def echo(self, ctx, *, message: str):
        """Echo back the user's message."""
        await ctx.send(message)


def setup(bot):
    bot.add_cog(FunCog(bot))
