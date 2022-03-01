valor = float(input('Qual é o valor atual do imóvel? R$'))
renda = float(input('Quanto é a sua renda mensal? R$'))
tempo = int(input('Em quantos anos você precisa parcelar? '))
prestação = valor / (tempo * 12)
rmin = renda * 30 / 100
if prestação < rmin:
    print('Empréstimo aprovado!')
    print('O valor da prestação será de R${:.2f} por mês.'.format(prestação))
else:
    print('Sinto muito, mas sua renda de R${:.2f} não permite fazer este empréstimo.'.format(renda))
print('Muito obrigado por requisitar nossos seviços!')
