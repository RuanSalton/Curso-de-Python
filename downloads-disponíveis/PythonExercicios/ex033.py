'''import math
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
lista = [n1, n2, n3]
print('O número maior é o {}.'.format(max(lista)))
print('O menor número é o {}.'.format(min(lista)))'''
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor número é {}.'.format(menor))
print('O maior número é {}.'.format(maior))
