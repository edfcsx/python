#Escreva um programa que pergunta o salario de um funcionario e calcule o valor de
#aumento para salarios acima de R$ 1250 calcule aumento de 10 para inferiores calcule
#15%

salary = float(input('How much is the salary ? ->'))
if salary<=1250:
    perc = salary*0.15
    print('The current salary is {} with increased 15% {} the actual salary is {}'.format(salary, perc, salary+perc))
else:
    perc = salary * 0.10
    print('The current salary is {} with increased 10% {} the actual salary is {}'.format(salary, perc, salary + perc))