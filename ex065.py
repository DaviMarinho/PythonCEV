#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

maiornum = 0
menornum = 999
soma = float(0)
cont = 0
resp = str('S')

while resp == 'S':
    num = int(input('Digite um número:\n'))
    resp = str(input('Você quer continuar ? [S/N]\n')).strip().upper()
    soma += num
    cont += 1
    if num > maiornum:
        maiornum = num
    if num < menornum:
        menornum = num

print(f'Você digitou {cont} números e a média foi {soma/cont:.2f}.')
print(f'O maior valor foi {maiornum} e o menor foi {menornum}.')
