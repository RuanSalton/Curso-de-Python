peso = float(input('Quanto você pesa? '))
altura = float(input('Qual é a sua altura?'))
imc = peso / altura ** 2
if imc <= 18.5:
    status = 'Abaixo do peso'
elif imc > 18.5 and imc <= 25:
    status = 'Peso ideal'
elif imc > 25 and imc <= 30:
    status = 'Sobrepeso'
elif imc > 30 and imc <= 40:
    status = 'Obesidade'
else:
    status = 'Obesidade mórbida'
print('Seu IMC é de {:.1f} e o status do seu IMC é, {}.'.format(imc, status))
