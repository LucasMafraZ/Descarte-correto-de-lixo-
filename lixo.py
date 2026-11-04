import discord
import random
import os
import requests
from discord.ext import commands
from Bot_logic2 import gen_pass
from Bot_logic2 import g_personagem
from Bot_logic2 import moeda 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá! eu sou um bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(f'eu escolho {random.choice(choices)}')

@bot.command()
async def senha(ctx, tamanho = 8):
    await ctx.send(f'senha = {gen_pass(tamanho)}')

@bot.command(name="personagem")
async def comando_personagem(ctx, *, nome: str):
    resultado = g_personagem(nome)
    await ctx.send(resultado)

@bot.command()
async def meme_beta(ctx):
    with open('images/mem1.png', 'rb') as f:
        #Vamos armazenar o arquivo convertido da biblioteca do Discord nesta variável!
        picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        #Vamos armazenar o arquivo convertido da biblioteca do Discord nesta variável!
        picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)

@bot.command()
async def spam(ctx, times: int, content='repeating...'):
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def CaraCoroa(ctx):
    resultado = moeda()
    await ctx.send(resultado)

@bot.command()
async def pokemon(ctx):
    img_name = random.choice(os.listdir('pokemon'))
    with open(f'pokemon/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def lixo(ctx, lixo):
    if lixo == 'papel':
        await ctx.send(f'{lixo}: Jornais, revistas, caixas de papelão e folhas')
        await ctx.send('Devemos descarta-lo na Lixeira azul (recicláveis)')
    elif lixo == 'plástico':
        await ctx.send(f'{lixo}: Garrafas PET, embalagens e sacolas')
        await ctx.send('Devemos descarta-lo na Lixeira vermelha (recicláveis)')
    elif lixo == 'vidro':
        await ctx.send(f'{lixo}: Garrafas, potes e frascos')
        await ctx.send('Devemos descarta-lo na Lixeira verde (recicláveis)')
    elif lixo == 'metal':
        await ctx.send(f'{lixo}: Latas de refrigerante e alimentos')
        await ctx.send('Devemos descarta-lo na Lixeira amarela (recicláveis)')
    elif lixo == 'orgânico':
        await ctx.send(f'{lixo}: Restos de comida, cascas de frutas e verduras')
        await ctx.send('Devemos descarta-lo na compostagem ou lixo orgânico')
    elif lixo == 'eletrônico':
        await ctx.send(f'{lixo}: Celulares, pilhas, baterias e carregadores')
        await ctx.send('Devemos descarta-lo em pontos de coleta específicos')
    elif lixo == 'lixo':
        await ctx.send('tipos de lixo que aceitamos: papel, plástico, vidro, metal, eletrônico, orgânico, rejeito (escrito em minúsculo)')
    elif lixo == 'rejeito':
        await ctx.send(f'{lixo}: Papel higiênico, fraldas e absorventes')
        await ctx.send('Devemos descarta-lo no lixo comum')
    else:
        await ctx.send('desculpe, não conheço esse tipo de lixo. ')
        await ctx.send('tipos de lixo que aceitamos: papel, plástico, vidro, metal, eletrônico, orgânico, rejeito (escrito em minúsculo)')
        
bot.run("token")
