#Crie um programa que leia o nome de uma cidade e diga se ela
#começa ou não com o nome SANTO

town = input('write the name of any city -> ').strip().upper().split()
print('does SANTO exist in the first name of the city? :{}'.format('SANTO' in town[0]))