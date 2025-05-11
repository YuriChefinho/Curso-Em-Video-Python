'''O mesmo professor do desafio 19 quer criar uma ordem de apresentação do trabalho dos alunos,
crie um programa para ajudar ele a escolher essa ordem e mostre o nome dos 4 alunos'''
import random
print('vamos escolher em ordem os alunos para apresentação do trabalho: ')
a1 = str(input('Qual é o primeiro aluno?  '))
a2 = str(input('Qual é o segundo aluno?  '))
a3 = str(input('Qual é o terceiro aluno? '))
a4 = str(input('Qual é o quarto aluno?  '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(lista)