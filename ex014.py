#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

tempc = float(input('Escreva a temperatura em graus Celsius:\n'))

tempf = ((tempc/5)*9)+32

print('A temperatura de {}ºC é de {:.2f}ºF!'.format(tempc, tempf))