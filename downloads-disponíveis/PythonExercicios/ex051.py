print('=' * 30)
print('{:^30}'.format('10 TERMOS DE UMA PA'))
print('=' * 30)
prim = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
dec = prim +(10 - 1) * raz
for c in range(prim, dec, raz):
    print('{}'.format(c), end= ' → ')
print('Acabou!')
