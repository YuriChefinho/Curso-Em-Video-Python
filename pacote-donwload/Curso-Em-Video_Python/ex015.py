'''Escreva um programa de aluguel de carros, sendo que cada dia custra 60R$ e cada Km custa R$0.15'''
print('O valor do aluguel do carro é de R$60.00 + R$0.15 Por Km rodados: ')
dias = int(input('Quantos dias você gostarai de alugar o carro? '))
km = float(input('Quantos Km deseja rodar? '))
valorD = dias * 60
total  = valorD + (km * 0.15)
print('Voce quer alugar o carro por {} Dias e vai rodar {:.2f}Km o valor total a pagar é de R${:.2f}'.format(dias, km,total))