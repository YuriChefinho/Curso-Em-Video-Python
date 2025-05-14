'''ESTRUTURA DE REPETIÇÃO'''
from time import sleep

'''for c in range(10):
    
    print(c)
    sleep(1)'''

'''for a in range(10):
    if a == 2 or a == 4:
        continue
    print(a)
    sleep(1)'''

'''for c in range(0, 100):
    print('Olá')
    sleep(0.1)
print("FIM")'''

"""inicio = int(input('Digite um numero: '))
fim = int(input('Digite um numero: '))
passos = int(input('Digite um numero: '))
'''for n in range( n):
    print(n)
    sleep(0.3)'''

for contador in range(inicio, fim+1, passos ):
    print(contador)
    
print('Fim')"""
n = 0
for contador in range(0, 4):
    valor = int(input('Digite um valor:'))
    n = n + valor
    print(n) 
print('Fim Valor')
