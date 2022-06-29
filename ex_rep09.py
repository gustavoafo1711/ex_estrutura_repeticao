"""
Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número,
com exceção dele próprio.
Ex: A soma dos divisores do número 66 é: 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78

"""

try:
    num = int(input('Digite um número inteiro positivo: '))
    i = 2
    soma = 0
    lst = []

    """
    for z in range(num):
        if (num % i) == 0:
            print(num / i)
        i += 1
    """

    while i <= num:
        if (num % i) == 0:
            lst.append(num / i)
            soma = soma + (num / i)
        i += 1

    print(f'Os divisores de {num} são: {lst}')
    print(f'A soma dos divisores de {num} é: {soma}')
except ValueError as err:
    print(f'Ocorreu o seguinte erro: {err}')
