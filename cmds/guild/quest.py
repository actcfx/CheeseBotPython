import re
import json
import nextcord
from core.classes import Cog_Extension
from modal import QuestModal
from nextcord.ext import commands


class Quest(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="求助", description="發送求助")
    async def 求助(self, interaction: nextcord.Interaction):
        try:
            with open("data/uid.json", "r", encoding="utf8") as uid_file:
                user_uid = json.load(uid_file)

            user_id_str = str(interaction.user.id)
            if user_id_str in user_uid:
                content = user_uid[user_id_str]["content"]
                my_uid = re.search(r"\b\d{9}\b", content)
                my_name = re.search(r"[^名字:：\s]\w{1,}", content)

                if my_uid and my_name:
                    await interaction.response.send_modal(
                        QuestModal(my_uid.group(), my_name.group())
                    )
                else:
                    raise ValueError("Invalid UID or name format in user introduction.")
            else:
                await interaction.response.send_modal(QuestModal())

        except Exception as error:
            await interaction.response.send_message(
                f"發生錯誤：```{str(error)}```請將此錯誤私訊給<@407881227270356994>協助處理",
                ephemeral=True,
            )


def setup(bot):
    bot.add_cog(Quest(bot))
