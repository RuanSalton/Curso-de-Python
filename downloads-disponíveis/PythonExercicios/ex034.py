'''sal = float(input('Qual o salário atual do funcionário? R$'))
if sal <= 1250.00:
    print('Seu aumento será de R${:.2f} totalizando R${:.2f}.'.format(sal * 0.15, (sal * 0.15) + sal))
else:
    print('Seu aumento será de R${:.2f} totalizando R${:.2f}'.format(sal * 0.1, (sal * 0.1) + sal))'''
salário = float(input('Quanto é o salário atual do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem tinha um salário de R${:.2f} vai passar a receber R${:.2f}.'.format(salário, novo))
