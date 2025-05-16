
"""Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
 Se o valor digitado for ímpar, desconsidere-o."""

soma = 0
contador = 0
for c in range(1,7):
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        soma += numero
        contador += 1


        print(f'Você digitou {contador} numeros pares e a soma entre eles é {soma} ')
        
     
    else:
        print('IMPAR')

print(f'Você digitou {contador} numeros PARES e a soma entre eles é {soma}')

