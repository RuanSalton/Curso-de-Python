'''from random import choice
lista = ['Pedra', 'Papel', 'Tesoura']
pc = choice(lista)
print('\033[34m-=\033[m' * 10)
print('\033[31mVamos Jogar Jokempô?\033[m')
print('\033[34m-=\033[m' * 10)
usuario = str(input('Faça sua escolha: ')).strip().title()
print('Eu escolho {}.'.format(pc))
print('Você escolheu {}.'.format(usuario))
if pc == 'Pedra' and usuario == 'Tesoura' or pc == 'Tesoura' and usuario == 'Papel' or pc == 'Papel' and usuario == 'Pedra':
    print('Eu ganhei, você perdeu seu lixo !!!')
elif pc == usuario:
    print('Empate !!')
    print('Vamos jogar de novo.')
else:
    print('Parabéns, você me venceu.')
    print('Game over bitch.')'''
from random import randint
from time import sleep
itens = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
print('''Suas opções são:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print('Computador jogou {}.'.format(itens[computador]))
print('Jogador jogou {}.'.format(itens[jogador]))
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHOU')
    elif jogador == 2:
        print('COMPUTADOR GANHOU')
    else:
        print('Jogada inválida, jogue de novo.')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHOU')
    else:
        print('Jogada inválida, jogue de novo.')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR GANHOU')
    elif jogador == 1:
        print('COMPUTADOR GANHOU')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada inválida, jogue de novo.')
