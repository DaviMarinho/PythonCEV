#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = float(input('Qual a velocidade atual do carro ?\n'))

if vel > 80:
    print('Você foi multado!!')
    multa = vel   80
    print('O valor da multa foi R${:.2f}!'.format(multa*7))
else:
    print('Você está dentro do limite de velocidade!')