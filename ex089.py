alunos = []
aluno = []
notas = []
continua = ''

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2

    notas.append(nota1)
    notas.append(nota2)
    aluno.append(nome)
    aluno.append(notas[:])
    aluno.append(media)
    alunos.append(aluno[:])

    notas.clear()
    aluno.clear()

    continua = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continua != 'S':
        break

print('='*25)
print(f'{"No."} {"NOME":<10} {"MEDIA":<4}')
print('-'*20)

for i, aluno in enumerate(alunos):
    print(f'{i:<3} {aluno[0]:<10} {aluno[2]:>4.1f}')

while True:
    print('-' * 20)
    indice = int(input('Mostrar nota de qual aluno? (999 interrompe) '))
    if indice == 999:
        break

    print(f'Notas de {alunos[indice][0]} são {alunos[indice][1]}')
