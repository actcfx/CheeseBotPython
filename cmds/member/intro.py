import json
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
from core.classes import Cog_Extension


class Introduction(Cog_Extension):
    DATA_FILE = "data/uid.json"

    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="自我介紹")
    async def 自我介紹(
        self,
        interaction: Interaction,
        user: nextcord.User = nextcord.SlashOption(name="要查詢的人", required=False),
    ):
        user_uid = self.load_data()
        target_user = user if user else interaction.user

        if str(target_user.id) in user_uid:
            embed = self.create_introduction_embed(
                target_user, user_uid[str(target_user.id)]
            )
            await interaction.send(embed=embed)
        else:
            await interaction.send("請先去<#990553527547990046>輸入資料")

    def load_data(self):
        with open(self.DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    def create_introduction_embed(self, user, user_data):
        embed = nextcord.Embed(color=0xFFDBDB, title=f"自我介紹-{user.display_name}")
        embed.set_thumbnail(user.display_avatar.url)
        embed.add_field(name="", value=user_data["content"], inline=False)
        embed.add_field(
            name="",
            value=f'[跳轉到此訊息](https://discord.com/channels/978680658740260865/990553527547990046/{user_data["id"]})',
            inline=False,
        )
        return embed


def setup(bot):
    bot.add_cog(Introduction(bot))
