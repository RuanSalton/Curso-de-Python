média = 0
maior = 0
cont = 0
novelho = ''
for c in range(1, 5):
    print('-'* 5, ' {}ª PESSOA '.format(c), '-'* 5 )
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    média += idade
    if sexo == 'M':
        if c == 1:
            maior = idade
            novelho = nome
        else:
            if idade > maior:
                maior = idade
                novelho = nome
    if sexo == 'F' and idade < 20:
        cont += 1
print('A média de idade do grupo é de {:.1f} anos'.format(média / c))
print('O homem mais velho tem {} anos e se chama {}.'.format(maior, novelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(cont))
