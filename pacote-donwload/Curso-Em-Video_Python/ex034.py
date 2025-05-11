'''Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
 Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''
from time import sleep
salario = float(input('Qual é seu salário atual? '))

sleep(1)
print('!!!ANALIZANDO O AUMENTO!!!')
sleep(2)
if salario > 1250:
    n_salario = salario + salario * (10/100)
    print(
        'Salario atual R${:.2f} \nComo seu salario é acima de R$1250.00 \n' \
        'Você só vai ter um aumento de 10% salario atual R${:.2f}'.format(salario, n_salario))

else:
    n_salario = salario + salario * (15/100)
    print('Seu salario é de R${:.2f} \n Como seu salario é inferior a R$1250.00 \n' \
    'Você vai ganhar um bonus de 15% no aumento do salario! \nSalario atual R${:.2f}'.format(salario, n_salario))
    
