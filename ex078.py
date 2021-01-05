valores = []
menor = maior = 0

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        menor = valores[cont]
        maior = valores[cont]
    else:
        if valores[cont] < menor:
            menor = valores[cont]
        if valores[cont] > maior:
            maior = valores[cont]

print('-'*4)
print(f'Você digitou os valores {valores}')

print(f'O maior valor é {maior} e está nas posições ', end='')
for c, v in enumerate(valores):
    if v == maior:
        print(f'{c}... ', end='')

print(f'\nO menor valor é {menor} e está nas posições ', end='')
for c, v in enumerate(valores):
    if v == menor:
        print(f'{c}... ', end='')

#for c, v in enumerate(valores):
#    if v == menor:
#        posMenores.append(c)
#    if v == maior:
#        posMaiores.append(c)