'''Crie um programa que leia o nome de uma pessa completa e diga se tem "SILVA " no nome '''
print('esse é um programa de verificação: ')
silva = str(input('Porfavor digite seu nome: ')).strip()
print('Seu nome é {}'.format(silva))
print('Seu nome tem Silva? ','SILVA' in silva.upper())