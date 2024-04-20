# import json
# import nextcord
# from nextcord.ext import commands
# from nextcord import SlashOption, Member
# from core.classes import Cog_Extension, ConfigData


# ADMIN_DATA: json = ConfigData.load_data("config/roles.json")
# ADMIN_ROLES_ID: dict = ADMIN_DATA["admin_roles"]


# class Points(Cog_Extension):
#     def __init__(self, bot):
#         self.bot = bot

#     @commands.has_any_role(ADMIN_ROLES_ID["boss"])
#     @nextcord.slash_command(name="給予點數", description="給予點數")
#     async def give_point(
#         self,
#         interaction: nextcord.Interaction,
#         member: Member = SlashOption(name="給誰點數", required=True),
#         give_points: int = SlashOption(name="給多少點數", required=True),
#     ):
#         POINTS_DATA: json = ConfigData.load_data("data/points.json")
#         original_points: int = 0

#         if str(member.id) in POINTS_DATA:
#             original_points = POINTS_DATA[str(member.id)]

#         new_points = original_points + give_points

#         POINTS_DATA[f"{str(member.id)}"] = new_points
#         ConfigData.save_data("data/points.json", POINTS_DATA)

#         await interaction.response.send_message(f"已給予 {member.mention} {give_points}點")

#     @commands.has_any_role(ADMIN_ROLES_ID["boss"])
#     @nextcord.slash_command(name="刪除點數", description="刪除點數")
#     async def delete_point(
#         self,
#         interaction,
#         member: Member = SlashOption(name="刪除誰點數", required=True),
#         delete_points: int = SlashOption(name="刪除多少點數", required=True),
#     ):
#         POINTS_DATA: json = ConfigData.load_data("data/points.json")
#         original_points: int = 0

#         if str(member.id) in POINTS_DATA:
#             original_points = POINTS_DATA[str(member.id)]
#         else:
#             await interaction.response.send_message(
#                 f"{member.mention} 還未擁有點數", ephemeral=True
#             )
#             return

#         new_points = original_points - delete_points

#         POINTS_DATA[f"{str(member.id)}"] = new_points
#         ConfigData.save_data("data/points.json", POINTS_DATA)

#         await interaction.response.send_message(
#             f"已刪除 {member.mention} {delete_points}點"
#         )

#     @commands.has_any_role(ADMIN_ROLES_ID["boss"])
#     @nextcord.slash_command(name="清空點數", description="清空點數")
#     async def clear_points(
#         self, interaction, member: Member = SlashOption(name="清空誰點數", required=True)
#     ):
#         POINTS_DATA: json = ConfigData.load_data("data/points.json")

#         if str(member.id) not in POINTS_DATA:
#             await interaction.response.send_message(
#                 f"{member.mention} 還未擁有點數", ephemeral=True
#             )
#             return

#         POINTS_DATA[f"{str(member.id)}"] = 0
#         ConfigData.save_data("data/points.json", POINTS_DATA)

#         await interaction.response.send_message(f"已清空 {member.mention} 所有點數")

#     @nextcord.slash_command(name="查詢點數", description="查詢點數")
#     async def search_points(
#         self, interaction, member: Member = SlashOption(name="查詢誰的", required=False)
#     ):
#         search_embed = nextcord.Embed(title="查詢結果", color=0x8F77B5)

#         if member != None:
#             MEMBER_ID = member.id
#             if str(MEMBER_ID) in point_dict:
#                 search_embed.add_field(
#                     name=member, value=point_dict[str(MEMBER_ID)], inline=False
#                 )
#             else:
#                 await interaction.response.send_message(
#                     f"{member} 還未擁有點數", ephemeral=True
#                 )
#                 return
#         else:
#             for dict_member_id in point_dict:
#                 search_embed.add_field(
#                     name=self.bot.get_user(int(dict_member_id)),
#                     value=point_dict[dict_member_id],
#                     inline=False,
#                 )
#         await interaction.response.send_message(embed=search_embed)


# def setup(bot):
#     bot.add_cog(Points(bot))

import json
import nextcord
from nextcord import User, SlashOption
from nextcord.ext import commands
from core.classes import Cog_Extension


with open("data/points.json", "r", encoding="utf8") as points_json:
    point_dict = json.load(points_json)

BOSS_ROLE_ID = 978680963099942912
# BOSS_ROLE_ID = 1080095809175035984
GUILD_ID = 978680658740260865


class Points(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="給予點數", description="給予點數")
    async def 給予點數(
        self,
        interaction: nextcord.Interaction,
        member: User = SlashOption(name="給誰點數", required=True),
        points: int = SlashOption(name="給多少點數", required=True),
    ):

        MEMBER_ID = member.id
        member_points = 0

        if str(MEMBER_ID) in point_dict:
            member_points = point_dict[str(MEMBER_ID)]

        member_points = member_points + points

        point_dict[f"{str(MEMBER_ID)}"] = member_points
        with open("data/points.json", "w", encoding="utf8") as point_json:
            json.dump(point_dict, point_json)

        await interaction.response.send_message(f"已給予 '{member}' {points}點")

    @nextcord.slash_command(name="刪除點數", description="刪除點數")
    async def 刪除點數(
        self,
        interaction,
        member: User = SlashOption(name="刪除誰點數", required=True),
        points: int = SlashOption(name="刪除多少點數", required=True),
    ):

        MEMBER_ID = member.id
        member_points = 0

        if str(MEMBER_ID) in point_dict:
            member_points = point_dict[str(MEMBER_ID)]
        else:
            await interaction.response.send_message(f"{member} 還未擁有點數", ephemeral=True)
            return

        member_points = member_points - points

        point_dict[f"{str(MEMBER_ID)}"] = member_points
        with open("data/points.json", "w", encoding="utf8") as point_json:
            json.dump(point_dict, point_json)

        await interaction.response.send_message(f"已刪除 '{member}' {points}點")

    @nextcord.slash_command(name="清空點數", description="清空點數")
    async def 清空點數(
        self, interaction, member: User = SlashOption(name="清空誰點數", required=True)
    ):

        MEMBER_ID = member.id
        member_points = 0

        if str(MEMBER_ID) not in point_dict:
            await interaction.response.send_message(f"{member} 還未擁有點數", ephemeral=True)
            return

        point_dict[f"{str(MEMBER_ID)}"] = member_points
        with open("data/points.json", "w", encoding="utf8") as point_json:
            json.dump(point_dict, point_json)

        await interaction.response.send_message(f"已清空 '{member}' 所有點數")

    @nextcord.slash_command(name="查詢點數", description="查詢點數")
    async def 查詢點數(
        self, interaction, member: User = SlashOption(name="查詢誰的", required=False)
    ):

        search_embed = nextcord.Embed(title="查詢結果", color=0x8F77B5)

        if member != None:
            MEMBER_ID = member.id
            if str(MEMBER_ID) in point_dict:
                search_embed.add_field(name = member, value = point_dict[str(MEMBER_ID)], inline = False)
            else:
                await interaction.response.send_message(f"{member} 還未擁有點數", ephemeral=True)
                return
        else:
            for dict_member_id in point_dict:
                search_embed.add_field(name = self.bot.get_user(int(dict_member_id)), value = point_dict[dict_member_id], inline = False)
        await interaction.response.send_message(embed=search_embed)


def setup(bot):
    bot.add_cog(Points(bot))
