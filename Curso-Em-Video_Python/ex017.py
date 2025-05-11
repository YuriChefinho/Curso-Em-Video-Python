'''Faça um programa que leia o comprimento do cateto oposto e o cateto adjacente de um triangulo retangulo,
 calcule e mostre o comprimento da hipotenusa'''
import math
print('vamos ler a soma dos catetos e dizer o valor da hipotenusa: ')
cat_o = float(input('Digite o valor do cateto oposto: '))
cat_a = float(input('Digite o valor do cateto adjacente'))
'''soma = (cat_o **2 + cat_a **2)'''
soma = math.pow(cat_o,2) + math.pow(cat_a,2)
hip = math.sqrt(soma)
print('A soma do cateto oposto {} e do cateto adjacente{} = hipotenusa {:.2f}'.format(cat_o, cat_a, hip))
print(math.hypot(cat_o, cat_a))