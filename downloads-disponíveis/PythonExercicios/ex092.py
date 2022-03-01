from datetime import date
ficha = dict()
atual = date.today().year
ficha['nome'] = str(input('Nome: '))
ficha['idade'] = atual - (int(input('Ano de Nascimento: ')))
ficha['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if ficha['ctps'] != 0:
    ficha['contratação'] = int(input('Ano de contratação: '))
    ficha['salário'] = float(input('Salário: R$'))
    apos = ((ficha['contratação']) + 35) - atual
    ficha['aposentadoria'] = apos + ficha['idade']
print('-=' * 40)
for k, v in ficha.items():
    print(f'{k} tem o valor {v}.')
