print('Vamos dizer o dobro, o triplo e a raiz quadrada do numero que for digitado: ')
num = int(input('Digite qualquer numero: '))
dob = num * 2
tri = num * 3
raiz = num ** (1/2)
print('O dobro de {} é {} \nO triplo de {} e {} \nE a raiz de {} é {:.3}'.format(num, dob, num, tri, num, raiz))


'''Outra forma de calcular raiz quadrada'''
raizq = pow(num,(1/2))
print(raizq)
