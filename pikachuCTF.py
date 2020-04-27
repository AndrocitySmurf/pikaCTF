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

mydb = mysql.connector.connect(
user = "AndrewInk",
passwd = "Inf0rmat10N!",
host = "localhost",
auth_plugin = "mysql_native_password"
)

print(mydb)

@bot.event
async def on_ready():
    print('Pika Pika!')

@bot.command()
async def pik(ctx):
    await ctx.send('''
List of commands to get you started!
pikascore - See which problems you have or haven't completed
pikaCTF - Rules and guidelines when completing challenges
pikaCTF_1...2 - Visit different challenges and complete them!
    ''')
#Starting help command that shows the user usable commands
#
# @bot.command()
# async def test1(ctx):
#     username = ctx.message.author.name
#     print('Working...')
#     completedproblems.CTFtest_solved = CTFtest
#     CTFtest.append(username)

@bot.command()
async def score(ctx):
    username = ctx.message.author.name
    if username in CTF1_solved:
        status1 = 'Solved'
    else:
        status1 = 'Unsolved'
    if username in CTF2_solved:
        status2 = 'Solved'
    else:
        status2 = 'Unsolved'
    if username in CTF3_solved:
        status3 = 'Solved'
    else:
        status3 = 'Unsolved'
    if username in CTF4_solved:
        status4 = 'Solved'
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
async def CTF_1(ctx):
    username = ctx.message.author.name
    if username not in CTF1_solved:
        retStr = str("""```fix\nhttps://bit.ly/2xOgLtb```""")
        embed = discord.Embed(title="yO4 cAn'T d0 tHiS 0n3!")
        embed.add_field(name="N0 speci@l châractèrs\nUse_underscore_for_spaces\nWhere was this photo taken? (Google Maps official name):",value=retStr)
        await ctx.send(embed=embed)
        await ctx.send('Input flag:')
        correct_answer = 'pikaCTF{Pokemon_Center_Mega_Tokyo}'
        def check(message : discord.Message) -> bool:
            return message.author == ctx.author and message.content == correct_answer
        try:
            message = await bot.wait_for('message', timeout = 20, check = check)
        except asyncio.TimeoutError:
            await ctx.send(f'{random.choice(incorrect_responses)}\nincorrect...')
        else:
            await ctx.channel.purge(limit = 2)
            await ctx.send(f'{random.choice(correct_responses)}\ncorrect!')
            CTF1_solved.append(username)
    else:
        await ctx.send('Challenge already completed!')
        print(f'{username} has tried to turn in challenge 1 more than once!')
#pikaCTF{Pokemon_Center_Mega_Tokyo}

@bot.command()
async def CTF_2(ctx):
    username = ctx.message.author.name
    if username not in CTF2_solved:
        retStr = str("""```fix\nhttps://bit.ly/2yF9xHO```""")
        embed = discord.Embed(title="st3Gos4rUas")
        embed.add_field(name="What company runs the facility circled?:",value=retStr)
        await ctx.send(embed=embed)
        await ctx.send('Input flag:')
        correct_answer = 'pikaCTF{Chevron}'
        def check(message : discord.Message) -> bool:
            return message.author == ctx.author and message.content == correct_answer
        try:
            message = await bot.wait_for('message', timeout = 20, check = check)
        except asyncio.TimeoutError:
            await ctx.send(f'{random.choice(incorrect_responses)}\nincorrect...')
        else:
            await ctx.channel.purge(limit = 2)
            await ctx.send(f'{random.choice(correct_responses)}\ncorrect!')
            CTF2_solved.append(username)
    else:
        await ctx.send('Challenge already completed!')
        print(f'{username} has tried to turn in challenge 2 more than once!')
#pikaCTF{P1kac5u_is_c001!}

@bot.command()
async def CTF_3(ctx):
    username = ctx.message.author.name
    if username not in CTF3_solved:
        retStr = str("""```fix\nAtgksprk_nd_iths_rkxeitl_12345678```""")
        embed = discord.Embed(title="3reN3G1v")
        embed.add_field(name="N0 speci@l châractèrs\nUse_underscore_for_spaces\nFrom what resturaunt was this photo taken? (name only):",value=retStr)
        await ctx.send(embed=embed)
        await ctx.send('Input flag:')
        correct_answer = 'pikaCTF{Pizza_Hut}'
        exception_answer = 'pikaCTF{Abou_Shakra}'
        def check(message : discord.Message) -> bool:
            return message.author == ctx.author and message.content == correct_answer
        try:
            message = await bot.wait_for('message', timeout = 20, check = check)
        except:
            await ctx.send(f'{random.choice(incorrect_responses)}\nincorrect...')
        # except asyncio.TimeoutError:
        #     await ctx.send(f'{random.choice(incorrect_responses)}\nout of time')
        else:
                await ctx.channel.purge(limit = 2)
                await ctx.send(f'{random.choice(correct_responses)}\ncorrect!')
                CTF3_solved.append(username)
    else:
        await ctx.send('Challenge already completed!')
        print(f'{username} has tried to turn in challenge 3 more than once!')
#pikaCTF{Vigenere_is_inch_resting_12345678}

#         def check(message : discord.Message) -> bool:
#             return message.author == ctx.author and message.content == correct_answer
#
# await ctx.send('''
# Hmm, Abou Shakra, WAIT A MINUTE...
# You didn\'t happen to use Google Reverse Image Search now would you?
# Still incorrect however
# Very close though... or maybe I\'m lying?
# ''' )

@bot.command()
async def CTF_4(ctx):
    username = ctx.message.author.name
    if username not in CTF4_solved:
        retStr = str("""```fix\n10111110 01001110 10101110 10000010 11001110 10011110 01101110 10010110 11111010 11001100 00110110 00101110 01001110 10001100 10101110 10001110 11001110 11111010 10101110 00010110 11000110 10000110 11010110 10001100 00001110 11011110 01100010 00101010 11000010 10000110 11010110 10010110 00001110```""")
        embed = discord.Embed(title="b1n ary no w0rk?")
        embed.add_field(name="decode:",value=retStr)
        await ctx.send(embed=embed)
        await ctx.send('Input flag:')
        correct_answer = 'pikaCTF{p1kachu_squ1rtl3_ivysAur}'
        def check(message : discord.Message) -> bool:
            return message.author == ctx.author and message.content == correct_answer
        try:
            message = await bot.wait_for('message', timeout = 20, check = check)
        except asyncio.TimeoutError:
            await ctx.send(f'{random.choice(incorrect_responses)}\nincorrect...')
        else:
            await ctx.channel.purge(limit = 2)
            await ctx.send(f'{random.choice(correct_responses)}\ncorrect!')
            CTF4_solved.append(username)
    else:
        await ctx.send('Challenge already completed!')
        print(f'{username} has tried to turn in challenge 3 more than once!')
#pikaCTF{p1kachu_squ1rtl3_ivysAur}

@bot.command()
async def CTF_5(ctx):
    username = ctx.message.author.name
    if username not in CTF5_solved:
        retStr = str("""```fix\nhttps://bit.ly/3elpDGP```""")
        embed = discord.Embed(title="EzPz.txt")
        embed.add_field(name="decode:",value=retStr)
        await ctx.send(embed=embed)
        await ctx.send('Input flag:')
        correct_answer = 'pikaCTF{txt_d0cum3nts_tu_h4bles19302}'
        def check(message : discord.Message) -> bool:
            return message.author == ctx.author and message.content == correct_answer
        try:
            message = await bot.wait_for('message', timeout = 20, check = check)
        except asyncio.TimeoutError:
            await ctx.send(f'{random.choice(incorrect_responses)}\nincorrect...')
        else:
            await ctx.channel.purge(limit = 2)
            await ctx.send(f'{random.choice(correct_responses)}\ncorrect!')
            CTF5_solved.append(username)
    else:
        await ctx.send('Challenge already completed!')
        print(f'{username} has tried to turn in challenge 4 more than once!')
#pikaCTF{txt_d0cum3nts_tu_h4bles19302}

@bot.command()
async def CTF_test2(ctx):
    activetest2 = []
    correct_answer = '4'
    activetest2.append(ctx.author.id)
    await ctx.send('Input:')
    @bot.event()
    async def on_message(ctx):
        if ctx.author.id in activetest2:
            activetest2.remove(ctx.author.id)
            ctx.message = message
            ctx.author.id = author
            if message == correct_answer and author not in activetest2:
                await ctx.send('correct')
            else:
                await ctx.send('incorrect')
        else:
            await ctx.send('already completed')

# @bot.command()
# async def CTF_text(ctx):
#     await ctx.send('put answer here:')
#     correct_answer = 'testanswer'
#     eliftest = 'testelif'
#     def check (message : discord.Message) -> bool:
#         if correct_answer == message.content:
#             await ctx.send('test correct')
#         elif message.content == eliftest:
#             await ctx.send('test elif')
#         else:
#             await ctx.send('test else')

@bot.command()
@has_role('Pikachu')
async def clear(ctx, amount = 10):
    await ctx.channel.purge(limit = 10)
    await ctx.send('10 lines succesfully cleared!')
#Clears last 10 lines and leaves message notifying people + only usable by user with a "Pikachu" role

bot.run('Njk4NDI1NTQ5OTE1MTYwNjA2.XpN1dQ.pqbY3PxOhe-bNWBddHY6aLlaSM8')
