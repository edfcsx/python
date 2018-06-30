maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa ->'.format(c)))
    if maior == 0 and menor == 0:
        maior = peso
        menor = peso

    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print('''Pesos:
[1] Maior = {}Kgs
[2] Menor = {}Kgs
'''.format(maior, menor))