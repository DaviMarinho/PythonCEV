#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

import random

def sorteando(sorteados):
    print(f'Sorteando 5 valores da lista: ')
    for i in range(0,5):
        print(f'{sorteados[i]}', end=' ')
    print(f'PRONTO!')

def somando(sorteados):
    soma = 0
    for i in range(0,5):
        if sorteados[i] % 2 == 0:
            soma += sorteados[i]
    print(f'Somando os valores pares de {sorteados}, temos {soma}')

sorteados = []

for i in range(0,5):
    sorteados.append(random.randint(0,10))

sorteando(sorteados)
somando(sorteados)