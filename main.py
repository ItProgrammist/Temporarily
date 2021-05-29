import conf


import discord
import random
from discord.utils import get
from discord.ext import commands
import img_handler as imhl
import os

# # Настраиваем расширенный доступ Intents
intense = discord.Intents.default()
intense.members = True
# # Создаём подключение бота
# client = discord.Client(intents=intense)


# id_channel = 825340703084118046

# @client.event
# async def on_message(message):
#     # <Message 
#     # id=825337927005110293 
#     # channel=<TextChannel id=822806350886207542 name='флудильня' position=0 nsfw=False news=False category_id=822806350886207539> 
#     # type=<MessageType.default: 0> 
#     # author=<Member id=635376536761139211 name='Ulan' discriminator='9113' bot=False nick=None guild=<Guild id=822806350886207538 name='Bots' shard_id=None chunked=False member_count=29>>
#     # flags=<MessageFlags value=0>>

#     # Проверка на дурака №1 - Отправлятор является самим ботом
#     if message.author == client.user:
#         return
    
#     # Проверка на дурака №2 - Отправлятор является другим ботом
#     if message.author.bot:
#         return

#     # задаём каналы для бота [Канал General]
#     global id_channel
#     if message.channel.id == id_channel:
#         # Изначально, сообщение пустое
#         msg = None
        
#         # Контекс, разбивающийся на два эл-а списка (команду /... и 'само сообщение')
#         ctx = message.content.split(" ", maxsplit = 1) # Максимальное количество

#         # 1. /hello - просто сообщение
#         if message.content == "/hello":
#             msg = f'Hello, {message.author.name}. I am {client.user.name}'

#         # 2. /about_me - сообщение пользователю по его параметрам id/name (если есть ник то добавить "твой ник nick")
#         elif message.content == "/about me":
#             msg = f'Hello, {message.author.name}, your id is: {message.author.id}'

#         # *3. /repeat [] - повторить за пользователем
#         elif ctx[0] == "/repeat":
#             msg = ctx[1]

#         #*4 /get_member
#         elif ctx[0] == "/get_member":
#             name = ctx[1]
#             if message.author.guild.name == 'Bots':
#                 for idx, member in list(enumerate(message.author.guild.members)):
#                     if ctx[1] == member.id or ctx[1] == member.name:
#                         msg = f'Есть такой: {member.name}, {member.id}'
#                         break
            
#                     else:
#                         msg = f'Такого пользователя нет, попробуйте ввести другие параметры.'

#         # *5 /get_members
#         elif ctx[0] == '/get_members':
#             msg = ""
#             if message.author.guild.name == 'Bots':
#                 for idx, member in list(enumerate(message.author.guild.members)):
#                     msg += f'{idx+1}. {member.name} { f"[{member.nick}]" if member.nick else ""} - {member.id}\n'          

#         # *6 /get_channels
#         elif ctx[0] == "/get_channels":
#              msg = ""
#              if message.author.guild.name == 'Bots':
#                 for idx, channel in list(enumerate(message.author.guild.channels)):
#                     msg += f'{idx+1}. {channel.name} - {channel.id}\n'

#         # *7 /goto
#         elif ctx[0] == "/goto":
#             if message.author.guild.name == 'Bots':
#                 for idx, channel in list(enumerate(message.author.guild.channels)):
#                     if ctx[1] == channel.id or ctx[1] == channel.name:
#                         id_channel = ctx[1]
#                         break
#                     else:
#                         msg = f'Ошибка подключения к каналу. Пожалуйста, укажите правильное имя/id канала!'

#         # Отправляем сообщение если оно есть
#         if msg != None:
#             await message.channel.send(msg)





# client.run(conf.bot_token)


bot = commands.Bot(command_prefix= "!", intents=intense)


channel = 825340703084118046

# Просто выводит сообщение hello...
@bot.command(name = "hello") # Декоратор
async def command_hello(ctx, *args): # args = tuple (кортежи)
    message = " ".join(args)
    if ctx.channel.id == 825340703084118046:
        msg = f"Hello to you! You said: '{message}'"
        await ctx.channel.send(msg)

# 2. !about_me - сообщение пользователю по его параметрам id/name (если есть ник то добавить "твой ник nick")
@bot.command(name = "about_me")
async def command_about_me(ctx):
    if ctx.channel.id == 825340703084118046:
        msg = f'Hello, {ctx.author.name}, your id is: {ctx.author.id}'
        await ctx.channel.send(msg)

# *3. !repeat [] - повторить за пользователем
@bot.command(name="repeat")
async def command_repeat(ctx, *args):
    if ctx.channel.id == 825340703084118046:
        message = " ".join(args)
        msg = f'{message}'
        await ctx.channel.send(msg)

#*4 !get_member
@bot.command(name="get_member")
async def command_get_member(ctx, member: discord.Member=None):
    msg = None
    global channel
    if ctx.channel.id == channel:

        if member:
            msg = f'Member {member.name} {"({member.nick})" if member.nick else ""} - {member.id}'

        if msg == None:
            msg = "Error"
        
        await ctx.channel.send(msg)
         

#*5 !get_members
@bot.command(name="get_members")
async def command_ger_members(ctx, *args):
    if ctx.channel.id == 825340703084118046:
        if ctx.author.guild.name == 'Bots':
            msg = ""
            for idx, member in list(enumerate(ctx.author.guild.members)):
                msg += f'{idx+1}. {member.name} { f"[{member.nick}]" if member.nick else ""} - {member.id}\n'
            await ctx.channel.send(msg)

#*6 !get_channels
@bot.command(name="get_channels")
async def command_get_channels(ctx, *args):
    if ctx.channel.id == 825340703084118046:           
        msg = ""
        if ctx.author.guild.name == 'Bots':
            for idx, channel in list(enumerate(ctx.author.guild.channels)):
                msg += f'{idx+1}. {channel.name} - {channel.id}\n'
        await ctx.channel.send(msg)

#*7 !mk
@bot.command(name="mk")
async def command_mk(ctx, f1: discord.Member=None, f2: discord.Member=bot.user):
    global channel
    if ctx.channel.id == channel:
        if f1 and f2:
            # Передаём аватары обработчику
            await imhl.vs_create(f1.avatar_url, f2.avatar_url)
            # Отправляем полученный результат
            await ctx.channel.send(file=discord.File(os.path.join("./img/result.png")))

#*8 !mka
@bot.command(name="mka")
async def command_mka(ctx, f1: discord.Member=None, f2: discord.Member=bot.user):
    global channel
    if ctx.channel.id == channel:
        if f1 and f2:
            # Передаём аватары обработчику
            await imhl.vs_create_animated(f1.avatar_url, f2.avatar_url, f1.name, f2.name)
            # Отправляем полученный результат
            await ctx.channel.send(file=discord.File(os.path.join("./img/result.gif")))

#*9 !join
@bot.command(name = "join")
async def vc_join(ctx):
    msg = ""
    global channel

    voice_channel = ctx.author.voice.channel

    if voice_channel and ctx.channel.id == channel:
        if ctx.voice_client == None:
            msg = f"Подключаюсь к {voice_channel.name}"
            await ctx.channel.send(msg)
            await voice_channel.connect()
        else:
            msg = f"Бот уже подключен к каналу."
            await ctx.channel.send(msg)

#*10 !leave
@bot.command(name = "leave")
async def vc_leave(ctx):
    msg = ""
    global channel

    voice_channel = ctx.author.voice.channel

    if voice_channel and ctx.channel.id == channel:
        if ctx.voice_client != None:
            msg = f"Отключаюсь от {voice_channel.name}"
            await ctx.channel.send(msg)
            await ctx.voice_client.disconnect()
        else:
            msg = f"Бот уже отключился от канала"
            await ctx.channel.send(msg)

#*11 !ost
@bot.command(name = "ost")
async def vc_ost(ctx, *args):
    msg = ""
    global channel

    if ctx.channel.id == channel:

        if "Crysis" in args or "crysis" in args:
            voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
            msg = f"Maximum Armor!"

            await ctx.channel.send(msg)
            await voice_client.play(discord.FFmpegPCMAudio(executable="./sound/ffmpeg.exe", source="./sound/Crysis2.mp3"))
        else:
            voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
            msg = f"MORTAL KOMBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAT!!!!!!!!!!!!!!!"

            await ctx.channel.send(msg)
            await voice_client.play(discord.FFmpegPCMAudio(executable="./sound/ffmpeg.exe", source="./sound/mk.mp3"))
        


#*12 !fight
@bot.command(name = "fight")
async def command_fight(ctx):
    msg = ""
    global channel

    if ctx.channel.id == channel:

        voice_channel = ctx.author.voice.channel
        
        for q in ctx.author.voice.channel.members:
            print(q.name)

        if len(ctx.author.voice.channel.members) >= 2:
            mas_member = ctx.author.voice.channel.members

            idx_member = random.randint(0, len(mas_member)-1)
            f1 = mas_member[idx_member]

            idx_member = random.randint(0, len(mas_member)-1)
            f2 = mas_member[idx_member]


            msg = f'В бой вступают {f1.name} {f"({f1.nick})" if f1.nick else ""} и {f2.name} {f"({f2.nick})" if f2.nick else ""}'


            await imhl.vs_create_animated(f1.avatar_url, f2.avatar_url, f1.name, f2.name)
            # await voice_channel.connect()
            await ctx.channel.send(msg)
            await ctx.channel.send(file=discord.File(os.path.join("./img/result.gif")))
            voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
            await voice_client.play(discord.FFmpegPCMAudio(executable="./sound/ffmpeg.exe", source="./sound/mk.mp3"))

        elif len(ctx.author.voice.channel.members) == 1:

            f1 = ctx.author.voice.channel.members[0]
            f2 = bot.user

            msg = f'В бой вступают {f1.name} {f"({f1.nick})" if f1.nick else ""} и {f2.name}'


            await imhl.vs_create_animated(f1.avatar_url, f2.avatar_url, f1.name, f2.name)
            # await voice_channel.connect()
            await ctx.channel.send(msg)
            await ctx.channel.send(file=discord.File(os.path.join("./img/result.gif")))
            voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
            await voice_client.play(discord.FFmpegPCMAudio(executable="./sound/ffmpeg.exe", source="./sound/mk.mp3"))
    


bot.run(conf.bot_token)