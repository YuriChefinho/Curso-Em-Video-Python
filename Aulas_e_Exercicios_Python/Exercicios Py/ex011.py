'''Faça um programa que leia a altura e a largura de uma parede em metros,
calcule a sua área e a quantidade de tintas nescessária para pinta-la.
sabemos que cada litro de tinta, pinta uma área de 2M².'''

print('Vamos calcular a quantidade de tintas gasta em uma parede por M²')
altura = float(input('Digite a Altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = largura * altura
tinta = area / 2
print('A sua área são de {:.2f}M² \nCada 1 litro de tinta cobre 2M² logo {}M² vai gastar {:.2f}l de tinta'.format(area,area,tinta))

