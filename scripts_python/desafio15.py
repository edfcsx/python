#escreva um programa que pergunte a quantidade de km percorridos
#por um carro alugado e a quantidade de dias pelos quais ele foi alugado
#calcule o preço a pagar sabendo que o carro custa R$ 60,00 por dia e R$0,15 por km.

days = int(input('How many days do you want to rent the car ? '))
distance = float(input('What is the distance to be traveled in km ?'))

print('Total days cost R$ {}'.format(days*60))
print('Total km cost R$ {:.2f}'.format(distance*0.15))
print('Total cost rent in R$ {:.2f}'.format(days*60 + distance*0.15))