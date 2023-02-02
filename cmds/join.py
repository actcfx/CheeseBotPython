import json
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension


class Join(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        chat_channel = self.bot.get_channel(978708780445495328) #💬聊天頻道
        welcome_channel = self.bot.get_channel(978680659428147292)  #🎊歡迎-請詳閱群規並領取身分組🎉

        embeds=nextcord.Embed(title = "大東亞帝國", description = "大明王朝Ming dynasty", color = 0xe32626)
        embeds.add_field(name = "新手須知", value = f"{member.mention} 請詳閱 <#978707952640872548> 以了解伺服器規範！\n 同時可以透過 <#978708014695600188> 熟悉頻道功能，\n 如果想快速認識大家可以到 <#990553527547990046> 。", inline = False)
        embeds.add_field(name = "身分組領取", value = "並且可透過 <#978740632086523914> 開啟色色區或者是內鬼情報區哦！", inline = False)
        embeds.add_field(name = "遊戲疑難", value = "另外有任何遊戲疑問可在 <#1070424932850352178> 進行詢問，\n 打不過的秘境或者BOSS也可於 <#978924406745210900>  來發布委託！", inline = False)
        embeds.set_image("https://upload.cc/i1/2022/11/10/rb6dCB.png")

        with open('list.json','r',encoding='utf8') as loli:
            loli1=json.load(loli)
        if member.id in loli1['ban']:
            await member.ban(reason='機器人行為')
            await chat_channel.send(f"{member.mention} 抓到你咯 還敢亂群")
            print(f'-> {member} is banned!')
        else:
            await chat_channel.send(f'旅行者 {member.name}，歡迎您的到來！')
            await welcome_channel.send(embed = embeds)
            print(f'-> {member} join the server!')


def setup(bot):
    bot.add_cog(Join(bot))