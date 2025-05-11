'''Crie um programa que reajuste o salario do funcionario em 15%'''
print('A partir de hoje você ganhara um almento salarial de 15%: ')
salario = float(input('Qual é seu salario atual? '))
n_salario = salario + (salario * 15/100)
print('Seu salario atual é de R${:.2f} : \nCom o acréscimo de 15% seu nomo salario é R${:.2f}'.format(salario, n_salario))
