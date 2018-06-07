#Anon Bot for Hacking Server
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from random import randint
import time
import datetime
import os

bot = commands.Bot(command_prefix='?A ')
@bot.event
async def on_ready():
    print ("Anon Bot online.")
    await bot.change_presence(game=discord.Game(name='anonymously.')) #Makes it so it says bot is 'playing anonymously.'

@bot.command(pass_context=True)
async def server(ctx):
    embed = discord.Embed(title="This is the info of: {}".format(ctx.message.server.name), description="Found info.", color=0x0000)
    embed.add_field(name="Name.", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Members.", value=len(ctx.message.server.members), inline=True)
    embed.add_field(name="Roles.", value=len(ctx.message.server.roles), inline=True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)
    
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("Users name is {}".format(user.name))
    await bot.say("Highest role is {}".format(user.top_role))
    await bot.say("User's ID is {}".format(user.id))

@bot.command(pass_context=True)
async def info_embed(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Found info.", color=0xff0000)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined at", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s avatar".format(user.name), description="Just drag to save.", color=0xff0000)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def Guy_Fawkes(ctx):
    await bot.say("Inserting picture of Guy Fawkes Mask.")
    await bot.say("https://cdn.discordapp.com/attachments/437071201903312906/437090276322836480/Anonymous_mask.jpg")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Pinged.")

@bot.command(pass_context=True)
async def playing(ctx):
    await bot.say("https://www.pandora.com/web-version/1.10.0/images/eq-white-playing.gif")

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def kick(ctx, user: discord.Member):
    await bot.say("Kicking {}.".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
async def random(ctx, random1, random2):
    random1 = int(random1)
    random2 = int(random2)
    await bot.say(randint(random1, random2))

@bot.command(pass_context=True)
async def RNG(ctx):
    rng = randint(0, 10000000000)
    await bot.say(rng)

@bot.command(pass_context=True)
async def subtract(number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    await bot.say(number1 - number2)

@bot.command(pass_context=True)
async def add(number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    await bot.say(number1 + number2)

@bot.command(pass_context=True)
async def math(ctx, number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    await bot.say(number1 + number2)
    await bot.say(number1 - number2)
    await bot.say(number1 * number2)
    await bot.say(number1 % number2)

@bot.command(pass_context=True)
async def multiply(number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    await bot.say(number1 * number2)

@bot.command(pass_context=True)
async def exponent(number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    await bot.say(number1 ** number2)

@bot.event
async def on_member_join(member):
    server = member.server
    role = discord.utils.get(member.server.roles, name='Online')
    fmt = "Welcome {0.mention} to {1.name}, please welcome them."
    await bot.add_roles(member, role)
    await bot.send_message(server, fmt.format(member, server))
    
@bot.command(pass_context=True)
async def purge(ctx, number):
    number = int(number)
    if number > 99 or number < 1:
        await bot.say("Only possible to purge greater than one and less than ninety-nine messages.")
    else:
        messages = []
        channel = ctx.message.channel
        async for x in bot.logs_from((channel), limit = number + 1):
            messages.append(x)
        await bot.delete_messages(messages)
        await bot.say("Purged.")

@bot.command(pass_context=True)
async def eightball(ctx):
    saying = randint(1, 8)
    if saying == 1:
        await bot.say("`It is decidedly so.`")
    elif saying == 2:
        await bot.say("`Concentrate and ask again.`")
    elif saying == 3:
        await bot.say("`It is not.`")
    elif saying == 4:
        await bot.say("`It is certain.`")
    elif saying == 5:
        await bot.say("`Reply hazy, ask again later.`")
    elif saying == 6:
        await bot.say("`Better not tell you now.`")
    elif saying == 7:
        await bot.say("`As I see it, yes.")
    else:
        await bot.say("`As I see it, no.")

@bot.command(pass_context=True)
async def dm(ctx, user: discord.Member, *, message: str):
    await bot.send_message(user, message)
    await bot.say("DM'd.")

@bot.command(pass_context=True)
async def diceroll(ctx):
    die_roll = randint(1, 6)
    await bot.say(die_roll)

@bot.event
async def on_message_delete(message, member):
    await bot.send_message(message + ' Was deleted by: ' + member)

@bot.event
async def on_member_remove(member):
    await bot.send_message(member, "Farewell, please enjoy the rest of your time on Earth. We hope to see you again soon.")
                           
bot.run(os.environ['BOT_TOKEN'])
