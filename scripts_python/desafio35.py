#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario
#se elas podem ou não formar um triangulo
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

r1 = float(input('write the length of the first line ->'))
r2 = float(input('write the length of the second line ->'))
r3 = float(input('write the length of the third line ->'))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('{}{}{}'.format(cores['green'], 'the 3 straight lines can form a triangle', cores['e']))
else:
    print('the 3 straight lines cannot form a triangle')