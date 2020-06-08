#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual o valor do salário ?\n'))

if sal > 1250.00:
    aum = sal * 0.10
    sal = sal + aum
    print(f'O valor do salário com o aumento será de R${sal}')
if sal <= 1250.00:
    aum = sal * 0.15
    sal = sal + aum
    print(f'O valor do salário com o aumento será de R${sal}')