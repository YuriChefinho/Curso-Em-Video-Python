'''Faça um programa que peça o nome completo de uma pessoa e mostre o primeiro e ultimo nome separados'''
print('Vamos analizar seu nome completo:')
nome = str(input('Me informe seu nome completo: ')).strip()
separa = nome.split()
print(separa[0])
print(separa[len(separa)-1])
