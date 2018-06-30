nome = str(input('Whats you name ? ')).strip().lower()
if nome == 'eduardo':
    print('Esse nome é lindo')
else:
    print('Que nome normal você tem')
print('Bom dia, {}!'.format(nome))
print('{}'.format('-'*25))
n1 = float(input('Write first note ->'))
n2 = float(input('Write second note ->'))
m = (n1+n2) / 2
print('Parabéns' if m >=7 else 'Reprovado')
