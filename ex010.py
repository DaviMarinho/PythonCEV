#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. 1 Dolar = R$ 3,27

reais = float(input('Quantos reais você tem na carteira ?\n'))

dolares = (reais/3.27)

print('Com R${} você pode comprar exatamente U${:.2f}!' .format(reais, dolares))