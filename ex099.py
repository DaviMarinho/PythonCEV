#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

import random

def maior(* valor):
    total = maior = 0
    print('\nAnalisando os valores passados: ')
    for num in valor:
        print(f'{num}', end=' ')
        if total == 0:
            maior = num
        else:
            if num > maior:
                maior = num
        total += 1
    print(f'Foram informados {total} números: ')
    print(f'O maior valor foi {maior}!')


maior(2, 9, 4, 5, 7, 1)
maior(4, 9, 0)
maior()
