lista = list()
registro = dict()
listagols = []
partidagol = [[], []]
totgol = 0
while True:
    registro['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {registro["nome"]} jogou? '))
    for c in range(1, partidas + 1):
        gols = int(input((f'Quantos gols na {c}ª partida? ')))
        partidagol[0].append(c)
        partidagol[1].append(gols)
        listagols.append(gols)
        totgol += gols
    registro['gols'] = listagols[:]
    registro['total'] = totgol
    lista.append(registro.copy())
    listagols.clear()
    cont = str(input('Quer continuar? [S/N] '))
    if cont in 'Nn':
        break
print('-=' * 30)
print(f'{"cod":>3} {"nome":<15}{"gols":<15}{"total":<5}')
print('-' * 40)
for p, r in enumerate(lista):
    print(f'{p:>3} {r["nome"]:<15}{r["gols"]}  {r["total"]:<5}')
print('-' * 40)
while True:
    dados = int(input(('Mostrar dados de qual jogador? ')))
    if dados == 999:
        break
    if dados <= len(lista):
        print(f'-- LEVANTAMENTO DO JOGADOR {lista[dados]["nome"]}')
        for i, v in enumerate(lista):
            print(f'   No jogo {i + 1} fez {v["gols"]} gols.')
    else:
        print(f'ERRO! Não existe jogador com código {dados}! Tente Novamente')
print('<< VOLTE SEMPRE >>')





