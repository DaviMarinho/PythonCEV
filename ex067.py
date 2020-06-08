#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo. 

while True:
    num = int(input('Quer ver a tabuada de qual valor ?\n'))
    if num < 0:
        break
    for i in range(1,11):
        print(f'{num} x {i} = {num*i}')
    print('='*35)

print('='*35)
print('Programa encerrado. Volte sempre!')