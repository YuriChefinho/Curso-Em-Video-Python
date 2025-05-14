'''Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida'''


peso = float(input('Qual é seu peso (Kg)'))
altura = float(input('Qual é sua altura? (m)'))
imc = peso / (altura ** 2)
print(f'Seu IMC é {imc:.2f}')
if imc > 40:
    print('Cuidado, !!!OBESIDADE MÓRBIDA!!!')

elif imc <= 40 and imc >= 30:
    print('Melhor se cuidar, Você esta OBESO')

elif imc < 30 and imc >= 25:
    print('Você esta com SOBREPESO')

elif imc < 25 and imc >= 18.5:
    print('seu PESO é IDEAL')

else:
    print('Melhor se alimentar, Você está ABAIXO DO PESO')