#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Digite o valor atual da casa: \nR$'))
sal = float(input('Digite o valor do seu salário: \nR$'))
anos = int(input('Digite em quantos anos você deseja pagar a casa:\n'))

meses = anos*12

prest = casa/meses
salp = sal*0.30

if salp > prest:
    print('Parabéns! Você poderá comprar essa casa!')
    print('EMPRESTIMO ACEITO!')
else:
    print(f'Desculpe o valor da prestação dessa casa é de R${prest:.2f}, é maior que seu orçamento!')
    print('EMPRESTIMO NEGADO!')

