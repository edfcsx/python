#faça um programa que leia o comprimento do cateto oposto e do cateto
#adjacente de um trianbulo retangulo, calcule e mostre o comprimento da hipotenusa
import math
co = float(input('length of opposite leg ->'))
ca = float(input('length of adjacent leg ->'))
hi = (co**2 + ca**2) ** (1/2)
print('the length of the hypotenuse is {:.2f}'.format(hi))
hii = math.hypot(co, ca)
print('{}'.format('-'*10))
print('the length of the hypotenuse is {:.2f}'.format(hii))