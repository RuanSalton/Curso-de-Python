def leiaDinheiro(msg):
    while True:
        v = str(input(msg)).replace(',', '.').strip()
        if '.' in v:
            v = float(v)
            break
        if v.isnumeric():
            v = float(v)
            break
        else:

            print(f'ERRO! "{v}" é um preço inválido!')
    return v
