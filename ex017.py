#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math

catetoo = float(input('Escreva o comprimento do Cateto Oposto:\n'))
catetoa = float(input('Escreva o comprimento do Cateto Adjacente:\n'))

hipotenusa = math.pow(catetoo, 2) + math.pow(catetoa, 2)

print('O valor da hipotenusa com os comprimentos dos catetos sendo {} e {} é {:.2f}'.format(catetoo, catetoa, math.sqrt(hipotenusa)))