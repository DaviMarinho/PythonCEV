#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = 0
gol = list()

jogador['nome'] = str(input('Nome do Jogador:\n')).strip()
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou?\n'))

for i in range(0, jogador["partidas"]):
    gols = int(input(f'Quantos gols {jogador["nome"]} fez na partida {i+1}?\n'))
    gol.append(gols)
    jogador['gols'] = gol

jogador['total'] = sum(gol)

print(f'{jogador}')
print()
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print()

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for i in range(0, jogador["partidas"]):
    print(f'=> Na partida {i+1}, ele marcou {jogador["gols"][i]}')
print(f'Foi um total de {jogador["total"]} gols!')


