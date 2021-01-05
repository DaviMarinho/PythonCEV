matriz = []

for i in range(0, 3):
    linha = []
    for j in range(0, 3):
        valor = int(input(f'Digite um valor para [{i}, {j}]: '))
        linha.append(valor)
    matriz.append(linha)

for i in range(0, 3):
    for j in range(0, 3):
            print(f'[{matriz[i][j] :^5}]', end='')
    print()
