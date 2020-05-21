#Test-bot py Piiixxxel

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import praw
import random
import time
import logging

client = commands.Bot(command_prefix="!")

reddit = praw.Reddit(client_id="nmNjm5-kOyATOA", client_secret="n3Sf8xOmZIJka9-bvjtcwQUWPsw", password="IcPMLmJUK3CbXONRk2dv", user_agent="test by /u/gamedeal_bot", username="gamedeal_bot")
subreddit = reddit.subreddit("gamedeals")
reddit.read_only = True

banned_words = []

msg = None

tts_state = False

playlist = []
current = None
player = None


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.command(pass_context=True, name="join", description="Join the voice channel the user is currently in")
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)


@client.command(pass_context=True, name="leave", description="Make the bot leave from the current voice chat it is in")
async def leave(ctx):
    voice_client = client.voice_client_in(ctx.message.guild)
    await voice_client.disconnect()


@client.command(pass_context=True, name="play", description="Starts the queue")
async def play(ctx, url):
    global player
    
    playlist.append(url)
    voice_client = client.voice_client_in(ctx.message.guild)
    player = await voice_client.create_ytdl_player(url)
    #playlist.remove(playlist[0])
    player.volume = 0.1
    player.start()

@client.command(pass_context=True, name="addsong", description="Add song to the current queue")
async def addsong(ctx, url):
    playlist.append(url)
    print(playlist)
    

@client.command(pass_context=True, name="stop", description="Stops the player")
async def stop(ctx):
    player.stop()


@client.command(pass_context=True, name="pause", description="Pauses the player")
async def pause(ctx):
    player.pause()


@client.command(pass_context=True, name="resume", description="Resumes the player's current song")
async def resume(ctx):
    player.resume()


@client.command(pass_context=True, name="vol", description="Change the volume of the player")
async def vol(ctx, a: int):
    player.volume = a / 100
    print(player.volume)


@client.command(pass_context=True, name="deals", description="Outputs all the games from the subreddit 'GameDeals' with 'free' or '100' tags on them")
async def deals(ctx):
    deals = []
    embed = discord.Embed(title=":gift: Latest free games in r/GameDealsFree :gift:", description="Here are the latest free games from r/GameDeals ", color=0x426bf4)
    for submission in reddit.subreddit("gamedealsfree").hot(limit=10):
        if (not "Suggestion thread - " in submission.title): 
            if not "indiegala" in submission.title.lower():    
                embed.add_field(name=submission.title, value=submission.url, inline=False)
        
    await ctx.send(embed=embed)
    
    
@client.command(pass_context=True, name="ping", description="Play ping pong with the bot")
async def ping(ctx):
    await ctx.send(":ping_pong: Pong!! :ping_pong:")


@client.command(pass_context=True, name="info", description="Outputs the mentioned player's name, ID, status and joining date")
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I found", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Joined at", value=user.joined_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)
    


@client.command(pass_context=True, name="serverinfo", description="Outputs the server's author, name, ID, roles and members")
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.guild.name), description="Here's what I found.", color=0x00ff00)
    embed.set_author(name="Owner: Pixel")
    embed.add_field(name="Name", value=ctx.message.guild.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.guild.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.guild.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.guild.members), inline=True)
    embed.set_thumbnail(url=ctx.message.guild.icon_url)
    await ctx.send(embed=embed)


@client.command(pass_context=True, name="meme", description="Gives a random dankmeme from the subreddit r/dankmemes")
async def meme(ctx):
    await ctx.send(reddit.subreddit("dankmemes").random().url)

@client.command(pass_context=True, name="twice")
async def twice(ctx):
    await ctx.send(reddit.subreddit("twicemedia").random().url)

@client.command(signature="rpost", usage="xd", description="asdasd")
async def rpost(ctx, a):
    await ctx.send(reddit.subreddit(a).random().url)

    

@client.command(pass_context=True, name="num", description="Gives you a random number between the given range")
async def num(ctx, a: int, b: int):
    r_number = random.randint(a, b)
    await ctx.send("Your random number is: " + str(r_number))

@client.command(pass_context=True, name="repeat", description="Repeats the given message")
async def repeat(ctx, a: int, *b: str):
    if a <= 50:
        for i in range(0, a):
            await ctx.send(" ".join(b))
        time.sleep(1)
    else:
        await ctx.send("The number you have entered is too high for me to handle.")

@client.command(pass_context=True, name="rate", description="Rates out of 10")
async def rate(ctx, name: str, surname: str):
    chars = []
    name_chars = []
    surname_chars = []
    points = 0
    vowels = None
    cons = None

    names = name + surname

    for char in list(names):
        chars.append(char.lower())

    for char in list(chars):
        if char in ("a", "e", "i", "o", "u", "y", "ä", "å", "ö"):
            points = points + 0.5
        if char in ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"):
            points = points + 0.75

    if len(name) <= 4:
        points = points + 5
    elif len(name) > 4 or len(name) <= 6:
        points = points + 1
    elif len(name) > 6:
        points = points - 1

    if len(surname) <= 6:
        points = points - 1 
    elif len(surname) > 6:
        points = points + 2
    
    points = round(points)
    
    if points > 10.0:
        points = 10.0
    elif points < 0:
        points = 0.0
    
    if name == "Juho" and surname == "Vähäkangas":
        points = 4

    if name.lower() == "western" or surname.lower() == "western":
        points = 0

    await ctx.send("I'd say " + str(points) + "/10")

'''
@asyncio.coroutine
def playsong(ctx, song):
    voice_client = client.voice_client_in(ctx.message.server)
    player = await voice_client.create_ytdl_player(url, after=lambda: nextsong(ctx))
    playlist.remove(playlist[0])
    player.volume = 0.35
    player.start()

def nextsong(ctx):
    player.stop()
    playsong()
'''

if __name__ == "__main__":
    import config
    client.run(config.token)
