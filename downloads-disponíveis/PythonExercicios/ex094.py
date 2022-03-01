lista = list()
pessoa = {}
midade = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] '))
    pessoa['idade'] = int(input('Idade: '))
    lista.append(pessoa.copy())
    midade += pessoa['idade']
    cont = str(input('Quer continuar? [S/N] '))
    if cont in 'Nn':
        break
média = midade / len(lista)
print('-=' * 30)
print(f'- O grupo tem {len(lista)} pessoas.')
print(f'- A média de idade é de {média:.2f} anos.')
print('- As mulheres cadastradas foram: ',end='')
for p in lista:
    if p['sexo'] in 'Ff':
        print(p['nome'], end=' ')
print()
print('- Lista das pessoas que estão acima da média:')
for p in lista:
    if p['idade'] > média:
        for k, v in p.items():
            print(f'{k} = {v}; ',end='')
        print()
print('<< ENCERRADO >>')
