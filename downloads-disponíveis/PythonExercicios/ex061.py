prim = int(input('Primeiro Termo da PA: '))
raz = int(input('Razão da PA: '))
termo = prim
cont = 1
while cont <= 10:
    print('{} → '.format(termo), end='')
    termo += raz
    cont += 1
print('Fim')
