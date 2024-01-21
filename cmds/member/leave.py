import json
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension


class Leave(Cog_Extension):
    DATA_FILE = "data/list.json"
    CHARLOTTE_LEAVE_CHANNEL_ID = 1167041977133580309

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        charlotte_leave_channel = self.bot.get_channel(self.CHARLOTTE_LEAVE_CHANNEL_ID)
        # banlast = self.load_data()

        # if member.id in banlast["ban"]:
        #     # Member is in ban list, no further action required.
        #     pass
        # elif str(member.id) not in banlast["leavl"]:
        #     # Member is leaving for the first time.
        #     banlast["leavl"][str(member.id)] = 1
        # elif banlast["leavl"][str(member.id)] >= 1:
        #     # Member has left previously, moving to ban list.
        #     banlast["ban"].append(member.id)
        #     del banlast["leavl"][str(member.id)]
        # else:
        #     # Increment the leave count for the member.
        #     banlast["leavl"][str(member.id)] += 1

        # self.save_data(banlast)
        await charlotte_leave_channel.send(f"{member} just left the server")
        print(f"-> {member} left the server!")

    def load_data(self):
        with open(self.DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_data(self, data):
        with open(self.DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)


def setup(bot):
    bot.add_cog(Leave(bot))
