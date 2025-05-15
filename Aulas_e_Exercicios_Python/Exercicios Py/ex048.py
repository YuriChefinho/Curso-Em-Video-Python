'''Exercício Python 48: Faça um programa que calcule a soma entre todos os números
 que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''

from time import sleep
soma =0
quantidade = 0
for contador in range(1, 500+1, 2):
    if contador % 3 == 0: # contador divisível por 3
        soma = soma + contador
        quantidade = quantidade + 1
        sleep(0.2)
        print(soma)
print(f'a Soma entre todos os {quantidade} numeros tem um total de {soma}')