#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:

#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada

from time import sleep

def contagem(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo =1
    if inicio > fim:
        passo = passo * -1
    for i in range(inicio, fim, passo):
        print(f'{i}', end=' ', flush=True)
        sleep(0.5)
    print('FIM!')


def printalinha():
    print(f'-='*30)


printalinha()
print(f'Contagem de 1 até 10 de 1 em 1:')
contagem(1, 11, 1)
printalinha()

print(f'Contagem 10 até 0 de 2 em 2:')
contagem(10, -1, 2)
printalinha()

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
printalinha()

contagem(inicio, fim-1, passo)