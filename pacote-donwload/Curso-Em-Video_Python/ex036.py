'''Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

print('Vamos fazer uma analise de credito')
casa = float(input('Qual valor da casa? '))
salário = float(input('QUal valor é seu salario? '))
anos = int(input('Quantos anos pretende pagar? '))


10000
1000
10
prestação = casa / (anos*12)
mínimo = salário * 30 / 100
print('30% do seu salario é R${:.2f} '.format(mínimo))
print('O valor da casa é de R${:.2f} seu salario é de R${:.2f} e a prestação vai sair a R${:.2f}'.format(casa, salário, prestação))

if prestação <= mínimo:
    print("empréstimo pode ser !!!CONCEDIDO!!!")
else:
    print('Emprestimo !!!NEGADO!!!')