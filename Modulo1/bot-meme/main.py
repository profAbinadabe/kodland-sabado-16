import discord
import random
import os

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Fizemos o login como {bot.user}!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return 
    
    if message.content.startwith('$meme'):
        folder = "images"

        try:
            memes = os.listdir(folder)

            if not memes:
                await message.channel.send('A pasta de memes está vazia!')
                return
        
            meme_aleatorio = random.choice(memes)
            caminho = os.path.join(folder, meme_aleatorio)

            with open(caminho, "rb") as f:
                picture = discord.File(f)
                await message.channel.send(file=picture)

        except FileNotFoundError:
            await message.channel.send(f'Erro: A pasta {folder} não foi encontrada. Crie a pasta e coloque os memes lá!')
        
bot.run("Aqui vai o token!")