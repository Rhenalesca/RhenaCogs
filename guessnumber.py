import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def kick(self, user : discord.Member):
    """I will kick anyone! >.<"""
await self.bot.say("ONE PUNCH! And " + user.mention + " is out! ლ(ಠ益ಠლ)")


def setup(bot):
    bot.add_cog(Mycog(bot))
    
