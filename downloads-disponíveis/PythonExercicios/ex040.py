nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
média = (nota1 + nota2) / 2
if média < 5.0:
    print('Sua média foi de {:.2f}, você foi REPROVADO !!'.format(média))
elif média >= 5.0 and média < 7:
    print('Sua média foi de {:.2f}, você ficou de RECUPERAÇÃO !!'.format(média))
else:
    print('Parabéns !!')
    print('Sua média foi de {:.2f}, e você foi APROVADO !!!'.format(média))
    