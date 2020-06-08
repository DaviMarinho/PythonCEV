#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiroTermo = int(input('Escreva o primeiro termo da PA:\n'))
razao = int(input('Escreva a razão da PA:\n'))

termos = 1
parada = 10

while primeiroTermo < razao*10:
    print(f'{primeiroTermo} -> ', end='')
    primeiroTermo +=  razao
print('Pausa')

while termos != 0:
    termos = int(input('Quantos termos você quer mostrar a mais?\n'))
    parada += termos
    while primeiroTermo < razao*parada:
        print(f'{primeiroTermo} -> ', end='')
        primeiroTermo +=  razao
    if termos != 0:
        print('Pausa')

print(f'Progressão finalizada com {parada} termos mostrados!')