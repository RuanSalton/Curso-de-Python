from datetime import date
ano = date.today().year
cont = 0
cont2 = 0
for c in range(1, 8):
    nascimento = int(input('Qual é o ano de nascimento da {}° pessoa? '.format(c)))
    idade = ano - nascimento
    if idade < 21:
        cont += 1
    else:
        cont2 += 1
print('{} pessoas ainda são menor de idade.'.format(cont))
print('{} pessoas já são maiores de idade.'.format(cont2))
