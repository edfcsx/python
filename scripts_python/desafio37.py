#escreva um programa que leia um numero inteiro qualquer e paça para o usuario escolher qual sera
#a base de conversão
#1 para binario
#2 para octal
#3 para hexadecimal

numero = int(input('Digite um numero inteiro ->'))
print('''Escolha uma base de conversão:
[1] para converter em binario
[2] para converter em octal
[3] para converter em hexadecimal''')

menu = int(input('->'))

if menu == 1:
    print('{} convertido para binario é igual a {}'.format(numero, bin(numero)[2:]))
elif menu ==2:
    print('{} convertido para octal é igual a {}'.format(numero, oct(numero)[2:]))
elif menu == 3:
    print('{} convertido para hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Digite um valor valido')