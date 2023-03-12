import json
import asyncio
import time

now = lambda: time.time()
start = now()

with open('/Users/arcticfox/Downloads/columbina/roles.json', 'r' , encoding = 'utf-8') as roles:
    roles = json.load(roles)

role_list = [list(roles["world_level"].values())[:-1],
             list(roles["server"].values())[:-1],
             list(roles["announcement"].values())[:-1],
             list(roles["guild_roles"].values())[:-1],
             list(roles["eyes"].values())[:-1],]
print(role_list)
set_role_list = set(role_list[0])

emoji_list = [list(roles["world_level"])[:-1],
              list(roles["server"])[:-1],
              list(roles["announcement"])[:-1],
              list(roles["guild_roles"])[:-1],
              list(roles["eyes"])[:-1],]
print(emoji_list)
print(emoji_list[0].index('8\ufe0f\u20e3'))

mes_id = 1079813967570022421

mem_roles = []

mem_roles = [996416756086222961, 996470702880346182]
set_user_roles = set(mem_roles)
repeat_role = set_user_roles & set_role_list
print(repeat_role)

print(now() - start)