from datetime import date
data = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = data - nasc
if idade <= 9:
    cat = 'Mirim'
elif idade > 9 and idade <= 14:
    cat = 'Infantil'
elif idade > 14 and idade <= 19:
    cat = 'Junior'
elif idade == 20:
    cat = 'Sênior'
else:
    cat = 'Master'
print('Você tem {} anos e sua categoria é {}'.format(idade, cat))
