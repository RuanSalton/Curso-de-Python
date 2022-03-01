'''r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 == r2 and r2 == r3:
    print('Este conjunto de retas formam sim um triângulo.E ele é Equilátero.')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 == r2 and r2 != r3:
    print('Este conjunto de retas formam sim um triângulo.E ele é Isóceles.')
elif r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2 and r1 != r2 and r1 != r3:
    print('Este conjunto de retas formam sim um triângulo.E ele é Escaleno.')
else:
    print('Este conjunto de retas não formam um triângulo.')'''
print('\033[31m-=\033[m' * 12)
print('\033[34mAnalizador de triângulos\033[m')
print('\033[31m-=\033[m' * 12)
r1 = float(input('Primeira medida de reta:'))
r2 = float(input('Segunda medida de reta:'))
r3 = float(input('Terceira medida de reta:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[36mEste conjunto de retas formam sim um triângulo \033[m', end= '')
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 != r2 != r3 !=r1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('\033[31mEste conjunto de retas não formam um triângulo.\033[m')
