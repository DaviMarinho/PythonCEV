#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
    -> Calcular o fatorial de um número
    Args:
        num (int): O número a ser calculado o fatorial
        show (bool, optional): Mostrar ou não a conta. Defaults to False.
    Returns:
        Inteiro: Retorna o fatorial do número
    """
    fact = 1
    for i in range(num, 0, -1):
        if show:
            if i != 1:
                print(f'{i} x', end=' ')
            if i == 1:
                print(f'{i} =', end=' ')
        fact *= i 
    return fact


help(fatorial)