#Faça um programa que leia o nome completo de uma pessoa e mostre em seguida
#o primeiro e o ultimo nome separadamente

name = input('Whats you name ? ').split()
print('Bem vindo {} {}'.format(name[0], name[-1]))