m = float(input('Qual é o valor em metros? '))
print('{} metros são {:.0f}cm e {:.0f}mm.'.format(m, (m*100), (m*1000)))
print('Convertendo {:.2f}m também em {:.2f}Km, {:.2f}hm, {:.2f}dam, {:.2f}dm.'.format(m, (m/1000), (m/100), (m/10), (m*10)))
