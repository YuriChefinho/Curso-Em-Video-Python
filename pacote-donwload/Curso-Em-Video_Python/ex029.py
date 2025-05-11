'''Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''
from time import sleep
velo = float(input('Qual velocidade o carro esta? '))
multa = (velo - 80) * 7
if velo > 80:
    print('Sua velocidade foi de {}Km/h Voce ultrapassou a velocidade permitida de 80Km/h:'.format(velo))
    sleep(2)
    print('!!!Você Foi Multado!!! \nO valor da sua multa foi de R${:.2f} equivalente a R$7,00 por Km\h ultrapassado'.format(multa))
else:
    print('Esta tudo OK com seu limite de velocidade, Bom dia!')
