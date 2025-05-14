'''Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
 mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO'''

print('Vamos calcular sua media, porfavor digite suas notas: ')
nota1 = float(input('Qual foi sua primeira nota? '))
nota2 = float(input('Qual foi sua segunda nota? '))

média = (nota1 + nota2) /2
if média < 5:
    print(f'Sua Media foi {média:.1f} Média abaixo de 5.0: REPROVADO')

elif média >=5 and média <= 6.9:
    print(f'A sua media foi {média:.1f}  Média entre 5.0 e 6.9: RECUPERAÇÃO')

else:
    print(f'Sua media foi {média:.1f} Média 7.0 ou superior: APROVADO*** ')