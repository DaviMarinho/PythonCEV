#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
#  O nome com todas as letras maiúsculas e minúsculas.
#  Quantas letras ao todo (sem considerar espaços).
#  Quantas letras tem o primeiro nome.

nome = str(input('Escreva seu nome:\n')).strip()

print('O nome com todas as letras maiúsculas: {}.'.format(nome.upper()))
print('O nome com todas as letras minúsculas: {}.'.format(nome.lower()))
print('Quantas letras tem ao todo: {} letras.'.format(len(nome.replace(' ',''))))
nome = nome.split()
print('Quantas letras somente no primeiro nome: {} letras.'.format(len(nome[0])))