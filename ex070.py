#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato. 

soma = 0
maiores = 0
menor = 999
nomeMenor = ''

while True:
    nome = str(input('Digite o nome do produto:\n')).strip()
    preco = float(input('Digite o preço do produto:\n'))
    soma += preco
    if preco > 1000:
        maiores += 1
    if preco < menor:
        menor = preco
        nomeMenor = nome
    resposta = str(input('Você quer continuar a cadastrar produtos ?[S/N]\n')).strip().upper()
    if resposta == 'N':
        break

print(f'O preço total da compra foi de R${soma:.2f}!')
print(f'{maiores} produto(s) custaram mais de 1000 reais!')
print(f'O produto mais barato foi o/a {nomeMenor} custando R${menor:.2f}!')