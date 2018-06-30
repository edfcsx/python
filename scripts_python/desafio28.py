#Escreva um programa que faça o computador pensar em um numero inteiro de 0 a 5
#para o usuario tentar descobrir qual foi o numero escolhido pelo computador
#o programa devera escrever na tela se o usuario venceu ou perdeu

from random import randint
rand = randint(1, 5)

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

print('{}{}{}'.format(cores['red'], '-='*20, cores['e']))
print('{}{}{}'.format(cores['purple'], 'Welcome the Python number game', cores['e']))
num = int(input('\033[1;34mPlease Write anyone number from 1 to 5 ->\033[m'))

if num == rand:
    print('\033[4;32mCongratulationz Yoooou Win!!!\033[m')
else:
    print('\033[4;31mOhhh no you lose! the correct number is {}\033[m'.format(rand))

