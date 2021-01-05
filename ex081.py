valores = []

while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)

    continua = str(input('Deseja continuar? [S/N] ')).upper()
    if continua not in 'SIM':
        break

valores.sort(reverse=True)

print('-'*10)
print(f'Você digitou {len(valores)} número(s)')
print(f'Os valores em ordem decrescente são: {valores}')
if 5 not in valores:
    print('O número 5 não faz parte da lista!')
else:
    print('O número 5 faz parte da lista')
