import re
import json
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension, ConfigData, ErrorHandler
from nextcord import Interaction, SlashOption, User, Embed, Message


class Introduction(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="自我介紹")
    async def 自我介紹(
        self,
        interaction: Interaction,
        user: User = SlashOption(name="要查詢的人", required=False),
    ):
        await interaction.response.defer(ephemeral=True)

        try:
            UID_DATA: json = ConfigData.load_data("data/intro.json")
            TARGET_USER: User = user if user else interaction.user

            if str(TARGET_USER.id) in UID_DATA:
                embed = self.create_introduction_embed(
                    TARGET_USER, UID_DATA[str(TARGET_USER.id)]
                )
                await interaction.send(embed=embed)
            else:
                await interaction.send("請先去<#990553527547990046>輸入資料")

        except Exception as unexpected_error:
            await ErrorHandler.handle_error(
                self,
                interaction,
                command="search_introduction",
                error_content=unexpected_error,
                error_type="unexpected_error",
            )

    def create_introduction_embed(self, user, user_data):
        embed = Embed(color=0xFFDBDB, title=f"自我介紹-{user.display_name}")
        embed.set_thumbnail(user.display_avatar.url)
        embed.add_field(name="", value=user_data["content"], inline=False)
        embed.add_field(
            name="",
            value=f'[跳轉到此訊息](https://discord.com/channels/978680658740260865/990553527547990046/{user_data["id"]})',
            inline=False,
        )
        return embed

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        PATTERN = r"【原神】\n名字：(.*?)\nUID：(.*?)\n伺服器：.*?^【星穹鐵道】"
        INTRODUCTION_CHANNEL_ID: int = ConfigData.load_data("config/channels.json").get(
            "introduction_channel"
        )
        intro_data: json = ConfigData.load_data("data/intro.json")

        if message.channel.id != INTRODUCTION_CHANNEL_ID:
            return

        search: re.Match[str] = re.search(PATTERN, message.content, re.S | re.M)
        if search:
            user_name: str = search.group(1)
            user_uid: int = int(search.group(2).strip())
        else:
            user_uid: int = None

        intro_data[str(message.author.id)] = {
            "name": user_name,
            "content": message.content,
            "id": message.id,
            "genshin_uid": user_uid,
        }

        ConfigData.save_data("data/intro.json", intro_data)


def setup(bot):
    bot.add_cog(Introduction(bot))
