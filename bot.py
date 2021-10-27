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
    print("Bot Ready!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=" -Help | Nookavan Studios"))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements :angry:")


@client.command()
async def help(message):
    embedVar = discord.Embed(
        title="Help", description="Help for the commands", color=000000)
    embedVar.add_field(
        name="Ban", value="Bans members", inline=False)
    embedVar.add_field(
        name="Kick", value="Kicks members", inline=False)
    embedVar.add_field(
        name="too lazy", value="Im too lazy to add all of em now.", inline=False)
    await message.channel.send(embed=embedVar)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
    if not reason:
        await user.kick()
        await ctx.send(f"**{user}** has been kicked for **no reason**.")
    else:
        await user.kick(reason=reason)
        await ctx.send(f"**{user}** has been kicked for **{reason}**.")
        await user.kick(reason=reason)
        await ctx.send(f"{user} have been kicked sucessfully")


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
    await user.ban(reason=reason)
    await ctx.send(f"{user} have been bannned sucessfully")


@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f"{user} have been unbanned sucessfully")
        return

    if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned {user.mention}')
        return


@client.command(pass_context=True)
@has_permissions(manage_messages=True)
async def say(ctx, *, message=None):
    if "gay" in message:
        await ctx.send("You are gay!")
    else:
        await ctx.send(f"{message}")
        await ctx.message.delete()



client.run("Ur token")
