#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#  à vista dinheiro/cheque: 10% de desconto
#  à vista no cartão: 5% de desconto
#  em até 2x no cartão: preço formal
#  3x ou mais no cartão: 20% de juros:

produto = float(input('Digite o valor a ser pago no produto:\nR$'))

print('FORMAS DE PAGAMENTO:')
print('[ 1 ]   À VISTA DINHEIRO OU CHEQUE')
print('[ 2 ]   À VISTA CARTÃO')
print('[ 3 ]   2x NO CARTÃO')
print('[ 4 ]   3x NO CARTÃO OU MAIS')

opcao = int(input('Escolha a opção que melhor te satisfaz:\n'))

if opcao == 1:
    print(f'Sua compra de R${produto:.2} vai custar {produto (produto*0.10):.2f}')

elif opcao == 2:
    print(f'Sua compra de R${produto:.2} vai custar {produto (produto*0.05):.2f}')

elif opcao == 3:
        print(f'Seu produto vai ser dividido em duas parcelas de R${produto/2:.2f}')
        print(f'Sua compra não recebeu alteração de preço e continuara custando R${produto:.2f}')

elif opcao == 4:
    parcelas = int(input('Em quantas parcelas vai comprar ?\n'))
    print(f'Você vai pagar em {parcelas} de R${(produto+(produto*0.20))/parcelas:.2f}')
    print(f'Sua compra de R${produto:.2f} vai custar {produto+(produto*0.20):.2f}')

