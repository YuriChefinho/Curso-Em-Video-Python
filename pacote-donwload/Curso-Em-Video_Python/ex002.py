'''nome = input('Qual é seu nome? ')
print('prazer em te conhecer {:=^20}!'.format(nome))'''

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
ad = n1 + n2
su = n1 - n2
mu = n1 * n2
di = n1 / n2
po = n1 ** n2
redi =  n1 % n2
print('A soma é {} \nA subtração é {} \nO produto é {} \nA divisão é {:.3f}'.format(ad,su,mu,di))
print('A potencia é {} \nO resto da divisão é {}'.format(po,redi))