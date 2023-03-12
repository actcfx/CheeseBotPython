import nextcord
import json
from ast import Pass
from nextcord.ext import commands
from core.classes import Cog_Extension

global s, s1, s2


class password_channel(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='create_channel', help='Create a password-protected voice channel')
    async def create_channel(self, ctx, password: str):
        with open('list.json', 'r', encoding='utf-8') as list:
            list1 = json.load(list)

        s = self.bot.get_guild(978680658740260865)  # 獲取伺服器
        s1 = s.get_channel(1067052338616999989)  # 設置動態語音頻道位置
        s2 = s1.category
        member_role = s.get_role(978732220154007613)

        create_channel = {
            # 給予成員身分組瀏覽頻道的權限
            member_role: nextcord.PermissionOverwrite(view_channel=True),
            ctx.guild.default_role: nextcord.PermissionOverwrite(connect=False),
            ctx.author: nextcord.PermissionOverwrite(connect=True)
        }

        global secret_password
        secret_password = password
        voice_channel = await ctx.guild.create_voice_channel(name='Private Voice Channel')
        await voice_channel.edit(user_limit=1, category=s2)
        await voice_channel.edit(overwrites=create_channel)

        list1['tmp_channels'].append(int(voice_channel.id))
        with open('list.json', 'w', encoding='utf-8') as list:
            json.dump(list1, list)

        await ctx.author.move_to(voice_channel)
        await ctx.send(f'Voice channel created. Password sent in a direct message.')
        await ctx.author.send(f'The password for the voice channel is "{password}"')

    @commands.command(name='join_channel', help='Join the password-protected voice channel')
    async def join_channel(self, ctx, password: str):
        voice_channel = nextcord.utils.get(
            ctx.guild.voice_channels, name='Private Voice Channel')
        if not voice_channel:
            await ctx.send('Voice channel not found.')
            return
        if voice_channel.user_limit != 1:
            await ctx.send('Voice channel is not password-protected.')
            return
        if password != secret_password:
            await ctx.send('Incorrect password.')
            return
        await ctx.author.move_to(voice_channel)
        await ctx.send(f'{ctx.author.mention} joined the voice channel.')


def setup(bot):
    bot.add_cog(password_channel(bot))