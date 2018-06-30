#Crie um programa que leia um número inteiro e mostra na tela
#se ele e par ou impar

number = int(input('Write anyone number ->'))
c = number%2
if c == 0:
    print('{} this number is even'.format(number))
else:
    print('{} this number is odd'.format(number))