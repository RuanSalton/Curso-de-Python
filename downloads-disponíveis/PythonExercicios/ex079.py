lista = []
while True:
    valor = (int(input('Digite um valor: ')))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! não vou adicionar...')
    while True:
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continua not in 'SN':
            print('Opção inválida.',end=' ')
        else:
            break
    if continua == 'N':
        break
print('-='* 30)
lista.sort()
print(f'Você digitou os valores {lista}')
