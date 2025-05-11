"""Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer
 e peça para o usuário escolher qual será a base de conversão:
 1 para binário, 2 para octal e 3 para hexadecimal."""

número = int(input("Digite um número inteiro: "))
print("""ESCOLHA UMA DAS BASES DE CONVERSÃO: 
      [1] Converter para BINÁRIO
      [2] Converter para OCTAL
      [3] Converter para HEXADECIMAL""")
opção = int(input('Sua opção: '))

if opção == 1:
    print('O número {} convertido para BINÁRIO é: {}'.format(número, bin(número)[2:])) #[2:] Fatiamento da estring

elif opção == 2:
    print('O número {} convertido para OCTAL é: {}'.format(número, oct(número)[2:]))

elif opção == 3:
    print ("O número {} convertido para EXADECIMAL é: {}".format(número, hex(número)[2:]))
else:
    ('Nada')