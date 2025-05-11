'''Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''
from time import sleep
num = int(input('Digite um numero inteiro: '))
sleep(1)
print('!!!INDENTIFICANDO O NUMERO!!!')
sleep(2)
if num %2 == 1:
    print('O numero {} é !!IMPAR!!'.format(num))

else:
    print('O numero {} é !!PAR!!'.format(num))