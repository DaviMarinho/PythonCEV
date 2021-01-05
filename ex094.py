#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: 
#A) Quantas pessoas foram cadastradas
#B) A média de idade
#C) Uma lista com as mulheres
#D) Uma lista de pessoas com idade acima da média

galera = list()
pessoa = {}
soma = 0
resposta = ''
sexo = ''


while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome:\n')).strip()

    pessoa['sexo'] = str(input('Sexo: [M/F]\n')).strip().upper()
    while True:
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Responda somente com (M/F)!')
        pessoa['sexo'] = str(input('Sexo: [M/F]\n')).strip().upper()

    pessoa['idade'] = int(input('Idade:\n'))
    soma += pessoa['idade']

    galera.append(pessoa.copy())

    resposta = str(input('Quer continuar ? (S/N)\n')).strip().upper()
    while resposta != 'N':
        if resposta in 'SN':
            break
        print('ERRO! Responda somente com (S/N)')
        resposta = str(input('Quer continuar ? (S/N)\n')).strip().upper()

    if resposta == 'N':
        break

print(f'Ao todo temos {len(galera)} pessoas cadastradas!')
print(f'A média de idade é {soma/len(galera)}')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média:\n', end='')
for p in galera:
    if p['idade'] > (soma/len(galera)):
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()