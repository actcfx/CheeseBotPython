import json
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension

with open('/Users/arcticfox/Downloads/columbina/roles.json', 'r', encoding='utf-8') as roles:
    roles = json.load(roles)

role_mes_list = list(roles["role_mes"].values())

role_list = [list(roles["world_level"].values())[:-1],
                list(roles["server"].values())[:-1],
                list(roles["announcement"].values())[:-1],
                list(roles["guild_roles"].values())[:-1],
                list(roles["eyes"].values())[:-1],]

emoji_list = [list(roles["world_level"])[:-1],
                list(roles["server"])[:-1],
                list(roles["announcement"])[:-1],
                list(roles["guild_roles"])[:-1],
                list(roles["eyes"])[:-1],]

repeatable_list = [list(roles["world_level"].values())[-1],
                    list(roles["server"].values())[-1],
                    list(roles["announcement"].values())[-1],
                    list(roles["guild_roles"].values())[-1],
                    list(roles["eyes"].values())[-1],]

server_roles = list(roles["server"].values())

class Role(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        try:
            mes_id_index = role_mes_list.index(payload.message_id)
            mes_id = payload.message_id
        except:
            return

        mem_roles = []
        guild = self.bot.get_guild(payload.guild_id)
        channel = guild.get_channel(payload.channel_id)
        mes = channel.get_partial_message(mes_id)

        role_index = emoji_list[mes_id_index].index(str(payload.emoji))
        await payload.member.add_roles(guild.get_role(role_list[mes_id_index][role_index]))

        if repeatable_list[mes_id_index] == True:
            return
        for mem_role in payload.member.roles:
            mem_roles.append(mem_role.id)
        set_mem_roles = set(mem_roles)
        set_role_list = set(role_list[mes_id_index])
        set_repeat_role = (set_mem_roles & set_role_list)
        if any(set_repeat_role):
            repeat_roles = list(set_repeat_role)
            repeat_index = role_list[mes_id_index].index(repeat_roles[0])
            await mes.remove_reaction(emoji_list[mes_id_index][repeat_index], payload.member)


    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        try:
            mes_id_index = role_mes_list.index(payload.message_id)
            mes_id = payload.message_id
        except:
            return

        guild = self.bot.get_guild(payload.guild_id)
        channel = guild.get_channel(payload.channel_id)
        member = guild.get_member(payload.user_id)

        role_index = emoji_list[mes_id_index].index(str(payload.emoji))
        await member.remove_roles(guild.get_role(role_list[mes_id_index][role_index]))

def setup(bot):
    bot.add_cog(Role(bot))
