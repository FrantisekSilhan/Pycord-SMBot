import os, json, discord
from discord.ext import commands, tasks
import asyncio

from dotenv import load_dotenv
load_dotenv()

statusy = ["Znáš pojem vysoká bílá papírová čepice?", "{} zmatených", "Namazat... teda vymazat, na chleba si ji namažu", "Tohle už není slovíčkaření, to je mezerkování", "Když už tak spoluvole, když je to spolužák", "nespim"]

intents = discord.Intents().all()
client = commands.Bot(intents = intents, activity=discord.Game(name=statusy[0], status=discord.Status.idle))

@tasks.loop(seconds=30)
async def change_status():
    await asyncio.sleep(10)
    status = statusy[change_status.counter % len(statusy)]

    if "{}" in status:
        with open("zmateny.txt", "r") as f:
            zmateny = f.read()
        status = status.format(zmateny)

        await client.change_presence(activity=discord.Activity(name=status, type=discord.ActivityType.watching))
    else:
        await client.change_presence(status=discord.Status.online, activity=discord.Game(name=status))
    change_status.counter = (change_status.counter + 1) % len(statusy)

change_status.counter = 1
change_status.start()

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(os.environ["TOKEN"])