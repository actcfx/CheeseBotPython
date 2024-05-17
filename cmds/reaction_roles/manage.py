import nextcord
from nextcord import Interaction, SlashOption, User
from core.classes import Cog_Extension, ConfigData, PermissionChecker, ErrorHandler


class ManageReactionRoles(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    # @nextcord.slash_command(name="設定身份組領取訊息", description="請先發送要作為身份組領取用的訊息，請在與該訊息相同的頻道發送")
    # async def 設定身份組領取訊息(
    #     self,
    #     interaction: Interaction,
    #     message_id: str = SlashOption(
    #         name="訊息id",
    #         description="要作為身份組領取用的訊息id，如複製出來像這樣：1223908781952466954-1238394541145325599，請只貼上-後面的部分",
    #         required=True,
    #     ),
    #     name: str = SlashOption(
    #         name="身份組名稱",
    #         description="要領取什麼身份組",
    #         required=True,
    #     ),
    #     repeatable_str: str = SlashOption(
    #         name="重複領取",
    #         description="是否可以重複領取",
    #         choices=["可以", "不可以"],
    #         required=True,
    #     ),
    # ):
    #     await interaction.response.defer(ephemeral=True)

    #     try:
    #         reaction_roles_dict: dict
    #         repeatable: bool

    #         if not await PermissionChecker.have_roles(
    #             self, interaction, check_command="設定身份組領取訊息"
    #         ):
    #             return

    #         reaction_roles_dict = ConfigData.load_data("data/reaction_roles.json")
    #         repeatable = repeatable_str == "可以"

    #         reaction_roles_dict[str(message_id)] = {
    #             "name": name,
    #             "roles": {
    #                 "emoji": [],
    #                 "role_id": [],
    #             },
    #             "repeatable": repeatable,
    #         }

    #         ConfigData.save_data("data/reaction_roles.json", reaction_roles_dict)
    #         await interaction.followup.send(f"已將 https://discord.com/channels/{interaction.guild_id}/{interaction.channel_id}/{message_id} 設定為領取身份組訊息，後續請使用 `/編輯身份組領取` 添加身份組")

    #     except Exception as unexpected_error:
    #         await ErrorHandler.handle_error(
    #             self,
    #             interaction,
    #             command="設定身份組領取訊息",
    #             error_content=unexpected_error,
    #             error_type="unexpected_error",
    #         )
    pass


def setup(bot):
    bot.add_cog(ManageReactionRoles(bot))
