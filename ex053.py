#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

n = str(input('Escreva uma frase:\n')).strip().upper()
palavras = n.split()
junto = ''.join(palavras)
inverso = str('')

for i in range (0, len(junto)):
    inverso = junto[:: 1]

print(f'O inverso de {junto} é {inverso}!')
if inverso == junto:
    print(f'A frase {n} é um palíndromo!')
else:
    print(f'A frase {n} não é um palíndromo!')