#Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

 num = float(input('Digite um número para ver sua tabuada:\n'))

for i in range(0, 11):
    print(f'{ num} x {i} = { num*i}')

