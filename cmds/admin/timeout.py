import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension, ConfigData, ErrorHandler


class Timeout(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(Timeout(bot))
