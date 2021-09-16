import discord
import random
from discord.ext import commands
import youtube_dl
import os
import praw
import asyncio
import time
client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    print('Little Ultron is ready.')


@client.command()
async def ping(ctx):
    await ctx.send(f'pong!  {round(client.latency * 1000)}ms')

@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    responses = ['Maybe','100%','unlikely','Nope!','No chance','Yes','Absolutly',
    'Yes, right now','0% chance','Are you stupid?','In a long time, Yes',
    'In a long time, No','Is the sky blue?','Are the oceans red?','How did you know?','lolz, no','stop talking to me']

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def loser(ctx):
    await ctx.send(f'your the one on discord loser')

@client.command(aliases=["hi","hello","Hello","sup"])
async def Hi(ctx):
    await ctx.send(f'Go away no one likes you, not even a BOT!!!')

@client.command()
async def commands(ctx):
    await ctx.send('.Hi')
    await ctx.send('.loser')
    await ctx.send('.8ball')
    await ctx.send("```arm\nNSFW\n```")
    await ctx.send('.MEME')
    await ctx.send('.play(youtube url)')
    await ctx.send('.milpic')
    await ctx.send(".shawn")
    await ctx.send('.pup')
    await ctx.send('.MC_server')
    await ctx.send('.coinflip')


@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the '.stop' command")
        return

    channel = ctx.author.voice.channel
    await channel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


reddit = praw.Reddit(client_id='PNm9GZ98VjQlDw',
                     client_secret='6IKViCh4Xbd2203QCt6H9WYgbKs5-A',
                     user_agent='UltronMemeGenerator', check_for_async=False)

@client.command()
async def MEME(ctx):
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)

@client.command()
async def wsp(ctx):
    WSP_submissions = reddit.subreddit('WinStupidPrizes').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in WSP_submissions if not x.stickied)

    await ctx.send(submission.url)

@client.command()
async def Cursed(ctx):
    cursed_submissions = reddit.subreddit('cursedcomments').hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in cursed_submissions if not x.stickied)

    await ctx.send(submission.url)

@client.command(aliases=[f"milpics",])
async def milpic(ctx):
    specops_submissions = reddit.subreddit('SpecOpsArchive',).hot()
    post_to_pick = random.randint(1, 100)
    for i in range(0, post_to_pick):
        submission = next(x for x in specops_submissions if not x.stickied)

    await ctx.send(submission.url)


@client.command()
async def shawn(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("songs\\shawn.mp4"))
    await ctx.send("https://upload.wikimedia.org/wikipedia/commons/thumb/4/48/Gay_Pride_Flag.svg/640px-Gay_Pride_Flag.svg.png")

@client.command()
async def pup(ctx):
    puppic = ['https://drive.google.com/file/d/1uDkYf53u18xrdzJC3CC_g1_WrgefGflY/view?usp=sharing',
             'https://drive.google.com/file/d/1tHUanYQcsPYvAX1OhSWvrUZArvB-jpT6/view?usp=sharing',
             'https://drive.google.com/file/d/1tJ8mlL_jrqJy8NDYk2Xa9Qzdc1d0cx2P/view?usp=sharing']

    await ctx.send(f'{random.choice(puppic)}')

@client.command()
async def lolz(ctx):
    await ctx.send("")


@client.command(pass_context=True)
async def coinflip(ctx):
    variable = [
        "https://i.ebayimg.com/images/g/xtcAAOSwLwBaZigS/s-l400.jpg",
        "https://i.ebayimg.com/images/g/wGEAAOSwYu1crzzn/s-l400.jpg",]

    await ctx.send(f'{random.choice(variable)}')

@client.command(aliases=[f"nsfw"])
async def NSFW(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("songs\\rickroll.mp4"))
    await ctx.send("https://static.wikia.nocookie.net/meme/images/d/db/Rick-astley.png/revision/latest/top-crop/width/360/height/450?cb=20200713010539")

@client.command()
async def test(ctx):
    await ctx.send("")

@client.command()
async def Cringe(ctx):
    await ctx.send("That cringy looser needs to get friends")

@client.command()
async def zane(ctx):
    await ctx.send("Zane is the creator of this bot!")

@client.command()
async def mason(ctx):
    await ctx.send("https://youtu.be/1ehaThDr_bg")

@client.command()
async def backup(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.play(discord.FFmpegPCMAudio("songs\\help.mp4"))


@client.command()
async def face(ctx):
    print("( ͡° ͜ʖ ͡°)")




client.run('ODQ0MTEyODc0NTk0ODkzODc0.YKNrYA.XxSMPEaSTJzh1pd9LsBLKIliFsA')
