import json
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension


class Leave(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        with open('/Users/arcticfox/Downloads/columbina/ban.json','r',encoding = 'utf-8') as ban_l:
            banlast = json.load(ban_l)
        if member.id in (banlast['ban']):
            pass
        elif (str(member.id)) not in (banlast['leavl']):
            banlast['leavl'][member.id] = 1
            with open('/Users/arcticfox/Downloads/columbina/ban.json', 'w', encoding = 'utf-8') as ban_l:
                json.dump(banlast, ban_l, indent = 4)
        elif banlast['leavl'][str(member.id)] >= 1:
            banlast['ban'].append(int(member.id))
            del banlast['leavl'][str(member.id)]
            with open('/Users/arcticfox/Downloads/columbina/ban.json', 'w', encoding = 'utf8') as loli:
                json.dump(banlast, loli, indent = 4)
        else:
            banlast['leavl'][str(member.id)] += 1
            with open('/Users/arcticfox/Downloads/columbina/ban.json', 'w', encoding='utf-8') as ban_l:
                json.dump(banlast, ban_l, indent = 4)

        print(f'-> {member} leave the server!')


def setup(bot):
    bot.add_cog(Leave(bot))