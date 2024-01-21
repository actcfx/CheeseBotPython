import json
import datetime
from nextcord.ext import commands
from nextcord import Interaction, channel, Member, Embed


class Cog_Extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


class ConfigData:
    def load_data(_path: str) -> json:
        with open(_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_data(_path: str, _data: str) -> None:
        with open(_path, "w", encoding="utf-8") as file:
            json.dump(_data, file, indent=4)

class ErrorHandler:
    async def handle_error(
        self,
        interaction: Interaction,
        command: str,
        error_content: Exception,
        error_type: str,
    ) -> None:
        """Handles errors that occur during the execution of a slash command."""

        LOG_CHANNEL: channel = interaction.guild.get_channel(
            ConfigData.load_data("config/channels.json").get("log_channel")
        )

        # 取得機器人資訊
        BOT_INFO: json = ConfigData.load_data("config/bot_info.json")
        DEVELOPER: Member = interaction.guild.get_member(BOT_INFO.get("developer"))
        VERSION: str = BOT_INFO.get("version")

        # 取得錯誤訊息內容
        ERROR_CONFIG: dict = ConfigData.load_data("config/errors.json").get(error_type)
        TITLE: str = ERROR_CONFIG.get("title")
        MESSAGE: str = ERROR_CONFIG.get("message")
        COLOR: int = ERROR_CONFIG.get("color")

        error_embed = Embed(title=command, color=COLOR, description=MESSAGE)
        error_embed.set_author(name=TITLE, icon_url=self.bot.user.avatar.url)
        error_embed.set_footer(
            text=f"開發：{DEVELOPER.global_name}・版本：{VERSION}",
            icon_url=DEVELOPER.avatar.url,
        )
        error_embed.timestamp = datetime.datetime.now()
        await interaction.followup.send(embed=error_embed, ephemeral=True)

        log_embed = error_embed
        log_embed.add_field(name="user: ", value=interaction.user.mention, inline=False)
        log_embed.add_field(name="guild: ", value=interaction.guild.name, inline=False)
        log_embed.add_field(
            name="channel: ", value=interaction.channel.mention, inline=False
        )
        log_embed.add_field(
            name="error content: ", value=f"```{str(error_content)}```", inline=False
        )
        await LOG_CHANNEL.send(content=DEVELOPER.mention, embed=log_embed)

        print(f"❌ {command} | {command} raise an unexpected error [{error_content}]")
