#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = float(0)
menor = float(9999)

for i in range(0,5):
    peso = float(input(f'Escreva o peso da {i+1}ª pessoa:\n'))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'O maior peso listado foi {maior:.2f}!')
print(f'O menor peso listado foi {menor:.2f}!')