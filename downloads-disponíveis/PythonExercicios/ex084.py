lista = []
pessoas = []
maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso Kg: ')))
    lista.append(pessoas[:])
    pessoas.clear()
    for i in range(len(lista)):
        if i == 1:
            maior = menor = lista[0][1]
        else:
            if lista[i][1] > maior:
                maior = lista[i][1]
            if lista[i][1] < menor:
                menor = lista[i][1]
    cont = str(input('Quer continuar? [S/N] '))
    if cont in 'Nn':
        break
print('-=' * 30)
print(f'Foram {len(lista)} pessoas cadastradas no total.')
print(f'O maior peso foi de {maior:.1f}Kg. Peso de ', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor:.1f}Kg. Peso de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
