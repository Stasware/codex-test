from discord.ext import commands


class RelayCog(commands.Cog):
    """Relays all messages to a specific channel."""

    def __init__(self, bot):
        self.bot = bot
        self.guild_id = 842956728085118997
        self.channel_id = 964663566366027826

    @commands.Cog.listener()
    async def on_message(self, message):
        # Ignore messages from bots to prevent loops
        if message.author.bot:
            return

        # Avoid relaying messages that are already in the target channel
        if message.guild and message.guild.id == self.guild_id and message.channel.id == self.channel_id:
            await self.bot.process_commands(message)
            return

        guild = self.bot.get_guild(self.guild_id)
        if guild:
            channel = guild.get_channel(self.channel_id)
            if channel:
                await channel.send(f"{message.author}: {message.content}")

        # Ensure commands still work
        await self.bot.process_commands(message)


def setup(bot):
    bot.add_cog(RelayCog(bot))
