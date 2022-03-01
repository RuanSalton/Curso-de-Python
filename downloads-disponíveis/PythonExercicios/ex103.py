def ficha(n, g):
    if n == '':
        n = '<desconhecido>'
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    return f'O jogador {n} fez {g} gol(s) no campeonato.'


# Programa principal
print('-' * 30)
nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Número de gols: '))
print(ficha(nome, gols))

