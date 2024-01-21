import math
import json
import nextcord
from nextcord.ext import commands
from core.views import Pagination_View
from nextcord import Interaction, SlashOption, Embed
from core.classes import Cog_Extension, ConfigData, ErrorHandler

ADMIN_DATA: json = ConfigData.load_data("config/roles.json")
ADMIN_ROLES_ID: dict[int] = ADMIN_DATA["admin_roles"].values()


class Ban_list(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_any_role(ADMIN_ROLES_ID)
    @nextcord.slash_command(name="ban人清單", description="顯示ban list")
    async def ban人清單(
        self,
        interaction: Interaction,
        number: int = SlashOption(
            name="人數",
            required=False,
            description="一頁顯示幾筆資料（5~25）",
            max_value=25,
            min_value=5,
            default=25,
        ),
    ):
        # 直接回應確認信息，避免交互超時
        await interaction.response.defer(ephemeral=True)

        try:
            ban_list: list[int] = ConfigData.load_data("data/ban_list.json").get("ban")
            total_pages: int = math.ceil(len(ban_list) / number)
            ban_list_embeds: list[Embed] = []

            for page in range(total_pages + 1):
                ban_list_embeds.append(
                    self.set_ban_list_embed(ban_list, page, number, total_pages)
                )

            view = Pagination_View(total_pages, ban_list_embeds)
            await interaction.channel.send(embed=ban_list_embeds[0], view=view)
            await interaction.delete_original_message()

        except Exception as unexpected_error:
            await ErrorHandler.handle_error(
                self,
                interaction,
                command="ban 人清單",
                error_content=unexpected_error,
                error_type="unexpected_error",
            )

    # 產生 ban_list 的 embed
    def set_ban_list_embed(
        self,
        _ban_list: list[int],
        _page: int,
        _number: int,
        _total_pages: int,
    ):
        ban_list_embed = Embed(title="ban人清單", color=0xFFE380)
        ban_list_embed.set_footer(
            text=f"第 {_page + 1}/{_total_pages} 頁，共 {len(_ban_list)} 人"
        )
        for banned in _ban_list[(_page * _number) : ((_page + 1) * _number)]:
            ban_list_embed.add_field(
                name=self.bot.get_user(banned), value=banned, inline=False
            )
        return ban_list_embed


def setup(bot):
    bot.add_cog(Ban_list(bot))
