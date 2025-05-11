'''tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 5:
    print('carro nomo')
else:
    print('carro velho')
print('carro nomo' if tempo <=5 else 'carro velho')'''

nome = str(input('Qual é seu nome? ')).strip()
if 'yuri'  in nome:
    print('Que nome maravilhoso {} '.format(nome))
else:
    print('Olá {}, Tudo bem?'.format(nome))
print('Prazer em te conhecer!')

