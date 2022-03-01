galera = list()
notas = list()
pessoa = list()
while True:
    pessoa.append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    pessoa.append(notas[:])
    notas.clear()
    galera.append(pessoa[:])
    pessoa.clear()
    cont = str(input('Quer continuar? [S/N] '))
    if cont in 'Nn':
        break
print('-=' * 30)
print('No. NOME         MÉDIA')
print('-' * 26)
for p, v in enumerate(galera):
    print(f'{p:<4}{galera[p][0]:<13}{(galera[p][1][0] + galera[p][1][1]) / 2:>5.1f}')
print('-' * 35)
while True:
    n = int(input('Mostras notas de qual aluno ? (999 para interromper) '))
    if n != 999:
        print(f'Notas de {galera[n][0]} são {galera[n][1]}')
    else:
        break
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
