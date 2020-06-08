#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere o.

soma = 0
cont = 0

for i in range(0,6):
     num = int(input(f'Escreva o {i+1}º número inteiro:\n'))
    if  num%2==0:
        soma +=  num
        cont += 1

print(f'Desses 6 números {cont} foram pares e a soma deles foi {soma}!')

