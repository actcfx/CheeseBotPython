import json
import nextcord
from nextcord.ui import TextInput
from nextcord import Interaction, Embed
from core.classes import ConfigData


class QuestModal(nextcord.ui.Modal):
    def __init__(self, name=None, uid=None):
        super().__init__("委託單")
        self.name = name
        self.uid = uid

        self.uid_input = TextInput(
            label="UID",
            min_length=9,
            max_length=10,
            required=True,
            placeholder="輸入你的UID",
            default_value=(uid if uid else None),
        )
        self.add_item(self.uid_input)

        self.name_input = TextInput(
            label="名稱",
            max_length=12,
            required=True,
            placeholder="輸入你的名稱",
            default_value=(name if name else None),
        )
        self.add_item(self.name_input)

        self.help_input = TextInput(
            label="需要幫助內容",
            min_length=1,
            max_length=30,
            required=True,
            placeholder="需要幫助內容",
        )
        self.add_item(self.help_input)

    async def callback(self, interaction: Interaction):
        ROLE_DATA = ConfigData.load_data("config/roles.json")
        WORLD_ROLES_SET: set = set(ROLE_DATA.get("genshin_world_roles"))
        SERVER_ROLES_SET: set = set(ROLE_DATA.get("genshin_server_roles"))
        QUEST_NOTIFY_ROLES_DICT: dict = ROLE_DATA.get("quest_notify_roles")
        user_roles_set = {role.id for role in interaction.user.roles}
        intro_data: json = ConfigData.load_data("data/intro.json")

        # Find the common roles
        world_role = interaction.guild.get_role(
            next(iter(user_roles_set.intersection(WORLD_ROLES_SET)))
        )
        server_role = interaction.guild.get_role(
            next(iter(user_roles_set.intersection(SERVER_ROLES_SET)))
        )
        notify_role = QUEST_NOTIFY_ROLES_DICT[str(server_role.id)]

        if not world_role or not server_role:
            return await interaction.response.send_message(
                "缺少身分組，請確認自己是否已領取**<世界等級 & 遊玩的伺服器>之身分組**，若沒領去請去<#978740632086523914>領取",
                ephemeral=True,
            )

        if self.name == None:
            intro_data[str(interaction.user.id)]["name"] = int(self.name_input.value)
            ConfigData.save_data("data/intro.json", intro_data)

        if self.uid == None:
            intro_data[str(interaction.user.id)]["genshin_uid"] = int(self.uid_input.value)
            ConfigData.save_data("data/intro.json", intro_data)

        # Create Embed
        embed = Embed(
            title=f"UID-{self.uid_input.value}",
            description=f"伺服器－{server_role}｜{world_role}",
        )
        embed.set_author(
            name=self.name_input.value, icon_url=interaction.user.display_avatar.url
        )
        embed.add_field(
            name="求助人", value=f"{interaction.user.mention}", inline=False
        )
        embed.add_field(name="求助事項", value=self.help_input.value, inline=False)

        # Send Quest
        help_message = await interaction.channel.send(
            embed=embed, content=interaction.guild.get_role(notify_role).mention
        )
        quest_thread = await help_message.create_thread(
            name=str(self.help_input.value), auto_archive_duration=60
        )
        await quest_thread.send(self.uid_input.value)
