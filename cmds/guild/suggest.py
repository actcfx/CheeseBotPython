import nextcord
from nextcord import Interaction
from core.classes import Cog_Extension, ErrorHandler


class Suggest(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="建議與反饋", description="向「管理員」回報建議與反饋")
    async def 建議與反饋(self, interaction: Interaction):
        try:
            await interaction.response.send_message("你的專屬建議與反饋討論串已開啟")
            suggest_theard = await interaction.channel.create_thread(
                name=interaction.user.name, type=nextcord.ChannelType.private_thread
            )
            await suggest_theard.send(
                f"> {interaction.user.mention} 這裡是你專屬的建議與反饋區\n```你在這裡輸入的所有內容都只能被糾察、管理、工程、社長以及被@到的人看到``` 你可以提出你的建議與反饋，而不會被其他人看見\n 如果要讓其他人看到此討論串，可以@該成員\n\n<@&978958227016409088><@&978956326359138314> 有新的建議與反饋唷！"
            )

        except Exception as unexpected_error:
            await ErrorHandler.handle_error(
                self,
                interaction,
                command="suggest",
                error_content=unexpected_error,
                error_type="unexpected_error",
            )


def setup(bot):
    bot.add_cog(Suggest(bot))
