import json
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension


class Join(Cog_Extension):
    DATA_FILE = "data/list.json"
    POTATO_GUILD_ID = 1022573475552055337
    CHARLOTTE_GUILD_ID = 978680658740260865

    def __init__(self, bot):
        self.bot = bot
        self.load_data()

    def load_data(self):
        with open(self.DATA_FILE, "r", encoding="utf8") as file:
            self.loli = json.load(file)

    async def on_member_join(self, member):
        channels = self.setup_channels()
        await self.handle_member_join(member, channels)

    def setup_channels(self):
        return {
            "potato_ch": self.bot.get_channel(1078651841191100486),
            "charlotte_wel_ch": self.bot.get_channel(978680659428147292),
            "charlotte_chat_ch": self.bot.get_channel(1154429182122672253),
        }

    async def handle_member_join(self, member, channels):
        if member.guild.id == self.POTATO_GUILD_ID:
            await self.handle_potato_guild_join(member)
        elif member.guild.id == self.CHARLOTTE_GUILD_ID:
            await self.handle_charlotte_guild_join(member, channels)

        print(f"-> {member} joined the server!")

    async def handle_potato_guild_join(self, member):
        potato_welcome_channel = self.bot.get_channel(1094600607442149397)
        await potato_welcome_channel.send(f"{member.mention} 歡迎來到移民署，請備好你的護照和機票錢")

    async def handle_charlotte_guild_join(self, member, channels):
        if member.id in self.loli["ban"]:
            await member.ban(reason="機器人行為")
            await channels["charlotte_chat_ch"].send(f"{member.mention} 抓到你咯 還敢亂群")
            print(f"-> {member} is banned!")
        else:
            await self.welcome_charlotte_member(member, channels)

    async def welcome_charlotte_member(self, member, channels):
        embeds = self.create_charlotte_welcome_embed()
        member_role = member.guild.get_role(978732220154007613)
        await channels["charlotte_chat_ch"].send(
            f"旅行者 {member.name} 向著星辰與深淵 歡迎來到原神夏洛特亞洲討論區"
        )
        await channels["charlotte_wel_ch"].send(embed=embeds)
        await member.add_roles(member_role)
        await self.assign_default_roles(member)

    def create_charlotte_welcome_embed(self):
        embeds = nextcord.Embed(
            title="大東亞帝國", description="大明王朝Ming dynasty", color=0xE32626
        )
        embeds.add_field(
            name="新手須知",
            value="請詳閱 <#978707952640872548> 以了解伺服器規範！\n 同時可以透過 <#978708014695600188> 熟悉頻道功能，\n 如果想快速認識大家可以到 <#990553527547990046> 。",
            inline=False,
        )
        embeds.add_field(
            name="身分組領取",
            value="並且可透過 <#978740632086523914> 開啟色色區或者是內鬼情報區哦！",
            inline=False,
        )
        embeds.add_field(
            name="遊戲疑難",
            value="另外有任何遊戲疑問可在 <#1070424932850352178> 進行詢問，\n 打不過的秘境或者BOSS也可於 <#978924406745210900>  來發布委託！",
            inline=False,
        )
        embeds.set_image(
            url="https://media.discordapp.net/attachments/1024157798117933106/1145967908376301649/image.png"
        )
        return embeds

    async def assign_default_roles(self, member):
        for role_id in [1148349321666887782, 1148349956273479781, 1148352076351545475]:
            await member.add_roles(member.guild.get_role(role_id))


def setup(bot):
    bot.add_cog(Join(bot))
