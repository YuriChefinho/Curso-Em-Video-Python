'''Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
 indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''

from time import sleep
print('Contagem regressiva para os fogos de de artifícios \nVamos contar comigo? ')
for contagem in range(10, 0-1, -1):
    print(contagem)
    sleep(1)

print('BOOM, BOOM, POOOW!!!!!')