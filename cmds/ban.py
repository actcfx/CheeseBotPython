from tkinter.tix import TCL_IDLE_EVENTS
from nextcord import Interaction
from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands

class ban(Cog_Extension):
  @commands.Cog.listener()
  async def on_member_join(self,mem):
    with open('list.json','r',encoding='utf8') as loli:
      loli1=json.load(loli)
      if mem.id in loli1['ban']:
        await mem.ban(reason='機器人行為')
        c=self.bot.get_channel(1028977856287604736)
        await c.send(f"{mem.mention}Got caught still play play")
      else:
        c=self.bot.get_channel(1028977856287604736)
        await c.send(f"{mem.mention} Welcome to 新时代动漫展团")

  @commands.command()
  @commands.has_any_role(1028710466664550490,1028710721942454292,"工程師")
  @commands.has_permissions(ban_members=True)
  async def ban(self,ctx,*,member,reason=None):
    c_r=member.replace('<','').replace('@','').replace('>','')
    c=str(c_r).split(' ')
    for c_kick in c:
        a=ctx.guild.get_member(int(c_kick))
        await a.ban(reason=reason)

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def join_ban(self,ctx,*,member):
    with open('list.json','r',encoding='utf8') as loli:
      loli1=json.load(loli)
    c_r=member.replace('<','').replace('@','').replace('>','')

    c=str(c_r).split(' ')
    for c_kick in c:
        loli1['ban'].append(int(c_kick))
    with open('list.json','w',encoding='utf8') as loli:
      json.dump(loli1,loli)

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def remove_ban(self,ctx,*,member):
    with open('list.json','r',encoding='utf8') as loli:
      loli1=json.load(loli)
    c_r=member.replace('<','').replace('@','').replace('>','')

    c=str(c_r).split(' ')
    for c_kick in c:
        loli1['ban'].remove(int(c_kick))
    with open('list.json','w',encoding='utf8') as loli:
      json.dump(loli1,loli)

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def join_ban(self,ctx,*,member):
    with open('list.json','r',encoding='utf8') as loli:
      loli1=json.load(loli)
    c_r=member.replace('<','').replace('@','').replace('>','')

    c=str(c_r).split(' ')
    for c_kick in c:
        loli1['ban'].append(int(c_kick))
    with open('list.json','w',encoding='utf8') as loli:
      json.dump(loli1,loli)

  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def remove_ban(self,ctx,*,member):
    with open('list.json','r',encoding='utf8') as loli:
      loli1=json.load(loli)
    c_r=member.replace('<','').replace('@','').replace('>','')

    c=str(c_r).split(' ')
    for c_kick in c:
        loli1['ban'].remove(int(c_kick))
    with open('list.json','w',encoding='utf8') as loli:
      json.dump(loli1,loli)
    print(f'-> Remove {c_r} successful!')

def setup(bot):
    bot.add_cog(ban(bot))