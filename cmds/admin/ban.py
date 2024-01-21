import json
import datetime
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension, ConfigData, ErrorHandler


ADMIN_DATA: json = ConfigData.load_data("config/roles.json")
ADMIN_ROLES_ID: dict = ADMIN_DATA["admin_roles"].values()


class Ban(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(ban_members=True)
    @nextcord.slash_command(name="ban", description="用指令 ban 人")
    async def ban(
        self,
        interaction: nextcord.Interaction,
        member: nextcord.User = nextcord.SlashOption(
            name="誰", description="ban 誰", required=True
        ),
        reason: str = nextcord.SlashOption(name="原因", required=True, default=None),
        delete_previous_hours: int = nextcord.SlashOption(
            name="刪除過去幾小時訊息",
            description="不刪除訊息請輸入 0",
            required=True,
            min_value=0,
            max_value=336,
        ),
    ):
        try:
            deleted_count: int = 0

            await interaction.response.defer(ephemeral=True)

            # ban 人
            # await member.ban(reason=reason)

            if delete_previous_hours != 0:
                original_message = await interaction.followup.send(
                    f"你把 {member.mention} ban 掉了，原因：{reason}\n`訊息刪除中，請稍候約 30 秒...`",
                    ephemeral=True,
                )

                # 刪除被 ban 人過去 n 小時訊息
                for channel in interaction.guild.text_channels:
                    async for message in channel.history(
                        limit=20,
                        after=datetime.datetime.now()
                        - datetime.timedelta(hours=delete_previous_hours),
                    ):
                        if message.author == member:
                            await message.delete()
                            deleted_count += 1

                await original_message.edit(
                    f"你把 {member.mention} ban 掉了，原因：{reason}，並刪除了過去 {delete_previous_hours} 小時訊息共 {deleted_count} 則"
                )

            else:
                await interaction.followup.send(
                    f"你把 {member.mention} ban 掉了，原因：{reason}",
                    ephemeral=True,
                )

        except Exception as unexpected_error:
            await ErrorHandler.handle_error(
                self,
                interaction,
                command="ban",
                error_content=unexpected_error,
                error_type="unexpected_error",
            )

    # @commands.has_permissions(ban_members=True)
    # @nextcord.slash_command(name="join_ban", description="join ban")
    # async def join_ban(
    #     self,
    #     interaction: nextcord.Interaction,
    #     member: nextcord.User = nextcord.SlashOption(name="成員", required=False),
    # ):
    #     with open("data/list.json", "r", encoding="utf8") as loli:
    #         loli1 = json.load(loli)
    #     c_r = member.replace("<", "").replace("@", "").replace(">", "")

    #     c = str(c_r).split(" ")
    #     for c_kick in c:
    #         loli1["ban"].append(int(c_kick))
    #     with open("data/list.json", "w", encoding="utf8") as loli:
    #         json.dump(loli1, loli)
    #     await ctx.send("Join ban successful!")
    #     print(f"-> Join {c_r} to ban list!")

    # @commands.command()
    # @commands.has_permissions(ban_members=True)
    # async def remove_ban(self, ctx, *, member):
    #     with open("data/list.json", "r", encoding="utf8") as loli:
    #         loli1 = json.load(loli)
    #     c_r = member.replace("<", "").replace("@", "").replace(">", "")

    #     c = str(c_r).split(" ")
    #     for c_kick in c:
    #         loli1["ban"].remove(int(c_kick))
    #     with open("data/list.json", "w", encoding="utf8") as loli:
    #         json.dump(loli1, loli)
    #     await ctx.send("Remove ban successful!")
    #     print(f"-> Remove {c_r} from ban list!")


def setup(bot):
    bot.add_cog(Ban(bot))
