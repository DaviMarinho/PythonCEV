#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

 num = int(input('Escreva um número inteiro para ser convertido:\n'))

escolha = int(input('Escolha a opção que você quer converter: \n[ 1 ]   Binário\n[ 2 ]   Octal\n[ 3 ]   Hexadecimal\n'))

if escolha == 1:
    print(f'{ num} convertido para BÍNARIO fica : {bin( num)[2:]}')
elif escolha == 2:
    print(f'{ num} convertido para OCTAL fica : {oct( num)[2:]}')
elif escolha == 3:
    print(f'{ num} convertido para HEXADECIMAL fica : {hex( num)[2:]}')
else:
    print('Opção inválida!')