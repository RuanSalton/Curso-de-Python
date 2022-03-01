from random import randint
print('''Sou o seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que consegue adivinhar qual foi?''')
num = randint(0, 10)
usu = int(input('Qual é o seu palpite? '))
cont = 0
while usu != num:
    if usu < num:
        print('Mais... Tente mais uma vez.')
    if usu > num:
        print('Menos... Tente mais uma vez.')
    usu = int(input('Qual é o seu palpite? '))
    cont += 1
print('Acertou com {} tentativas. Parabéns!'.format(cont + 1))
