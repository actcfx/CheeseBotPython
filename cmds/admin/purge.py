import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
from core.classes import Cog_Extension, ErrorHandler


class mod(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="purge", description="批量刪除訊息")
    @commands.has_guild_permissions(manage_messages=True)
    async def purge(
        self,
        interaction: Interaction,
        limit: int = SlashOption(name="刪除數量", required=True, min_value=1),
    ):
        await interaction.response.defer(ephemeral=True)

        try:
            await interaction.channel.purge(limit=limit)
            await interaction.followup.send(f"已刪除 {limit} 則訊息")

        except Exception as unexpected_error:
            await ErrorHandler.handle_error(
                self,
                interaction,
                command="purge",
                error_content=unexpected_error,
                error_type="unexpected_error",
            )


def setup(bot):
    bot.add_cog(mod(bot))
