numeros = (int(input('Primeiro valor: ')), int(input('Segundo valor: ')),
            int(input('Terceiro valor: ')), int(input('Último valor: ')))
print(f'Você digitou os valores {numeros}')

print('----')
print(f'O número 9 aparece {numeros.count(9)} vez(es)')

print('----')
#if 3 not in numeros:
if numeros.count(3) == 0:
    print('Não há número 3 em nenhuma posição')
else:
    print(f'O número 3 aparece na {numeros.index(3)+1}ª posição')

print('----')
print('Os valores pares digitados foram: ', end='')
for num in numeros:
    if num % 2 == 0:
        print(f'{num}', end=' ')
print('')
