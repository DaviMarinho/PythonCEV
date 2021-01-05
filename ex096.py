#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def calculaArea(largura, comprimento):
    areaM = float(largura * comprimento)
    print(f'A área do terreno {largura}x{comprimento} é de {areaM}m².')


largura = float(input(f'Largura(m): '))
comprimento = float(input(f'Comprimento(m): '))
calculaArea(largura, comprimento)

