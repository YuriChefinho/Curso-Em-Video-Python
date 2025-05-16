'''Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

número = int(input('Digite um número: '))

total = 0
for c in range(1, número +1):
    if número %  c == 0:
        print('\033[33m', end="")
        total =+ 1
    else:
        print ('\033[31m', end='')
    print(f'{c}', end=" ")

print(f'\nO  numero {número} foi divisível {total} vezes.')