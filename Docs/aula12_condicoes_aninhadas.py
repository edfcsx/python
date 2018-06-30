nome = str(input('Qual seu nome ?')).lower()
if nome == 'eduardo':
    print('Que nome bonito!')
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    print('Seu nome e bem popular no brasil')
elif nome in 'Ana Claudia jessica juliana':
    print('belo nome feminino!')
else:
    print('Seu nome é bem normal')

print('tenha um bom dia, {}!'.format(nome))
