#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

npc = int(random.randrange(0,5))

 num = int(input('Escreva um número entre 0 a 5 e veja se você acertou:\n'))

if npc ==  num:
    print('Você acertou, parabéns!!')
else:
    print('Você errou! O número que o computador escolheu foi {}'.format(npc))