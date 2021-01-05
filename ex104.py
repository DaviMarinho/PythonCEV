#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt('Digite um n: ')

def leiaInt(frase):
    while True:
        print(f'{frase}', end='')
        n = str(input(''))
        if n.isnumeric() == False:
            print('ERRO! Digite um número inteiro válido')
        else:
            break
    return n


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}!')