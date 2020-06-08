#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Escreva o salário do funcionário:\n'))

print('O salário do funcionário com o aumento será de R${:.2f}!'.format(salario+salario*0.15))