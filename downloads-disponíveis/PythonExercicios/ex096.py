def área(l, c):
    a = l * c
    print(f'A área de um terreno {l:.2f} x {c:.2f} é de {a:.2f}m².')

# Programa Principal
print(' Controle de terrenos')
print('-'*20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)
