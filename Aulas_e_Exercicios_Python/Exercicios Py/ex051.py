"""Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão."""

from time import sleep
print('Vamos ler um termo e mostrar a razão de PA')

termo = int(input('Primeiro termo: '))
razão = int(input('Digite a razão: '))
décimo = termo + (11 - 1) * razão
for c in range(termo, décimo,razão):
   
    print(c, '↓')
    sleep(.05)
