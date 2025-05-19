'''Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.'''
from time import sleep

lista = ["eu", "vc", "ela", "nos", "somos"]
for i, nome in enumerate(lista):
    
    print(i, nome)
    sleep(.3)

for nome in range(7):
    lista = ["eu", "vc", "ela", "nos", "somos"]
    print(nome, lista)

dict_alunos = {'joão':5, 'ana':9}
for aluno, nota in dict_alunos.items():
    print(f"O(a) aluno(a) {aluno} tirou nota {nota} na prova")