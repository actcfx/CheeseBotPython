from nextcord import User
from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands
class kick (Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, *, member, reason = None):
        c_r = member.replace('<','').replace('@','').replace('>','')
        c = str(c_r).split(' ')
        for c_kick in c:
            a = ctx.guild.get_member(int(c_kick))
            await a.kick(reason = reason)

def setup(bot):
    bot.add_cog(kick(bot))