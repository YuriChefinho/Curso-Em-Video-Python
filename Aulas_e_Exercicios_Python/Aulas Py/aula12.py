nome = str(input('Qual é seu nome? ')).strip().capitalize()

if nome.upper() == 'YURI':
    print('Que nome Bonito {}!'.format(nome))

elif nome.upper() == 'PEDRO' or nome == 'MARIA' or nome == 'JOÃO':
    print('Seu nome é bem popular no Brasil {}!'.format(nome))

elif nome.upper() in 'LAIS AGHATA AMANDA BRENDA':
    print('Belo nome feminino {}!'.format(nome))

else:
    print('Seu nome é bem normal {}!'.format(nome.capitalize()))

print('Tenha um bom dia!')