#escreva um programa que leia um valor em metros e o exiba
#convertido em centimetros e milimetros

meters = float(input('Please insert value in meters for conversion->'))

print('{} Meters = {:.0f} Centimeters and {:.0f}MM'.format(meters, meters*100, meters*1000))