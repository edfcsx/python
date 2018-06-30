from datetime import date
idade = int(input('Digite o ano de nascimento do nadador ->'))
idade = date.today().year - idade
if idade <= 9:
    print('Sua categoria e mirim')
elif idade <= 14:
    print('Sua categoria e infantil')
elif idade <= 19:
    print('Sua categoria e junior')
else:
    print('Sua categoria e master')