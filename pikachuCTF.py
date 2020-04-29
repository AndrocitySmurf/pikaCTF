import os
from discord.ext import commands
from discord.ext.commands import has_role
from discord.ext.commands import Bot
import asyncio
import random
import discord
import mysql.connector

bot = commands.Bot(command_prefix = 'pika')

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


mydb = mysql.connector.connect(
user = 'AndrewInk',
passwd = 'Inf0rmat10N!',
host = 'localhost',
auth_plugin = 'mysql_native_password'
)
print(mydb)
#MySQL python connector


@bot.event
async def on_ready():
    print('Pika Pika!')
#Prints 'Pika Pika!' when bot is ready to function

@bot.command()
async def pik(ctx):
    await ctx.send('''
List of commands to get you started!
pikascore - See which problems you have or haven't completed
pikaCTF - Rules and guidelines when completing challenges
pikaCTF_1...2 - Visit different challenges and complete them!
    ''')
#Primary help command

@bot.command()
async def score(ctx):
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
1. Get different problems by typing pikaCTF_1..._2...
2. Flag format: pikaCTF{{flag}}
3. Collaboration is allowed
4. Please have embeds enabled to see the challenges
5. The bot will automatically erase your answer if it is correct
6. Questions will automatically expire after 20 seconds of inactivity
7. You can also DM the bot to play as well
    ''')
#Lists beginning instructions and guidelines + personally greets people by username

@bot.command()
async def clear(ctx, amount = 10):
    await ctx.channel.purge(limit = 10)
    await ctx.send('*10 lines succesfully cleared!*')
#Clears last 10 lines and leaves message notifying people + only usable by user with a 'Pikachu' role

@bot.command()
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
#pikaCTF{Chevron}

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
            await bot.process_commands(message)
        else:
            await message.channel.send(f'{random.choice(incorrect_responses)}\nincorrect...')
            await bot.process_commands(message)
        activetest1.remove(message.author.id)
        await bot.process_commands(message)
    else:
        if author in activetest2:
            correct_answer = 'pikaCTF{Chevron}'
            message1 = message.content
            if message1 == correct_answer:
                await message.channel.purge(limit = 2)
                await message.channel.send(f'{random.choice(correct_responses)}\ncorrect!')
                CTF2_solved.append(author)
                await bot.process_commands(message)
            else:
                await message.channel.send(f'{random.choice(incorrect_responses)}\nincorrect...')
                await bot.process_commands(message)
            activetest2.remove(message.author.id)
        else:
            if author in activetest3:
                correct_answer = 'pikaCTF{Pizza_Hut}'
                message1 = message.content
                if message1 == correct_answer:
                    await message.channel.purge(limit = 2)
                    await message.channel.send(f'{random.choice(correct_responses)}\ncorrect!')
                    CTF3_solved.append(author)
                    await bot.process_commands(message)
                else:
                    await message.channel.send(f'{random.choice(incorrect_responses)}\nincorrect...')
                    await bot.process_commands(message)
                activetest3.remove(message.author.id)
            else:
                await bot.process_commands(message)

bot.run('TOKEN')
