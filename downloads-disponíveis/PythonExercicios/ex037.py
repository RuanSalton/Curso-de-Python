print('\033[34m-=\033[m' * 17)
num = int(input('Digite um número inteiro qualquer: '))
print('Considere:')
print('[1] para Binário')
print('[2] para Octal')
print('[3] para Hexadecimal')
base = int(input('Escolha a base de conversão: '))
if base == 1:
    print('O número {} em binário fica: {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('O número {} em Octal fica: {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('O número {} em Hexadecimal fica : {}'.format(num, hex(num)[2:]))
