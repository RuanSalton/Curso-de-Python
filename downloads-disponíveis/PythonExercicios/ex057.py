sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()
if sexo in 'MF':
    print('Sexo {} registrado com sucesso.'.format(sexo))
else:
    while sexo not in 'MmFf':
        sexo = str(input('Dados inválidos. Por favor, informe o seu sexo: ')).strip().upper()
        if sexo in 'MF':
            print('Sexo {} registrado com sucesso.'.format(sexo))
