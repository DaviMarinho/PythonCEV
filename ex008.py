#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Escreva um valor em metros para ser convertido:\n'))

print('{}m em centímetros é = {}cm'.format(metros, metros*100))
print('{}m em milímetros é = {}mm'.format(metros, metros*1000))