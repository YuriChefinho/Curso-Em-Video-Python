'''Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''
from time import sleep
print('As passagens tem um valor cobrade de R$0.50 para viagem ate 200Km \nViagens com Km maior o custo é de R$0.45 por Km')
sleep(1)
viagem = float(input('Qual a distancia em Km da sua viagem? '))
print('!!!CALCULANDO O VALOR DA PASSAGEM!!!')
sleep(2)
if viagem <=200:
    val1 = viagem * 0.50
    print('A sua viagem tem {}Km logo o valor cobrado vai ser de R${:.2f}'.format(viagem, val1))
else:
    val2 = viagem * 0.45
    print('A Sua viagem tem {}Km Viagem longa, seu valor da passagem é R${:.2f}'.format(viagem, val2))
print('BOA VIAGEM!')