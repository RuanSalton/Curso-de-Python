geral = [[], [], []]
spares = tercol = maior = 0
for p in range(0, 3):
    for v in range(0, 3):
        geral.append(int(input(f'Digite um valor para [{p}, {v}]: ')))
del geral[0:3]
print('-=' * 30)
for c, n in enumerate(geral):
    if c < 3:
        print(f'[ {n} ]',end='')
        if c == 2:
            tercol += n
        if n % 2 == 0:
            spares += n
print()
for c, n in enumerate(geral):
    if 3 <= c < 6:
        print(f'[ {n} ]',end='')
        if c == 3:
            maior = n
        else:
            if c > maior:
                maior = c
        if c == 5:
            tercol += n
        if n % 2 == 0:
            spares += n
print()
for c, n in enumerate(geral):
    if 6 <= c:
        print(f'[ {n} ]',end='')
        if c == 6 and c > maior:
            maior = c
        if c == 8:
            tercol += n
        if n % 2 == 0:
            spares += n
print()
print('-=' * 30)
print(f'A soma dos valores pares é {spares}.')
print(f'A soma dos valores da terceira coluna é {tercol}.')
print(f'O maior valor da segunda linha é {maior}.')
