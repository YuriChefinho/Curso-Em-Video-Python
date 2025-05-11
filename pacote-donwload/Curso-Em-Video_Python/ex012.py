'''Faça um algoritmo que leia o preço de um produto e  mostre o novo preço, com 5% de desconto. '''
print('Olá Você tem um cupom de 5% de desconto, vamos usar esse cupom? ')
preço = float(input('Qual o valor atual do produto: '))
desconto = preço * (5/100)
n_preço = preço - desconto
print('O Valor do produto é de R${:.2f} \nCom o desconto de 5% o novo valor é de R${:.2f} '.format(preço,n_preço))
