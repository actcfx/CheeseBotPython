from tkinter.tix import TCL_IDLE_EVENTS
from nextcord import Interaction
from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands

class ban(Cog_Extension):
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