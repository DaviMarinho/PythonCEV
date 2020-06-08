#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 

num = int(input('Quantos termos da sequência de Fibonacci você quer mostrar ?\n'))

i = 0
ultimoNumero = 0
anterior = 1
soma = 0

print('0 -> ', end='')
while i < num-1:
    soma = ultimoNumero + anterior
    anterior = ultimoNumero
    ultimoNumero = soma
    print(f'{soma} ' , end='-> ')
    i += 1
print('Fim')