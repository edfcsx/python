from random import randint
import playsound

cores = {'e': '\033[m',
         'white': '\033[1;30m',
         'red': '\033[1;31m',
         'green': '\033[1;32m',
         'yellow': '\033[1;33m',
         'blue': '\033[1;34m',
         'purple': '\033[1;35m',
         'turquesa': '\033[1;36m',
         'gray': '\033[1;37m',
         }
playsound.playsound('desafio45_intro.mp3')
print('{}{}{}'.format(cores['blue'], 'Eu sou o computador e quero jogar um jogo com você', cores['e']))
print('{}{}{}'.format(cores['red'], 'Iremos jogar Jokenpo faça sua escolha:', cores['e']))
print('{}{}{}'.format(cores['purple'], '1 - Pedra', cores['e']))
print('{}{}{}'.format(cores['yellow'], '2 - Papel', cores['e']))
print('{}{}{}'.format(cores['red'], '3 - Tesoura', cores['e']))
cpu = randint(1, 3)
papel = 2
pedra = 1
tesoura = 3
jogador = int(input('->>>'))
print('{}{}{}'.format(cores['blue'], '=-'*20, cores['e']))
if jogador == 1:
    print('{}{}{}'.format(cores['purple'], 'Você escolheu Pedra', cores['e']))
elif jogador == 2:
    print('{}{}{}'.format(cores['purple'], 'Você escolheu Papel', cores['e']))
elif jogador == 3:
    print('{}{}{}'.format(cores['purple'], 'Você escolheu Tesoura', cores['e']))
else:
    print('{}{}{}'.format(cores['red'], 'Digite um numero valido', cores['e']))

if cpu == 1:
    print('{}{}{}'.format(cores['red'], 'Eu escolhi Pedra', cores['e']))
elif cpu == 2:
    print('{}{}{}'.format(cores['red'], 'Eu escolhi Papel', cores['e']))
else:
    print('{}{}{}'.format(cores['red'], 'Eu escolhi Tesoura', cores['e']))

if jogador == 1 and cpu == 2: #pedra vs papel
    print('{}{}{}'.format(cores['red'], 'Oh maquina sempre mais inteligente', cores['e']))
    playsound.playsound('desafio45_lose.mp3')

elif jogador == 1 and cpu == 3: #Pedra vs tesoura
    print('{}{}{}'.format(cores['green'], 'Oh humano maldito você ganhou', cores['e']))
    playsound.playsound('desafio45_youwin.mp3')

elif jogador == 2 and cpu == 1: #papel vs pedra
    print('{}{}{}'.format(cores['green'], 'Oh humano maldito você ganhou', cores['e']))
    playsound.playsound('desafio45_youwin.mp3')

elif jogador == 2 and cpu == 3: #papel vs tesoura
    print('{}{}{}'.format(cores['red'], 'Oh maquina sempre mais inteligente', cores['e']))
    playsound.playsound('desafio45_lose.mp3')

elif jogador == 3 and cpu == 1: #tesoura vs pedra
    print('{}{}{}'.format(cores['red'], 'Oh maquina sempre mais inteligente', cores['e']))
    playsound.playsound('desafio45_lose.mp3')

elif jogador == 3 and cpu == 2: #tesoura vs papel
    print('{}{}{}'.format(cores['green'], 'Oh humano maldito você ganhou', cores['e']))
    playsound.playsound('desafio45_youwin.mp3')

elif jogador == cpu:
    print('{}{}{}'.format(cores['yellow'], 'Empate', cores['e']))