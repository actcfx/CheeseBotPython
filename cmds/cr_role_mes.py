import json
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension

with open("/Users/arcticfox/Downloads/columbina/roles.json", "r", encoding = "utf-8") as role:
    roles = json.load(role)

class Cr_role_mes(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def cr_WL(self, ctx):
        embed = nextcord.Embed(
            title = "世界等級", description="領取你的世界等級", color=0x7b219f)
        embed.add_field(
            name = "點擊下方表情符號即可領取對應身份組", value = "", inline = False)
        embed.add_field(
            name = "`發送求助前請先領取世界等級身份組`", value = "", inline = False)
        embed.set_image(
            "https://media.discordapp.net/attachments/1045948166274555914/1045948629413793882/2560-1440.png")
        mes = await ctx.send(embed = embed)
        roles["role_mes"]["world_level_mes"] = mes.id
        with open("/Users/arcticfox/Downloads/columbina/roles.json", "w", encoding = "utf-8") as role:
            json.dump(roles, role)

    @commands.command()
    @commands.is_owner()
    async def cr_server(self, ctx):
        embed = nextcord.Embed(
            title = "遊戲伺服器", description = "請選擇遊玩的伺服器", color = 0x7b219f)
        embed.add_field(
            name="點擊下方表情符號即可領取對應身份組", value= "🇦 ：北美，🇧 ：歐洲，🇨 ：亞洲，🇩 ：台港澳", inline = False)
        embed.add_field(
            name = "`發送求助前請先領取遊戲伺服器身份組`", value = "", inline = False)
        embed.set_image(
            "https://media.discordapp.net/attachments/1045948166274555914/1045948947488837703/3-11920x1080_.jpg")
        mes = await ctx.send(embed=embed)
        roles["role_mes"]["game_server_mes"] = mes.id
        with open("/Users/arcticfox/Downloads/columbina/roles.json", "w", encoding="utf-8") as role:
            json.dump(roles, role)

def setup(bot):
    bot.add_cog(Cr_role_mes(bot))
