#faça um programa que leia um ano qualquer e mostre se ele é bisexto

year = int(input('Write some year ->'))
c = year%4
if c == 0:
    print('{} is a leap year'.format(year))
else:
    print('{} is a nothing leap year'.format(year))
