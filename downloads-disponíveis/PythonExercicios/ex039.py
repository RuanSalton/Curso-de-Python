print('Central de alistamento no serviço militar:')
idade = int(input('Quantos anos você tem? '))
if idade > 18:
    print('Já passou do prazo do seu alistamento, siga para o setor de multa.')
    print('Você passou {} anos do prazo, sua multa será equivalente.'.format(idade - 18))
elif idade < 18:
    print('Ainda não chegou a hora de você se alistar')
    print('Volte daqui a {} anos.'.format(18 - idade))
else:
    print('Está na hora de se alistar, entre na fila.')
