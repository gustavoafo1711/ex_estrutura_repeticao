"""
Faça um programa que calcule e mostre a soma dos 50 primeiros númeors pares.
"""
i = 1
soma = 0
while i <= 100:
    if i % 2 == 0:
        soma = soma + i
    i += 1

print(f'A soma dos 50 primeiros números pares (0 - 100) é: {soma}')
