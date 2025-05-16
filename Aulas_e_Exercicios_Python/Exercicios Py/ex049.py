"""Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, 
só que agora utilizando um laço for."""

print("Vamos analisas a tabuado do determinado numero que pedir. ")



"""for numero in (10):
    numero = int(input('Digite um numero: '))

    print(f'''
{numero} x {0} = {numero*0}
{numero} x {1} = {numero*1}
{numero} x {2} = {numero*2}
{numero} x {3} = {numero*3}
{numero} x {4} = {numero*4}
{numero} x {5} = {numero*5}
{numero} x {6} = {numero*6}
{numero} x {7} = {numero*7}
{numero} x {8} = {numero*8}
{numero} x {9} = {numero*9}
{numero} x {10} = {numero*10}''')"""
    
num = int(input("Digite um numero: "))

for c in range(1, 10):
    
    print(f"{num} x {c} = {num*c}")