aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] < 7:
    aluno['situacao'] = 'Reprovado'
else:
    aluno['situacao'] = 'Aprovado'

print(f'Nome é {aluno["nome"]}')
print(f'Média é {aluno["media"]}')
print(f'Situação final é {aluno["situacao"]}')
