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
            with open('/Users/arcticfox/Downloads/columbina/uid.json', 'r', encoding='utf8') as uid:
                user_uid = json.load(uid)
            user_uid[str(message.author.id)]={}
            user_uid[str(message.author.id)]["content"] = message.content
            user_uid[str(message.author.id)]["id"] = message.id
            with open('/Users/arcticfox/Downloads/columbina/uid.json', 'w', encoding='utf8') as uid:
                json.dump(user_uid, uid, indent = 2, ensure_ascii = False)

        elif message.content == '北極狐':
            await message.channel.send("https://cdn.discordapp.com/attachments/1024158796840435732/1072579505077637130/A0F61329-4F0C-47A5-8788-3F54C6E7BD97.png")

        elif message.content == '容克':
            await message.channel.send('https://cdn.discordapp.com/attachments/978708780445495328/1079750964279513119/7PTJUV.png')

        elif message.content == '溫門':
            await message.channel.send('倘若温迪有1000名信徒 我就是那千分之一\n倘若温迪有100名信徒 我就是那普通百分之一\n倘若温迪有10名信徒 我就是那坚定的是十分之一\n倘若温迪只有有1名信徒 我便是那至死不渝的唯一\n各位朋友停下脚步给我一分钟来了解一下风吟诗人我们的教主吗\n温门永复存在')

        elif (message.content in hi_keyword) and (message.author.id not in bot_id):
            await message.reply(f'hi {message.author.name}')

        elif ('歡迎' in message.content) and (len(message.content) <= 6) and (message.author.id not in bot_id):
            await message.channel.send('歡迎～')

        elif (message.content.startswith('6')) and (len(message.content) <= 10) and (message.author.id not in bot_id):
            await message.channel.send(message.content)

def setup(bot):
    bot.add_cog(Message(bot))