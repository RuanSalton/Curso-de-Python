registro = dict()
registro['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {registro["nome"]} jogou? '))
listagols = []
partidagol = [[], []]
registro['gols'] = listagols
totgol = 0
for c in range(1, partidas + 1):
    gols = int(input((f'Quantos gols na {c}ª partida? ')))
    partidagol[0].append(c)
    partidagol[1].append(gols)
    listagols.append(gols)
    totgol += gols
registro['total'] = totgol
print('-=' * 30)
print(registro)
print('-=' * 30)
for k, v in registro.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {registro["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(registro['gols']):
    print(f'=> Na partida {partidagol[0][i]}, fez {partidagol[1][i]} gols.')
print(f'Foi um total de {totgol} gols.')
