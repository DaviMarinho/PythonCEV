#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

coisa = input ('Escreva qualquer coisa que vier na sua cabeça:\n') 

print('O tipo primitivo dessa váriavel é\n', type(coisa))

print('{} É um número ?\n'.format(coisa), coisa.is numeric())
print('{} São letras ?\n'.format(coisa), coisa.isalpha())
print('{} Está em letras minusculas ?\n'.format(coisa), coisa.islower())
print('{} Está em letras maiúsculas ?\n'.format(coisa), coisa.isupper())
print('{} São somente espaços ?\n'.format(coisa), coisa.isspace())
print('{} Faz parte da tabela ASCII ?\n'.format(coisa), coisa.isascii())
print('{} Está capitalizada ?\n'.format(coisa), coisa.istitle())