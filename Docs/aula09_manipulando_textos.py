#Analises

#Len -> comando para pegar o tamanho de uma frase
#count -> ele vai contar quantas vezes aparece tal caractere
#find -> ele vai mostrar o indice que começa a frase se retornar valor negativo
#significa que não foi encontrado
#in verifica se existe uma palavra dentro da frase = OPERADOR

#Transformação

#replace -> ele troca os caracteres
#upper -> transforma tudo em maisculo
#lower -> transforma tudo em minusculo
#capitalize -> transforma tudo em minusculo e a primeira letra fica em maisculo
#title-> transforma o inicio de cada palavra em maisculo
#strip -> remove todos os espaços inuteis
#rstrip -> remove todos os espaços inuteis a direita
#lstrip -> remove todos os espaços inuteis a esquerda

#Divisão

#split -> ele divide as strings através dos espaços
#'-'.join(frase) -> ele junta todos os elementos usando um separador definido

frase = 'Curso em video Python'
print(len(frase))
print(frase.count('o'))
print(frase.find('deo'))
print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())