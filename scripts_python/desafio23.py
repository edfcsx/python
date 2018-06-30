#Faça um programa que leia um número de 0 a 9999 e mostra na tela cada um dos
#digitos separados Ex 1234 - unidade 4 - dezena 3 - centena 2 - milhar 1

num = int(input('Write anyone number ->'))
u = num //1%10
d = num //10%10
c = num //100%10
m = num //1000%10
print('Unity: {}'.format(u))
print('Ten: {}'.format(d))
print('Hundred: {}'.format(c))
print('Thousand: {}'.format(m))