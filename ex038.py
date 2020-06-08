#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare os. mostrando na tela uma mensagem:
#  O primeiro valor é maior
#  O segundo valor é maior
#  Não existe valor maior, os dois são iguais

 num1 = int(input('Escreva o primeiro valor:\n'))
 num2 = int(input('Escreva o segundo valor:\n'))

if  num1 >  num2:
    print('O primeiro valor é maior!')
elif  num2 >  num1:
    print('O segundo valor é maior!')
else:
    print('Os valores são iguais!')