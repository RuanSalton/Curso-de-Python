d = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos quilômetros você rodou? '))
pd = d * 60
pkm = km * 0.15
print('O valor do Seu aluguel ficou em R${:.2f}.'.format(pd + pkm))
