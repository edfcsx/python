#faça um programa que leia tres numeros e mostral quel é o maior e qual o menor

n1 = int(input('Please write first number ->'))
n2 = int(input('Please write second number ->'))
n3 = int(input('Please write third number ->'))

major = max(n1, n2, n3)
minor = min(n1, n2, n3)

print('The major number is {} the minor number is {}'.format(major, minor))