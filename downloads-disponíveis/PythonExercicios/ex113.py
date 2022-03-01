def leiaint(msg):
    while True:
        try:
            n = input(msg)
        except:
            return f'\033[31mERRO! Digite um número inteiro válido.\033[m'
        else:
            if n.isnumeric():
                n = int(n)
                break
    return n


def leiafloat(msg):
    while True:
        v = str(input(msg)).replace(',', '.').strip()
        if '.' in v:
            v = float(v)
            break
        if v.isnumeric():
            v = float(v)
            break
    return v


i = leiaint('Digite um inteiro: ')
r = leiafloat('Digite um real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}.')
