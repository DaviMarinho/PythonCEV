#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Escreva seu nome completo:\n')).strip()

print('Muito prazer em te conhecer!')
nome = nome.split()
un = len(nome)
print('Seu primeiro nome é {}!'.format(nome[0]))
print('Seu último nome é {}!'.format(nome[un 1]))