s = 0
for c in range(0, 501):
    n = c % 2
    if n != 0:
        multiplo = c % 3
        if multiplo == 0:
            s += c
print('A Soma total dos multiplos de 3 de 1 a 500 é {}'.format(s))