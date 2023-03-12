import json
import nextcord
from cmds.ban import ban
from nextcord.ext import commands
from core.classes import Cog_Extension


class Ban_list(Cog_Extension):
    @commands.command()
    @commands.has_any_role(978680963099942912,979385876209610752,978956326359138314, 1070679396165373984)    #社長、工程師、管理員
    async def ban_list(self, ctx):
        with open('/Users/arcticfox/Downloads/columbina/ban.json', 'r', encoding = 'utf-8') as ban_l:
            banlast = json.load(ban_l)
        list_embed = nextcord.Embed(title = "ban人名單", color = 0xffe380)
        for i in banlast['ban']:
            u_name = self.bot.get_user(i)
            list_embed.add_field(name = u_name, value = i, inline = False)
        await ctx.send(embed = list_embed)
        print(f'-> List ban_list for {ctx.author}')


def setup(bot):
    bot.add_cog(Ban_list(bot))