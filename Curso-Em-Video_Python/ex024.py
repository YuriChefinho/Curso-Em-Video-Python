'''Crie um programa que pergunte o nome da cidade a um usuario e verifique se começa com "SANTO" '''
print('Vamos verificar o nome da sua cidade: ')
cidade = str(input('Qual é o nome da sua cidade? ')).strip()
print('santo' in cidade)
print(cidade[:5].upper()=='SANTO')