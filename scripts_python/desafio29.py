#Escreva um programa que leia a velocidade de um carro
#se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado
#a multa custa 7,00 por cada km acima do limite

print('Radar 1.0')
car = float(input('How fast is the car? Km/h-> '))
if car <=80:
    print('the car is normal speed')
else:
    car = (car-80)*7
    print('the car is over the limite, fine of R$ {:.0f}'.format(car))