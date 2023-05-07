import nextcord
from datetime import datetime
from nextcord.ext import commands
from core.classes import Cog_Extension


class Count_down(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot
        self.exam_date = datetime(2023, 5, 6)

    @nextcord.slash_command(name='去讀書', description='提醒水到渠程滾去讀書')
    async def count(self, interaction: nextcord.Interaction):
        delta = self.exam_date - datetime.utcnow()
        days, seconds = delta.days, delta.seconds
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)
        time_str = f'{days}天{hours}小時{minutes}分{seconds}秒'
        await interaction.response.send_message(f'距離<@988804427756478574> 考試還有 {time_str}，去讀書！')

    @nextcord.slash_command(name='去色色', description='提醒甜甜圈警長滾去色色')
    async def horny(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f'<@560450371491725313> [色色去](https://discord.com/channels/978680658740260865/978924169364406303)')

def setup(bot):
    bot.add_cog(Count_down(bot))