print('=======FIM DO PROGRAMA=======')
idade = contsexo = contconti = contidade = conthomem = contmulher = 0
sexo = 'M'
continua = 'S'
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo in 'MF':
        contsexo +=1
    else:
        while sexo not in 'MF':
            sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        conthomem += 1
    if sexo == 'F':
        if idade <= 20:
            contmulher += 1
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua in 'SN':
        contconti +=1
    else:
        while continua not in 'SN':
            continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        contidade += 1
    if continua == 'N':
        break
print(f'{contidade} pessoas tem maior de idade.')
print(f'Tiveram {conthomem} homens cadastrados.')
print(f'Tiveram {contmulher} mulheres com menos de 20 anos.')
