'''Faça  um programa que leia de 0 a 9999 e mostre na tela cada um dos digitos separados.'''
print('vamos ler de 0 a 9999 cada gidito separado: ')
numero = int(input('Digite um valor entre 0 a 9999: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('Unidade',u)
print('Dezena', d)
print('Centena', c)
print('Milhar', m)
