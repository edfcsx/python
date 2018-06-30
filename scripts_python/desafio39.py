#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade
#Se ele ainda vai se alistar ao serviço militar
#se e a hora de se alistar
#se ja passou do tempo de alistamento
#seu programa também devera mostrar o tempo que falta ou que passsou do prazo
from datetime import date
al_anos = 17
al_meses = al_anos * 12

print('Alistamento 1.0')
idade = int(input('Digite seu ano de nascimento ->'))

idade = date.today().year - idade
if idade < al_anos:
    print('Você ainda não precisa se alistar, faltam {} ano(s)'.format((al_anos-idade)))
elif idade > al_anos:
    print('Você precisa se alistar imediatamente, está em atraso em {} ano(s)'.format((idade-al_anos)))
else:
    print('Você já tem a idade necessária para se alistar, procure uma junta militar')
