'''Crie um programa que leia o nome completo de uma pessoa e mostre todas as letras maiusculas, minusculas,
quantas letras sem espaços, quantas letras tem em cada primeiro nome'''
print('Quero que me informe um nome completo para que eu possa fazer uma refatoração')
nome = str(input('Qual é seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome))
print(len(nome)- nome.count(' '))
print(nome.find(' '))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
