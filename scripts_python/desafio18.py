#faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
#cosseno e tangente desse angulo
from math import radians, sin, cos, tan

radius = int(input('Write anyone angle ->'))
print('The cosine of {}º is {:.2f}'.format(radius, cos(radians(radius))))
print('The sine of {}º is {:.2f}'.format(radius, sin(radians(radius))))
print('The tangent of {}º is {:.2f}'.format(radius, tan(radians(radius))))