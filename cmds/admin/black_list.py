import math
import nextcord
from core.views import Pagination_View
from nextcord import Interaction, SlashOption, User, Embed
from core.classes import Cog_Extension, ConfigData, PermissionChecker, ErrorHandler


class BackBan(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="join_ban", description="join ban")
    async def join_ban(
        self,
        interaction: Interaction,
        user: User = SlashOption(name="要ban的人或id", required=True),
    ):
        await interaction.response.defer(ephemeral=True)

        try:
            user_id: int
            black_list: list[int]

            if not await PermissionChecker.have_roles(
                self, interaction, check_command="ban 人清單"
            ):
                return

            if user:
                user_id = user.id

            black_list = ConfigData.load_data("data/black_list.json")

            if user_id in black_list:
                return
            else:
                black_list.append(user_id)
                ConfigData.save_data("data/black_list.json", black_list)
                await interaction.followup.send(f"已將 {user_id} 加入 ban list")

        except Exception as unexpected_error:
            await ErrorHandler.handle_error(
                self,
                interaction,
                command="join_ban",
                error_content=unexpected_error,
                error_type="unexpected_error",
            )

    @nextcord.slash_command(name="remove_ban", description="remove ban")
    async def remove_ban(
        self,
        interaction: Interaction,
        user: User = SlashOption(name="要remove_ban的人或id", required=True),
    ):
        await interaction.response.defer(ephemeral=True)

        try:
            user_id: int
            black_list: list[int]

            if not await PermissionChecker.have_roles(
                self, interaction, check_command="ban 人清單"
            ):
                return

            if user:
                user_id = user.id

            black_list = ConfigData.load_data("data/black_list.json")

            if user_id in black_list:
                black_list.remove(user_id)
                ConfigData.save_data("data/black_list.json", black_list)
                await interaction.followup.send(f"已將 {user_id} 從 ban list 移除")
            else:
                await interaction.followup.send(f"{user_id} 不在 ban list 裡")
                return

        except Exception as unexpected_error:
            await ErrorHandler.handle_error(
                self,
                interaction,
                command="remove_ban",
                error_content=unexpected_error,
                error_type="unexpected_error",
            )

    @nextcord.slash_command(name="ban_list", description="顯示ban list")
    async def ban_list(
        self,
        interaction: Interaction,
        limit: int = SlashOption(
            name="顯示幾筆資料",
            required=False,
            description="一頁顯示幾筆資料（5~25）",
            max_value=25,
            min_value=5,
            default=25,
        ),
    ):
        await interaction.response.defer(ephemeral=True)

        try:
            BLACK_LIST: list[int] = ConfigData.load_data("data/black_list.json")

            black_list_embeds: list[Embed] = []
            total_pages: int = math.ceil(len(BLACK_LIST) / limit)

            if not await PermissionChecker.have_roles(
                self, interaction, check_command="ban_list"
            ):
                return

            for page in range(total_pages + 1):
                black_list_embeds.append(
                    self.set_black_list_embed(BLACK_LIST, page, limit, total_pages)
                )

            view = Pagination_View(total_pages, black_list_embeds)
            await interaction.followup.send(embed=black_list_embeds[0], view=view)

        except Exception as unexpected_error:
            await ErrorHandler.handle_error(
                self,
                interaction,
                command="ban_list",
                error_content=unexpected_error,
                error_type="unexpected_error",
            )

    # 產生 black_list 的 embed
    def set_black_list_embed(
        self,
        _black_list: list[int],
        _page: int,
        _number: int,
        _total_pages: int,
    ) -> Embed:
        black_list_embed: Embed = Embed(title="ban人清單", color=0xFFE380)
        black_list_embed.set_footer(
            text=f"第 {_page + 1}/{_total_pages} 頁，共 {len(_black_list)} 人"
        )
        for banned in _black_list[(_page * _number) : ((_page + 1) * _number)]:
            black_list_embed.add_field(
                name=self.bot.get_user(banned), value=banned, inline=False
            )
        return black_list_embed


def setup(bot):
    bot.add_cog(BackBan(bot))
