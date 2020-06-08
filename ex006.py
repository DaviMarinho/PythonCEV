#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
from math import sqrt

 num = float(input('Escreva um número qualquer:\n'))

print('O dobro de {:.0f} é: {}' .format( num,  num*2))
print('O triplo de {:.0f} é: {}' .format( num,  num*3))
print('A raiz quadrada de {:.0f} é: {:.2f}' .format( num, sqrt( num)))