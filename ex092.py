#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date

funcionario = {}
dataAtual = date.today()

funcionario['nome'] = str(input('Nome do funcionario:\n')).strip()
funcionario['nascimento'] = int(input('Ano de nascimento do funcionario:\n'))
funcionario['carteira'] = int(input('Número da carteira de trabalho (0 não tem):\n'))
if funcionario['carteira'] != 0:
    funcionario['contratação'] = int(input('Ano de contratação:\n'))
    funcionario['salário'] = float(input('Salário:\nR$'))

print('-='*30)
idade = dataAtual.year - funcionario['nascimento']
aposentar = (funcionario['contratação'] - funcionario["nascimento"]) + 35

for k, v in funcionario.items():
    print(f'    -{k} tem o valor {v}')
print(f'    -aposentadoria tem o valor {aposentar}')

