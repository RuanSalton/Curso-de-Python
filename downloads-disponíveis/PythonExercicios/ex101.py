from datetime import date


def voto(ano):
    print(f'Com {idade} anos: ', end='')
    if 18 < idade < 65:
        print('VOTO OBRIGATÓRIO.')
    elif idade < 16:
        print('NÃO VOTA.')
    else:
        print('VOTO OPCIONAL.')


# Programa principal
print('=' * 30)
ano = int(input('Em que ano você nasceu? '))
atual = date.today().year
idade = atual - ano
voto(ano)
