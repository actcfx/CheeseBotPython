import nextcord


class EmbedModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__("Embed Marker")
        self.title_input = nextcord.ui.TextInput(
            label="Embed title",
            min_length=2,
            max_length=124,
            required=True,
            placeholder="Enter the embed title here!",
        )
        self.add_item(self.title_input)
        self.description_input = nextcord.ui.TextInput(
            label="Embed Description",
            min_length=5,
            max_length=4000,
            required=True,
            placeholder="Enter the embed description here!",
            style=nextcord.TextInputStyle.paragraph,
        )
        self.add_item(self.description_input)

    async def callback(self, interaction: nextcord.Interaction):
        embed = nextcord.Embed(
            title=self.title_input.value, description=self.description_input.value
        )
        await interaction.response.send_message(embed=embed)


class QuestModal(nextcord.ui.Modal):
    def __init__(self, uid=None, name=None):
        super().__init__("委託單")
        self.uid_input = nextcord.ui.TextInput(
            label="UID",
            min_length=9,
            max_length=9,
            required=True,
            placeholder="輸入你的UID",
            default_value=uid,
        )
        self.add_item(self.uid_input)
        self.name_input = nextcord.ui.TextInput(
            label="名稱",
            max_length=12,
            required=True,
            placeholder="輸入你的名稱",
            default_value=name,
        )
        self.add_item(self.name_input)
        self.help_input = nextcord.ui.TextInput(
            label="需要幫助內容",
            min_length=1,
            max_length=30,
            required=True,
            placeholder="需要幫助內容",
        )
        self.add_item(self.help_input)

    async def callback(self, interaction: nextcord.Interaction):
        user_roles = {role.id for role in interaction.user.roles}
        word_roles = {
            996416756086222961,
            996416970314489987,
            996417043140182097,
            996417097620004975,
            996417176099635271,
            996417295834423458,
            996417376725762089,
            996417493474230282,
        }
        server_roles = {
            996470460407627786,
            996470641073061939,
            996470572475228270,
            996470702880346182,
        }

        # Find the common roles
        common_word_roles = user_roles.intersection(word_roles)
        common_server_roles = user_roles.intersection(server_roles)

        if not common_word_roles or not common_server_roles:
            return await interaction.response.send_message(
                "缺少身分組，請確認自己是否已領取**<世界等級 & 遊玩的伺服器>之身分組**，若沒領去請去<#978740632086523914>領取",
                ephemeral=True,
            )

        # Create Embed
        world_role = interaction.guild.get_role(next(iter(common_word_roles)))
        server_role = interaction.guild.get_role(next(iter(common_server_roles)))
        embed = nextcord.Embed(
            title=f"UID-{self.uid_input.value}",
            description=f"伺服器－{server_role}｜{world_role}",
        )
        embed.set_author(
            name=self.name_input.value, icon_url=interaction.user.display_avatar.url
        )
        embed.add_field(name="求助人", value=f"{interaction.user.mention}", inline=False)
        embed.add_field(name="求助事項", value=self.help_input.value, inline=False)

        help_message = await interaction.channel.send(embed=embed)
        help_channel = interaction.guild.get_channel(978708780445495328)
        await help_channel.send("好像有人需要幫助喔<#978924406745210900>")
        quest_thread = await help_message.create_thread(
            name=str(self.help_input.value), auto_archive_duration=60
        )
        await quest_thread.send(f"<@&{next(iter(common_server_roles))}>")
        await quest_thread.send(self.uid_input.value)
