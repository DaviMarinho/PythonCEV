#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

import datetime

def vota():
    ano = int(input('Em que ano você nasceu? '))
    anoAtual = datetime.date.today().year
    idade = anoAtual - ano
    return idade

idade = vota()

if idade > 18:
    print(f'Com {idade} anos: VOTA')

if idade > 15 and idade < 18:
    print(f'Com {idade} anos: OPCIONAL')

if idade < 16:
    print(f'Com {idade} anos: NÃO VOTA')