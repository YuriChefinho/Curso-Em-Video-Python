'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa
 que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER'''

import datetime

print('Vamos ler seu ano de nascimento e mostrar a categoria de idade para a competição: ')

ano_nascimento = int(input("Em qual ano você nasceu? "))
data = datetime.date.today().year



if data - ano_nascimento <= 9:
    print(f'Você tem {data - ano_nascimento} e a sua categoria é MIRIM:' )

elif data - ano_nascimento > 9 and data - ano_nascimento <= 14:
    print(f'Você tem {data - ano_nascimento} e a sua categoria é INFANTIL:')

elif  data - ano_nascimento > 14 and data - ano_nascimento <= 19:
    print(f'Você tem {data - ano_nascimento} e a sua categoria é JÚNIOR:')

elif  data - ano_nascimento > 19 and data - ano_nascimento <= 25:
    print(f'Você tem {data - ano_nascimento} e a sua categoria é SÉNIOR:')

elif  data - ano_nascimento > 25:
    print(f'Você tem {data - ano_nascimento} e a sua categoria é MASTER:')
    
