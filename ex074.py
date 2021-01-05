from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: {numeros}')

numeros = sorted(numeros)

print(f'Menor valor: {min(numeros)}')
print(f'Maior valor: {max(numeros)}')
#print(f'Menor valor: {numeros[0]}')
#print(f'Maior valor: {numeros[len(numeros)-1]}')
