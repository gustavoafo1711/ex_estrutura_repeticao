"""Escreva um algoritmo que leia  um número inteiro entre 100 e 999 e imprima na saída
cada um dos algarismos que compõem o número."""
print('==================== Separando os números ====================')
try:
    num = int(input('Digite um número entre 100 e 999: '))
    if 100 <= num <= 999:
        numstr = str(num)
        i = 0

        for i in range(len(numstr)):
            print(numstr[i])
            i += 1
    else:
        print('Informe um número entre 100 e 999!!!')
except ValueError as e:
    print(f'Ocorreu o seguinte erro: {e}')
