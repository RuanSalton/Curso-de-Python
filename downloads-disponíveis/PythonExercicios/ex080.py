lista = []
for p in range(0, 5):
    v = int(input('Digite um valor: '))
    if p == 0 or v > lista[-1]:
        lista.append(v)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if v <= lista[pos]:
                lista.insert(pos, v)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos +=1
print('-=' * 30)
print(f'Você digitou os valores {lista}')
