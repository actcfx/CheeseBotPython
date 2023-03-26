import time
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension

class Count_down(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name = '去讀書', description = '提醒水到渠程滾去讀書')
    async def count(self, interaction: nextcord.Interaction):
        timeString = "2023-05-07 00:00:00"
        struct_time = time.strptime(timeString, "%Y-%m-%d %H:%M:%S")
        test_time = int(time.mktime(struct_time))
        now = time.time()
        time_delta = test_time - now
        time_delta_str = time.strftime("%H小時%M分%S秒", time.localtime(time_delta))
        time_delta_str = f'{int(time_delta / 36400)}天' + time_delta_str
        await interaction.response.send_message(f'距離<@988804427756478574>考試還有{time_delta_str}，去讀書！')

    @nextcord.slash_command(name='去色色', description='提醒甜甜圈警長滾去色色')
    async def horny(self, interaction: nextcord.Interaction):
        await interaction.response.send_message(f'<@560450371491725313>[色色去](https://discord.com/channels/978680658740260865/978924169364406303)')

def setup(bot):
    bot.add_cog(Count_down(bot))