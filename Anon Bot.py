#Anon Bot for Hacking Server
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from random import randint
import time
import datetime

startup_extensions = []

bot = commands.Bot(command_prefix='?A ')
@bot.event
async def on_ready():
    print ("Anon Bot online.")
    await bot.change_presence(game=discord.Game(name='anonymously.')) #Makes it so it says bot is 'playing anonymously.'

def raw_input(x):
    input(x)

@bot.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))

@bot.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    """Get's a user's info."""
    await bot.say("Users name is {}".format(user.name))
    await bot.say("Highest role is {}".format(user.top_role))
    await bot.say("User's ID is {}".format(user.id))

@bot.command(pass_context=True)
async def info_embed(ctx, user: discord.Member):
    """Embeds a user's info."""
    embed = discord.Embed(title="{}'s info".format(user.name), description="Found info.", color=0xff0000)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined at", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_cotext=True)
async def avatar(user: discord.Member):
    """Get's a user's avatar."""
    embed = discord.Embed(title="{}'s avatar".format(user.name), description="Just drag to save.", color=0xff0000)
    embed.add_field(name="Avatar", value=user.avatar_image)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def Guy_Fawkes(ctx):
    """Inserts a Guy Fawkes mask."""
    await bot.say("Inserting picture of Guy Fawkes Mask.")
    await bot.say("https://cdn.discordapp.com/attachments/437071201903312906/437090276322836480/Anonymous_mask.jpg")

@bot.command(pass_context=True)
async def ping(ctx):
    """Pings the bot."""
    await bot.say("Pinged.")

@bot.command(pass_context=True)
async def playing(ctx):
    """Shows the Pandora playing gif."""
    await bot.say("https://www.pandora.com/web-version/1.10.0/images/eq-white-playing.gif")

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def kick(ctx, user: discord.Member):
    """Kicks a user."""
    await bot.say("Kicking {}.".format(user.name))
    await bot.kick(user)

@bot.event
async def on_message_delete(message):
    fmt = "{0.author.name} has deleted the message:\n{0.content}"
    await bot.send_message(message.channel(bot.get_channel('447205976785944576'), fmt.format(message))

@bot.command(pass_context=True)
async def server_info(ctx):
    embed = discord.Embed(name="{}'s info.".format(ctx.message.server.name), description="The server info.", color=0xff0000)
    embed.set_author(name="Bot and server by Prox")
    embed.add_field(name="Server name", value=ctx.message.server, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def google_image(ctx, search):
    """Searches Google for an image."""
    await bot.say("https://www.google.com/search?tbm=isch&q=%s" % search)

@bot.command(pass_context=True)
async def google_term(ctx, term):
    """Searches Google for a term."""
    await bot.say("https://www.google.com/search?q=%s&oq=thing&aqs=chrome.0.69i59j69i57j69i61l3j0.653j0j7&sourceid=chrome&ie=UTF-8" % term)

@bot.command(pass_context=True)
async def guess(ctx):
    """Guessing game. In debugging phase."""
    await bot.say("Guess a number between one and ten.")
    def guess_check(m):
        return m.content.isdigit()

    guess = await bot.wait_for_message(timeout=5.0, author=ctx.message.author, check=guess_check)
    answer = randint(1, 10)
    if guess is None:
        fmt = "Took too long, number was {}."
        await bot.send_message(ctx.message.channel, fmt.format(answer))
        return
    elif int(guess.content) == answer:
        await bot.send_message(ctx.message.channel, "You're correct.")
    else:
        await bot.send_message(ctx.message.channel, "Number was: {}".format(answer))

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def ban(ctx, user: discord.Member):
    """Bans a user."""
    await bot.say("Banning {}.".format(user.name))
    await bot.ban(user)

@bot.command(pass_context=True)
async def heil(ctx): #Yes, a command solely to post Hitler stuff. To hell with you.
    """Posts a random Hitler image or meme."""
    heil_random = randint(1, 10)
    if heil_random == 1:
        await bot.say("https://cdn.discordapp.com/attachments/437180422192103425/438027992153718794/image.png")
    elif heil_random == 2:
        await bot.say("https://i.imgflip.com/1ujlm6.jpg")
    elif heil_random == 3:
        await bot.say("https://i.pinimg.com/originals/29/57/30/29573088580908d18fb868ec33414cf1.jpg")
    elif heil_random == 4:
        await bot.say("https://cdn.discordapp.com/attachments/437973953546289172/447077207966482447/image.png")
    elif heil_random == 5:
        await bot.say("https://www.historyguy.com/Hitler.jpg")
    elif heil_random == 6:
        await bot.say("https://i.ndtvimg.com/i/2016-10/adolf-hitler_240x180_61476716835.jpg")
    elif heil_random == 7:
        await bot.say("https://c8.alamy.com/comp/BPW39F/adolf-hitler-nazi-leader-01-may-1944-BPW39F.jpg")
    elif heil_random == 8:
        await bot.say("https://vignette.wikia.nocookie.net/hitlerparody/images/4/4e/Real_Adolf_Hitler.jpeg/revision/latest?cb=20161203175404")
    elif heil_random == 9:
        await bot.say("http://www.abc.net.au/news/image/1063612-3x4-700x933.jpg")
    else:
        await bot.say("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Hitler_portrait_crop.jpg/220px-Hitler_portrait_crop.jpg")

@bot.command(pass_context=True)
async def dice_roll():
    """Rolls a die."""
    random_number = randint(1, 6)
    await bot.say("Rolling die:")
    await bot.say(random_number)

@bot.event
async def on_member_join(member):
    server = member.server
    role = discord.utils.get(member.server.roles, name='Online')
    fmt = "Welcome {0.mention} to {1.name}, please welcome them."
    await bot.add_roles(member, role)
    await bot.send_message(message.channel(bot.get_channel('448142180335222816')) member, "Welcome to `Cyber Security Reverse-Engineering`, please enjoy your stay.")
    await bot.send_message(server, fmt.format(member, server))
    await bot.send_message(message.channel(bot.get_channel('447205976785944576'), 'User ' + member ' has joined.')

@bot.event
async def on_member_remove(member):
    await bot.send_message(member, "Farewell, please enjoy the rest of your time on Earth. We hope to see you again soon.")
    await bot.send_message(message.channel(bot.get_channel('447205976785944576'), 'User ' + member ' has left.')

@bot.command(pass_context=True)
async def eightball(ctx):
    """Ask eightball a question."""
    random_response = randint(1, 8) #Gets a random number through one and eight.
    if random_response == 1:
        await bot.say("It is certain.")
    elif random_response == 2:
        await bot.say("It's decidely so.")
    elif random_response == 3:
        await bot.say("Ask again later.")
    elif random_response == 4:
        await bot.say("Not certain.")
    elif random_response == 5:
        await bot.say("It is not.")
    elif random_response == 6:
        await bot.say("It's decidely not.")
    elif random_response == 7:
        await bot.say("Concentrate and ask again.")
    else:
        await bot.say("Better not tell you now.")

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def purge(ctx, amount=100):
    """Purges chat of messages."""
    channel = ctx.message.channel
    messages = []
    async for message in bot.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await bot.delete_messages(messages)
    await bot.say("Purged.")

@bot.command(pass_context=True)
@commands.has_role("Admin")
async def mute(ctx, user: discord.Member):
    """Mutes an user, in debugging phase."""
    role = discord.utils.get(member.server.roles, name='Muted')
    await bot.say("Muting {}.".format(user.name))
    await bot.add_roles(user, role)
    await bot.say("Muted.")

@bot.command(pass_context=True)
async def dm(ctx, member : discord.Member, *, content: str):
    """DMs an user."""
    if member == "@everyone":
        for server_member in ctx.message.server.members:
            await bot.send_message(server_member, content)
    else:
        await bot.send_message(member, content)
    time.sleep(1)
    await bot.say("Person has been DM'd.")

@bot.command(pass_context=True)
async def timenow(ctx):
    """Gets the bot's current time."""
    time = datetime.datetime.now()
    await bot.say(time)

@bot.command(pass_context=True)
async def rng(ctx):
    """Get a number between 0 and 1000000"""
    rn = randint(0, 1000000)
    await bot.say(rn)

@bot.command(pass_context=True)
async def Anonymous(ctx):
    """Anonymous meme."""
    await bot.say("We Are Anonymous")
    await bot.say("We Are Boring")
    await bot.say("We Do Not Have Fun")
    await bot.say("We Do Not Enjoy")

@bot.command(pass_context=True)
async def discrim(ctx, discrim):
    """Gets all users with a discrim, in testing and debugging."""
    p = discrim
    p = bot.get_all_members()
    found_members = filter(lambda m: m.discriminator[0], p)
    await bot.say(found_members)

@bot.command(pass_context=True)
async def invite(ctx):
    """Gets Anon's invite link."""
    await bot.say("This is my invite link.")
    await bot.say("https://discordapp.com/oauth2/authorize?&client_id=436874723725410305&scope=bot&permissions=470019135")

bot.run("NDM2ODc0NzIzNzI1NDEwMzA1.Dbw66g.EwI9rSV1XVBCOfS5we00xGj5qo8")