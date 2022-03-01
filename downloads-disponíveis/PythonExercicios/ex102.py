def fatorial(n, show=False):
    """
    ==> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    print('-' * 30)
    f = 1
    for c in range(n, 0, -1):
        if show:
            if c <= n:
                print(c, end='')
                if c > 1:
                    print(' x ', end='')
                else:
                    print(' = ', end='')
        f *= c
    return f


# Programa principal
print(fatorial(5, show=True))
help(fatorial)
