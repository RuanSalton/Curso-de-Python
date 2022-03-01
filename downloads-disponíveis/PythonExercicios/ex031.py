km = int(input('Quantos Km tem até o seu destino? '))
if km <=200:
    print('Sua passagem vai custar R${:.2f}.'.format(km * 0.50))
else:
    print('Sua passagem vai custar R${:.2f}.'.format(km * 0.45))
    