'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
import random
from time import sleep
print('Vamos jogar um joguinho de advinhação dos numeros: ')
numero = int(input('escolha um numero entre 0 a 5: '))
print('Pensando em um numero...')
sleep(3)

cpu = random.randint(0,5)

if numero == cpu:
    print('o numero que a maquina escolheu foi {} e o seu numero foi  o mesmo {} \n*Você Venceu!!!!*'.format(cpu, numero))
else:
    print('O numero da maquina foi {} e o seu numero foi {} \n!!Desculpa Você Perdeu!!'.format(cpu, numero))
print('Obrigado pelo jogo!')