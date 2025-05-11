"""Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais"""

print('Vamos comparar dois numero e falar qual o maior e qual o menor: ')
número_1 = int(input("Digite um numero: "))
número_2 = int(input("Digite outro numero: "))

if número_1 > número_2:
    print(f'O primeiro numero é maior: {número_1}')

elif número_2 > número_1:
    print(f"o segundo número é maior: {número_2}")

elif número_1 == número_2:
    print(f"O número {número_1} é o número {número_2} São iguais")

else:
    #número_1 = str(número_1)
    #número_2 = str(número_2)

    print("Você não digitou valores validos, tente novamente")