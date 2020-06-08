#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Por favor, informe seu sexo: [M/F]\n')).strip().upper()

while sexo != 'M' and sexo != 'F':
    print('Sexo inválido!')
    sexo = str(input('Por favor, informe seu sexo: [M/F]\n')).strip().upper()

print('Sexo cadastrado com sucesso!')