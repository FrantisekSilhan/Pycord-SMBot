import discord
from discord.ext import commands
from unidecode import unidecode

class MessageCog(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.ignored_channels = ["1032556298904031272"]

  @commands.Cog.listener()
  async def on_message(self, message):
    if self.client.user == message.author:
      return
    
    if message.channel.id in self.ignored_channels:
      return
    
    normalized_content = unidecode(message.content.lower())
    cleaned_content = normalized_content.translate(str.maketrans("?.!,", "    "))
    words = cleaned_content.split(" ")

    reply = ""
    if "spis" in words:
      reply += "nespim "
    if "vole" in words:
      reply += "spoluvole "
    if reply:
      await message.reply(reply)


def setup(client):
  client.add_cog(MessageCog(client))