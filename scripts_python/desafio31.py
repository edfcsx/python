#Desenvolva um programa que pergunte a distancia de uma viagem em km
#calcule o preço da passagem, cobrando 0.50 por km em viagens até 200km e
#0.45 para viagens mais longas

d = float(input('The distance you need to travel ? in km ->'))
if d <= 200:
    print('The travel cost R$ {}'.format(d*0.50))
else:
    print('The travel cost R$ {}'.format(d*0.45))