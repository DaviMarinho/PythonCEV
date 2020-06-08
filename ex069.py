#Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos. 

maiores = 0
homens = 0
mulheresmaiores = 0

while True:
    idade = int(input('Quantos anos têm ?\n'))
    sexo = str(input('Qual o sexo ? [M/F]\n')).strip().upper()
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade > 20:
        mulheresmaiores += 1
    resultado = str(input('Deseja continuar ? [S/N]\n')).strip().upper()
    if resultado == 'N':
        break

print(f'{maiores} pessoa(s) tem mais de 18 anos!')
print(f'{homens} pessoa(s) é/são homens!')
print(f'{mulheresmaiores} pessoa(s) é/são mulheres maiores de 20 anos!')