#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Escreva o preço do produto:\n'))

print('O produto com 5% de desconto custará R${:.2f}!'.format(preco preco*0.05))

