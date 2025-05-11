'''Crie um programa que converta real para dolar'''
print('Vamos converter o valor em Real para Dolar: ')
real = float(input('Digite quantos Reail você quer converter: '))
dolar = real / 5.673
print('Acotação do Dolar atual é de 1$ = R$5.68, Logo: \nR${:.2f} é igual a ${:.2f}'.format(real,dolar))
