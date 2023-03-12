import re
import json
import os
import nextcord
from unicodedata import name
from nextcord.ext import commands

bot = commands.Bot(command_prefix = '%', intents = nextcord.Intents.all())

with open('/Users/arcticfox/Downloads/columbina/token.json', 'r', encoding = 'utf8') as token:
    token_data = json.load(token)

test_id = 1070679396165373984
actcfx_id = 1080095809175035984

#bot is online
@bot.event
async def on_ready():
    print(f'-> Logged in as {bot.user}!')


@bot.command()
async def ping(ctx):
    ping = round(bot.latency * 1000)
    await ctx.send(f'ping:{ping}ms')
    print(f'-> {bot.user} ping is {ping}ms')


@bot.command()
@commands.has_role(test_id)
@commands.has_role(actcfx_id)
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'導入{extension}成功')
    print(f'-> Loaded {extension} successful!')

@bot.command()
@commands.has_role(test_id)
@commands.has_role(actcfx_id)
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'導出{extension}成功')
    print(f'-> Unloaded {extension} successful!')

@bot.command()
@commands.has_role(test_id)
@commands.has_role(actcfx_id)
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'重置{extension}成功')
    print(f'-> Reloaded {extension} successful!')


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(error)


@bot.event
async def on_message(message):
    if message.author.id == 393768752434380804 and message.channel.id == 978708780445495328 and ('youtube.com/watch' in message.content or 'youtu.be/' in message.content):
        # Remove the old role
        old_role = message.guild.get_role(978732220154007613)
        await message.author.remove_roles(old_role)

        # Add the new role
        new_role = message.guild.get_role(1080891325093773373)
        await message.author.add_roles(new_role)

        await message.channel.send(f"{message.author.mention} 你已经被禁言一周因为发影片之前警告过了。")

    await bot.process_commands(message)


for Filename in os.listdir('/Users/arcticfox/Downloads/columbina/cmds'):
    if Filename.endswith('.py'):
        bot.load_extension(f'cmds.{Filename[:-3]}')

if __name__ == '__main__':
    bot.run(token_data['token2'])