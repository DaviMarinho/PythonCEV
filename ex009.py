#Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

 num = int(input('Escreva o valor que você deseja para a tabuada:\n'))

print('                 ')
for i in range(1,11):
    print('{} x {} = {}'.format( num, i,  num*i))
print('                 ')
