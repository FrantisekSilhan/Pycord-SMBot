import discord
from discord.ext import commands
from unidecode import unidecode

class MessageCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_message(self, message):
    if self.client.user == message.author:
      return
    messageContent = unidecode(message.content.lower()).replace("?", " ").replace("!", " ").replace(".", " ").replace(",", " ").split(" ")
    spis = False
    vole = False
    for i in messageContent:
      if i == "spis":
        spis = True
      elif i == "vole":
        vole = True

    if spis and vole:
      await message.reply("nespim spoluvole")
    elif spis:
      await message.reply("nespim")
    elif vole:
      await message.reply("spoluvole")

def setup(client):
  client.add_cog(MessageCog(client))