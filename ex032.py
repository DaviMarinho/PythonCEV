#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

import datetime

ano = int(input('Escreva o ano que desejar:\nSe quiser saber se o ano atual é bissexto, digite 0.\n'))

if ano == 0:
    ano = datetime.date.today().year

if ano % 400 == 0:
    print('{} é bissexto!!'.format(ano))
elif ano % 4 == 0 and ano % 100 != 0:
    print('{} é bissexto!!'.format(ano))
else:
    print('{} não é bissexto!!'.format(ano))