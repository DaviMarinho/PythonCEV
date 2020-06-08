#Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
import math

 num = float(input('Escreva um número real qualquer:\n'))

print('A porção inteira de {} é {}!'.format( num, math.trunc( num)))