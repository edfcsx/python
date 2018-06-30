#Crie um algoritmo que leia um número e mostre seu dobro
#triplo e raiz quadrada

n = int(input('Digite um numero: '))

print('O numero digitado é: {}'.format(n))
print('Seu dobro é: {}'.format(n*2))
print('Seu triplo é {}'.format(n*3))
print('Sua raiz é {:.2f}'.format(n**(1/2)))