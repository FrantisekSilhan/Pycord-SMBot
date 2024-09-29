import discord
from discord.ext import commands
import datetime

class ContextMenuCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  def log_command_usage(self, ctx, command_name):
    user = ctx.author
    time_used = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("command_usage.log", "a") as f:
      f.write(f"{time_used} - {user} used {command_name}\n")

  @commands.message_command(name="Zmatenej", integration_types={discord.IntegrationType.guild_install,discord.IntegrationType.user_install})
  async def zmatenej(self, ctx, message: discord.Message):
    self.log_command_usage(ctx, "Zmatenej")
    
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
    self.log_command_usage(ctx, "Proč?")
    
    await ctx.respond("Strýček Mach se otázal", ephemeral = True)
    await message.reply("Proč?")

def setup(client):
  client.add_cog(ContextMenuCog(client))