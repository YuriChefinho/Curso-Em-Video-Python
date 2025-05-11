'''vamos criar um conversor de medidas '''
print('Vamos criar um conversor de medidas, transformando metros em: \n ',end=""
      'Km / Hm / Dam / Dm / Cm / Mm \n')
metros = float(input('Digite um valor em metros: '))

'''Se 1M tem 100Cm e 1M tem 0,001Km'''


mm = metros * 1000
cm = metros * 100
dm = metros * 10
dam = metros / 10
hm = metros / 100
km = metros / 1000
print('{}M se transformará em: \n{:.2f}Mm \n{:.2f}Cm \n{:.2f}Dm \n{:.2f}Dam \n{:.2f}Hm \n{:.2f}Km'.format(metros, mm, cm , dm, dam, hm, km))