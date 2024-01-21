import json
import nextcord
from nextcord.ui import View, Button
from nextcord.ext import commands
from core.classes import Cog_Extension


class Message(Cog_Extension):
    # QUEST_CHANNEL_ID = 978924406745210900
    # INTRODUCTION_CHANNEL_ID = 990553527547990046
    # CHAT_CHANNEL_ID = 978708780445495328
    # BOT_IDS = [
    #     972137604470407168,
    #     992351373280690206,
    #     1065293003532546090,
    #     1070748028123750420,
    # ]
    # ARCTICFOX_ID = 407881227270356994
    # HI_KEYWORDS = ["hi", "Hi", "hello", "Hello", "嗨"]

    # def __init__(self, bot):
    #     self.bot = bot

    # async def send_dm(self, user, message):
    #     try:
    #         await user.send(message)
    #     except nextcord.HTTPException:
    #         chat_channel = self.bot.get_channel(self.CHAT_CHANNEL_ID)
    #         time_out = await chat_channel.send(
    #             f"<@{user.id}>無法私訊給您，請先確認是否將：隱私設定>允許私人訊息選項開啟(訊息30秒自動刪除)"
    #         )
    #         await time_out.delete(delay=30)

    # @commands.Cog.listener()
    # async def on_message(self, message: nextcord.Message):
    #     if message.channel.id == self.QUEST_CHANNEL_ID:
    #         await self.handle_quest_channel(message)
    #     elif message.channel.id == self.INTRODUCTION_CHANNEL_ID:
    #         await self.handle_introduction_channel(message)
    #     else:
    #         await self.handle_general_message(message)

    # async def handle_quest_channel(self, message):
    #     if (
    #         message.type != nextcord.MessageType.chat_input_command
    #         and message.author.id not in self.BOT_IDS
    #         and message.author.id != self.ARCTICFOX_ID
    #     ):
    #         await message.delete()
    #         await self.send_dm(
    #             message.author, f"在<#{message.channel.id}>請使用斜線指令喔(詳細說明請看頻道訂選訊息)"
    #         )

    # async def handle_introduction_channel(self, message):
    #     with open("data/uid.json", "r", encoding="utf8") as uid_file:
    #         user_uid = json.load(uid_file)

    #     if user_uid.get(str(message.author.id)) is None:
    #         tip4_button = Button(
    #             style=nextcord.ButtonStyle.link,
    #             url="https://discord.com/channels/978680658740260865/978708780445495328",
    #             label="聊天頻道",
    #         )
    #         button_view = View(timeout=0)
    #         button_view.add_item(tip4_button)
    #         await message.reply(
    #             "> 入群小助手\n你完成入群手續了，去聊天吧", view=button_view, delete_after=180
    #         )

    #     user_uid[str(message.author.id)] = {
    #         "content": message.content,
    #         "id": message.id,
    #     }
    #     with open("data/uid.json", "w", encoding="utf8") as uid_file:
    #         json.dump(user_uid, uid_file, indent=2, ensure_ascii=False)

    # async def handle_general_message(self, message):
    #     if message.content == "北極狐":
    #         await message.channel.send("https://upload.cc/i1/2023/02/08/QkjlHU.png")
    #     elif message.content == "容克":
    #         await message.channel.send("https://upload.cc/i1/2023/02/08/7PTJUV.png")
    #         await message.channel.send("https://upload.cc/i1/2023/02/12/xD5fRl.png")
    #     elif (
    #         message.content in self.HI_KEYWORDS
    #         and message.author.id not in self.BOT_IDS
    #     ):
    #         await message.reply(f"hi {message.author.name}")
    #     elif (
    #         "歡迎" in message.content
    #         and len(message.content) <= 6
    #         and message.author.id not in self.BOT_IDS
    #     ):
    #         await message.channel.send("歡迎～")
    #     elif (
    #         message.content.startswith("6")
    #         and len(message.content) <= 10
    #         and message.author.id not in self.BOT_IDS
    #     ):
    #         await message.channel.send(message.content)
    pass


def setup(bot):
    bot.add_cog(Message(bot))
