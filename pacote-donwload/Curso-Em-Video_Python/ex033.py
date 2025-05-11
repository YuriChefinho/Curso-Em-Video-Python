'''Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
a = int(input('Digite um numero: '))
b = int (input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))

if a < b and a < c:
    menor = a

if b < a and b < c:
    menor = b

if c < a and c < b:
    menor = c


if a > b and a > c:
    maior = a

if b > a and b > c:
    maior = b

if c > a and c > b:
    maior = c


print('Maior {}'.format(maior))
print('menor {}'.format(menor))




'''if num1 > num2 and num1 > num3:
    print ('{} é maior que {} e {}'.format(num1, num2, num3))

if num1 > num3:
    print('{} e maior que {}'.format(num1, num3))'''