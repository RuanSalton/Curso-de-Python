from time import sleep
def sajph(msg):
    print('\033[43m~' * (len(msg) + 4))
    print(f'\033[43m  {msg}')
    print('\033[43m~' * (len(msg) + 4))


def acesso(msg):
    print('\033[44m~' * (len(msg) + 4))
    print(f'\033[44m  {msg}')
    print('\033[44m~' * (len(msg) + 4))


def atelogo(msg):
    print('\033[41m~' * (len(msg) + 4))
    print(f'\033[41m  {msg}')
    print('\033[41m~' * (len(msg) + 4))


def helpme(msg):
    print('\033[7;40m' * (len(msg) + 4))
    print(f'\033[7;40m{msg.__doc__}')
    print('\033[7;40m\033[m', end='')
    sleep(1)


while True:
    sajph('SISTEMA DE AJUDA PyHELP')
    com = str(input('\033[mFunção ou Biblioteca > '))
    if com in 'FIMfim':
        break
    acesso(f'Acessando o manual do comando {com}')
    sleep(1)
    helpme(com)
atelogo('ATÉ LOGO!')
