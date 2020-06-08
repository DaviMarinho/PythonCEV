#Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0

for i in range(0,501):
    if i%3==0 and i%2!=0:
        soma += i 
        cont +=1

print(f'A soma de todos os {cont} valores foi {soma}!')