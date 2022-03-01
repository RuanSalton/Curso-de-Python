from random import randint
cont = 0
while True:
    print('-='*20)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('-='*20)
    pc = randint(0, 11)
    v = int(input('Diga um valor: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    soma = pc + v
    print('-'*30)
    if soma % 2 == 0:
        jogo = 'PAR'
    else:
        jogo = 'ÍMPAR'
    print(f'Você jogou {v} e o computador jogou {pc}. Total de {soma} deu {jogo}.')
    print('-'*30)
    if pi == 'P' and jogo == 'PAR':
        print('Você VENCEU !')
        print('Vamos jogar novamente...')
    else:
        print('Você PERDEU !')
        print('-='*20)
        break
    cont += 1
print(f'GAME OVER ! Você venceu {cont} vezes.')
