from random import randint
from time import sleep
print('-' * 30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-' * 30)
numeros = list()
qjogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'{f" SORTEANDO {qjogos} JOGOS ":=^30}')
for c in range(0, qjogos):
    for n in range(0, 6):
        numeros.append(randint(1, 61))
    numeros.sort()
    print(f'Jogo {c + 1}: {numeros}')
    numeros.clear()
    sleep(1)
print(F'{"< BOA SORTE >":=^30}')
print(numeros)
