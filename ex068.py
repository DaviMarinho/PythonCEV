#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. 

import random

print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)

resultado = ''
cont = 0

while True:
    num = int(input('Digite um valor:\n'))
    escolha = str(input('Você quer par ou ímpar ? [P/I]\n')).strip().upper()
    pc = random.randint(1,10)
    soma = num + pc
    if soma % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'
    print('=-'*40)
    print(f'Você jogou {num} e o computador jogou {pc}. O resultado deu {resultado}')
    print('=-'*40)
    if resultado == escolha:
        print('VOCÊ GANHOU!!')
        print('=-'*20)
        cont += 1
    else:
        print('Você perdeu =(')
        print('=-'*20)
        break

print(f'GAME OVER! Você ganhou {cont} vezes!')
print('=-'*20)
