import os
import random
import time
import string
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


@client.command(pass_context=True, name="kick")
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} Has been kicked.')


@client.command(pass_context=True, name="ban")
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} Has been banned.')

client.run("ODYzMDE5MDU5NjAyNzg0MjY3.YOgzIQ.-_HM3-DIXHNa15v5eGDdFISu-fQ")
