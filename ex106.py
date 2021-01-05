#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.

def ajuda():
    frase = str(input('Sistema de ajuda\nFunção ou biblioteca'))
    return frase

frase = ajuda()
help(frase)