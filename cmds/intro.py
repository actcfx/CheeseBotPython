import json
import nextcord
from nextcord import User, Interaction
from nextcord.ext import commands
from core.classes import Cog_Extension

class Introduction(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name = '自我介紹')
    async def 自我介紹(self, interaction:Interaction, message:User = nextcord.SlashOption(name = '要查詢的人', required = False)):
        with open('data/uid.json', 'r', encoding = 'utf-8') as uid:
            user_uid = json.load(uid)

        if (message is None) and (str(interaction.user.id) in user_uid):
            embed=nextcord.Embed(color = 0xffdbdb, title = f'自我介紹-{interaction.user.display_name}')
            embed.set_thumbnail(interaction.user.display_avatar.url)
            embed.add_field(name = '', value = f'{user_uid[str(interaction.user.id)]["content"]}', inline=False)
            embed.add_field(name = '', value = f'[跳轉到此訊息](https://discord.com/channels/978680658740260865/990553527547990046/{user_uid[str(interaction.user.id)]["id"]})', inline = False)
            await interaction.send(embed = embed)

        elif message is not None:
            embed=nextcord.Embed(color = 0xffdbdb, title = f'自我介紹-{message.display_name}')
            embed.set_thumbnail(message.display_avatar.url)
            embed.add_field(name = '', value = f'{user_uid[str(message.id)]["content"]}', inline = False)
            embed.add_field(name = '', value = f'[跳轉到此訊息](https://discord.com/channels/978680658740260865/990553527547990046/{user_uid[str(message.id)]["id"]})', inline = False)
            await interaction.send(embed = embed)

        else:
            await interaction.send('請先去<#990553527547990046>輸入資料')

def setup(bot):
    bot.add_cog(Introduction(bot))