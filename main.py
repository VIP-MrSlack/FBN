import discord
from discord.ext import commands, tasks
intents = discord.Intents.default()
intents.messages = True
client = commands.Bot(command_prefix="!", intents=intents)
stored_server_names = {}
@client.event
async def on_ready():
    print("Bot is ready!")
    for guild in client.guilds:
        stored_server_names[guild.id] = guild.name
@client.event
async def on_guild_update(before, after):
    if before.name != after.name:
        stored_server_names[after.id] = before.name
        send_message.start()
        print(f"Server '{before.name}' changed its name to '{after.name}'.")
@tasks.loop(seconds=60)
async def send_message():
    channel = client.get_channel(1208201212101402697)
    for i in range(1):
        await channel.send("[Fuck BlackNet](<https://youareanidiot.cc/>) `CyberFace`")
token = input("Enter your token → ")
client.run(token)
