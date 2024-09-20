import discord
from discord.ext import commands
import nekos
import random

class ContextMenuCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.message_command(name="Zmatenej", integration_types={discord.IntegrationType.guild_install,discord.IntegrationType.user_install})
  async def zmatenej(self, ctx, message: discord.Message):
    try:
      with open("zmateny.txt", "r") as f:
        pass
    except FileNotFoundError:
      with open("zmateny.txt", "w") as f:
        f.write("1")
    
    with open("zmateny.txt", "r") as f:
      zmateny = int(f.read())+1
    with open("zmateny.txt", "w") as f:
      f.write(str(zmateny))
    await ctx.respond(f"Počet zmatených: {zmateny}", ephemeral = True)
    await message.reply("Seš zmatenej, co?")

  @commands.message_command(name="Proč?", integration_types={discord.IntegrationType.guild_install,discord.IntegrationType.user_install})
  async def proc(self, ctx, message: discord.Message):
    await ctx.respond("Strýček Mach se otázal", ephemeral = True)
    await message.reply("Proč?")

def setup(client):
  client.add_cog(ContextMenuCog(client))