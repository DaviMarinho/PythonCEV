#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Qual a quantidade de Km rodados pelo carro ?\n'))
dias = float(input('Qual a quantidade de dias que o carro ficou alugado ?\n'))

total = (km*0.15) + (dias*60)

print('O total a pagar tendo rodado {}Km e {} dias é de R${:.2f}!'.format(km, dias, total))