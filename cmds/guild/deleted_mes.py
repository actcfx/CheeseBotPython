import json
from nextcord.ext import commands
from nextcord import TextChannel, Embed, Message
from core.classes import Cog_Extension, ConfigData


class DeletedMessage(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        BOT_INFO: json = ConfigData.load_data("config/bot_info.json")
        GUILD_ID: int = BOT_INFO.get("guild_id")

        DEL_MES_CHANNEL_ID: int = ConfigData.load_data("config/channels.json").get("del_mes_channel")
        DEL_MES_CHANNEL: TextChannel = self.bot.get_channel(DEL_MES_CHANNEL_ID)
        DEL_ATTACHMENT_CHANNEL_ID: int = ConfigData.load_data("config/channels.json").get("del_attachment_channel")
        DEL_ATTACHMENT_CHANNEL: TextChannel = self.bot.get_channel(DEL_ATTACHMENT_CHANNEL_ID)

        if message.guild.id != GUILD_ID:
            return

        embed: Embed = Embed(title="Message Deleted", color=0xFB9966)
        embed.add_field(name="Author", value=message.author.mention, inline=False)
        embed.add_field(name="Channel", value=message.channel.mention, inline=False)

        if message.content:
            embed.add_field(name="Content", value=message.content, inline=False)
        for attachment in message.attachments:
            embed.add_field(name="Attachment", value=attachment.url, inline=False)

        del_mes: Message = await DEL_MES_CHANNEL.send(embed=embed)
        del_mes_url = del_mes.jump_url

        if len(message.attachments) > 0:
            for attachment in message.attachments:
                await DEL_ATTACHMENT_CHANNEL.send(
                    f"link: {del_mes_url}\nattchment: ", file=await attachment.to_file()
                )


def setup(bot):
    bot.add_cog(DeletedMessage(bot))
