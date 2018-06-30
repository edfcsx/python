#crie um programa que leia quando dinheiro uma pessoa tem
#na carteira e mostre quantos dolares ela pode comprar
#considere U$$ = R$ 3,27

print('Conversion R$ for U$')
money = float(input('How much money do you have in R$? '))

print('R$ {} in conversion U${:.2f}'.format(money, money/3.27))