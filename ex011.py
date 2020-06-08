#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Escreva a largura da parede:\n'))
altura = float(input('Escreva a altura da parede:\n'))

area = altura*largura

print('A quantidade de tinta necessaria para pintar {}m² de parede será de {} litros de tinta.'.format(area, area/2))