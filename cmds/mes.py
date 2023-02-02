import asyncio
from nextcord import Embed, slash_command
from core.classes import Cog_Extension
import nextcord
import json
from nextcord.ext import commands
class mes (Cog_Extension):
  def __init__(self, bot):
        self.bot = bot
  @commands.Cog.listener()
  async def on_message(self,mes:nextcord.Message):
    if mes.channel.id == 992008416140734574 or mes.channel.id == 978924406745210900:
      if mes.type != (nextcord.MessageType.chat_input_command)and mes.author.id not in  [972137604470407168,537846086749126657,992351373280690206, 407881227270356994]:
        try:
          await mes.delete()
          await mes.author.send(f'在<#{mes.channel.id}>請使用斜線指令喔(詳細說明請看頻道訂選訊息)')
        except:
          no_dm=self.bot.get_channel(978708780445495328)
          time_out=await no_dm.send(f"<@{mes.author.id}>無法私訊給您，請先確認是否將：隱私設定>允許私人訊息選項開啟(訊息30秒自動刪除)")
          await time_out.delete(delay=30)

    elif mes.channel.id == 990553527547990046:
      with open('uid.json','r',encoding='utf8') as uid:
        user_uid=json.load(uid)
      user_uid[str(mes.author.id)]={}
      user_uid[str(mes.author.id)]["content"]=mes.content
      user_uid[str(mes.author.id)]["id"]=mes.id
      with open('uid.json','w',encoding='utf8') as uid:
        json.dump(user_uid,uid,indent=2,ensure_ascii=False)
def setup(bot):
    bot.add_cog(mes(bot))