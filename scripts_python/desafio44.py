preco = float(input('Digite o valor do produto ->'))

print('Digite 1 - A vista chegue 10% desconto')
print('Digite 2 - A vista no debito 5% desconto')
print('Digite 3 - Em até 2x no cartão sem juros')
print('Digite 4 - 3x ou mais no cartão - 20% de juros')
menu = int(input('Opção ->>'))

if menu == 1:
    print('Valor do produto R${} valor do desconto R${} valor final R${}'.format(preco, preco*0.1, preco - (preco*0.1)))
elif menu == 2:
    print('Valor do produto R${} valor do desconto R${} valor final R${}'.format(preco, preco * 0.1, preco - (preco * 0.05)))
elif menu == 3:
    print('Valor do produto R${} valor do desconto R${} valor final R${}'.format(preco, 0, preco))
elif menu == 4:
    print('Valor do produto R${} valor do acrescimo R${} valor final R${}'.format(preco, preco * 0.2,preco + (preco * 0.2)))
else:
    print('Digite uma opção valida')