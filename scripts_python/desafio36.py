#Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa
#o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
#calcule o valor da prestacao mensal sabendo que ela não pode exceder 30% do salario ou então o empresitmo sera negado

cores = {'e': '\033[m',
         'white': '\033[1;30m',
         'red': '\033[1;31m',
         'green': '\033[1;32m',
         'yellow': '\033[1;33m',
         'blue': '\033[1;34m',
         'purple': '\033[1;35m',
         'turquesa': '\033[1;36m',
         'gray': '\033[1;37m',
         }

print('{}{}{}'.format(cores['blue'], 'Banco do nordeste Financiamento', cores['e']))
imovel = float(input('Digite o valor do imovel ->'))
anos = int(input('Digite a quantidade em anos que você deseja pagar 10,20,30,40,50 ->'))

print('O valor do imovel é {}'.format(imovel))
print('Quantidade de parcelas do orçamento {} X'.format(anos*12))
print('O valor da parcela é ->{:.2f}'.format(imovel / (anos*12)))
salario = float(input('Digite a renda familiar em R$ ->'))
print('{}{}{}{}{}'.format(cores['red'], '=-'*10, 'Analisando', '=-'*10, cores['e']))

anos10 = imovel/(10*12)
anos20 = imovel/(20*12)
anos30 = imovel/(30*12)
anos40 = imovel/(40*12)
anos50 = imovel/(50*12)

if (salario*0.30) > imovel / (anos*12):
    print('Parabéns seu financiamento foi aprovado')
elif (salario*0.30) > anos10:
    print('Parabens Financiamento aprovado com 10 anos')
    print('Valor da parcela com 10 anos {}'.format(imovel/anos10))
elif (salario*0.30) > anos20:
    print('Parabens Financiamento aprovado com 20 anos')
    print('Valor da parcela com 20 anos {}'.format(imovel / anos20))
elif (salario*0.30) > anos30:
    print('Parabens Financiamento aprovado com 30 anos')
    print('Valor da parcela com 30 anos {}'.format(imovel / anos30))
elif (salario * 0.30) > anos40:
    print('Parabens Financiamento aprovado com 40 anos')
    print('Valor da parcela com 40 anos {}'.format(imovel / anos40))
elif (salario * 0.30) > anos50:
    print('Parabens Financiamento aprovado com 50 anos')
    print('Valor da parcela com 50 anos {}'.format(imovel / anos50))
else:
    print('Infelizmente o orçamento foi negado')
