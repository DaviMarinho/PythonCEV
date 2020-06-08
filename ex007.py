#Exercício Python 007: Desenvolva um programa que leia duas notas de um aluno, calcule e mostre sua média.

nota1 = float(input('Escreva a primeira nota do aluno:\n'))
nota2 = float(input('Escreva a segunda nota do aluno:\n'))

notaf = nota1 + nota2

print('A média do aluno foi {:.1f}!' .format(notaf/2))