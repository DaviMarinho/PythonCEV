#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#  IMC abaixo de 18,5: Abaixo do Peso
#  Entre 18,5 e 25: Peso Ideal
#  25 até 30: Sobrepeso
#  30 até 40: Obesidade
#  Acima de 40: Obesidade Mórbida

peso = float(input('Escreva seu peso atual:\n'))
altura = float(input('Escreva sua altura:\n'))

imc = peso/(altura*altura)

if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}!')
    print('Você está abaixo do peso ideal!')

if imc > 18.5 and imc <= 25:
    print(f'Seu IMC é {imc:.2f}!')
    print('Você está no peso ideal!')

if imc > 25 and imc <= 30:
    print(f'Seu IMC é {imc:.2f}!')
    print('Você está com sobrepeso!')

if imc > 30 and imc <= 40:
    print(f'Seu IMC é {imc:.2f}!')
    print('Você tem obesidade!')

if imc > 40:
    print(f'Seu IMC é {imc:.2f}!')
    print('Você tem obesidade morbida!')