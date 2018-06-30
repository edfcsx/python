import sys
print('Leitor de palindromo')
frase = str(input('Digite uma frase para saber se ela é um palindromo ->')).lower()
frase = frase.replace(' ', '')
frase_invertida = frase[::-1]

if frase == frase_invertida:
    print('A frase é um palindromo')
else:
    print('A frase não é um palindromo')

