#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random

contador = 0

npc = int(random.randrange(0,10))

print('Olá, eu me chamo BMO, e sou seu computador!')
print('Eu acabei de pensar em um número.')
print('Será que você consegue adivinhar qual número foi ?')
 num = int(input('Escreva um número entre 0 a 10 e veja se você consegue adivinhar esse número:\n'))

while npc !=  num:
    if  num < npc:
        print('Mais... tente mais uma vez.')
         num = int(input('Qual é o seu palpite ?\n'))
    if  num > npc:
        print('Menos... tente mais uma vez.')
         num = int(input('Qual é o seu palpite ?\n'))
    contador += 1

print(f'Você acertou em {contador+1} tentativa(s), PARABÉNS!!')
