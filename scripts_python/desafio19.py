#um professor quer sortear um de seus 4 alunos para apagar o quadro, faça um programa
#que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
from  random import choice
std1 = 'Marcelo'
std2 = 'Ana'
std3 = 'Julhao'
std4 = 'Joca'
row = [std1, std2, std3, std4]
selected = choice(row)
print('The selected student was {}'.format(selected))
