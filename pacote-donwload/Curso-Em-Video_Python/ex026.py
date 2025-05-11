'''Crie um programa pra indentificar quantos 'A' tem em uma frase, qual primeira posição e a ultima'''
print('Vamos indentificar quantos á tem nessa frase, qual a primeira possição e a ultima')
texto = str(input('Escreva a frase que vc quer indentificar: ')).strip().upper()
print('A letra A aparece {} na prase'.format(texto.count('A')))
print('A primeira letra á se encontra na posição {}'.format(texto.find('A')+1))
print('A ultima posição da letra A fica {}'.format(texto.rfind('A')+1))