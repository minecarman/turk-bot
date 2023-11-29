import io
import discord
from discord.ext import commands
import random
import jokeapi
# -*- coding: utf-8 -*-
def random_kufur():
    with io.open("kufur.txt", "r", encoding="utf8") as file:
        kufurler = file.readlines()
        return(random.choice(kufurler))

def kufurlist():
    with io.open("kufur.txt", "r", encoding="utf8") as file:
        kufurler = file.readlines()
        return kufurler


def read_token():
    with open("token.txt", "r") as file:
        return (file.readlines())[0].strip()


intents = discord.Intents.all()
intents.message_content = True

token = read_token()
client = commands.Bot(command_prefix = '!',intents=intents)

@client.event
async def on_ready():
    print("hazır")


@client.event
async def on_message(message):

    if message.content.startswith('mal bot'): # Mal bot
        await message.channel.send("ananı sikerim "+ random_kufur())

    if message.content.startswith('oç bot'): # Mal bot
        await message.channel.send("ananı sikerim "+ random_kufur())

    if message.content.startswith('gay bot'): # gay bot
        await message.channel.send("ananı sikerim "+ random_kufur())

    if message.content.startswith('iyi bot'): # İyi bot
        await message.channel.send("EYW")

    if message.content.startswith('nice greek bot'):
        await message.channel.send("BEN TÜRKÜZ DOĞRUYUZ ANANI SİKERİZ AQ YUNAN DÖLÜ")

    if message.content.startswith('xd'):
        await message.channel.send("çok komik mk "+ random_kufur())

    if message.content.startswith('haha'):
        await message.channel.send("çok komik mk malı "+ random_kufur())

    if message.content.startswith('31'):
        await message.channel.send("çok komik mk malı "+ random_kufur())

    if message.content.startswith('bot'):
        await message.channel.send("????????????")

    if message.content.startswith('zekeriya'):
        await message.channel.send("ZEKERIYA MI BURDA OFFF SIKIM KALKTI")

    if message.content.startswith('turkey is not european'):
        await message.channel.send("I AM MORE WHITE THAN YOU YOU LOOK GYPSY BLÖNDE HAIR İ HAVE")

    if message.content.startswith('baklava is greek'):
        await message.channel.send("anayınki amıki türk şimdi sen bi de cacıki dersin piçki ", random_kufur())

    if message.content.startswith('cacıki'):
        await message.channel.send("olum dassak mı geciyon döverim seni"+ random_kufur())

    await client.process_commands(message)


@client.command() # Plays rock paper scissors.
async def taskagitmakas(ctx, user_choice: str):
    computer_choice = random.choice(["taş", "kağıt", "makas"])
    await ctx.send(computer_choice + " seçtim")
    if user_choice == computer_choice:
        await ctx.send("berabere")
    elif user_choice == "taş" and computer_choice == "makas":
        await ctx.send("hay amk kaybettim!")
    elif user_choice == "kağıt" and computer_choice == "taş":
        await ctx.send("nası kaybediyom lan hile kapat oç!")
    elif user_choice == "makas" and computer_choice == "kağıt":
        await ctx.send("sanalda kaybettim ama irl ananı sikiyom!")
    else:
        await ctx.send("zaa mal kaybettin")


@client.command()
async def saka(ctx):
    j = await jokeapi.Jokes()
    joke = await j.get_joke()
    msg = ""
    if joke["type"] == "single":
        msg = joke["joke"]
    else:
        msg = joke["setup"]
        msg += f"||{joke['delivery']}||"
    await ctx.send(msg)




@client.command() # Sends random integral formula
async def integral(ctx):
    integrals = ["∫ 1 dx = x + C", "∫ a dx = ax+ C", "∫ sin x dx = – cos x + C", "∫ cos x dx = sin x + C", "∫ sec^2x dx = tan x + C", "∫ csc^2x dx = -cot x + C", "∫ e^x dx = e^x + C", "∫ 1/x dx = ln|x| + C"]
    await ctx.send(random.choice(integrals))

@client.event # Welcomes when someone joins.
async def on_member_join(member):
    channel = client.get_channel(1179054712813785118)
    await channel.send("NABER LEN " + random_kufur() + member.mention)


@client.event # Goodbye
async def on_member_remove(member):
    channel = client.get_channel(1179054712813785118)
    await channel.send("KENDINE IYI BAK ADAMIM " + member.mention)


@client.command() # pupping
async def pup(ctx):
    await ctx.send("sana da pup adamım")


@client.command() # Sends random number
async def rastgele(ctx, minn : int, maxn : int):
    await ctx.send(random.randrange(minn, maxn+1))


@client.command() # Calculates the numbers given.
async def hesapla(ctx, sayi1: float, islem: str, sayi2: float):
    answer = 0
    if islem == "+":
        answer = sayi1 + sayi2
    elif islem == "-":
        answer = sayi1 - sayi2
    elif islem == "/":
        answer = sayi1 / sayi2
    elif islem == "*":
        answer = sayi1 * sayi2
    else:
        answer = "ne bileyim amk"

    await ctx.send(answer)

    if answer == 31 or answer == 69:
        await ctx.send("ohhhh çok severim ohhhhhh")


@client.command() # Sends random turkish image.
async def turk(ctx):
    images = ["resim\T1.png", "resim\T2.png", "resim\T3.png", "resim\T4.png", "resim\T5.png", "resim\T6.png", "resim\T7.png", "resim\T8.png", "resim\T9.png", "resim\T10.jpg", "resim\T11.jpg", "resim\T12.jpg", "resim\T13.jpg"]
    await ctx.send(file=discord.File(random.choice(images)))


@client.command() # Sends random turkish image.
async def kurt(ctx):
    await ctx.send(file=discord.File('resim\K1.jpeg'))


@client.command(pass_context = True)
async def sesgelpic(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("kardeşim seste değilsin amk")


@client.command(pass_context = True)
async def siktirgit(ctx):
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("üzdün bro...")
    else:
        await ctx.send("seste değilim AMK")


@client.command() # Command list
async def yardim(ctx):
    await ctx.send("!turk   Rastgele Türk resmi gönderir\n!kurt   Kürt resmi gönderir\n!hesapla sayi islem sayi\n!taskagitmakas   Taş kağıt makas oynar\n!saka   Şaka yapar\n!rastgele min max   Aralıktan rastgele sayı seçer\n!sesgelpic   Botu sese ekler\n!siktirgit   Botu sesten çıkarır\n!integral   Integral formülü gönderir")


client.run(token)