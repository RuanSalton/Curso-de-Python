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

