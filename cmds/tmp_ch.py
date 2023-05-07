import nextcord
import json
from ast import Pass
from nextcord.ext import commands
from core.classes import Cog_Extension

global s, s1, s2

class tmp_channel(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        with open('data/list.json', 'r', encoding = 'utf-8') as list:
            list1 = json.load(list)
        tmp_channels_list = list1['tmp_channels']

        global create_channel
        everyone_role = self.bot.get_guild(member.guild.id).get_role(978680658740260865)
        member_role = self.bot.get_guild(member.guild.id).get_role(978732220154007613)

        create_channel = {
            member:nextcord.PermissionOverwrite(manage_channels = True),    #給予頻道創建者編輯該頻道的權限
            everyone_role:nextcord.PermissionOverwrite(view_channel = False),   #使everyone身分組無法瀏覽頻道
            member_role:nextcord.PermissionOverwrite(view_channel = True),    #給予成員身分組瀏覽頻道的權限
        }

        s = self.bot.get_guild(978680658740260865)      #獲取伺服器
        s1 = s.get_channel(1067052338616999989)     #設置動態語音頻道位置
        s2 = s1.category

        if after.channel == None:   #如果切換頻道 (後) 不在語音頻道
            if int(before.channel.id) in tmp_channels_list:     #看退出去前的語音頻道是否為機器人創建的頻道
                if before.channel == None:
                    pass
                else:
                    if before.channel.members == []:
                        await before.channel.delete()
                        tmp_channels_list.remove(int(before.channel.id))
                        with open('data/list.json', 'w', encoding='utf-8') as list:
                            json.dump(list1,list)
                        print(f'-> Delete temporary_channel {before.channel.name}!')
            elif before.channel != None:    #如果之前所在的頻道為其他的語音頻道
                if int(before.channel.id) in tmp_channels_list:
                    if before.channel.members == []:
                        await before.channel.delete()
                        tmp_channels_list.remove(int(before.channel.id))
                        with open('data/list.json', 'w', encoding='utf-8') as list:
                            json.dump(list1,list)
                        print(before.id)

        if before.channel == None:   #如果在切換頻道 (前) 不在語音頻道
            if after.channel.id == 1067052338616999989:     #設置動態語音頻道位置
                try:
                    if before.channel.members == []:
                        if int(before.channel.id) in tmp_channels_list:
                            await before.channel.delete()
                            tmp_channels_list.remove(int(before.channel.id))
                            with open('data/list.json', 'w', encoding='utf-8') as list:
                                json.dump(list1,list)
                            print(f'-> Delete temporary_channel {before.channel.name}!')
                except:
                    now_channel = await s.create_voice_channel(f'└[{str(member).split("#")[0]}] 的頻道', overwrites = create_channel, category = s2, bitrate = 384000)  #設置名稱
                    tmp_channels_list.append(int(now_channel.id))
                    with open('data/list.json', 'w', encoding='utf-8') as list:
                        json.dump(list1,list)
                    await member.move_to(now_channel)
                    print(f'-> Create temporary_channel {now_channel.name}!')
            else:
                try:
                    if int(before.channel.id) in tmp_channels_list:
                        if before.channel.members == []:
                            await before.channel.delete()
                            tmp_channels_list.remove(int(before.channel.id))
                            with open('data/list.json', 'w', encoding='utf-8') as list:
                                json.dump(list1,list)
                            print(f'-> Delete temporary_channel {before.channel.name}!')
                except:
                    pass

        if before.channel != None and after.channel  != None: #在兩語音頻道切換時
            if after.channel.id == 1067052338616999989: #設置動態語音頻道位置
                if int(before.channel.id) in tmp_channels_list:
                    if before.channel.members == []:
                        await before.channel.delete()
                        tmp_channels_list.remove(int(before.channel.id))
                        with open('data/list.json', 'w', encoding='utf-8') as list:
                            json.dump(list1,list)
                        print(f'-> Delete temporary_channel {before.channel.name}!')
                now_channel = await s.create_voice_channel(f'└[{str(member).split("#")[0]}] 的頻道', overwrites = create_channel, category = s2, bitrate = 384000)  #設置名稱
                tmp_channels_list.append(int(now_channel.id))
                with open('data/list.json', 'w', encoding='utf-8') as list:
                    json.dump(list1,list)
                await member.move_to(now_channel)
                print(f'-> Create temporary_channel {now_channel.name}!')
            else:
                if before.channel.members == []:
                    if int(before.channel.id) in tmp_channels_list:
                        await before.channel.delete()
                        tmp_channels_list.remove(int(before.channel.id))
                        with open('data/list.json', 'w', encoding='utf-8') as list:
                            json.dump(list1,list)
                        print(f'-> Delete temporary_channel {before.channel.name}!')


    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def append(self, ctx, channel_id: int):
        with open('data/list.json', 'r', encoding = 'utf-8') as list:
            list1 = json.load(list)

        list1['tmp_channels'].append(channel_id)
        with open('data/list.json', 'w', encoding='utf-8') as list:
            json.dump(list1,list)

        await ctx.send(f'添加動態語音頻道 {channel_id} 成功')
        print(f'-> Appended temporary_channel {channel_id} successful!')

    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def remove(self, ctx, channel_id: int):
        with open('data/list.json', 'r', encoding = 'utf-8') as list:
            list1 = json.load(list)

        list1['tmp_channels'].remove(channel_id)
        with open('data/list.json', 'w', encoding='utf-8') as list:
            json.dump(list1,list)

        await ctx.send(f'刪除動態語音頻道 {channel_id} 成功')
        print(f'-> Remove temporary_channel {channel_id} successful!')

def setup(bot):
    bot.add_cog(tmp_channel(bot))