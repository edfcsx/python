#Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem:
#o primeiro valor é maior
#o segundo valor e maior
#nao existe valor maior os dois são iguais

n1 = int(input('Digite um valor inteiro :->'))
n2 = int(input('Digite um valor inteiro :->'))

if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n1 < n2:
    print('{} e maior que {}'.format(n2, n1))
else:
    print('Os dois valores são iguais')