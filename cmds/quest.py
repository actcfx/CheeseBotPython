import re
from unicodedata import name
from core.classes import Cog_Extension
import nextcord
import json
from modal import quest as qu
from nextcord.ext import commands


class quest (Cog_Extension):
  def __init__(self, bot):
        self.bot = bot

  @nextcord.slash_command(name='求助',description='發送求助')
  async def 委託(self,interaction:nextcord.Interaction):
    with open('/Users/arcticfox/Downloads/columbina/uid.json','r',encoding='utf8') as uid:
        user_uid=json.load(uid)
    if str(interaction.user.id) in user_uid:
      try:
        find_uid = re.compile(r'(?<=\D)[0-9]{9}(?=\D)')
        uid=user_uid[str(interaction.user.id)]["content"]
        find_name = re.compile(r'[^名字:：\s]\w{1,}')
        name=user_uid[str(interaction.user.id)]["content"]
        my_uid = re.findall(find_uid, uid)
        my_name=re.findall(find_name,name)
        await interaction.response.send_modal(qu(my_uid[0],my_name[0]))
      except:
        await interaction.response.send_message("請先確認自我介紹是否照著格式或資訊是否完整",ephemeral=True)

    else:
      await interaction.response.send_modal(qu())


def setup(bot):
    bot.add_cog(quest(bot))