#Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

aluno1 = input('Escreva o nome do primeiro aluno:\n')
aluno2 = input('Escreva o nome do segundo aluno:\n')
aluno3 = input('Escreva o nome do terceiro aluno:\n/')
aluno4 = input('Escreva o nome do quarto aluno:\n')

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)

print('A lista da ordem de apresentação é:\n{}'.format(lista))



