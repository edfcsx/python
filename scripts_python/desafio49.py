n = int(input('Digite um numero para ver sua tabuada ->'))

for c in range(1, 11):
    print('{:2}{:2}{}{}{:2}'.format(c, ' X ', n, ' = ', c * n))