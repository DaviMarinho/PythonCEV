#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

viagem = float(input('Qual a distância da sua viagem ?\n'))

if viagem <= 200:
    print('O valor da sua viagem é de R${:.2f}'.format(viagem*0.5))
else:
    print('O valor da sua viagem é de R${:.2f}'.format(viagem*0.45))