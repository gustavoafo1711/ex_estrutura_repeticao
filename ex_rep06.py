"""
Faça um programa que leia um número inteiro positivo N e imprima todos os números
naturais de 0 até N em ordem decrescente.
"""


def soma_n():
    try:
        num = int(input("Informe um número inteiro positivo: "))
        for i in range(num, -1, -1):
            print(i)
    except ValueError as err:
        print(f'Ocorreu o seguinte erro: {err}')
        soma_n()

soma_n()
