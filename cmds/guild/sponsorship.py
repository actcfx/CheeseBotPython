import nextcord
from nextcord import Interaction
from core.classes import Cog_Extension, ErrorHandler


class Sponsorship(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="工商合作與贊助", description="社群工商申請")
    async def 工商合作與贊助(self, interaction: Interaction):
        try:
            sponsorship_theard = await interaction.channel.create_thread(
                name=f"{interaction.user.name} 的專屬工商合作與贊助串", type=nextcord.ChannelType.private_thread
            )
            await interaction.response.send_message(f"你的專屬工商合作與贊助討論串已開啟\n{sponsorship_theard.mention}")
            await sponsorship_theard.send(
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
    bot.add_cog(Sponsorship(bot))
