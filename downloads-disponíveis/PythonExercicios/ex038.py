print('-=' * 11)
print('Comparador de números:')
print('-=' * 11)
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1 > n2:
    print('O número {} que é o primeiro, é o maior.'.format(n1))
elif n2 > n1:
    print('O número {} que é o segundo, é o maior.'.format(n2))
else:
    print('Não existe valor maior, os dois números são iguais.')
print('-=' * 11)
print('  Fim da comparação.')