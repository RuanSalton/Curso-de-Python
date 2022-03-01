from random import randint
from time import sleep
resultados = dict()
lista = list()
print('Valores sorteados:')
for c in range(1, 5):
    resultados['nome'] = f'jogador{c}'
    resultados['dado'] = randint(1, 6)
    print(f'O {resultados["nome"]} tirou {resultados["dado"]}')
    sleep(1)
    lista.append(resultados.copy())

print('Ranking dos Jogadores:')
for p, c in enumerate(lista):
    print(f'{p + 1}º lugar: {c["nome"]} com {c["dado"]}')
    sleep(1)
