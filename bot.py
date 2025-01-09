from Generatore_di_password import generatore_di_password
import discord


# la variabile intents contiene i permessi al bot
intents = discord.Intents.default()
# abilita il permesso a leggere i contenuti dei messaggi
intents.message_content = True
# crea un bot e passa gli indents
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$password'):
        await message.channel.send(generatore_di_password())
    elif message.content.startswith('$arrivederci'):
        await message.channel.send("\U0001f642")
    else:
        await message.channel.send(message.content)

print("ciao")

client.run("token")