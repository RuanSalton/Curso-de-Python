ficha = {}
ficha['Nome'] = str(input('Nome: '))
ficha['Media'] = float(input(f'Média de {ficha["Nome"]}: '))
if ficha['Media'] >= 7:
    ficha['Situação'] = 'Aprovado'
elif 5 <= ficha['Media'] < 7:
    ficha['Situação'] = 'Recuperação'
else:
    ficha['Situação'] = 'Reprovado'
for k, v in ficha.items():
    print(f'{k} é igual a {v}.')
