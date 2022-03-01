'''from math import sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
ip = pow(co, 2) + pow(ca, 2)
print('O comprimento da ipotenusa é {:.2f}cm.'.format(sqrt(ip)))'''

from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}.'.format(hi))
