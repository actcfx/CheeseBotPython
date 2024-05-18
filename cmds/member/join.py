from nextcord.ext import commands
from nextcord import User, TextChannel, Embed, Role
from core.classes import Cog_Extension, ConfigData


class Join(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: User):
        GUILD_ID: int = ConfigData.load_data("config/bot_info.json").get("guild_id")

        CHAT_CHANNEL: TextChannel = self.bot.get_channel(ConfigData.load_data("config/channels.json").get("chat_channel"))
        WELCOME_CHANNEL: TextChannel = self.bot.get_channel(ConfigData.load_data("config/channels.json").get("welcome_channel"))
        DEFAULT_ROLES_ID: list[int] = list(ConfigData.load_data("config/roles.json").get("default_roles").values())

        WELCOME_MES_IN_CHAT_CHANNEL: str = ConfigData.load_data("config/assets.json").get("welcome_mes_in_chat_channel")
        WELCOME_EMBED_CONTENT: dict = ConfigData.load_data("config/assets.json").get("welcome_embed_content")
        WELCOME_EMBED: Embed = Embed.from_dict(WELCOME_EMBED_CONTENT)

        BLACK_LIST: list[int] = ConfigData.load_data("data/black_list.json")

        if member.guild.id != GUILD_ID:
            return

        if member.id in BLACK_LIST:
            await member.ban(reason="機器人行為")
            await CHAT_CHANNEL.send(f"{member.mention} 抓到你咯 還敢亂群")
            print(f"-> {member} is banned!")
            return

        await WELCOME_CHANNEL.send(content=member.mention, embed=WELCOME_EMBED)
        await CHAT_CHANNEL.send(content=(member.mention + WELCOME_MES_IN_CHAT_CHANNEL))

        for role_id in DEFAULT_ROLES_ID:
            await member.add_roles(member.guild.get_role(role_id))


def setup(bot):
    bot.add_cog(Join(bot))
