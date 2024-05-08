import json
import nextcord
from json import JSONDecodeError
from nextcord.ext import commands
from core.classes import Cog_Extension, ErrorHandler
from nextcord import Interaction, Attachment, File, Embed


class SendEmbed(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="發送embed訊息", description="timestamp目前不可用！")
    @commands.has_any_role(978680963099942912, 1069934439200735233)
    async def 發送embed訊息(
        self, interaction: Interaction, attachment: Attachment
    ):
        await interaction.response.defer(ephemeral=True)

        try:
            # 讀取附件中的 JSON 內容
            ATTACHMENT_FILE: File = await attachment.to_file()
            CONTENT: json = json.loads(ATTACHMENT_FILE.fp.read().decode("utf-8"))

            # 處理普通消息
            if "content" in CONTENT:
                await interaction.channel.send(CONTENT["content"])

            # 處理嵌入消息
            for embed_data in CONTENT.get("embeds", []):
                embed: Embed = Embed.from_dict(embed_data)
                await interaction.channel.send(embed=embed)

            await interaction.followup.send("發送成功！", ephemeral=True)

        except (JSONDecodeError, TypeError) as file_error:
            await ErrorHandler.handle_error(
                self,
                interaction,
                command="發送 embed 訊息",
                error_content=file_error,
                error_type="file_error",
            )

        except Exception as other_error:
            await ErrorHandler.handle_error(
                self,
                interaction,
                command="發送 embed 訊息",
                error_content=other_error,
                error_type="other_error",
            )


def setup(bot):
    bot.add_cog(SendEmbed(bot))
