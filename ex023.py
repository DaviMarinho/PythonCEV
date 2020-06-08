#Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

 num = str(input('Escreva um número entre 0 a 9999:\n')).strip()

print('{} tem:'.format( num))

if len( num) == 4:
    print('Unidade: {}'.format( num[3]))
    print('Dezena: {}'.format( num[2]))
    print('Centena: {}'.format( num[1]))
    print('Milhar: {}'.format( num[0]))

if len( num) == 3:
    print('Unidade: {}'.format( num[2]))
    print('Dezena: {}'.format( num[1]))
    print('Centena: {}'.format( num[0]))
    print('Milhar: 0')

if len( num) == 2:
    print('Unidade: {}'.format( num[1]))
    print('Dezena: {}'.format( num[0]))
    print('Centena: 0')
    print('Milhar: 0')

if len( num) == 1:
    print('Unidade: {}'.format( num[0]))
    print('Dezena: 0')
    print('Centena: 0')
    print('Milhar: 0')
