# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# ** Potenciação
# // Divisão inteira
# % modulo ou resto da divisão

#Ordem de precendencia
# 1 = tudo que estiver dentro de parenteses
# 2 = Potencia
# 3 = Multiplicação / divisão / divisao inteira/resto da divisão
# 4 = Adição e Subtração

a = float(5)
b = float(2)
print('A soma entre {} e {} vale {}'.format(a, b, a+b))
print('A subtração entre {} e {} vale {}'.format(a, b, a-b))
print('A multiplicação entre {} e {} vale {}'.format(a, b, a*b))
print('A divisão entre {} e {} vale {}'.format(a, b, a/b))
print('A potencia entre {} e {} vale {}'.format(a, b, a**b))
print('A divisão inteira entre {} e {} vale {}'.format(a, b, a//b))
print('O resto da divisão entre {} e {} vale {}'.format(a, b, a%b))
