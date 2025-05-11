'''Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''
import datetime
ano = int(input('Qual ano quer analisar: !!!Coloque 0 Para analizar o ano atual!!! '))

if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O Ano {} é BISSEXTO'.format(ano))
else:
    print('O Ano {} não é BISSEXTO'.format(ano))