"""
Faça um programa que leia 10 inteiros positivos, ignorando os não positivos
e imprima sua média.
"""
lst = []
i = 0

try:
    while i < 10:
        num = float(input("Informe um número: "))
        if num >= 0:
            lst.append(num)
            i += 1
        else:
            print("Informe um número positivo.")
except ValueError as err:
    print(f'Informe um número inteiro.\nOcorreu o seguinte erro: {err}')

soma = 0
for x in range(len(lst)):
    soma = soma + lst[x]

print(soma)
