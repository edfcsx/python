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

n = int(input('Digite um numero para verificar se ele é primo ->'))
div = 0
c = 0
for intervalo in range(1, n+1):
    c += 1
    verificador = n % intervalo
    if verificador == 0:
        div += 1
        print('{}{:2}{}{}'.format(cores['green'], intervalo, ' ', cores['e']), end='')
    else:
        print('{}{:2}{}{}'.format(cores['red'], intervalo, ' ', cores['e']), end='')
    if c == 20:
        print('')
        c -= 20
if div == 2:
    print('Ele é primo')
else:
    print('Ele não é primo ele foi dividido {} vezes'.format(div-1))
