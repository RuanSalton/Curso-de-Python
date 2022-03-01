'''l1 = float(input('Primeira medida de reta: '))
l2 = float(input('Segunda medida de reta: '))
l3 = float(input('Terceira medida de reta: '))
sl1 = l1 + l2
sl2 = l1 + l3
sl3 = l2 + l3
if sl1 < l3:
    print('As medidas não formam um triângulo.')
if sl2 < l2:
    print('As medidas não formam um triângulo.')
if sl3 < l1:
    print('As medidas não formam um triângulo.')
else:
    print('As medidas formam sim, um triângulo.')'''
print('\033[31m-=\033[m' * 12)
print('\033[34mAnalizador de triângulos\033[m')
print('\033[31m-=\033[m' * 12)
r1 = float(input('Primeira medida de reta:'))
r2 = float(input('Segunda medida de reta:'))
r3 = float(input('Terceira medida de reta:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[36mEste conjunto de retas formam sim um triângulo.\033[m')
else:
    print('\033[31mEste conjunto de retas não formam um triângulo.\033[m')
