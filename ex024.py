#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Escreva o nome da cidade que você nasceu:\n')).strip()

cidade = cidade.lower()
cidade = cidade.split()

print('santo' in cidade[0])