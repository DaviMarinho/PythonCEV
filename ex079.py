valores = []
continua = 's'

while True:
    valor = int(input('Digite o valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado!')
    else:
        print('Valor duplicado! Não foi adicionado')

    continua = str(input('Deseja continuar? [S/N] ')).upper()
    if continua not in 'SIM':
        break

valores.sort()
print(f'Você digitou os valores {valores}')
