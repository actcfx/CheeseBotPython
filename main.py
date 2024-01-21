import os
import json
import nextcord
from core.classes import ConfigData
from nextcord.ext import commands

bot = commands.Bot(command_prefix="%", intents=nextcord.Intents.all())

TOKEN_DATA: json = ConfigData.load_data("config/token.json")
TOKEN: str = TOKEN_DATA["test_token"]

ADMIN_DATA: json = ConfigData.load_data("config/roles.json")
ADMIN_ROLES_ID: dict = ADMIN_DATA["admin_roles"]


# bot 上線
@bot.event
async def on_ready():
    print(f"ONLINE | Logged in as {bot.user}!")


@bot.command()
async def ping(ctx):
    ping = round(bot.latency * 1000)
    await ctx.send(f"ping:{ping}ms")
    print(f"PING | {bot.user} ping is {ping}ms")


@bot.command()
@commands.is_owner()
@commands.has_any_role(
    ADMIN_ROLES_ID["boss"], ADMIN_ROLES_ID["developer"], ADMIN_ROLES_ID["actcfx"]
)
async def load(ctx, extension):
    bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"導入 {extension} 成功")
    print(f"LOAD | Load {extension} successful!")


@bot.command()
@commands.is_owner()
@commands.has_any_role(
    ADMIN_ROLES_ID["boss"], ADMIN_ROLES_ID["developer"], ADMIN_ROLES_ID["actcfx"]
)
async def unload(ctx, extension):
    bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"導出 {extension} 成功")
    print(f"UNLOAD | Unload {extension} successful!")


@bot.command()
@commands.is_owner()
@commands.has_any_role(
    ADMIN_ROLES_ID["boss"], ADMIN_ROLES_ID["developer"], ADMIN_ROLES_ID["actcfx"]
)
async def reload(ctx, extension):
    bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"重置 {extension} 成功")
    print(f"RELOAD | Reload {extension} successful!")


# 載入 cog files
for foldername in os.listdir("cmds"):
    for filename in os.listdir(f"cmds/{foldername}"):
        if filename.endswith(".py"):
            try:
                bot.load_extension(f"cmds.{foldername}.{filename[:-3]}")
                print(f"✅ | {foldername}/{filename} is online!")
            except Exception as cog_load_error:
                print(
                    f"❌ | {foldername}/{filename} has passed, because of an unexpected error [{cog_load_error}]"
                )

print("--------------------------------------------------")

if __name__ == "__main__":
    bot.run(TOKEN)
