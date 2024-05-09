import json
import nextcord
from nextcord import Role, Guild
from nextcord.ext import commands
from core.classes import Cog_Extension, ConfigData


class Role(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        GUILD_ID: int = ConfigData.load_data("config/bot_info.json").get("guild_id")
        GUILD: Guild = self.bot.get_guild(GUILD_ID)

        REACTION_ROLES_DICT: dict = ConfigData.load_data("data/reaction_roles.json")
        REACTION_ROLES_GROUPS: list[str] = list(REACTION_ROLES_DICT.keys())
        REACTION_ROLES_MESSAGES_ID: list[int] = [
            REACTION_ROLES_DICT.get(roles_group).get("message_id")
            for roles_group in REACTION_ROLES_GROUPS
        ]

        MEMBER_ROLES_ID_SET: set[int] = {role.id for role in payload.member.roles}

        target_group: dict
        target_group_roles_dict: dict
        target_group_roles: list[int]
        target_group_emojis: list[int]
        target_role_index: int
        target_role: Role
        repeat_emoji_set: set[int]
        repeat_emoji_list: list[int]

        if payload.guild_id != GUILD_ID:
            return

        if payload.message_id not in REACTION_ROLES_MESSAGES_ID:
            return

        target_group = REACTION_ROLES_DICT.get(
                    REACTION_ROLES_GROUPS[REACTION_ROLES_MESSAGES_ID.index(payload.message_id)]
                )
        target_group_roles_dict = target_group.get("roles")
        target_group_roles = target_group_roles_dict.get("role_id")
        target_group_emojis = target_group_roles_dict.get("emoji")

        target_role_index = target_group_emojis.index(str(payload.emoji))
        target_role = GUILD.get_role(target_group_roles[target_role_index])

        await payload.member.add_roles(target_role)

        if target_group.get("repeatable"):
            return
        else:
            repeat_emoji_set = MEMBER_ROLES_ID_SET.intersection(target_group_roles)
            if any(repeat_emoji_set):
                repeat_emoji_list = list(repeat_emoji_set)
                for repeat_emoji_id in repeat_emoji_list:
                    repeat_emoji_index = target_group_roles.index(repeat_emoji_id)
                    repeat_emoji = target_group_emojis[repeat_emoji_index]

                    message = GUILD.get_channel(payload.channel_id).get_partial_message(payload.message_id)
                    await message.remove_reaction(repeat_emoji, payload.member)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        GUILD_ID: int = ConfigData.load_data("config/bot_info.json").get("guild_id")
        GUILD: Guild = self.bot.get_guild(GUILD_ID)

        REACTION_ROLES_DICT: dict = ConfigData.load_data("data/reaction_roles.json")
        REACTION_ROLES_GROUPS: list[str] = list(REACTION_ROLES_DICT.keys())
        REACTION_ROLES_MESSAGES_ID: list[int] = [
            REACTION_ROLES_DICT.get(roles_group).get("message_id")
            for roles_group in REACTION_ROLES_GROUPS
        ]

        target_group: dict
        target_group_roles_dict: dict
        target_group_roles: list[int]
        target_group_emojis: list[int]
        target_role_index: int
        target_role: Role

        if payload.guild_id != GUILD_ID:
            return

        if payload.message_id not in REACTION_ROLES_MESSAGES_ID:
            return

        target_group = REACTION_ROLES_DICT.get(
            REACTION_ROLES_GROUPS[REACTION_ROLES_MESSAGES_ID.index(payload.message_id)]
        )
        target_group_roles_dict = target_group.get("roles")
        target_group_roles = target_group_roles_dict.get("role_id")
        target_group_emojis = target_group_roles_dict.get("emoji")

        target_role_index = target_group_emojis.index(str(payload.emoji))
        target_role = GUILD.get_role(target_group_roles[target_role_index])

        await GUILD.get_member(payload.user_id).remove_roles(target_role)


def setup(bot):
    bot.add_cog(Role(bot))
