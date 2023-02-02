from cmds.ban import ban
from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands
from main import load


class ban_list (Cog_Extension):
  @commands.command()
  @commands.has_any_role(978680963099942912,979385876209610752,978956326359138314)
  async def ban_list(self,ctx):
    with open('token.json','r',encoding='utf-8') as ban_l:
      banlast=json.load(ban_l)
    em=nextcord.Embed(title="ban人名單", color=0xffe380)
    for a in banlast['ban']:
      u_name=self.bot.get_user(a)
      em.add_field(name=f"{u_name}", value=f"{a}", inline=False)
    await ctx.send(embed=em)
  @commands.Cog.listener()
  async def on_member_remove(self,mem:nextcord.Member):
    with open('list.json','r',encoding='utf-8') as ban_l:
      banlast=json.load(ban_l)
    if mem.id in (banlast['ban']):
      pass
    elif (str(mem.id)) not in (banlast['leavl']):
      banlast['leavl'][mem.id]=1
      with open('list.json','w',encoding='utf-8') as ban_l:
        json.dump(banlast,ban_l,indent=4)
    elif banlast['leavl'][str(mem.id)] >=1:
      banlast['ban'].append(int(mem.id))
      del banlast['leavl'][str(mem.id)]
      with open('list.json','w',encoding='utf8') as loli:
        json.dump(banlast,loli,indent=4)
    else:
      banlast['leavl'][str(mem.id)]+=1
      with open('list.json','w',encoding='utf-8') as ban_l:
        json.dump(banlast,ban_l,indent=4)

def setup(bot):
    bot.add_cog(ban_list(bot))