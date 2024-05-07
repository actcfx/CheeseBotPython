from nextcord.ext import commands
from nextcord import Guild, Role, channel, PermissionOverwrite, CategoryChannel
from core.classes import Cog_Extension, ConfigData


class tmp_channel(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, user, before_channel, after_channel):
        GUILD: Guild = self.bot.get_guild(
            ConfigData.load_data("config/bot_info.json").get("guild_id")
        )
        INITIALIZE_ROLES_DICT: dict = ConfigData.load_data("config/roles.json").get(
            "initialize_roles"
        )
        MEMBER_ROLE: Role = GUILD.get_role(INITIALIZE_ROLES_DICT.get("member"))
        EVERYONE_ROLE: Role = GUILD.get_role(
            ConfigData.load_data("config/roles.json").get("everyone_role")
        )
        TMP_CREATE_CHANNEL: channel = GUILD.get_channel(
            ConfigData.load_data("config/channels.json").get("tmp_create_channel")
        )
        TMP_CHANNEL_CATEGORY: CategoryChannel = TMP_CREATE_CHANNEL.category

        OVERWRITES = {
            user: PermissionOverwrite(manage_channels=True),
            EVERYONE_ROLE: PermissionOverwrite(view_channel=False),
            MEMBER_ROLE: PermissionOverwrite(view_channel=True),
        }

        self.tmp_channels: list[int] = ConfigData.load_data("data/tmp_channels.json")

        if user.guild != GUILD:
            return

        if before_channel.channel != None:
            if self.is_tmp_channel_and_is_empty(before_channel.channel):
                await before_channel.channel.delete()
                self.tmp_channels.remove(int(before_channel.channel.id))

        if after_channel.channel != None:
            if after_channel.channel.id == TMP_CREATE_CHANNEL.id:
                new_tmp_channel = await GUILD.create_voice_channel(
                    f"└[{user.name}] 的頻道",
                    overwrites=OVERWRITES,
                    category=TMP_CHANNEL_CATEGORY,
                    bitrate=384000,
                )
                await user.move_to(new_tmp_channel)
                self.tmp_channels.append(new_tmp_channel.id)

        ConfigData.save_data("data/tmp_channels.json", self.tmp_channels)

    def is_tmp_channel_and_is_empty(self, channel: channel) -> bool:
        return (channel.id in self.tmp_channels) and (channel.members == [])

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def append(self, ctx, channel_id: int):
        tmp_channels: list[int] = ConfigData.load_data("data/tmp_channels.json")

        tmp_channels.append(channel_id)

        ConfigData.save_data("data/tmp_channels.json", tmp_channels)

        await ctx.send(f'添加動態語音頻道 {channel_id} 成功')
        print(f'-> Appended temporary_channel {channel_id} successful!')

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def remove(self, ctx, channel_id: int):
        tmp_channels: list[int] = ConfigData.load_data("data/tmp_channels.json")

        tmp_channels['tmp_channels'].remove(channel_id)

        ConfigData.save_data("data/tmp_channels.json", tmp_channels)

        await ctx.send(f'刪除動態語音頻道 {channel_id} 成功')
        print(f'-> Remove temporary_channel {channel_id} successful!')


def setup(bot):
    bot.add_cog(tmp_channel(bot))
