cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove','vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {cont[num]}.')
        while True:
            continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
            if continuar not in 'SN':
                print('Opção inválida. ',end= '')
            if continuar in 'SN':
                break
        if continuar == 'N':
            break
    else:
        print('Tente novamente.', end= ' ')
print('Fim do programa.')
