#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

import math

num = int(input('Escreva um número para saber o seu fatorial:\n'))

fact num = math.factorial( num)

i = 0

print(f'{ num}! =', end='')
while i <  num: 
    print(f' { num - i}', end='')
    if i !=  num-1:
        print(' x', end='')
    i += 1
print(f' = {fact num}')


