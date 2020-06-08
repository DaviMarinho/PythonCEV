#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

pessoas = int(input('Quantas pessoas você deseja analisar ?\n'))

mediaidade = 0
idademaior = 0
nomemaior = ''
 numM = 0

for i in range(0, pessoas):
    print(f'     {i+1}ª PESSOA     ')
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo[M/F]:')).strip()

    mediaidade += idade

    if sexo == 'M' and idade > idademaior:
        nomemaior = nome
        idademaior = idade

    if sexo == 'F' and idade < 20:
         numM += 1

print(f'A media da idade do grupo é {mediaidade/pessoas:.2f} anos!')
print(f'O homem mais velho se chama {nomemaior} e ele tem {idademaior} anos!')
print(f'E ao todo são { numM} mulheres com menos de 20 anos!')

