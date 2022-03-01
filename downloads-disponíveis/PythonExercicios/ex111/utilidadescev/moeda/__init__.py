def aumentar(n=0, p=0, form=False):
    porcent = n + (p * n / 100)
    if form:
        return moeda(porcent)
    else:
        return porcent


def diminuir(n=0, p=0, form=False):
    porcent = n - (p * n / 100)
    if form:
        return moeda(porcent)
    else:
        return porcent


def dobro(n=0, form=False):
    c = n * 2
    if form:
        return moeda(c)
    else:
        return c


def metade(n=0, form=False):
    c = n / 2
    if form:
        return moeda(c)
    else:
        return c


def moeda(n=0, m='R$'):
    return f'{m}{n:.2f}'.replace('.', ',')


def resumo(n=0, a=10, d=5):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR"}'.center(30))
    print('-' * 30)
    print(f'Preço analizado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{a}% de aumento: \t{aumentar(n, a, True)}')
    print(f'{d}% de redução: \t{diminuir(n, d, True)}')
    print('-' * 30)
