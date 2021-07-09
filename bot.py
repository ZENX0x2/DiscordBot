import os
import random
import time
from discord import channel
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check

client = discord.Client()

client = commands.Bot(command_prefix='-', case_insensitive=True)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Nookavan On YouTube"))


client.run("ODYzMDE5MDU5NjAyNzg0MjY3.YOgzIQ.-_HM3-DIXHNa15v5eGDdFISu-fQ")
