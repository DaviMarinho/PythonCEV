pessoas = []
dados =[]
continua = 'n'
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    pessoas.append(dados[:])

    if len(pessoas) == 1:
        maior = menor = dados[1]
    else:
        if dados[1] < menor:
            menor = dados[1]
        if dados[1] > maior:
            maior = dados[1]

    dados.clear()

    continua = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if continua not in 'SIM':
        break

print('-'*5)
print(f'Você cadastrou {len(pessoas)} pessoa(s)')

print(f'O maior peso foi de {maior:.1f}kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]', end=' ')

print(f'\nO menor peso foi de {menor:.1f}kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]', end=' ')
