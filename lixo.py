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
async def pokemon_beta(ctx):
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

def get_pokemon(id):    
    url = (f'https://pokeapi.co/api/v2/pokemon/{id}/')
    res = requests.get(url)
    data = res.json()
    pokemon = {}
    pokemon["nome"] = data["name"]
    pokemon['id'] = data['id']
    pokemon["imagem"] = data["sprites"]["other"]["home"]["front_default"]
    return pokemon


@bot.command('pokemon')
async def pokemon(ctx, id):
    pokemon = get_pokemon(id)
    await ctx.send(f'O pokemon sorteado foi {pokemon["nome"]}. Id = {pokemon['id']} {pokemon["imagem"]}')


lixos = {
    'papel': {
        'exemplos': 'Jornais, revistas, caixas de papelão e folhas',
        'descarte': 'Lixeira azul (recicláveis)'
    },

    'plástico': {
        'exemplos': 'Garrafas PET, embalagens e sacolas',
        'descarte': 'Lixeira vermelha (recicláveis)'
    },

    'vidro': {
        'exemplos': 'Garrafas, potes e frascos',
        'descarte': 'Lixeira verde (recicláveis)'
    },

    'metal': {
        'exemplos': 'Latas de refrigerante e alimentos',
        'descarte': 'Lixeira amarela (recicláveis)'
    },

    'orgânico': {
        'exemplos': 'Restos de comida, cascas de frutas e verduras',
        'descarte': 'Compostagem ou lixo orgânico'
    },

    'eletrônico': {
        'exemplos': 'Celulares, pilhas, baterias e carregadores',
        'descarte': 'Pontos de coleta específicos'
    },

    'rejeito': {
        'exemplos': 'Papel higiênico, fraldas e absorventes',
        'descarte': 'Lixo comum'
    }
}


@bot.command()
async def lixo(ctx, lixo):
    lixo = lixo.lower()

    if lixo == 'lixo':
        await ctx.send(
            'Tipos de lixo aceitos: papel, plástico, vidro, metal, '
            'eletrônico, orgânico e rejeito.'
        )

    elif lixo in lixos:
        await ctx.send(f'{lixo}: {lixos[lixo]["exemplos"]}')
        await ctx.send(f'Devemos descartar em: {lixos[lixo]["descarte"]}')
        with open(f'lixo/{lixo}.jpg', 'rb') as f:
                picture = discord.File(f)
                await ctx.send(file=picture)
        

    else:
        await ctx.send('Desculpe, não conheço esse tipo de lixo.')
        await ctx.send('Digite lixo para consultar os tipos aceitos.')

        
bot.run("token")
