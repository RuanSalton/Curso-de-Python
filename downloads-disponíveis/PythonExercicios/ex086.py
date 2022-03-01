geral = [[], [], []]
for p in range(0, 3):
    for v in range(0, 3):
        geral.append(int(input(f'Digite um valor para [{p}, {v}]: ')))
del geral[0:3]
print('-=' * 30)
for c, n in enumerate(geral):
    if c < 3:
        print(f'[{n:^5}]',end='')
print()
for c, n in enumerate(geral):
    if 3 <= c < 6:
        print(f'[{n:^5}]',end='')
print()
for c, n in enumerate(geral):
    if 6 <= c:
        print(f'[{n:^5}]',end='')
