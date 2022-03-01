def aumentar(n=0, p=0):
    porcent = (p * n) / 100
    return n + porcent


def diminuir(n=0, p=0):
    porcent = (p * n) / 100
    return n - porcent


def dobro(n=0):
    return n * 2


def metade(n=0):
    return n / 2


def moeda(n=0, m='R$'):
    return f'{m}{n:.2f}'.replace('.', ',')

