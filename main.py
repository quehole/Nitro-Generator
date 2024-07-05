from discord.ext.commands import BucketType, cooldown, Bot, CommandOnCooldown
from discord import Member, Embed, Intents
import discord
import random
import string
import os

# Define the required intents
intents = Intents.default()
intents.members = True  # If you need member-related events, such as on_member_join
intents.message_content = True  # To access message content

token = ""  # Replace with your actual bot token
admins = "794145307843624980"  # Put your ID here
prefix = "$"  # Prefix
nitro_timeout = 100  # Nitro timeout
welcome = 1219289058786672651  # Put welcome channel ID here
bots_channel = 1239970342877925377  # Put bot channel ID here
drop_amount = 1000  # Don't change this
whitelist = [794145307843624980, 1166453317778559001]  # Whitelisted users have no cooldown

# Initialize the bot with intents
bot = Bot(command_prefix=prefix, intents=intents)
bot.remove_command('help')

# bot events
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(f"{prefix}help"))
    print(f'Servers: {len(bot.guilds)}')
    print(f'Prefix -> "{prefix}" | Admins -> {admins}')
    for guild in bot.guilds:
        print(guild.name)

@bot.event
async def on_command(ctx):
    print(f'Command received: {ctx.command}')

@bot.event
async def on_command_error(ctx, error: Exception):
    if isinstance(error, CommandOnCooldown):
        embed = Embed(color=0xe67e22, description=f'{error}')
        await ctx.send(embed=embed)
    else:
        print(f'Error in command {ctx.command}: {error}')

@bot.event
async def on_member_join(member):
    print(f'Member joined: {member.name}')
    await bot.get_channel(welcome).send(f"{member.name} has joined")

@bot.event
async def on_member_remove(member):
    print(f'Member left: {member.name}')
    await bot.get_channel(welcome).send(f"{member.name} has left")

# Commands 
@bot.command()
async def kick(ctx, member: Member, *, reason=None):
    print(f'{ctx.author} used kick on {member} with reason: {reason}')
    staff = discord.utils.get(ctx.guild.roles, name='Owners')
    if staff in ctx.author.roles:
        await member.kick(reason=reason)
        embed = Embed(color=0xe67e22, description=f"{member} has been kicked for {reason}")
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/852980461264699443/853177249070055424/logo_1.jpg')
        await ctx.send(embed=embed)

@bot.command()
async def ban(ctx, member: Member, *, reason=None):
    print(f'{ctx.author} used ban on {member} with reason: {reason}')
    staff = discord.utils.get(ctx.guild.roles, name='Owners')
    if staff in ctx.author.roles:
        await member.ban(reason=reason)
        embed = Embed(color=0xe67e22, description=f"{member} has been banned for {reason}")
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/852980461264699443/853177249070055424/logo_1.jpg')
        await ctx.send(embed=embed)

@bot.command()
async def clear(ctx):
    print(f'{ctx.author} | {ctx.author.id} -> {bot.command_prefix}clear')
    staff = discord.utils.get(ctx.guild.roles, name='Owners')
    if ctx.channel.type != discord.ChannelType.private:
        if staff in ctx.author.roles:
            await ctx.channel.purge(limit=None)
            await ctx.send('https://media.giphy.com/media/3o6Ztm5TtARp8GqssU/giphy.gif')
        else:
            await ctx.message.delete()

@bot.command()
@cooldown(1, nitro_timeout, BucketType.user)
async def nitro(ctx):
    print(f'{ctx.author} used nitro in channel {ctx.channel.id}')
    if ctx.channel.id == bots_channel:
        x = 50
        bronze = discord.utils.get(ctx.guild.roles, name='Bronze')  # 100
        silver = discord.utils.get(ctx.guild.roles, name='Silver')  # 200
        gold = discord.utils.get(ctx.guild.roles, name='Gold')  # 300
        premium = discord.utils.get(ctx.guild.roles, name='Premium')  # 500
        if bronze in ctx.author.roles:
            x += 50
        elif silver in ctx.author.roles:
            x += 150
        elif gold in ctx.author.roles:
            x += 250
        elif premium in ctx.author.roles:
            x += 450

        embed = Embed(color=0xe67e22, description=f'I have sent you {x} nitro codes! Check your DMs!')
        await ctx.send(embed=embed)
        while x > 0:
            tokens = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(16))
            x -= 1
            with open("nitro.txt", "a") as a_file:
                a_file.write(f'discord.gift/{tokens}\n')

        target = await bot.fetch_user(ctx.author.id)
        await target.send(file=discord.File('nitro.txt'))
        os.remove("nitro.txt")
        print(f'{ctx.author} | {ctx.author.id} -> {prefix}nitro')
        await target.send("Enjoy your Unchecked Nitro codes!")

# whitelist
@nitro.after_invoke
async def reset_cooldown(ctx):
    for e in whitelist:
        if e == ctx.author.id:
            nitro.reset_cooldown(ctx)
        if e == ctx.message.channel.id:
            nitro.reset_cooldown(ctx)
        if e == ctx.message.guild.id:
            nitro.reset_cooldown(ctx)
        if e in [role.id for role in ctx.author.roles]:
            nitro.reset_cooldown(ctx)

@bot.command()
async def help(ctx):
    print(f'{ctx.author} used help')
    embed = Embed(color=0xe67e22)
    embed.add_field(name='Help', value=f'`{prefix}help`', inline=True)
    embed.add_field(name='Nitro', value=f'`{prefix}nitro`', inline=True)
    embed.add_field(name='Clear', value=f'`{prefix}clear`', inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def dm(ctx, user_id=None, *, args=None):
    print(f'{ctx.author} used dm to {user_id} with message: {args}')
    if user_id and args:
        try:
            target = await bot.fetch_user(user_id)
            await target.send(args)
            await ctx.channel.send(f"'{args}' sent to: {target.name}")
        except:
            await ctx.channel.send("Couldn't DM the given user.")
    else:
        await ctx.channel.send("You didn't provide a user's id and/or a message.")

@bot.command()
async def drop(ctx):
    print(f'{ctx.author} used drop')
    staff = discord.utils.get(ctx.guild.roles, name='Owners')
    if staff in ctx.author.roles:
        x = drop_amount
        while x > 0:
            tokens = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.digits) for _ in range(16))
            x -= 1
            with open("drop.txt", "a") as a_file:
                a_file.write(f'discord.gift/{tokens}\n')
        await ctx.send(file=discord.File('drop.txt'))
        os.remove('drop.txt')

@bot.command()
async def ticket(ctx):
    print(f'{ctx.author} used ticket')
    if ctx.channel.type != discord.ChannelType.private:
        channels = [str(channel) for channel in bot.get_all_channels()]
        if f'ticket-{ctx.author.id}' in channels:
            await ctx.message.delete()
        else:
            ticket_channel = await ctx.guild.create_text_channel(f'ticket-{ctx.author.id}')
            await ticket_channel.set_permissions(ctx.guild.default_role, send_messages=False, read_messages=False)
            await ticket_channel.set_permissions(ctx.author, send_messages=True, read_messages=True, add_reactions=True, embed_links=True, attach_files=True, read_message_history=True, external_emojis=True)
            embed = Embed(color=16083729, description=f'Please enter the reason for this ticket, type `{bot.command_prefix}close` if you want to close this ticket.')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/852980461264699443/853177249070055424/logo_1.jpg')
            await ticket_channel.send(f'{ctx.author.mention}', embed=embed)
            await ctx.message.delete()

bot.run(token)
