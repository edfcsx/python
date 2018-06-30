#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de
#trabalho dos alunos. faça um programa que leia o nome dos quatro alunos e mostre
#a ordem sorteada

from random import shuffle
std1 = 'Marcelo'
std2 = 'Ana'
std3 = 'Julhao'
std4 = 'Joca'
row = [std1, std2, std3, std4]
shuffle(row)
print('The order of apresentation is {}'.format(row))