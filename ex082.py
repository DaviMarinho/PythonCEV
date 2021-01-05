valores = []
pares = []
impares = []

while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)

    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

    continua = str(input('Deseja continuar? [S/N] ')).upper()
    if continua not in 'SIM':
        break

print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
