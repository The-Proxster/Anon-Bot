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

@bot.command(pass_cotext=True)
async def avatar(user: discord.Member):
    embed = discord.Embed(title="{}'s avatar".format(user.name), description="Just drag to save.", color=0xff0000)
    embed.add_field(name="Avatar", value=user.avatar_image)
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

@bot.event
async def on_member_join(member):
    server = member.server
    role = discord.utils.get(member.server.roles, name='Online')
    fmt = "Welcome {0.mention} to {1.name}, please welcome them."
    await bot.add_roles(member, role)
    await bot.send_message(server, fmt.format(member, server))

@bot.event
async def on_member_remove(member):
    await bot.send_message(member, "Farewell, please enjoy the rest of your time on Earth. We hope to see you again soon.")

@bot.event
async def on_message_delete(message):
    fmt = "{0.author.name} has deleted the message:\n{0.content}"
    await bot.send_message(message.channel(bot.get_channel('447205976785944576'), fmt.format(message))
                           
bot.run(os.environ['BOT_TOKEN'])
