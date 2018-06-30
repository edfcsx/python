from datetime import date
maior = 0
menor = 0
ano_atual = date.today().year
for c in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {} pessoa ->'.format(c)))
    if (ano_atual - ano) < 21:
        menor += 1
    else:
        maior += 1
print('Nesse grupo existem {} maiores de idade e {} menores de idade'.format(maior, menor))