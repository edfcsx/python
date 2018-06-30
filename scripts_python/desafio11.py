#Faça um programa que leia a largura e a altura de uma parede
#em metros, calcule a sua area e a quantidade de tinta
#necessaria para pinta-la, sabendo que a cada litro de tinta
#pinta uma área de 2m².

width = float(input('Please insert Width in meters for the wall ->'))
height = float(input('Please insert Height in meters for the wall ->'))
print('total wall area {:.2f} is required {:.1f} bucket paints'.format((width*height),(width*height)/2))