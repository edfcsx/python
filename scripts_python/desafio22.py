#Crie um programa que leia o nome completo de uma pessoa e mostre
# 1 -> o nome com todas as letras maisculas
# 2 -> o nome com todas as letras minusculas
# 3 -> quantas letras tem o nome sem espaço
# 4 -> quantas quantas letras tem o primeiro nome

name = str(input('Write your name ->').strip())
print('Your name in uppercase :{}'.format(name.upper()))
print('your name in lowercase :{}'.format(name.lower()))
print('Number of letters without space :{}'.format(len(name) - name.count(' ')))
#print('How many letters do you have in the first name? : {}'.format(name.find(' ')))
s = name.split()
print('How many letters do you have in the first name? : {}'.format(len(s[0])))