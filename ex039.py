#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

idade = int(input('Escreva sua idade:\n'))

if idade < 18:
    print('Você ainda irá se alistar!')
    print(f'Faltam {18 idade} ano(s) para você ser obrigado a se alistar.')
elif idade == 18:
    print('Está no momento exato de você ir se alistar!')
else:
    print('O tempo de você se alistar já passou!')
    print(f'Passaram {idade 18} ano(s) do prazo correto.')