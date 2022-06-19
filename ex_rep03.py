"""
Faça um programa que peça ao uauário para digitar 10 valores e some-os.
"""
i = 0
lst_num = 0

while i < 10:
    num = int(input("Digite um número: "))
    lst_num = lst_num + num
    i += 1

print(f'A soma dos números é {lst_num}')
