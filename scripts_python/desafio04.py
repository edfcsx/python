#Faça um programa que leia algo pelo teclado
#e mostre na tela o seu tipo primitivo e todas as
#informações possiveis sobre ele.

n = input('Digite algo: ')
print('Você digitou: {}'.format(n))
print('Ele é um número ?',n.isnumeric())
print('Ele é uma alfa ?',n.isalpha())
print('Ele é um alfa numerico ?',n.isalnum())
print('Ele está todo em letras maisculas ?',n.isupper())
print('Ele está todo em minusculo ?',n.islower())
print('Ele é um decimal ?',n.isdecimal())
print('Ele pode ser imprimido ?',n.isprintable())
print('Ele é um espaço ?',n.isspace())
print('Ele está capitalizada ?',n.istitle())