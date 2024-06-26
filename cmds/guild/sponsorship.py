import nextcord
from nextcord import Interaction
from core.classes import Cog_Extension, ErrorHandler


class Suggest(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="工商合作與贊助", description="社群工商申請")
    async def 工商合作與贊助(self, interaction: Interaction):
        try:
            await interaction.response.send_message("你的專屬建議與反饋討論串已開啟")
            suggest_theard = await interaction.channel.create_thread(
                name=interaction.user.name, type=nextcord.ChannelType.private_thread
            )
            await suggest_theard.send(
                f"> <@&978958227016409088><@&978956326359138314><@978680963099942912> 有新的建議與反饋唷！"
            )

        except Exception as unexpected_error:
            await ErrorHandler.handle_error(
                self,
                interaction,
                command="sponsorship",
                error_content=unexpected_error,
                error_type="unexpected_error",
            )


def setup(bot):
    bot.add_cog(Suggest(bot))
