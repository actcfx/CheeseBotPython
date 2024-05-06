import re
import json
import nextcord
from nextcord import Interaction
from core.modals import QuestModal
from core.classes import Cog_Extension, ErrorHandler, ConfigData


class Quest(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="求助", description="發送求助")
    async def 求助(self, interaction: Interaction):
        try:
            INTRO_DATA: json = ConfigData.load_data("data/intro.json")

            user_data = INTRO_DATA[str(interaction.user.id)]
            name = user_data.get("name")
            uid = user_data.get("genshin_uid")

            await interaction.response.send_modal(QuestModal(name, uid))

        except Exception as unexpected_error:
            await ErrorHandler.handle_error(
                self,
                interaction,
                command="quest",
                error_content=unexpected_error,
                error_type="unexpected_error",
            )


def setup(bot):
    bot.add_cog(Quest(bot))
