lista = (int(input('Digite um valor: ')),
         int(input('Digite outro valor: ')),
         int(input('Digite mais um valor: ')),
         int(input('Digite o último valor: ')))
print(f'Você digitou os valores {lista}')
print(f'O valor 9 apareceu {lista.count(9)} vezes')
if 3 in lista:
    print(f'O valor 3 apareceu na {lista.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print('Os valores pares digitados foram ', end='')
for c in lista:
    if c % 2 == 0:
        print(c, end=' ')
