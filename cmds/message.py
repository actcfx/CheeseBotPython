import json
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension


class Message(Cog_Extension):
    def __init__(self, bot):
            self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message:nextcord.Message):
        quest_channel_id = 978924406745210900
        information_channel_id = 990553527547990046
        chat_channel = self.bot.get_channel(978708780445495328)
        bot_id = [972137604470407168,537846086749126657,992351373280690206, 1065293003532546090]
        arcticfox_id = 407881227270356994

        if message.channel.id == quest_channel_id:
            if (message.type != nextcord.MessageType.chat_input_command) and (message.author.id not in bot_id) and (message.author.id != arcticfox_id):
                try:
                    await message.delete()
                    await message.author.send(f'在<#{message.channel.id}>請使用斜線指令喔(詳細說明請看頻道訂選訊息)')
                except:
                    time_out = await chat_channel.send(f'<@{message.author.id}>無法私訊給您，請先確認是否將：隱私設定>允許私人訊息選項開啟(訊息30秒自動刪除)')
                    await time_out.delete(delay = 30)

        elif (message.channel.id == information_channel_id):
            with open('uid.json', 'r', encoding='utf8') as uid:
                user_uid = json.load(uid)
            user_uid[str(message.author.id)]={}
            user_uid[str(message.author.id)]["content"] = message.content
            user_uid[str(message.author.id)]["id"] = message.id
            with open('uid.json', 'w', encoding='utf8') as uid:
                json.dump(user_uid, uid, indent = 2, ensure_ascii = False)


def setup(bot):
    bot.add_cog(Message(bot))