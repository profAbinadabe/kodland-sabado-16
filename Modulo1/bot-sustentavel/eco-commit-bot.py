import os
import random
import discord

from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="$", intents=intents)

impactos = {
    "plástico":"Plástico pode levar até 400 anos para se decompor. Descarte em coleta reciclável.",
    "pilha":"Pilhas contaminam solo e água. Devem ir para pontos de coleta.",
    "eletrônico":"Lixo eletrônico libera metais pesados. Leve para ecopontos."
}

desafios = [
    "Separe seu lixo reciclável hoje.",
    "Procure um ponto de coleta de lixo eletrônico.",
    "Explique para alguém como separa lixo corretamente."
]

ideias = [
    "Doe eletrônicos funcionando em vez de descartar.",
    "Use caixas de papelão como divisórias de gaveta."
]

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"O bot está conectado como {bot.user}")

@bot.tree.command(name="impacto", description="Mostra o impacto ambiental de um item")
async def impacto(interaction: discord.Interaction, item:str):
    item = item.lower()

    resposta = impactos.get(
        item,
        "Ainda não conheço esse item. Tente outro."
    )

    await interaction.response.send_message(
        # use \n para pular de linha na string
        f"**Impacto de {item}:**\n{resposta}\n\n Pense nisso como um bug ambiental que podemos corrigir."
    )

@bot.tree.command(name="ideia", description="Gera uma ideia de reaproveitamento")
async def ideia(interaction: discord.Interaction):
    await interaction.response.send_message(
        f" **Ideia rápida:**\n{random.choice(ideias)}"
    )

@bot.tree.command(name="desafio", description="Gera um desafio sustentável")
async def desafio(interaction: discord.Interaction):
    await interaction.response.send_message(
        f" **Desafio verde:**\n{random.choice(desafios)}"
    )

# Para executar o bot, use o comando: pipenv run python |nome do seu arquivo python|
bot.run(TOKEN)