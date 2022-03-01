def leiaint(msg):
    while True:
        n = input(msg)
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
    return n


# Programa principal
print('-' * 30)
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
