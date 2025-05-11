'''Crie um programa que converta Graus ºC para Graus ºF'''
print('Vamos converter a temperatura ºC para ºF')
grau_c = float(input('Quantos graus esta fazendo hoje? '))
grau_f = grau_c * 1.8 + 32
print('A temperatura ta de {:.1f}ºC equivalente a {}ºF'.format(grau_c, grau_f))
