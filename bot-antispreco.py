import discord
from discord.ext import commands, tasks
import time

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

#opzionale: messaggio ogni tanto
#waste_sorting

waste_sorting = {
    "bottiglia_di_plastica": True,
    "lattina_di_alluminio": True,
    "cartone_della_pizza": False,  # Se sporco di cibo, altrimenti riciclabile
    "bicchiere_di_vetro": True,
    "giornale": True,
    "sacchetto_di_plastica": True,
    "batteria": False,  # Da smaltire nei punti di raccolta specifici
    "lampadina": False,  # Da smaltire nei RAEE
    "tappo_di_sughero": True,
    "scatola_di_cartone": True,
    "piatto_di_ceramica": False,
    "contenitore_di_yogurt": True,
    "bottiglia_di_vetro": True,
    "busta_di_patatine": False,  # Contiene alluminio e plastica insieme
    "posate_di_plastica": False,
    "tubo_di_dentifricio": False,  # Troppo difficile da separare
    "scatoletta_di_tonno": True,
    "fazzoletto_di_carta_usato": False,  # Non può essere riciclato
    "stoffa": True,
    "pannolini": False,
    "cartone_del_latte": True,  # Tetra Pak, va riciclato se previsto dal comune
    "flacone_di_detersivo": True,
    "bottiglia_di_olio": False,  # Olio da smaltire in centri appositi
    "tappi_di_plastica": True,
    "cassette_di_legno": True,
    "bustine_del_tè": True,
    "gusci_di_uova": True,  # Se la raccolta organica è disponibile
    "mele_marce": True,  # Rifiuti organici
    "carta_stagnola": True,
    "carta_da_forno": False  # Trattata con siliconi
}

def saluto(ctx):
    ctx.send("Ciao! Sono il bot anti-spreco, sono qui per aiutarti a ridurre gli sprechi e a smaltire correttamente i rifiuti. Scrivi /help_me per vedere i comandi disponibili")

@bot.event
async def on_ready():
    print(f'Abbiamo fatto l\'accesso come {bot.user}')
    channel = bot.get_channel(1334577190058201222)
    await channel.send("Ciao! Sono il bot anti-spreco, sono qui per aiutarti a ridurre gli sprechi e a smaltire correttamente i rifiuti. Scrivi /help_me per vedere i comandi disponibili")
    send_reminder.start()
    
@tasks.loop(minutes=5)
async def send_reminder():
    channel = bot.get_channel(1334577190058201222)
    await channel.send("Ricordati di smaltire correttamente i rifiuti e di ridurre gli sprechi! Scrivi /help_me per vedere i comandi disponibili")

@bot.command()
async def help_me(ctx):
    await ctx.send("Ecco i comandi disponibili:\n"
                   "/spreco_alimentare: per vedere un'immagine sullo spreco alimentare\n"
                   "/smaltimento <oggetto>: per sapere se un oggetto è riciclabile o meno\n"
                    "/smaltimento lista: per vedere la lista degli oggetti che puoi smaltire\n")

@bot.command()
async def spreco_alimentare(ctx):
    with open("Spreco Alimentare (1).png", "rb") as file:
        picture = discord.File(file)
        await ctx.send(file=picture)

@bot.command()
async def smaltimento(ctx, arg: str = "default"):
    if arg == "lista":
        await ctx.send("Ecco la lista degli oggetti che puoi smaltire:")
        for waste in waste_sorting:
            await ctx.send(f"- {waste}")

    elif arg in waste_sorting:
        if waste_sorting[arg]:
            await ctx.send(f"{arg} è riciclabile")
        else:
            await ctx.send(f"{arg} non è riciclabile")
    else:
        await ctx.send(f"{arg} non è stato trovato")

bot.run('token')
