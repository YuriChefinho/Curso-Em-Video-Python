'''um professor quer sortear um dos alunos para apagar o quadro, crie um programa para ajudar o professor a sortear 
o nome de um dos alunos escolhidos'''
import random
print('vamos sortear quem vai ser o aluno a apagar o quadro: ')
aluno1 = str(input('Qual o nome do primeiro aluno: '))
aluno2 = str(input('Qual o nome do segundo aluno: '))
aluno3 = str(input('Qual o nome do terceiro aluno: '))
lista = [aluno1, aluno2, aluno3]
sorteio = random.choice(lista)
print('O aluno sorteado foi {}'.format(sorteio))