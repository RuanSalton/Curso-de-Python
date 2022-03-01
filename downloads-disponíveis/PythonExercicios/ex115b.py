while True:
    print('-=' * 20)
    print(f'{"Menu Principal":^40}')
    print('-=' * 20)
    print('1- Ver pessoas Cadastradas'
          '\n2- Cadastrar nova pessoa'
          '\n3- Sair do sistema')
    print('-=' * 20)
    while True:
        try:
            op = int(input('Sua opção: '))
        except:
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        else:
            if op <= 0 or op > 3:
                print('ERRO: Digite uma opção válida!')
            if op == 1 or op == 2:
                print('-=' * 20)
                print(f'{f"Opção {op}":^40}')
                print('-=' * 20)
            if op == 3:
                print('-=' * 20)
                print(f'{"Saindo do Sistema... Até logo!":^40}')
                print('-=' * 20)
                break
    break
