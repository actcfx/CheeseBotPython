from nextcord import User
from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands
class kick (Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,*,member,reason=None):
        c_r=member.replace('<','').replace('@','').replace('>','')
        c=str(c_r).split(' ')
        for c_kick in c:
            a=ctx.guild.get_member(int(c_kick))
            await a.kick(reason=reason)
    @nextcord.slash_command(name='自我介紹')
    async def 自我介紹(self,interaction:nextcord.Interaction,mes:User=nextcord.SlashOption(name='要查詢的人',required=False)):
        with open('uid.json','r',encoding='utf8') as uid:
            user_uid=json.load(uid)
        if mes is None and str(interaction.user.id) in user_uid:
            emb=nextcord.Embed(color=0xffdbdb,title=f"自我介紹-{interaction.user.display_name}")
            emb.set_thumbnail(interaction.user.display_avatar.url)
            emb.add_field(name="​", value=f'{user_uid[str(interaction.user.id)]["content"]}', inline=False)
            emb.add_field(name="​", value=f'[跳轉到此訊息](https://discord.com/channels/978680658740260865/990553527547990046/{user_uid[str(interaction.user.id)]["id"]})', inline=False)
            await interaction.send(embed=emb)
        elif mes is not None:
            emb=nextcord.Embed(color=0xffdbdb,title=f"自我介紹-{mes.display_name}")
            emb.set_thumbnail(mes.display_avatar.url)
            emb.add_field(name="​", value=f'{user_uid[str(mes.id)]["content"]}', inline=False)
            emb.add_field(name="​", value=f'[跳轉到此訊息](https://discord.com/channels/978680658740260865/990553527547990046/{user_uid[str(mes.id)]["id"]})', inline=False)
            await interaction.send(embed=emb)
        else:
            await interaction.send('請先去<#990553527547990046>輸入資料')
def setup(bot):
    bot.add_cog(kick(bot))