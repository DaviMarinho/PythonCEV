#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Escreva o primeiro valor:\n'))
n2 = int(input('Escreva o segundo valor:\n'))
n3 = int(input('Escreva o terceiro valor:\n'))

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2

if n3 > n1 and n3 > n2:
    maior = n3

menor = n1

if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3

print('O menor número foi {}!'.format(menor))
print('O maior número foi {}!'.format(maior))