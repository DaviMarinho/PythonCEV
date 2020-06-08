#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

import time

n = 0

n1 = float(input('Escreva o primeiro valor:\n'))
n2 = float(input('Escreva o segundo valor:\n'))

while n != 5:
    print('O que você deseja fazer com esses valores ?')
    n = int(input('[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\n'))
    if n == 1:
        print(f'{n1} + {n2} = {n1+n2}')
        print('=-==-==-==-==-==-==-==-=')
    if n == 2:
        print(f'{n1} * {n2} = {n1*n2}')
        print('=-==-==-==-==-==-==-==-=')
    if n == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
            print('=-==-==-==-==-==-==-==-=')
        else:
            print(f'{n2} é maior que {n1}')
            print('=-==-==-==-==-==-==-==-=')
    if n == 4:
        n1 = float(input('Escreva o primeiro valor:\n'))
        n2 = float(input('Escreva o segundo valor:\n'))
    time.sleep(3)