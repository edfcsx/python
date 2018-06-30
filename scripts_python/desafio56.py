from datetime import date
ano = date.today().year
m = 0
m20 = 0
nome_homem = 'a'
idade_homem = 0
print('*'*60)
print('{}{}{}'.format('=-'*10, 'Analisador de Grupos', '=-'*10))
print('*'*60)
for c in range(1, 5):
    nome = input('Digite o nome da pessoa ->')
    idade = int(input('Digite o ano de nascimento ->'))
    sexo = input('Digite o sexo M ou F ->').lower()
    idade = ano - idade
    m += idade

    if sexo == 'm':
        if nome_homem == 'a':
            nome_homem = nome
            idade_homem = idade
        elif idade_homem < idade:
            nome_homem = nome
            idade_homem = idade

    if sexo == 'f':
        if idade < 20:
            m20 += 1

    print('*'*60)

print('A media das idades é {}'.format(m/4))
if idade_homem == 0:
    print('Não existem homens no grupo')
else:
    print('O homem mais velho é {} com {} anos'.format(nome_homem, idade_homem))
if m20 == 0:
    print('Não existem mulheres com menos de 20 anos no grupo')
else:
    print('Existem {} mulheres menores de 20 anos'.format(m20))