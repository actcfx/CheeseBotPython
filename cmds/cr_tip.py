import nextcord
from nextcord.ui import View, Button
from nextcord.ext import commands
from core.classes import Cog_Extension

class Cr_tip(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def cr_role_tip(self, ctx):
        tip1_button = Button(style = nextcord.ButtonStyle.link,
                          url = 'https://discord.com/channels/978680658740260865/978740632086523914/996519987160293486', label = '點我前往領取')
        button_view = View(timeout = 0)
        button_view.add_item(tip1_button)
        await ctx.send("> 入群小助手\n閱讀完群規了嗎，接下來去領取身份組吧", view = button_view)

    @commands.command()
    @commands.is_owner()
    async def cr_roles_tip(self, ctx):
        tip2_button1 = Button(style = nextcord.ButtonStyle.link,
                              url = 'https://discord.com/channels/978680658740260865/1079677816192372817/1079813967570022421', label='點我前往領取')
        tip2_button2 = Button(style = nextcord.ButtonStyle.link,
                             url = 'https://discord.com/channels/978680658740260865/978708780445495328', label = '聊天頻道')
        button_view = View(timeout = 0)
        button_view.add_item(tip2_button1)
        button_view.add_item(tip2_button2)
        await ctx.send("> 入群小助手\n接著繼續領取原神相關身份組，或是直接聊天去吧", view = button_view)

    @commands.command()
    @commands.is_owner()
    async def cr_gen_tip(self, ctx):
        tip3_button = Button(style = nextcord.ButtonStyle.link,
                             url = 'https://discord.com/channels/978680658740260865/990553527547990046', label = '點我前往')
        button_view = View(timeout = 0)
        button_view.add_item(tip3_button)
        await ctx.send("> 入群小助手\n去自我介紹介紹一下自己吧", view = button_view)

def setup(bot):
    bot.add_cog(Cr_tip(bot))