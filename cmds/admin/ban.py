import datetime
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension, ConfigData, ErrorHandler
from nextcord import Interaction, SlashOption, channel, Member, Embed



class Ban(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    # @commands.has_permissions(ban_members=True)
    # @nextcord.slash_command(name="ban", description="用指令 ban 人")
    # async def ban(
    #     self,
    #     interaction: Interaction,
    #     member: Member = SlashOption(name="誰", description="ban 誰", required=True),
    #     reason: str = SlashOption(name="原因", required=True, default=None),
    #     hours: int = SlashOption(
    #         name="刪除過去幾小時訊息",
    #         description="不刪除訊息請輸入 0",
    #         required=True,
    #         min_value=0,
    #         max_value=336,
    #     ),
    # ):
    #     # 直接回應確認信息，避免交互超時
    #     await interaction.response.defer(ephemeral=True)

    #     try:
    #         VIOLATION_CHANNEL: channel = interaction.guild.get_channel(
    #             ConfigData.load_data("config/channels.json").get("violation_channel")
    #         )
    #         seconds: int = hours * 3600

    #         # ban 人
    #         await member.ban(delete_message_seconds=seconds, reason=reason)

    #         # 發送違規紀錄到違規紀錄區
    #         violation_embed: Embed = Embed(color=0x227D51)
    #         violation_embed.set_author(name="違規紀錄")
    #         violation_embed.set_thumbnail(url=member.avatar.url)
    #         violation_embed.add_field(name="違規者：", value=member.mention, inline=False)
    #         violation_embed.add_field(name="違規事項：", value=reason, inline=False)
    #         violation_embed.add_field(name="違規處分：", value="停權", inline=False)
    #         violation_embed.timestamp = datetime.datetime.now()
    #         await VIOLATION_CHANNEL.send(embed=violation_embed)

    #         if hours != 0:
    #             await interaction.followup.send(
    #                 f"你把 {member.mention} ban 掉了，原因：{reason}，並刪除了過去 {hours} 小時訊息",
    #                 ephemeral=True,
    #             )
    #         else:
    #             await interaction.followup.send(
    #                 f"你把 {member.mention} ban 掉了，原因：{reason}",
    #                 ephemeral=True,
    #             )

    #     except Exception as unexpected_error:
    #         await ErrorHandler.handle_error(
    #             self,
    #             interaction,
    #             command="ban",
    #             error_content=unexpected_error,
    #             error_type="unexpected_error",
    #         )
    pass


def setup(bot):
    bot.add_cog(Ban(bot))
