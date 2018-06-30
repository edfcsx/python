#Crie um programa que leia um número real qualquer pelo teclado e mostre
#e mostre na tela a sa porção inteira  ex: 6.66587 -> 6
from math import trunc
num = float(input('Write anyone float number ->'))
print('The whole part of number {} is {}'.format(num, trunc(num)))
print('The whole part of number {} is {}'.format(num, int(num)))