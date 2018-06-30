#Crie um algoritmo que pegue um numero e mostre seu
#sucessor e antecessor

n = int(input('Digite um numero: '))

print('O numero digitado foi {} seu antecessor {} e seu '
      'sucessor {} '.format(n, (n-1), (n+1)))