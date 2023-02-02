import nextcord

from cmds.role import role
class EmbedModal(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(
            "Embed Marker",
        )
        self.emTitle=nextcord.ui.TextInput(label="Embed title",min_length=2,max_length=124,required=True,placeholder="Enter the embed title here!")
        self.add_item(self.emTitle)
        self.emDesc=nextcord.ui.TextInput(label="Embed Des",min_length=5,max_length=4000,required=True,placeholder="Enter the embed desciption here!",style=nextcord.TextInputStyle.paragraph)
        self.add_item(self.emDesc)
    async def callback(self, interaction: nextcord.Interaction):
        title=self.emTitle.value
        desc=self.emDesc.value
        em=nextcord.Embed(title=title,description=desc)
        return await interaction.response.send_message(embed=em)

class quest(nextcord.ui.Modal):
    def __init__(self,uid=None,name=None):
        super().__init__(
            "委託單",
        )
        self.emTitle=nextcord.ui.TextInput(label="UID",min_length=9,max_length=9,required=True,placeholder="輸入你的UID",default_value=uid)
        self.add_item(self.emTitle)
        self.emname=nextcord.ui.TextInput(label="名稱",max_length=12,required=True,placeholder="輸入你的名稱",default_value=name)
        self.add_item(self.emname)
        self.emhelp=nextcord.ui.TextInput(label="需要幫助內容",min_length=1,max_length=30,required=True,placeholder="需要幫助內容")
        self.add_item(self.emhelp)
    async def callback(self, interaction: nextcord.Interaction):
        title=self.emTitle.value
        name=self.emname.value
        help=self.emhelp.value
        role=interaction.user.roles
        chat=interaction.guild.get_channel(978708780445495328)
        word_role=[996416756086222961,996416970314489987,996417043140182097,996417097620004975,996417176099635271,996417295834423458,996417376725762089,996417493474230282]
        server_role=[996470460407627786,996470641073061939,996470572475228270,996470702880346182]
        a_g=interaction.guild
        list_2 = []
        for users_role in role:
            list_2.append(users_role.id)
        intersection = [x for x in word_role for y in list_2 if x == y]
        intersection1 = [x for x in server_role for y in list_2 if x == y]
        if len(intersection) != 0:
            word=a_g.get_role(intersection[0])
            intersection.clear
        if len(intersection1) != 0:
            desc=a_g.get_role(intersection1[0])
            intersection.clear
        if len(intersection) == 0 or len(intersection1) == 0:
            return await interaction.response.send_message('缺少身分組，請確認自己是否已領取**<世界等級 & 遊玩的伺服器>之身分組**，若沒領去請去<#978740632086523914>領取',ephemeral=True)
        em=nextcord.Embed(title=(f"UID-{title}"),description=(f"伺服器-{desc}|{word}"))
        em.set_author(name=name, icon_url=interaction.user.display_avatar.url)
        em.add_field(name="求助人", value=f"{interaction.user.mention}",inline=False)
        em.add_field(name="求助事項", value=help, inline=False)

        a=await interaction.channel.send(embed=em)
        await chat.send('好像有人需要幫助喔<#978924406745210900>')
        await a.create_thread(name=str(help),auto_archive_duration=60)
