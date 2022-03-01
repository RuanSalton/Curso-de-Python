n = cont = soma = maior = menor = média = 0
r = 'S'
while r in 'S':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
média = soma / cont
print('Você digitou {} números e a média foi {}.'.format(cont, média))
print('O maior valor foi {} e o menor foi {}.'.format(maior,menor))
