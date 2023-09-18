import discord
from discord.ext import commands
from twilio.rest import Client

# Your Twilio account SID and auth token
twilio_account_sid = 'AC8efde7bfb9368057089102f5e3874e33'
twilio_auth_token = '1d4688d7373e117299b1c4d02ced3aff'
phone_number = '+2347053359102'

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

    # Get the guild (server) that the bot is connected to
    for guild in bot.guilds:
        if guild.name == 'AI Everything':  # Replace with your server name
            break
    else:
        print("Server not found.")
        return

    # Get the channel that the bot is monitoring
    for channel in guild.channels:
        if channel.name == 'general':  # Replace with your channel name
            break
    else:
        print("Channel not found.")
        return

    # Get the bot's member object for the guild
    member = guild.get_member(bot.user.id)

    # Get the bot's permissions for the channel
    permissions = channel.permissions_for(member)

    # Print the permissions
    for name, value in permissions:
        print(f'{name}: {value}')


@bot.event
async def on_message(message):
    # If the message is from the server you're interested in
    if message.channel.id == 1111721459010764824:  # Replace with your channel's ID
        content = f'{message.author}: {message.content}'
        print(content)

        # If the message has any attachments, add their URLs to the content
        if message.attachments:
            for attachment in message.attachments:
                content += f'\nAttachment: {attachment.url}'

        # Send an SMS with Twilio
        twilio_client = Client(twilio_account_sid, twilio_auth_token)
        twilio_client.messages.create(body=content, from_='+14345428483', to=phone_number)





bot.run('MTExMjI1MjAzOTU5OTIyNjkyMA.GPuLDG.2Cbat-fgivmfpMeoIzY8woflT43YWJaX2p3Y7Q')

