'''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
 de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
 se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

nascimento = int(input('Informe seu ano de nascimento: '))
idade = 2025 - nascimento 

if idade < 17 and idade >12:
    print(f"SUA idade é {idade}, quando tiver 18 anos pode se alistar ")

elif idade >= 17 and idade <=19 :
    print(f"sua idade é {idade}, hora de se alistar")

elif idade >= 20:
    print(f"Sua idade é {idade}, já passou do tempo de se alistar")

elif idade <= 12:
    print(f"Sua idade é {idade}, Você ainda é uma criança")

print(idade)