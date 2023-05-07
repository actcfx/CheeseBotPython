import json
import nextcord
from nextcord.ui import View, Button
from nextcord.ext import commands
from core.classes import Cog_Extension

class Message(Cog_Extension):
    def __init__(self, bot):
            self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message:nextcord.Message):
        quest_channel_id = 978924406745210900
        introduction_channel_id = 990553527547990046
        chat_channel = self.bot.get_channel(978708780445495328)

        bot_id = [972137604470407168, 992351373280690206, 1065293003532546090, 1070748028123750420]
        arcticfox_id = 407881227270356994
        hi_keyword = ['hi', 'Hi', 'hello', 'Hello','嗨']

        if message.channel.id == quest_channel_id:
            if (message.type != nextcord.MessageType.chat_input_command) and (message.author.id not in bot_id) and (message.author.id != arcticfox_id):
                try:
                    await message.delete()
                    await message.author.send(f'在<#{message.channel.id}>請使用斜線指令喔(詳細說明請看頻道訂選訊息)')
                except:
                    time_out = await chat_channel.send(f'<@{message.author.id}>無法私訊給您，請先確認是否將：隱私設定>允許私人訊息選項開啟(訊息30秒自動刪除)')
                    await time_out.delete(delay = 30)

        elif (message.channel.id == introduction_channel_id):
            with open('data/uid.json', 'r', encoding='utf8') as uid:
                user_uid = json.load(uid)

            if (user_uid.get(str(message.author.id)) == None):
                tip4_button = Button(style = nextcord.ButtonStyle.link,
                                     url = 'https://discord.com/channels/978680658740260865/978708780445495328', label = '聊天頻道')
                button_view = View(timeout = 0)
                button_view.add_item(tip4_button)
                await message.reply("> 入群小助手\n你完成入群手續了，去聊天吧", view = button_view, delete_after = 180)

            user_uid[str(message.author.id)]={}
            user_uid[str(message.author.id)]["content"] = message.content
            user_uid[str(message.author.id)]["id"] = message.id
            with open('data/uid.json', 'w', encoding='utf8') as uid:
                json.dump(user_uid, uid, indent = 2, ensure_ascii = False)

        elif message.content == '北極狐':
            await message.channel.send('https://upload.cc/i1/2023/02/08/QkjlHU.png')

        elif message.content == '容克':
            await message.channel.send('https://upload.cc/i1/2023/02/08/7PTJUV.png')
            await message.channel.send('https://upload.cc/i1/2023/02/12/xD5fRl.png')

        elif (message.content in hi_keyword) and (message.author.id not in bot_id):
            await message.reply(f'hi {message.author.name}')

        elif ('歡迎' in message.content) and (len(message.content) <= 6) and (message.author.id not in bot_id):
            await message.channel.send('歡迎～')

        elif (message.content.startswith('6')) and (len(message.content) <= 10) and (message.author.id not in bot_id):
            await message.channel.send(message.content)

#        elif (message.author.id == arcticfox_id):
#            await message.reply('你真的是他媽幹話王欸')

def setup(bot):
    bot.add_cog(Message(bot))