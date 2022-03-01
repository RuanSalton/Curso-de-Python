nome = ' '
preço = contpreço = valormil = barato = valor = 0
continua = 'S'
cont = 1
nomebarato = ' '
while True:
    nome = str(input('Nome do produto: ')).strip()
    preço = int(input('Preço do produto: R$'))
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua == 'S':
        cont += 1
    else:
        while continua not in 'SN':
            continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if preço >= 0:
        valor += 1
        if preço >= 1000:
            valormil += 1
    if valor == 1:
        nomebarato = nome
        barato = preço
    if preço < barato:
        nomebarato = nome
        barato = preço
    contpreço += preço
    if continua == 'N':
        break
print(f'O valor total gasto foi R${contpreço}')
print(f'Foram {valormil} produtos custando mais de R$1000,00.')
print(f'O produto mais barato foi o {nomebarato} e custou R${barato:.2f}')
