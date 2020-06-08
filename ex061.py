#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiroTermo = int(input('Escreva o primeiro termo da PA:\n'))
razao = int(input('Escreva a razão da PA:\n'))

while  primeiroTermo <  razao*10:
    print(f'{ primeiroTermo} ', end='')
    primeiroTermo +=  razao