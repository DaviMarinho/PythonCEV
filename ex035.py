#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

v1 = float(input('Escreva o valor do primeiro segmento:\n'))
v2 = float(input('Escreva o valor do segundo segmento:\n'))
v3 = float(input('Escreva o valor do terceiro segmento:\n'))

if ((v2   v3) < v1 and v1 < v2 + v3) and ((v1   v3) < v2 and v2 < v1 + v3) and ((v1   v2) < v3 and v3 < v1 + v2):
    print('Esses segmentos formam um triângulo!')
    if v1 != v2 != v3:
        print('\033[1;35mTriângulo escaleno!')
    if v1 == v2 != v3:
        print('\033[1;35mTriângulo isósceles!')
    if v1 == v2 == v3:
        print('\033[1;35mTriângulo equilátero!')
else:
    print('Esses segmentos não formam um triângulo!')