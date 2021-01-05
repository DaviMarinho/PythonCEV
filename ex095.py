#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogador = {}
jogadores = []
partidas = []
gols = 0
gol = list()
resposta = ''

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador:\n')).strip()
    partidas.clear()
    total = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for i in range(0, total):
        partidas.append(int(input(f'     Quantos gols {jogador["nome"]} fez na partida {i+1}? ')))
    gol.append(gols)
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    jogadores.append(jogador.copy())

    resposta = str(input('Quer continuar ? (S/N)\n')).strip().upper()
    while resposta != 'N':
        if resposta in 'SN':
            break
        print('ERRO! Responda somente com (S/N)')
        resposta = str(input('Quer continuar ? (S/N)\n')).strip().upper()

    if resposta == 'N':
        break

print('-'*50)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*50)

for k, v in enumerate(jogadores):
    print(f'{(k):<3} ', end='')
    for dados in v.values():
        print(f'{str(dados):<15}', end='')
    print()
print('-'*50)

while True:
    busca = int(input('Deseja mostrar os dados de qual jogador ? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'Não existe jogador com código {busca}! Tente novamente.')
    else:
        print(f' -- INFORMAÇÕES DO JOGADOR {jogadores[busca]["nome"]}: --')
        for p, g in enumerate(jogadores[busca]['gols']):
            print(f'    No jogo {p+1} fez {g} gols!')
print('Volte Sempre!')

