"""Faça um algoritmo que leia certa quantidade de números e imprima o maior deles
e quantas vezes o maior número foi lido. a quantidade de números a serem lidos deve ser
fornecido pelo usuário.
"""

print("=========================================")

qtdd = int(input("Informe a quantidade de numeros a serem lidos: "))

lst_num = []
for i in range(qtdd):
    num = int(input("Informe um numero: "))
    lst_num.append(num)
    qtdd += 1

print(f'\nO maior numero digitado foi: {max(lst_num)}')
n = lst_num.count(max(lst_num))
print(f'A quantidade devezes que o maior número foi repetido é {n}')
