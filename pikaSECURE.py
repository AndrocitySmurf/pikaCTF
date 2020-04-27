import os
from discord.ext import commands
from discord.ext.commands import has_role
from discord.ext.commands import Bot
from discord.utils import get
import discord
import asyncio

bot = commands.Bot(command_prefix = 'pika')

@bot.event
async def on_ready():
    print('Pika Pika!')

@bot.command()
@has_role('Easter Eggs')
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = 5)
    await ctx.send(f'5 lines cleared!')

@bot.command()
async def kick(ctx, member : discord.Member, *, reason = None):
    if ctx.message.author.id == 321439238497239040 or ctx.message.author.id == 562809498700349442:
        await member.kick(reason = reason)
    else:
        await ctx.send('*User verification failed*')

@bot.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    if ctx.message.author.id == 321439238497239040 or ctx.message.author.id == 562809498700349442:
        await member.ban(reason = reason)
    else:
        await ctx.send('*User verification failed*')

@bot.command()
async def mute(ctx, member : discord.Member):
    if ctx.message.author.id == 321439238497239040 or ctx.message.author.id == 562809498700349442:
        Mutedpre = discord.Member
        role = discord.utils.get(member.guild.roles, name="Muted")
        await member.add_roles(Mutedpre, role)
    else:
        await ctx.send('*User verification failed*')


bot.run('NzAyNDEyOTEyNjcyNzY4MDYx.Xp_rPQ.ECroKGJQTTQGCaLVLxmOzm2KfTI')
