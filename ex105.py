#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

#- Quantidade de notas
#- A maior nota
#- A menor nota
#- A média da turma
#- A situação (opcional)

#Adicione também as docstrings dessa função para consulta pelo desenvolvedor.  

def notas(*num, sit=0):
    nota = {}
    medias = []
    medias = num
    maior = 0
    menor = 999
    media = float(0)
    total = 0
    for i in range(0, len(medias)):
        total += 1
        if num[i] > maior:
            maior = num[i]
        if num[i] < menor:
            menor = num[i]
        media += num[i]
    nota['total'] = total 
    nota['maior'] = maior
    nota['menor'] = menor
    nota['media'] = (media/total)
    if sit == True:
        if nota['media'] < 5:
            nota['situação'] = 'RUIM'
        if nota['media'] > 5 and nota['media'] < 7:
            nota['situação'] = 'REGULAR'
        if nota['media'] > 7:
            nota['situação'] = 'OTIMO'
    return nota

#def notas(*n, sit=False):
    #nota['total'] = len(n) 
    #nota['maior'] = max(n)
    #nota['menor'] = min(n)
    #nota['media'] = sum(n)/len(n)

resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)