'''Vamos calcular a media de um aluno'''
print('Use 3 notas de um aluno, e calcule a media entre elas: ')
nota1 = float(input('Qual foi sua primeira nota? '))
nota2 = float(input('Qual foi sua segunda nota? '))
nota3 = float(input('Qual foi sua terceira nota? '))
to_nota = nota1 + nota2 + nota3
media = to_nota / 3
print('Sua primeira nota foi {} \nSua segunda nota foi {} \nSua terceira nota foi {} \n Amedia entre as notas é de {:.1f}'.format(nota1, nota2, nota3, media))