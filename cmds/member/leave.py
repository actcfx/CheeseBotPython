import json
import nextcord
from nextcord import TextChannel
from nextcord.ext import commands
from core.classes import Cog_Extension, ConfigData


class Leave(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        GUILD_ID: int = ConfigData.load_data("config/bot_info.json").get("guild_id")
        LEAVE_CHANNEL: TextChannel = self.bot.get_channel(ConfigData.load_data("config/channels.json").get("leave_channel"))
        LEAVE_DM_CONTENT: str = ConfigData.load_data("config/assets.json").get("leave_dm_content")

        if member.guild.id != GUILD_ID:
            return

        await LEAVE_CHANNEL.send(f"{member} just left the server")

        try:
            await member.send(LEAVE_DM_CONTENT)
        except Exception:
            print(f"❌ | Cannot send dm to {member}")


def setup(bot):
    bot.add_cog(Leave(bot))
