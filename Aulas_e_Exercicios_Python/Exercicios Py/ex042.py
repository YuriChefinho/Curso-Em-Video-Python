'''Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

a = float(input('Qual o tamanho do primeiro lado? '))
b = float(input('Qual o tamanho do segundo lado? '))
c = float(input('Qual o tamanho do terceiro lado? '))



''' if a == b and a != c and a + b >= c or a == c and a != b and a + c >= b or b == c and b != a  and b + c >= a  :
 print("ISÓCELES")

elif a == b == c:
 print('EQUILÁTERO')

elif a != b != c and a + b >= c and b + c >= a and a + c >= b:
 print('ESCALENO')

else:
    print('Esses Valores Não formão um triangulo')'''



if a + b > c and a + c > b and b + c > a :
    print('Os Valores digitados podem formar um TRIÂNGULO')

    if a == b and a != c or a == c and a != b or b == c != a:
        print("ISÓCELES")
    
    elif a == b == c:
        print('EQUILÁTERO')
   
    elif a != b != c and a != c:
        print('ESCALENO')

else:
    print('Esses Valores Não formão um triângulo')


# Falhei na lógica