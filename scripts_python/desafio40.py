#Crie um sistema que leia duas notas e calcule a media sendo
# < 5 reprovado
#5 a 6.9 em recuperação
#7 ou > aprovado

n1 = float(input('Digite a primeira nota ->'))
n2 = float(input('Digite a segunda nota ->'))
m = (n1+n2) / 2

if m<5:
    print('Aluno reprovado')
elif m<6.9:
    print('Aluno em recuperação')
else:
    print('Aluno aprovado')
