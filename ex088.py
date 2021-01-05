from random import randint
from time import sleep

print('-'*40)
print(f'{"JOGAR NA MEGA SENA":^40}')
print('-'*40)

jogos = []
qtde_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

for i in range(0, qtde_jogos):
    jogo = []
    for j in range(0, 6):
        while True:
            num = randint(1, 60)
            if num not in jogo:
                break
        jogo.append(num)
    jogos.append(jogo)

print('---------- SORTEANDO JOGOS ----------')
for i, jogo in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {sorted(jogo)}')
