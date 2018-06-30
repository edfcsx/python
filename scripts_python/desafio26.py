#Faça um programa que leia uma frase pelo teclado e mostre:
#1 -> quantas vezes aparece a letra A
#2 -> em que posição ela aparece a primeira vez
#3 -> em que posição ela aparece a ultima vez

frase = input('Write anyone phrase ->').strip().lower()
print('how many times does the letter A appear ? {}'.format(frase.count('a')))
print(frase.find('a'))
print(frase.rfind('a'))