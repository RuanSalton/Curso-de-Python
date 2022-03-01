vel = int(input('Qual é a sua velocidade? '))
multa = (vel - 80) * 7
if vel >80:
    print('Você foi multado e o valor da multa é de R${},00.'.format(multa))
else:
    print('Continue sua viagem com cuidado.')
