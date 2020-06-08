#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

import random
import time

print('SUAS OPÇÕES:')
print('[ 0 ]   PEDRA')
print('[ 1 ]   PAPEL')
print('[ 2 ]   TESOURA')

opcao = int(input('Qual sua jogada ?\n'))
jogador = str('')

lista = ['Pedra','Papel','Tesoura']

computador = random.choice(lista)

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('POO!!!')
time.sleep(1)

if opcao == 0:
    jogador = 'Pedra'
    if computador == 'Pedra':
        print(f'Você jogou {jogador}\nO computador jogou {computador}')
        print('EMPATOU')
    if computador == 'Papel':
        print(f'Você jogou {jogador}\nO computador jogou {computador}')
        print('VOCÊ PERDEU')
    if computador == 'Tesoura':
        print(f'Você jogou {jogador}\nO computador jogou {computador}')
        print('VOCÊ VENCEU')

if opcao == 1:
    jogador = 'Papel'
    if computador == 'Papel':
        print(f'Você jogou {jogador}\nO computador jogou {computador}')
        print('EMPATOU')
    if computador == 'Tesoura':
        print(f'Você jogou {jogador}\nO computador jogou {computador}')
        print('VOCÊ PERDEU')
    if computador == 'Pedra':
        print(f'Você jogou {jogador}\nO computador jogou {computador}')
        print('VOCÊ VENCEU')

if opcao == 2:
    jogador = 'Tesoura'
    if computador == 'Tesoura':
        print(f'Você jogou {jogador}\nO computador jogou {computador}')
        print('EMPATOU')
    if computador == 'Pedra':
        print(f'Você jogou {jogador}\nO computador jogou {computador}')
        print('VOCÊ PERDEU')
    if computador == 'Papel':
        print(f'Você jogou {jogador}\nO computador jogou {computador}')
        print('VOCÊ VENCEU')

