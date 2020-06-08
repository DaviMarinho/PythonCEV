#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

cinquenta = 0
vinte = 0
dez = 0
um = 0
valor = 0

valor = int(input('Digite o valor que você deseja sacar:\n'))

while True:
    if valor >= 50:
        valor -= 50
        cinquenta += 1
    if valor >= 20 and valor < 50:
        valor -= 20
        vinte += 1
    if valor >= 10 and valor < 20:
        valor -= 10
        dez += 1
    if valor >= 1 and valor < 10:
        valor -= 1
        um += 1
    if valor == 0:
        break

if cinquenta > 0:
    print(f'{cinquenta} cédulas de R$50')
if vinte > 0:
    print(f'{vinte} cédulas de R$20')
if dez > 0:
    print(f'{dez} cédulas de R$10')
if um > 0:
    print(f'{um} cédulas de R$1')

print('Volte sempre ao Banco DMC!')