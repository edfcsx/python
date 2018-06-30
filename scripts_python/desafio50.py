s = 0
for c in range(1, 7):
    a = int(input('Digite o {} numero ->'.format(c)))
    v = a % 2
    if v == 0:
        s += a
print('A soma de todos os numeros pares é {}'.format(s))