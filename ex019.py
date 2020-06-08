#Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random

aluno1 = input('Escreva o nome do primeiro aluno:\n')
aluno2 = input('Escreva o nome do segundo aluno:\n')
aluno3 = input('Escreva o nome do terceiro aluno:\n')
aluno4 = input('Escreva o nome do quarto aluno:\n')

lista = [aluno1, aluno2, aluno3, aluno4]

sorteado = random.choice(lista)

print('O aluno sorteado foi {}'.format(sorteado))

