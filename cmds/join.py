import json
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension

with open('/Users/arcticfox/Downloads/columbina/ban.json', 'r', encoding = 'utf8') as loli:
    loli=json.load(loli)

class Join(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        member_role = self.bot.get_guild(978680658740260865).get_role(978732220154007613)
        potato_id = 1022573475552055337
        charlotte_id = 978680658740260865
        channels = {'potato_ch': self.bot.get_channel(1078651841191100486),
                'charlotte_wel_ch': self.bot.get_channel(978680659428147292),
                'charlotte_chat_ch': self.bot.get_channel(978708780445495328)
                }
        embeds=nextcord.Embed(title = "大東亞帝國", description = "大明王朝Ming dynasty", color = 0xe32626)
        embeds.add_field(name = "新手須知", value = f"{member.mention} 請詳閱 <#978707952640872548> 以了解伺服器規範！\n 同時可以透過 <#978708014695600188> 熟悉頻道功能，\n 如果想快速認識大家可以到 <#990553527547990046> 。", inline = False)
        embeds.add_field(name = "身分組領取", value = "並且可透過 <#978740632086523914> 開啟色色區或者是內鬼情報區哦！", inline = False)
        embeds.add_field(name = "遊戲疑難", value = "另外有任何遊戲疑問可在 <#1070424932850352178> 進行詢問，\n 打不過的秘境或者BOSS也可於 <#978924406745210900>  來發布委託！", inline = False)
        embeds.set_image("https://upload.cc/i1/2022/11/10/rb6dCB.png")

        if member.guild.id == potato_id:
            await channels['potato_ch'].send(f'{member.mention} 歡迎來到移民署，請備好你的護照和機票錢')
        elif member.guild.id == charlotte_id:
            if member.id in loli['ban']:
                await member.ban(reason = '機器人行為')
                await channels['charlotte_chat_ch'].send(f"{member.mention} 抓到你咯 還敢亂群")
                print(f'-> {member} is banned!')
            else:
                await channels['charlotte_chat_ch'].send(f'旅行者 {member.name} 向著星辰與深淵 歡迎來到原神夏洛特亞洲討論區')
                await channels['charlotte_wel_ch'].send(embed = embeds)
                await member.add_roles(member_role)
                print(f'-> {member} join the server!')

def setup(bot):
    bot.add_cog(Join(bot))