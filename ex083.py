expressao = str(input('Digite a expressão matemática: '))
lista = []

for letra in expressao:
    lista.append(letra)

if lista.count('(') == lista.count(')'):
    print('Expressão válida!')
else:
    print('Expressão inválida!')
