#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#  Até 9 anos: MIRIM
#  Até 14 anos: INFANTIL
#  Até 19 anos: JÚNIOR
#  Até 25 anos: SÊNIOR
#  Acima de 25 anos: MASTER

import datetime

anoatual = datetime.date.today().year

ano = int(input('Escreva o seu ano de nascimento:\n'))

idade = anoatual   ano

if idade <= 9:
    print('Sua categoria é MIRIM')
if idade > 9 and idade <= 14:
    print('Sua categoria é INFANTIL')
if idade > 14 and idade <= 19:
    print('Sua categoria é JÚNIOR')
if idade > 19 and idade <= 25:
    print('Sua categoria é SÊNIOR')
if idade > 25:
    print('Sua categoria é MASTER')
