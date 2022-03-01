from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
op = int(input('Qual é a sua opção? '))
while op != 5:
    if op == 1:
        soma = v1 + v2
        print('A soma entre {} e {} é {}.'.format(v1, v2, soma))
    elif op == 2:
        mult = v1 * v2
        print('A multiplicação entre {} e {} é {}'.format(v1, v2, mult))
    elif op == 3:
        if v1 > v2:
            maior = v1
        else:
            maior = v2
        print('Entre {} e {}, {} é o maior valor.'.format(v1, v2, maior))
    elif op == 4:
        print('Informe os números novamente:')
        v1 = int(input('Primeiro número: '))
        v2 = int(input('Segundo número: '))
    elif op >= 6:
        print('Opção inválida. Tente novamente.')
    print('=-='* 10)
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    op = int(input('Qual é a sua opção? '))
print('Finalizando...')
print('=-='* 10)
sleep(2)
print('Programa encerrado. Volte sempre!')
