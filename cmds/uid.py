import asyncio
import nextcord
from nextcord.ui import View, Button, Modal
from nextcord.ext import commands
from core.classes import Cog_Extension

class UID_view(View):
    def __init__(self):
        super().__init__()
    @nextcord.ui.button(label = '驗證 UID', style = nextcord.ButtonStyle.primary)
    async def UID(self, button, interaction: nextcord.Interaction):
        await interaction.response.send_modal(UID_modal())

class UID_modal(Modal):
    def __init__(self, user_uid = None):
        super().__init__(
            "UID 驗證",
        )
        self.ctx = nextcord.ui.TextInput(
            label = "UID", min_length = 9, max_length = 9, required = True, placeholder = "輸入你的UID", default_value = user_uid)
        self.add_item(self.ctx)

    async def callback(self, interaction: nextcord.Interaction):
        user_uid = self.ctx.value
        guild = interaction.guild
        member = guild.get_member(interaction.user.id)

        if user_uid.startswith('8'):
            await member.add_roles(guild.get_role(996470572475228270))
        elif user_uid.startswith('9'):
            await member.add_roles(guild.get_role(996470702880346182))
        else:
            await interaction.response.followup_message('Invalid UID. Please try again.')
            return

        # Update the user's nickname to include the UID
        nickname = member.display_name.split(' ')[0]
        new_nickname = f'{nickname} ({user_uid})'
        await member.edit(nick=new_nickname)

        # Send a message to confirm the role and nickname change
        await interaction.response.send_message(f'Your UID ({user_uid}) has been verified for . You have been has been updated to {new_nickname}.')

class UID(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot
        self.uid_message = None

    @commands.command(name='uid')
    async def uid_command(self, ctx):
        view = UID_view()
        message = await ctx.send('Click the button to enter your UID', view = view)
        self.uid_message = message

def setup(bot):
    bot.add_cog(UID(bot))