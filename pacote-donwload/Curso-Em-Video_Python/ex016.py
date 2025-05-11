
'''Crie um progama que leia no teclado um numero qualquer e mostre na tela a sua porção inteira'''

print('Vou ler um numero e mostrar sua porção inteira')
num = float(input('Digite um numero Real: '))
print('O numero digitado foi {} e sua parte inteira é {}'.format(num, int(num)))


from math import trunc
print('Vou outro numero e mostrar sua porção inteira: ')
num1 = float(input('Digite outro numero Real: '))
print('O numero digitado foi {} e a sua porção inteira é {}'.format(num1, trunc(num1)))