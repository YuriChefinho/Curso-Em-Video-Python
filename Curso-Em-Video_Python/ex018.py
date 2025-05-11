'''Escreva um programa que leia um ângulo qualquer e mostre na tela seu valor de seno,
cosseno, tangente desse ângulo '''
import math
print('eu vou dizer o seno, cosseno, e a tangente de qualquer angulo: ')
ângulo = float(input('Digite um angulo: '))
rad = math.radians(ângulo)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print('o angulo foi {}° \nSeu seno é {:.2f} \nCosseno é {:.2f} \nE a Tangene é {:.2f}'.format(ângulo, sen, cos, tan))
