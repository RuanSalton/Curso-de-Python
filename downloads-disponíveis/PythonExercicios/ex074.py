from random import randint
print(f'Os valores sorteados foram:', end=' ')
cont = maior = menor = 0
for c in range(0, 5):
    sort = randint(0, 10)
    print(sort, end=' ')
    cont += 1
    if cont == 1:
        maior = sort
        menor = sort
    if sort > maior:
        maior = sort
    if sort < menor:
        menor = sort
print(f'\nO maior valor sorteado foi: {maior}')
print(f'O menor valor sorteado foi: {menor}')
