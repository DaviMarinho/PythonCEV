#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime

anoatual = datetime.date.today().year

maioridade = 0
menoridade = 0

for i in range(0,7):
    ano = int(input(f'Escreva o ano de nascimento da {i+1}ª pessoa:\n'))
    if (anoatual   ano) < 18:
        menoridade += 1
    else:
        maioridade += 1

print(f'Temos {menoridade} pessoas menores de 18 anos!')
print(f'E temos {maioridade} pessoas maiores de 18 anos!')