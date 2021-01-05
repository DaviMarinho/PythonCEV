palavras = ('frango', 'hamburguer', 'doritos', 'cookie', 'carbonara', 'nuggets', 'salgado')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos', end=' ')
    for cont in range(0, len(palavra)):
        if palavra[cont].lower() in 'aáàãâeéêiíâoóôõuúû':
            print(palavra[cont], end=' ')
