#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = float(input('Escreva um ângulo qualquer:\n'))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('Para o ângulo de {}º o valor de seno é {:.2f}, de cosseno é {:.2f} e da tangente é {:.2f}'.format(angulo, seno, cosseno, tangente))
