#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

 num = int(input('Escreva o primeiro termo da PA:\n'))
 num1 = int(input('Escreva a razão da PA:\n'))
cont = 0

for i in range( num, num1*10, num1):
    print(i)